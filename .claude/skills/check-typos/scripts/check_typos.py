#!/usr/bin/env python3
"""Check the text of the site for spelling errors and for errors in names.

The script reports and never edits. It reads the source files of the site,
so every finding carries a file and a line. It exits with 0 when it has no
finding, with 1 when it has findings, and with 2 when it cannot run.

Usage, from the repository root:
    python3 .claude/skills/check-typos/scripts/check_typos.py
"""

import argparse
import difflib
import glob
import html
import os
import re
import subprocess
import sys

DICTIONARY = "/usr/share/dict/words"
WORDS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "references", "words.txt")

# Both orders of the name are in deliberate use on the site. The author lists
# of the publications use the first form only.
OWNER = "Noor Nashid"
OWNER_FORMS = {"Noor Nashid", "Nashid Noor"}

PAGES = ["index.md", "nav/*.md", "_writings/*.md", "_includes/*.html", "_layouts/*.html"]
DATA = ["_data/*.yml"]
CONFIG = "_config.yml"
PAPERS = "_data/papers.yml"
ARXIV = "https://export.arxiv.org/api/query?search_query=au:%22{}%22&max_results=100"

# Only these fields hold prose. Identifiers and links are not checked.
DATA_KEYS = {"title", "authors", "venue", "award", "featured", "description", "location", "name", "role"}
CONFIG_KEYS = {"title", "group", "dept", "institution", "address", "keywords", "copyright", "description"}
FRONT_KEYS = {"title", "navtitle", "summary", "description"}

# The system dictionary holds headwords only, so inflected forms are reduced
# by these rules before the lookup. Each pair is a suffix and its replacement.
SUFFIXES = [
    ("ies", "y"), ("ied", "y"), ("ier", "y"), ("iest", "y"), ("ily", "y"),
    ("es", ""), ("s", ""), ("ed", ""), ("ed", "e"), ("d", ""),
    ("ing", ""), ("ing", "e"), ("ings", ""), ("ings", "e"),
    ("ly", ""), ("ally", ""), ("er", ""), ("er", "e"), ("ers", ""), ("ers", "e"),
    ("est", ""), ("est", "e"), ("ion", "e"), ("ions", "e"), ("ion", ""), ("ions", ""),
    ("ation", "e"), ("ations", "e"), ("ation", ""), ("ations", ""),
    ("ment", ""), ("ments", ""), ("ness", ""), ("able", ""), ("able", "e"),
]
IRREGULAR = {
    "held", "paid", "built", "sent", "spent", "kept", "led", "met", "chose", "chosen", "gave", "given",
    "took", "taken", "wrote", "written", "began", "begun", "became", "ran", "made", "found", "taught",
    "thought", "brought", "sought", "said", "saw", "seen", "went", "gone", "knew", "known", "grew",
    "grown", "drew", "drawn", "shown", "understood", "stood", "told", "sold", "left", "felt", "lost",
    "won", "read", "done", "did", "has", "was", "were", "been", "are", "its", "his", "her", "our",
    "their", "them", "these", "those", "children", "people", "criteria", "data", "media", "analyses",
    "theses", "hypotheses", "indices", "matrices", "men", "women",
}

TOKEN = re.compile(r"[^\W_]+(?:['’][^\W_]+)*")


def distance(first, second):
    """Return the edit distance, where a swap of two adjacent letters counts as one edit."""
    rows = [[0] * (len(second) + 1) for _ in range(len(first) + 1)]
    for i in range(len(first) + 1):
        rows[i][0] = i
    for j in range(len(second) + 1):
        rows[0][j] = j
    for i in range(1, len(first) + 1):
        for j in range(1, len(second) + 1):
            cost = 0 if first[i - 1] == second[j - 1] else 1
            rows[i][j] = min(rows[i - 1][j] + 1, rows[i][j - 1] + 1, rows[i - 1][j - 1] + cost)
            if i > 1 and j > 1 and first[i - 1] == second[j - 2] and first[i - 2] == second[j - 1]:
                rows[i][j] = min(rows[i][j], rows[i - 2][j - 2] + 1)
    return rows[-1][-1]


def blank(match):
    """Replace a match by spaces and keep its line breaks, so that line numbers hold."""
    return re.sub(r"[^\n]", " ", match.group(0))


def keep_attributes(match):
    """Replace a tag by the text of its alt and title attributes."""
    kept = " ".join(re.findall(r'\b(?:alt|title)="([^"]*)"', match.group(0)))
    return " " + kept + " " + "\n" * match.group(0).count("\n")


def field(line, keys):
    found = re.match(r"^\s*-?\s*([A-Za-z_]+):\s*(.*)$", line)
    if not found or found.group(1) not in keys:
        return None, ""
    value = re.sub(r"\s+#\s.*$", "", found.group(2)).strip()
    if len(value) > 1 and value[0] == value[-1] and value[0] in "\"'":
        value = value[1:-1]
    return found.group(1), value


def clean(text):
    text = re.sub(r"https?://\S+|www\.\S+|\S+@\S+\.\S+", " ", text)
    return html.unescape(text)


def page_lines(path):
    """Return the prose of a page as pairs of line number and text."""
    with open(path, encoding="utf-8", errors="replace") as handle:
        text = handle.read()
    front = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if front:
        kept = [field(line, FRONT_KEYS)[1] for line in front.group(1).split("\n")]
        text = "\n" + "\n".join(kept) + "\n\n" + text[front.end():]
    for pattern in [
        r"(?s)```.*?```",
        r"(?is)<(script|style|svg|pre|code)\b.*?</\1>",
        r"(?s)<!--.*?-->",
        r"(?s)\{%.*?%\}",
        r"(?s)\{\{.*?\}\}",
    ]:
        text = re.sub(pattern, blank, text)
    text = re.sub(r"(?s)<[^<>]*>", keep_attributes, text)
    text = re.sub(r"\]\([^)\n]*\)", "] ", text)
    text = re.sub(r"`[^`\n]*`", " ", text)
    return [(number, clean(line)) for number, line in enumerate(text.split("\n"), 1)]


def data_lines(path, keys):
    """Return the prose fields of a YAML file as triples of line number, key, and text."""
    with open(path, encoding="utf-8", errors="replace") as handle:
        lines = handle.read().split("\n")
    found = []
    for number, line in enumerate(lines, 1):
        key, value = field(line, keys)
        if key and value:
            found.append((number, key, clean(value)))
    return found


def load_words(path):
    exact, lower = set(), set()
    if os.path.exists(path):
        with open(path, encoding="utf-8") as handle:
            for line in handle:
                word = line.split("#")[0].strip()
                if word:
                    (lower if word == word.lower() else exact).add(word)
    return exact, lower


class Speller:
    def __init__(self, dictionary, words):
        with open(dictionary, encoding="utf-8", errors="replace") as handle:
            self.dictionary = {line.strip().lower() for line in handle if line.strip()}
        self.exact, self.lower = load_words(words)
        self.listed = sorted(self.exact | self.lower)

    def known(self, token):
        low = token.lower()
        if token in self.exact or low in self.lower:
            return True
        if any(letter.isdigit() for letter in token):
            # Numbers, ordinals, decades, and version labels such as "v2".
            return bool(re.fullmatch(r"\d+(st|nd|rd|th|s)?|v\d+", low))
        if len(low) < 3 or low in self.dictionary or low in IRREGULAR:
            return True
        for suffix, replacement in SUFFIXES:
            if not low.endswith(suffix):
                continue
            stem = low[: len(low) - len(suffix)] + replacement
            if len(stem) < 3:
                continue
            if stem in self.dictionary or stem in self.lower:
                return True
            # A doubled final consonant: "running" reduces to "run".
            if stem[-1] == stem[-2] and (stem[:-1] in self.dictionary or stem[:-1] in self.lower):
                return True
        return False

    def near(self, token):
        """Return a listed word or a dictionary word that the token may stand for."""
        close = difflib.get_close_matches(token, self.listed, n=1, cutoff=0.8)
        if close and close[0] != token:
            return close[0]
        low = token.lower()
        letters = "abcdefghijklmnopqrstuvwxyz"
        splits = [(low[:i], low[i:]) for i in range(len(low) + 1)]
        edits = [a + b[1:] for a, b in splits if b]
        edits += [a + b[1] + b[0] + b[2:] for a, b in splits if len(b) > 1]
        edits += [a + c + b[1:] for a, b in splits if b for c in letters]
        edits += [a + c + b for a, b in splits for c in letters]
        for edit in edits:
            if len(edit) > 2 and (edit in self.dictionary or edit in self.lower):
                return edit
        return ""


def normalize(token):
    token = token.replace("’", "'")
    return re.sub(r"'(s|S)?$", "", token)


def names_in(value):
    """Return the names of an author list. A remark in parentheses is not a name."""
    value = re.sub(r"\([^)]*\)", " ", value)
    return [name.strip() for name in re.split(r",|\band\b", value) if name.strip()]


def same_but_for_initials(first, second):
    strip = lambda name: [part for part in name.split() if not re.fullmatch(r"[A-Z]\.?", part)]
    return first != second and strip(first) == strip(second)


def paper_entries(path):
    """Return the publications as dictionaries of field to (line number, text)."""
    entries = []
    for number, key, text in data_lines(path, {"id", "title", "authors", "arxiv"}):
        if key == "id" or not entries:
            entries.append({})
        entries[-1][key] = (number, text)
    return entries


def arxiv_records(owner):
    """Return the arXiv records of the owner as a map of identifier to title and authors."""
    fetched = subprocess.run(
        ["curl", "-sL", "--fail", "--max-time", "30", ARXIV.format(owner.replace(" ", "+"))],
        capture_output=True,
    )
    if fetched.returncode != 0:
        return None
    records = {}
    for entry in re.findall(r"(?s)<entry>(.*?)</entry>", fetched.stdout.decode("utf-8", errors="replace")):
        identifier = re.search(r"<id>.*?/abs/([^<v]+)", entry)
        title = re.search(r"(?s)<title>(.*?)</title>", entry)
        if identifier and title:
            records[identifier.group(1)] = (
                re.sub(r"\s+", " ", html.unescape(title.group(1))).strip(),
                [html.unescape(name).strip() for name in re.findall(r"<name>(.*?)</name>", entry)],
            )
    return records


def letters(text):
    return re.sub(r"[^a-z0-9]", "", text.lower())


def compare_with_arxiv(path, shown_path, records):
    """Compare the author list and the title of each publication with its arXiv record."""
    authors, titles, absent = [], [], []
    for entry in paper_entries(path):
        if "title" not in entry or "authors" not in entry:
            continue
        line, title = entry["title"]
        record = None
        linked = re.search(r"arxiv\.org/abs/([0-9.]+)", entry.get("arxiv", (0, ""))[1])
        if linked:
            record = records.get(linked.group(1))
        if record is None:
            scored = [(difflib.SequenceMatcher(None, letters(title), letters(found[0])).ratio(), found) for found in records.values()]
            best = max(scored, default=(0, None), key=lambda pair: pair[0])
            record = best[1] if best[0] >= 0.85 else None
        if record is None:
            absent.append((shown_path, line, "\"{}\"".format(title)))
            continue
        number, listed = entry["authors"]
        if names_in(listed) != record[1]:
            authors.append((shown_path, number, "the site lists \"{}\" and arXiv lists \"{}\"".format(
                ", ".join(names_in(listed)), ", ".join(record[1]))))
        if letters(title) != letters(record[0]):
            titles.append((shown_path, line, "the site has \"{}\" and arXiv has \"{}\"".format(title, record[0])))
    return authors, titles, absent


def stop(message):
    """End the run with an error. The exit code 2 is kept apart from the code for findings."""
    print(message, file=sys.stderr)
    sys.exit(2)


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--root", default=".", help="root of the site sources")
    parser.add_argument("--words", default=WORDS, help="file of accepted words")
    parser.add_argument("--dictionary", default=DICTIONARY, help="dictionary, one word per line")
    parser.add_argument("--list-unknown", action="store_true", help="print the unknown words only, one per line")
    parser.add_argument("--arxiv", action="store_true", help="compare author lists and titles with arXiv")
    args = parser.parse_args()

    if not os.path.exists(args.dictionary):
        stop("The dictionary {} does not exist. Pass another one with --dictionary.".format(args.dictionary))
    speller = Speller(args.dictionary, args.words)

    def paths(patterns):
        found = []
        for pattern in patterns:
            found += sorted(glob.glob(os.path.join(args.root, pattern)))
        return found

    def shown(path):
        return os.path.relpath(path, args.root)

    # Every checked line, as (path, line number, kind, text). The kind is the
    # YAML key, or "page" for the prose of a page.
    lines = []
    for path in paths(PAGES):
        lines += [(path, number, "page", text) for number, text in page_lines(path)]
    for path in paths(DATA):
        lines += [(path, number, key, text) for number, key, text in data_lines(path, DATA_KEYS)]
    config = os.path.join(args.root, CONFIG)
    if os.path.exists(config):
        lines += [(config, number, key, text) for number, key, text in data_lines(config, CONFIG_KEYS)]
    if not lines:
        stop("No source file was found under {}. Run the script from the repository root.".format(args.root))

    authors = {}
    papers = os.path.join(args.root, PAPERS)
    for path, number, key, text in lines:
        if key == "authors":
            for name in names_in(text):
                authors.setdefault(name, (path, number))

    spelling, owner, prose_names, repeated = [], [], [], []
    for path, number, key, text in lines:
        tokens = [(match.group(0), match.start(), match.end()) for match in TOKEN.finditer(text)]
        for index, (raw, start, end) in enumerate(tokens):
            token = normalize(raw)
            if not speller.known(token):
                spelling.append((shown(path), number, token, speller.near(token)))
            gap = distance(token.lower(), "nashid")
            if 0 < gap <= 2:
                owner.append((shown(path), number, "\"{}\" is close to \"Nashid\"".format(token)))
            if index + 1 < len(tokens):
                following, next_start, _ = tokens[index + 1]
                following = normalize(following)
                between = text[end:next_start]
                if between.strip() == "" and token.isalpha() and len(token) > 1 and token.lower() == following.lower():
                    repeated.append((shown(path), number, "\"{} {}\"".format(token, following)))
                pair = {token: following, following: token}
                if "Nashid" in pair and between == " ":
                    other = pair["Nashid"]
                    if 0 < distance(other.lower(), "noor") <= 2 and other[:1].isupper():
                        owner.append((shown(path), number, "\"{}\" beside \"Nashid\" is close to \"Noor\"".format(other)))
        if key == "authors":
            continue
        # Names in prose are compared with the author lists of the publications.
        capitals = [item for item in tokens if item[0][:1].isupper()]
        for size in (2, 3):
            for index in range(len(tokens) - size + 1):
                window = tokens[index : index + size]
                if any(item not in capitals for item in window):
                    continue
                if any(text[window[k][2] : window[k + 1][1]] != " " for k in range(size - 1)):
                    continue
                name = " ".join(normalize(item[0]) for item in window)
                for author in authors:
                    if name == author or name in OWNER_FORMS:
                        continue
                    if sorted(name.split()) == sorted(author.split()):
                        prose_names.append((shown(path), number, "\"{}\" has the order of \"{}\" reversed".format(name, author)))
                    elif len(name.split()) == len(author.split()) and 0 < distance(name.lower(), author.lower()) <= 2:
                        prose_names.append((shown(path), number, "\"{}\" is close to \"{}\"".format(name, author)))

    missing, variants = [], []
    if os.path.exists(papers):
        for number, key, text in data_lines(papers, {"authors"}):
            listed = names_in(text)
            if OWNER not in listed:
                missing.append((shown(papers), number, "the author list does not contain \"{}\"".format(OWNER)))
            for name in listed:
                if name != OWNER and (name in OWNER_FORMS or 0 < distance(name.lower(), OWNER.lower()) <= 3):
                    owner.append((shown(papers), number, "\"{}\" in an author list is not \"{}\"".format(name, OWNER)))
    ordered = sorted(authors)
    for index, first in enumerate(ordered):
        for second in ordered[index + 1 :]:
            reason = ""
            if sorted(first.split()) == sorted(second.split()):
                reason = "the same words in a different order"
            elif same_but_for_initials(first, second):
                reason = "they differ by an initial"
            elif 0 < distance(first.lower(), second.lower()) <= 2:
                reason = "they differ by one or two letters"
            if reason:
                path, number = authors[second]
                variants.append((shown(path), number, "\"{}\" and \"{}\": {}".format(first, second, reason)))

    if args.list_unknown:
        for word in sorted({item[2] for item in spelling}):
            print(word)
        return

    def report(title, findings, render):
        print("\n{}: {}".format(title, len(findings)))
        for finding in sorted(set(findings)):
            print("  " + render(finding))

    print("Files checked: {}. Lines of text: {}. Accepted words: {}.".format(
        len({path for path, _, _, _ in lines}),
        sum(1 for _, _, _, text in lines if text.strip()),
        len(speller.listed),
    ))
    report("Words that are not known", spelling, lambda f: "{}:{}: {}{}".format(
        f[0], f[1], f[2], "  (near \"{}\")".format(f[3]) if f[3] else ""))
    plain = lambda f: "{}:{}: {}".format(*f)
    report("Name of the site owner", owner, plain)
    report("Publications without the site owner", missing, plain)
    report("Author names that may be variants of one name", variants, plain)
    report("Names in the text that differ from an author name", prose_names, plain)
    report("Repeated words", repeated, plain)

    differing = []
    if args.arxiv and os.path.exists(papers):
        records = arxiv_records(OWNER)
        if records is None:
            print("\nThe comparison with arXiv did not run, because arXiv could not be reached.")
        else:
            differing, titles, absent = compare_with_arxiv(papers, shown(papers), records)
            report("Author lists that differ from arXiv", differing, plain)
            # A published title may differ from the title of the preprint, and a
            # publication may have no preprint. Both are shown for review and
            # are not counted as findings.
            report("Titles that differ from arXiv, for review", titles, plain)
            report("Publications with no record on arXiv, for review", absent, plain)

    total = len(set(spelling)) + len(set(owner)) + len(set(missing)) + len(set(variants)) + len(set(prose_names)) + len(set(repeated)) + len(set(differing))
    print("\nFindings: {}".format(total))
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
