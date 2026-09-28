#!/usr/bin/env python3
"""Compare the committee roles on a conf.researchr.org profile with _data/services.yml.

The script reports and never edits. It lists every committee role on the
profile with the service entry it matched, followed by the roles that have no
entry. For each unmatched role it fetches the committee page, checks that the
name of the person appears on it, and prints the facts needed for the entry.

Usage, from the repository root:
    python3 .claude/skills/audit-services/scripts/audit_researchr.py
"""

import argparse
import html
import json
import re
import subprocess
import sys
from urllib.parse import urlparse

PROFILE = "https://conf.researchr.org/profile/noornashid"
SERVICES = "_data/services.yml"
PERSON = "Noor Nashid"
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
)

# The title attribute of each contribution states its kind. The visible label
# is unreliable: researchr has shown "Author in Program Committee" for a plain
# committee membership.
COMMITTEE = "Member of Committee"
AUTHORSHIP = "Contributed Item"


def fetch(url):
    result = subprocess.run(
        ["curl", "-sL", "--fail", "--max-time", "30", "-A", USER_AGENT, url],
        capture_output=True,
    )
    if result.returncode != 0:
        raise RuntimeError("could not fetch {} (curl exit {})".format(url, result.returncode))
    return result.stdout.decode("utf-8", errors="replace")


def read_source(source):
    if re.match(r"https?://", source):
        return fetch(source)
    with open(source, encoding="utf-8", errors="replace") as handle:
        return handle.read()


def load_services(path):
    try:
        import yaml

        with open(path, encoding="utf-8") as handle:
            return yaml.safe_load(handle)
    except ImportError:
        # The site already requires Ruby, which carries a YAML parser.
        converted = subprocess.run(
            ["ruby", "-ryaml", "-rjson", "-e", "puts YAML.load_file(ARGV[0]).to_json", path],
            capture_output=True,
            check=True,
        )
        return json.loads(converted.stdout)


def plain(markup):
    text = re.sub(r"<[^>]+>", " ", markup)
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def slug(url):
    parts = [part for part in urlparse(url).path.split("/") if part]
    return parts[-1].lower() if parts else ""


def normalized(url):
    parsed = urlparse(url.strip())
    return (parsed.netloc.lower() + parsed.path).rstrip("/")


def parse_profile(page):
    """Return the committee roles, the number of authorships, and unclassified lines."""
    start = page.find('id="contributions-timeline"')
    if start < 0:
        return [], 0, []
    end = page.find('id="embedWidget"', start)
    timeline = page[start : end if end > 0 else len(page)]

    roles, authorships, unclassified = [], 0, []
    blocks = re.split(r'<div class="contribution-year"><h3>(\d{4})</h3>', timeline)
    for year, block in zip(blocks[1::2], blocks[2::2]):
        for venue in re.finditer(r"<h4>(.*?)</h4>\s*<ul[^>]*>(.*?)</ul>", block, re.S):
            heading = plain(venue.group(1))
            external = heading.endswith("External")
            heading = re.sub(r"\s*-\s*External$", "", heading)
            for item in re.finditer(r"<li>(.*?)</li>", venue.group(2), re.S):
                kind = re.search(r'<small title="([^"]*)"', item.group(1))
                link = re.search(r'<a href="([^"]+)"[^>]*>(.*?)</a>', item.group(1), re.S)
                label = plain(link.group(2)) if link else plain(item.group(1))
                if kind and kind.group(1) == AUTHORSHIP:
                    authorships += 1
                elif kind and kind.group(1) == COMMITTEE and link:
                    roles.append(
                        {
                            "year": int(year),
                            "venue": heading,
                            "label": label,
                            "url": html.unescape(link.group(1)),
                            "external": external,
                        }
                    )
                else:
                    unclassified.append("{} {}: {}".format(year, heading, label))
    return roles, authorships, unclassified


def describe(role):
    """Return the track and committee names stated in the researchr label."""
    track = re.search(r"within the (.*?)\s*-track$", role["label"])
    committee = re.search(r" in (.*?) within the ", role["label"])
    return (
        track.group(1).strip() if track else role["label"],
        committee.group(1).strip() if committee else "",
    )


def venue_tokens(role):
    """Return the names under which a service entry may refer to the venue."""
    tokens = {role["venue"].lower()}
    tokens.update(found.lower() for found in re.findall(r"\(([^)]+)\)", role["venue"]))
    if not role["external"]:
        prefix = re.match(r"(.+?)-20\d\d", slug(role["url"]))
        if prefix:
            tokens.add(prefix.group(1))
    return {token for token in tokens if len(token) >= 3}


def names_venue(name, token):
    return re.search(r"(?<![a-z0-9]){}(?![a-z0-9])".format(re.escape(token)), name.lower())


def match(roles, services):
    """Assign each role to at most one service entry, strongest rule first."""
    used = set()

    def candidates(role):
        return [
            index
            for index, entry in enumerate(services)
            if index not in used and entry.get("year") == role["year"]
        ]

    def same_link(role):
        for index in candidates(role):
            if normalized(str(services[index].get("website", ""))) == normalized(role["url"]):
                return index
        return None

    def link_prefix(role):
        # A committee address extends the address of its track or workshop:
        # ".../ase-2026-tools-and-data-sets-program-committee" extends
        # ".../ase-2026-tools-and-data-sets".
        best, best_length = None, 0
        for index in candidates(role):
            entry_slug = slug(str(services[index].get("website", "")))
            if (
                re.search(r"20\d\d", entry_slug)
                and slug(role["url"]).startswith(entry_slug)
                and len(entry_slug) > best_length
            ):
                best, best_length = index, len(entry_slug)
        return best

    def venue_and_year(role):
        for index in candidates(role):
            name = str(services[index].get("name", ""))
            if any(names_venue(name, token) for token in venue_tokens(role)):
                return index
        return None

    rules = [
        ("same link", same_link),
        ("link prefix", link_prefix),
        ("venue and year", venue_and_year),
    ]
    for rule, find in rules:
        for role in roles:
            if "entry" in role:
                continue
            index = find(role)
            if index is not None:
                used.add(index)
                role["entry"] = services[index]
                role["rule"] = rule
    return roles


def inspect(role, person):
    """Fetch the committee page of an unmatched role and collect the evidence."""
    try:
        page = fetch(role["url"])
    except RuntimeError as error:
        return {"error": str(error)}
    place = re.search(r'<div class="place">(.*?)</div>', page, re.S)
    links = set()
    for href in re.findall(r'href="([^"#]+)"', page):
        if re.search(r"/(track|home)/", href) and slug(role["url"]).startswith(slug(href)):
            links.add(href)
    return {
        "listed": person.lower() in plain(page).lower(),
        "place": plain(place.group(1)) if place else "",
        "links": sorted(links, key=len, reverse=True),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--profile", default=PROFILE, help="profile address or a saved HTML file")
    parser.add_argument("--services", default=SERVICES, help="path of the services file")
    parser.add_argument("--name", default=PERSON, help="name to look for on committee pages")
    parser.add_argument("--skip-pages", action="store_true", help="do not fetch committee pages")
    args = parser.parse_args()

    services = load_services(args.services)
    try:
        page = read_source(args.profile)
    except (RuntimeError, OSError) as error:
        sys.exit(str(error))
    roles, authorships, unclassified = parse_profile(page)
    if not roles:
        # An empty parse must not read as a clean audit.
        sys.exit("No committee roles were parsed. The layout of the profile page may have changed.")

    match(roles, services)
    matched = [role for role in roles if "entry" in role]
    missing = [role for role in roles if "entry" not in role]

    print("Profile: {}".format(args.profile))
    print("Services file: {} ({} entries)".format(args.services, len(services)))
    print(
        "Committee roles on the profile: {}. Authorships skipped: {}. Unclassified lines: {}.".format(
            len(roles), authorships, len(unclassified)
        )
    )

    print("\nMatched roles: {}".format(len(matched)))
    for role in matched:
        track, _ = describe(role)
        print("  {}  {} | {}".format(role["year"], role["venue"], track))
        print("        {}: {}".format(role["rule"], role["entry"].get("name", "").strip()))

    print("\nRoles with no service entry: {}".format(len(missing)))
    for number, role in enumerate(missing, 1):
        track, committee = describe(role)
        print("  {}. {}  {} | {}".format(number, role["year"], role["venue"], track))
        if committee:
            print("     committee: {}".format(committee))
        print("     page: {}".format(role["url"]))
        if args.skip_pages:
            continue
        facts = inspect(role, args.name)
        if "error" in facts:
            print("     {}".format(facts["error"]))
            continue
        print("     {} on the page: {}".format(args.name, "yes" if facts["listed"] else "NO"))
        if facts["place"]:
            print("     dates and place: {}".format(facts["place"]))
        for link in facts["links"]:
            print("     venue page: {}".format(link))

    if unclassified:
        print("\nUnclassified lines, to be read by hand: {}".format(len(unclassified)))
        for line in unclassified:
            print("  {}".format(line))


if __name__ == "__main__":
    main()
