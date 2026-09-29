---
name: check-typos
description: Check the whole site for spelling errors and for errors in names, covering the name of the site owner, the author lists of the publications, and the names of coauthors in the text. Use whenever the user asks to check typos, to spell check or proofread the site, to check how a name is spelled, or to check author names, and before any PR that adds or changes text on a page (e.g. "check typos", "proofread my site", "is my name spelled right everywhere", "check the author names").
allowed-tools:
  - Bash
  - Read
  - Grep
  - WebFetch
  - AskUserQuestion
---

# Check typos

Find spelling errors and errors in names across the site, judge each finding, and report. The check edits nothing. A correction is made only after the user has approved it, as a small PR.

## When to run

- Before a PR that adds or changes text on a page.
- After a publication is added to `_data/papers.yml`.
- On request, for the whole site.

## Workflow

### 1. Run the script

From the repository root:

```bash
python3 .claude/skills/check-typos/scripts/check_typos.py --arxiv
```

The script reads the source files, so each finding carries a file and a line. It exits with 0 when it has no finding, with 1 when it has findings, and with 2 when it cannot run.

| Check | Finding |
| --- | --- |
| Spelling | A word that neither the dictionary nor `references/words.txt` knows, with the nearest known word |
| Name of the site owner | A word within two letters of "Nashid", a word beside "Nashid" that is close to "Noor", or an entry of an author list that is close to "Noor Nashid" |
| Publications without the site owner | An author list in `_data/papers.yml` that lacks "Noor Nashid" |
| Author variants | Two author names with the same words in a different order, with a different initial, or one or two letters apart |
| Names in the text | A name on a page that is close to the name of an author, or has its order reversed |
| Repeated words | The same word twice in a row |
| arXiv, with `--arxiv` | An author list that differs from the arXiv record of the publication |

The site uses the name in both orders, "Nashid Noor" and "Noor Nashid". Both are correct. The author lists use "Noor Nashid" only.

The script reads `index.md`, `nav/`, `_writings/`, `_includes/`, `_layouts/`, `_config.yml`, and the prose fields of `_data/`. It skips code, link targets, addresses, Liquid tags, and the identifiers and links in the data files.

### 2. Judge each finding

A finding is a candidate. Decide what each one is before reporting it.

- **An unknown word** is a typo, or a correct word that the dictionary lacks. The nearest known word shows which.
- **A name** is checked against a source before it is called wrong: the arXiv record, DBLP, the paper, or the page of the person. Spelling that looks unusual is often correct.
- **A title that differs from arXiv** is often intended, because a published title can differ from the title of the preprint. The script lists these for review and does not count them. Check the page of the publisher.

### 3. Read the pages

The script finds words that do not exist. It cannot find a wrong word that exists, such as "form" for "from", or an error of grammar, such as "looking forward to reviews the papers". Read the text for these: the changed pages before a PR, and every page on a full check.

### 4. Report

Give the user one table with the file and line, the text as it stands, the proposed correction, and the source of the correction. State which findings were judged correct and why. Make no edit before the user approves.

### 5. Correct after approval

- Open one small PR for each page or each kind of error, and wait for the user to merge it.
- A news item that is already merged is a log. Correct a typo in it only with approval, and leave the wording as it is.
- A correction in `_writings/` goes in a PR of its own that touches no other part of the site.
- Most content files use CRLF line endings. Keep them, and confirm with `git diff --stat` that only the corrected lines changed.

### 6. Keep the accepted words current

`references/words.txt` holds the words that the site uses and the dictionary lacks. Every name on the site belongs there, which is why a new spelling of a known name is reported.

Add a correct word under the matching heading, in the PR that brings the word to the site. Add a name only after it has been checked against a source. Each added word is a review item for the user.

## Limits

- The PDF files under `resources/` are not read.
- The dictionary holds headwords, and the script reduces inflected forms by rule. A misspelling that forms another word passes the spelling check. "Nashed" passes it as "nash" with an ending, and the check of the owner name reports it.
- The dictionary is `/usr/share/dict/words`, which macOS provides. On another system, pass one with `--dictionary`.
- The comparison with arXiv covers the publications that have a record there.
