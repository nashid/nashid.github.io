#!/usr/bin/env python3
"""Compare the citation sentence on the home page with Google Scholar.

The sentence states the total number of citations, the h-index, and the
citations of the CEDAR paper. The script reads the three numbers from the
Google Scholar profile, applies the rounding of the site, and reports the
difference. With --write it replaces the three numbers in the sentence and
changes nothing else.

Exit codes: 0 when the sentence is current, 1 when it needs a change or was
changed, 2 when the script cannot run, and 3 when Google Scholar refuses the
request or cannot be reached. Neither error edits the page.

Usage, from the repository root:
    python3 .claude/skills/refresh-citations/scripts/refresh_citations.py
    python3 .claude/skills/refresh-citations/scripts/refresh_citations.py --write
"""

import argparse
import datetime
import html
import re
import subprocess
import sys

CONFIG = "_config.yml"
PAGE = "index.md"
# The address without paging is the form that the robots rules of Google
# Scholar allow. Its first page holds the statistics and the twenty most
# cited papers.
PROFILE = "https://scholar.google.com/citations?user={}&hl=en"
PAPER = "Retrieval-Based Prompt Selection for Code-Related Few-Shot Learning"
SENTENCE = re.compile(
    rb"over (\d+) citations \(h-index: (\d+)\), including CEDAR which has been cited more than (\d+) times"
)
# The total and the count of the paper are rounded down to a multiple of 50,
# so the sentence stays true while the counts grow. The h-index is exact.
STEP = 50
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
)


def stop(message):
    print(message, file=sys.stderr)
    sys.exit(2)


def refused(message):
    """End the run because the source gave no profile. The cause lies outside the site."""
    print(message, file=sys.stderr)
    sys.exit(3)


def scholar_user(config):
    with open(config, encoding="utf-8", errors="replace") as handle:
        found = re.search(r"(?m)^gscholar:\s*(\S+)", handle.read())
    if not found:
        stop("The file {} has no gscholar entry.".format(config))
    return found.group(1)


def fetch(source):
    if not re.match(r"https?://", source):
        with open(source, encoding="utf-8", errors="replace") as handle:
            return handle.read()
    fetched = subprocess.run(
        ["curl", "-sL", "--max-time", "30", "-A", USER_AGENT, "-H", "Accept-Language: en-US,en;q=0.9",
         "-w", "\n%{http_code}", source],
        capture_output=True,
    )
    if fetched.returncode != 0:
        refused("Google Scholar could not be reached (curl exit {}).".format(fetched.returncode))
    page, _, status = fetched.stdout.decode("utf-8", errors="replace").rpartition("\n")
    if status != "200":
        refused("Google Scholar answered with HTTP status {}.".format(status))
    return page


def number(text):
    return int(text.replace(",", ""))


def read_profile(page):
    """Return the total citations, the h-index, and the citations of the paper."""
    cells = re.findall(r'<td class="gsc_rsb_std">([\d,]+)</td>', page)
    if len(cells) != 6:
        if re.search(r"unusual traffic|not a robot|captcha", page, re.I):
            refused("Google Scholar asked for a captcha, so it treats this machine as automated traffic.")
        if re.search(r"consent\.google|before you continue", page, re.I):
            refused("Google Scholar returned a consent page in place of the profile.")
        if re.search(r"accounts\.google\.com", page, re.I) and "gsc_prf_in" not in page:
            refused("Google Scholar returned a sign-in page in place of the profile.")
        stop("The statistics were not found on the profile page. Its layout may have changed.")
    # The cells come in pairs of all time and recent years. The first of each pair is all time.
    total, h_index = number(cells[0]), number(cells[2])
    for row in re.findall(r'(?s)<tr class="gsc_a_tr">(.*?)</tr>', page):
        title = re.search(r'(?s)class="gsc_a_at"[^>]*>(.*?)</a>', row)
        cited = re.search(r'class="gsc_a_ac[^"]*"[^>]*>([\d,]+)</a>', row)
        if title and cited and html.unescape(re.sub(r"<[^>]+>", "", title.group(1))).lower().startswith(PAPER.lower()):
            return total, h_index, number(cited.group(1))
    stop("The paper \"{}\" was not found on the profile page.".format(PAPER))


def floor(value):
    return value - value % STEP


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--write", action="store_true", help="replace the three numbers in the sentence")
    parser.add_argument("--page", default=PAGE, help="page that holds the sentence")
    parser.add_argument("--profile", help="address of the profile, or a saved copy of its page")
    parser.add_argument("--config", default=CONFIG, help="site configuration with the gscholar entry")
    args = parser.parse_args()

    source = args.profile or PROFILE.format(scholar_user(args.config))
    try:
        with open(args.page, "rb") as handle:
            content = handle.read()
    except OSError as error:
        stop("The page {} could not be read: {}.".format(args.page, error))
    found = SENTENCE.search(content)
    if not found:
        stop("The citation sentence was not found in {}. Its wording may have changed.".format(args.page))
    current = tuple(int(value) for value in found.groups())

    total, h_index, paper = read_profile(fetch(source))
    computed = (floor(total), h_index, floor(paper))
    # A number on the site is never lowered. A lower count points to an error
    # in the source, and the sentence states a floor that stays true.
    proposed = tuple(max(now, new) for now, new in zip(current, computed))

    form = "over {} citations, h-index {}, CEDAR cited more than {} times"
    print("Google Scholar on {}: {} citations, h-index {}, CEDAR cited {} times.".format(
        datetime.date.today().isoformat(), total, h_index, paper))
    print("Source: {}".format(source))
    print("Sentence now:      " + form.format(*current))
    print("Sentence proposed: " + form.format(*proposed))
    counts = (total, h_index, paper)
    for label, now, new, count in zip(("total citations", "h-index", "CEDAR citations"), current, computed, counts):
        if new < now:
            print("Kept as it is: {} stays at {}, although Google Scholar gives {}.".format(label, now, count))

    if proposed == current:
        print("The sentence is current.")
        sys.exit(0)
    labels = ("over {} citations", "h-index: {}", "more than {} times")
    for label, now, new in zip(labels, current, proposed):
        if now != new:
            print("Change: \"{}\" becomes \"{}\".".format(label.format(now), label.format(new)))

    if args.write:
        replacement = (
            "over {} citations (h-index: {}), including CEDAR which has been cited more than {} times"
            .format(*proposed).encode("ascii")
        )
        # The page is read and written as bytes, so its line endings stay as they are.
        with open(args.page, "wb") as handle:
            handle.write(content[: found.start()] + replacement + content[found.end():])
        print("The sentence in {} was changed.".format(args.page))
    sys.exit(1)


if __name__ == "__main__":
    main()
