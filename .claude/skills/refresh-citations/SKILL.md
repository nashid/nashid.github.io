---
name: refresh-citations
description: Bring the citation sentence on the home page up to date with Google Scholar, covering the total citations, the h-index, and the citations of the CEDAR paper. Use whenever the user asks to refresh, sync, or update the citation numbers, the h-index, the publication record, or the impact sentence, and when the quarterly workflow opens an issue or a PR about it (e.g. "refresh my citations", "sync my publication record", "is my h-index current", "update the citation stats").
allowed-tools:
  - Bash
  - Read
  - Edit
  - AskUserQuestion
---

# Refresh citations

Compare the citation sentence in `index.md` with the Google Scholar profile, show the difference, and change the sentence after the user has confirmed the numbers.

The sentence reads: "My research has received over 700 citations (h-index: 12), including CEDAR which has been cited more than 350 times". Only its three numbers change.

## When to run

- When the quarterly workflow `.github/workflows/citation-refresh.yml` opens a reminder issue. Google Scholar refuses some requests from the runners of GitHub. A refused run opens the reminder, and the skill then does the work from a personal machine.
- When the workflow opens a PR or an issue with a prepared branch. Review the numbers against the profile before the merge.
- On request.

## Rules of the sentence

| Number | Rule | Example |
| --- | --- | --- |
| Total citations | Rounded down to a multiple of 50 | 736 becomes "over 700" |
| h-index | Exact | 13 becomes "h-index: 13" |
| Citations of CEDAR | Rounded down to a multiple of 50 | 366 becomes "more than 350" |

Rounding down keeps the sentence true while the counts grow. A number on the site is never lowered: a lower count from the source points to an error in the source.

Google Scholar is the only source. OpenAlex reported 261 citations and an h-index of 6 on the day Google Scholar reported 736 and 13, so another source would contradict the numbers on the site.

## Workflow

### 1. Run the script

From the repository root:

```bash
python3 .claude/skills/refresh-citations/scripts/refresh_citations.py
```

The script prints the counts on Google Scholar with the date, the sentence as it stands, the sentence it proposes, and each change.

| Exit code | Meaning |
| --- | --- |
| 0 | The sentence is current |
| 1 | The sentence needs a change, or was changed with `--write` |
| 2 | The script cannot run: the sentence was not found, or the layout of the profile page changed |
| 3 | Google Scholar refused the request or could not be reached |

On exit 2 or 3, report the cause to the user and stop. Do not take the numbers from another source, and do not estimate them.

### 2. Confirm with the user

Show the counts and the proposed sentence, and ask for confirmation before any edit. The user reviews every change of content.

### 3. Change the sentence

Branch from fresh `main`, then run:

```bash
python3 .claude/skills/refresh-citations/scripts/refresh_citations.py --write
```

The script replaces the three numbers and nothing else. It writes bytes, so the CRLF line endings of `index.md` stay. Confirm with `git diff --stat` that one line changed.

### 4. Verify and open the PR

Run `bundle exec jekyll build` and confirm the new sentence in `_site/index.html`. Open one PR that states what changed, the counts with the date and the address of the profile as evidence, and the verification. PRs #99 and #109 are the precedents.

## Scope

- The news item of November 2025 states that CEDAR was cited nearly 300 times. It is a log entry and stays as it is.
- The skill changes the three numbers only. A change to the wording of the sentence is made by hand, and the pattern in the script is then updated in the same PR.

## Limits

- Google Scholar offers no interface for programs. The script reads the public profile page, in the form that the robots rules of Google Scholar allow, and it stops when the page is not the profile.
- The first page of the profile lists the twenty most cited papers. The script finds CEDAR by its title, so CEDAR must be among them.
