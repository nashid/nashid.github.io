---
name: audit-services
description: Compare the committee roles on the conf.researchr.org profile with the Service page and report the roles that have no entry in _data/services.yml. Use whenever the user asks which service roles, PC memberships, or committee roles are missing from the site, mentions the researchr profile, or asks to bring the Service page up to date (e.g. "check my researchr profile", "which conferences are not on my service page", "audit my services").
allowed-tools:
  - Bash
  - Read
  - WebFetch
  - AskUserQuestion
---

# Audit service roles

Find the committee roles that the researchr profile lists and `_data/services.yml` does not, confirm each one on its committee page, and report them. The audit edits nothing. Each confirmed role is then added as its own PR under the `add-service` conventions.

## When to run

The workflow `.github/workflows/service-audit.yml` runs the script on the first day of each month. It opens an issue when a role has no entry or when the audit cannot run. The workflow edits nothing, so the roles are added by invoking the skill.

Invoke the skill on two occasions.

- After a committee invitation is accepted and the committee page is public. The news month is then still known, and the role reaches the site while it is current.
- When the monthly workflow opens an issue. Chairs add members to a committee page without notice, and the service news items of 2023 to 2026 fall in eleven of the twelve months.

## Workflow

### 1. Run the script

From the repository root:

```bash
python3 .claude/skills/audit-services/scripts/audit_researchr.py
```

The script downloads the profile, keeps the contributions marked "Member of Committee", and skips authorships. It matches each role to one entry of `_data/services.yml` and prints the matched roles, the roles with no entry, and any line it could not classify. For a role with no entry it also fetches the committee page and prints whether the name appears there, the dates and place, and the venue pages.

Options: `--profile` takes another address or a saved HTML file, `--services` another services file, `--name` another name, and `--skip-pages` leaves the committee pages unfetched.

If the script stops with "No committee roles were parsed", the layout of the profile page has changed. Report that to the user and do not present the result as a clean audit.

### 2. Read the matches

The script applies three rules in order, and each service entry is used once.

| Rule | Meaning | Reliability |
| --- | --- | --- |
| same link | The entry and the role have the same address and year. | High |
| link prefix | The committee address extends the address of the entry. | High |
| venue and year | The entry names the venue and has the same year. | Check by hand |

Read every "venue and year" match and confirm that the entry is the same role. One venue can carry several roles in a year: MSR 2025 had an Industry Track role and a Junior PC role. Treat a wrong match as a missing role.

### 3. Confirm each missing role

The committee page is the evidence for the role, and its address goes in the PR description. A role whose page does not list the name is reported to the user as unconfirmed and is not added.

Take the role from the committee page. The label on the profile is unreliable: researchr showed "Author in Program Committee" for a plain PC membership.

Open the venue page for the facts that the entry and the news item need: the official name, the edition, the dates, the place, and any deadline that is still ahead. State only what the page states. A workshop page without an edition number gets no edition number.

### 4. Report

Give the user one table of the missing roles with the venue, the track, the year, and the committee page. List the unclassified lines as well, since they may hold roles in a form the script does not know.

### 5. Ask before editing

Ask for the news month of every missing role in one round. Researchr shows no date of joining, so the month is never inferred. Offer "No news item" as an answer.

### 6. Add the roles, one PR at a time

Follow `.claude/skills/add-service/SKILL.md` for the edits, and use the facts from the audit in place of its questions. Branch from fresh `main` for each role, open one PR, and wait for the merge before starting the next, because every PR edits the same lines of `_data/services.yml` and `nav/news.md`.

The entries of 2026 and 2027 give the forms to follow.

| Case | Name | Link |
| --- | --- | --- |
| Track of a conference | `International Conference on Software Engineering (ICSE) Artifact Evaluation Track` | The track page |
| Workshop | `Agentic Engineering (AGENT), Co-located with ICSE` | The workshop home page |
| Workshop with its own site | `Infrastructure for Trustworthy Software Agents (AGENTVERIFY), Co-located with ICSE` | The site that the researchr home page redirects to |

The `year` is the year of the conference. A role of a later year than any entry starts a new `# <year>` block at the top of the file.

Each PR description states what changed, the committee page as evidence, and the verification: the entry count of `_data/services.yml` against `main`, and a passing `bundle exec jekyll build` with the entry present in `_site/service/index.html` and `_site/news/index.html`.

## Limits

- Journals and venues outside researchr appear on the profile only where they were entered by hand, so the audit cannot find a missing journal role.
- The audit reads one direction. It does not list service entries that are absent from the profile.
