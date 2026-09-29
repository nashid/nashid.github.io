---
description: Automate adding academic service roles (PC memberships, reviewerships) to both the services page and news timeline with creative varied announcements
allowed-tools:
  - Read
  - Edit
  - Write
  - AskUserQuestion
  - Bash
---

# Add Academic Service Role

You are helping to add academic service roles (PC memberships, reviewerships) to both the services page and news timeline of an academic website with creative, varied announcements.

## Task Overview
When invoked with `/add-service`, you will:
1. Gather information about the new service role
2. Add it to `_data/services.yml` in the appropriate position
3. For conference PC roles (NOT journal reviews), also add a creative news announcement
4. Create a commit and PR with both changes

## Information Gathering

Use the AskUserQuestion tool to collect ALL necessary information upfront:

### Required Information:
1. **Service Type**: Conference PC Member, Journal Reviewer, Workshop PC, etc.
2. **Venue Name**: Full conference/journal name
3. **Year**: Which year (e.g., 2026)
4. **Website URL**: Link to the conference/track/journal
5. **For Conference PCs Only**:
   - **News Date**: When should this appear in the news? (e.g., "May 2026", "December 2025")
   - **Track/Special Info**: Any specific track (e.g., "Tools and Datasets", "Industry Track")

## Service Categories

### Skip News for These (Journal/Ongoing Reviews):
- Empirical Software Engineering (EMSE)
- ACM Transactions on Software Engineering and Methodology (TOSEM)
- Information and Software Technology
- Journal of Systems & Software
- Science of Computer Programming
- Future Generation Computer Systems
- Computer Applications in Engineering Education
- Any other journal/magazine

### Add News for These:
- Conference PC memberships
- Workshop PC memberships
- Conference organizing roles
- Special tracks (Industry, Tools, Artifacts, etc.)

## Prestigious Venue Detection

These venues get special emphasis in news:
- **ICSE** (International Conference on Software Engineering)
- **FSE/ESEC** (Foundations of Software Engineering)
- **ASE** (Automated Software Engineering)

Give the emphasis through a fact where the venue page provides one, such as the standing of the track within the conference or the edition. The clause "one of the premier venues in software engineering" is also available for these three venues. Attach it to a plain opening, as the ASE 2026 item does: "I am serving as a PC member for ASE 2026 Tools and Datasets Track, one of the premier venues in software engineering."

## News Wording

Every service news item differs in form from the items near it, and its interest comes from facts. The language is simple, formal, and academic. A reader of the timeline sees the items one below the other, so a repeated sentence form is noticed at once.

### Procedure

1. Read the five most recent service items in `nav/news.md` and note the form of each.
2. Choose a form from the two tables below that none of the five uses.
3. Add one or two facts from the venue page.
4. Choose the tense by the state of the reviewing.
5. Add a closing sentence in some items only, so that it does not become a pattern of its own.

### Forms in use on the site

| Form | Example |
| --- | --- |
| Role, then a fact about the track | "I am serving as a PC member for Mining Software Repositories (MSR) Technical Papers 2027, the main research track of the conference." |
| Joined, then the subject, then the deadline | "I joined the program committee of AGENTVERIFY 2027, the International Workshop on Infrastructure for Trustworthy Software Agents at ICSE 2027. The workshop studies how harnesses and benchmarks shape the behavior of software agents. Full papers are due on November 6, 2026." |
| Venue first, role second | "AISM 2026, the 2nd International Workshop on AI for Software Modernization, addresses the use of AI to understand and transform legacy systems, for example the migration of COBOL applications to Java. I served on its program committee. The workshop takes place at ASE 2026 in Munich, Germany." |
| Past tense, with the edition and the place | "I served as a PC member for ReSAISE 2026, the 4th IEEE International Workshop on Reliable and Secure AI for Software Engineering, co-located with ISSRE 2026 in Limassol, Cyprus." |
| Joined, then a call for submissions | "I joined the PC of AIware 2026 (Main Track). Have a look at the CfP and consider submitting your research!" |
| Plain | "I am serving as a PC member for Internetware 2026 Research Track." |

The plain form is one option among the others. It opens twenty items on the site, so choose it rarely.

### Further forms

| Form | Pattern | Condition |
| --- | --- | --- |
| Invitation | "I accepted an invitation to the program committee of [Venue], [fact]." | None |
| Returning member | "I return to the program committee of [Venue] for a [third] year. [Fact]." | `_data/services.yml` lists the same venue in the previous year |
| Place and date first | "[Venue] meets in [City] in [Month Year]. I am a member of its program committee." | The venue page states the place and the dates |
| Deadline first | "Submissions to [Venue] are due on [date]. I serve on its program committee, and the call covers [subject]." | The deadline is still ahead |
| Track within the venue | "For [Venue], I review in the [Track] track, which accepts [kind of submission]." | The role belongs to one track of a conference |
| Selection, with the numbers | "Selected as one of [X] junior PC members out of [Y] nominations for [Venue]." | The venue reports the numbers |
| Distinguished role | "Invited to serve as distinguished reviewer for [Journal]." | The role carries that title |

In every form, the name of the venue carries the link.

### Facts

Take each fact from the venue page, and state only what the page states.

- The subject that the venue or the track studies
- The standing of the track within the venue
- The edition
- The host conference, the place, and the dates
- A deadline that is still ahead
- The number of years served, counted in `_data/services.yml`
- The numbers of a selection

### Tense

Use the present tense while the reviewing is ahead or under way. Use the past tense once the venue has notified its authors.

### Closing sentences

Two closing sentences are in use on the site: "Looking forward to reviewing the papers!" and "Have a look at the CfP and consider submitting your research!". The second applies only while the deadline is ahead.

### Words to avoid

Do not open an item with Excited, Thrilled, Delighted, or Honored, and do not call a venue top-tier, flagship, or prestigious. Such a word reports a feeling or a rank, and the reader learns nothing about the venue from it. A fact does that work: the subject, the edition, the place, or the standing of the track.

## Icon Selection

For news entries, use appropriate icons:
- 📝 `icon-memo.svg` - Standard PC membership
- 🏆 `icon-trophy-modern.svg` - Distinguished roles or special selections
- 🎯 `icon-target.svg` - Focused tracks (Industry, Tools)
- 🔬 `icon-research.svg` - Research track specifically

## Implementation Steps

1. **Gather Information**: Use AskUserQuestion to get all details
2. **Update services.yml**:
   - Read current file
   - Determine correct position (prestigious venues first in each year)
   - Add new entry with proper formatting
3. **Update news.md** (for conferences only):
   - Read current file
   - Find correct chronological position
   - Write the news entry by the procedure in News Wording
   - Give emphasis to prestigious venues as Prestigious Venue Detection describes
4. **Create PR**:
   - Branch name: `add-[conference-abbreviation]-[year]-[role]`
   - Commit message: "Add [Conference] [Year] [Role] to services and news"
   - PR body: Explain the addition and highlight if prestigious

## Position Logic for services.yml

Within each year section:
1. Prestigious conference PCs (ASE, FSE, ICSE) - at the top
2. Other conference PCs
3. Workshop PCs
4. Journal reviewer roles

## Example Execution

When user types `/add-service`:

1. Ask: "What type of service role? (Conference PC, Journal Reviewer, etc.)"
2. Ask: "What is the venue name?"
3. Ask: "What year?"
4. Ask: "What is the website URL?"
5. If conference PC: "When should this appear in the news? (e.g., May 2026)"
6. If conference PC: "Any specific track or additional info?"

Then proceed with adding to both files and creating PR.

## Important Rules

- NEVER infer or guess conference dates - always ask the user
- ALWAYS vary the news wording - choose a form that none of the five most recent service items uses
- ONLY add news for conferences/workshops, NOT for journals
- ALWAYS emphasize prestigious venues (ASE, ICSE, FSE), through a fact where the venue page provides one
- Maintain chronological order in news (newest first within each year)
- Maintain the service organization (prestigious venues first in services.yml)

## Error Handling

- Check if service already exists before adding
- Verify URLs are valid format
- Ensure dates are in correct format (Month Year)
- Confirm year matches between service and news entry

Remember: The goal is to automate the repetitive task while maintaining creativity and accuracy in the announcements!