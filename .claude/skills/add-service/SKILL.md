---
description: Automate adding academic service roles (PC memberships, reviewerships) to both the services page and news timeline with varied announcements built on facts
allowed-tools:
  - Read
  - Edit
  - Write
  - AskUserQuestion
  - Bash
  - WebFetch
---

# Add Academic Service Role

You are helping to add academic service roles (PC memberships, reviewerships) to both the services page and news timeline of an academic website with varied announcements built on facts.

## Task Overview
When invoked with `/add-service`, you will:
1. Gather information about the new service role
2. Add it to `_data/services.yml` in the appropriate position
3. For conference PC roles (NOT journal reviews), also add a news announcement
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

The list covers the tracks of these three conferences. It does not cover workshops and other events co-located with them.

Give the emphasis through a fact where the venue pages provide one, such as the edition or the place of the track within the conference. Where they provide none, add the clause "one of the premier venues in software engineering" after the name of the venue, as the ASE 2026 item does: "I am serving as a PC member for ASE 2026 Tools and Datasets Track, one of the premier venues in software engineering." The clause fits any form that names the venue in its first sentence. It is the one exception to the words to avoid below: the site already uses it, and it is limited to these three venues.

## News Wording

Every service news item opens differently from the items near it, and its interest comes from facts. The language is simple, formal, and academic. A reader of the timeline sees the items one below the other, so a repeated opening is noticed at once.

A service item is a news item that announces a committee role or a reviewing role. The form of an item is its opening words together with the order of its parts. Two items that open with the same words have the same form, whatever follows.

### Procedure

1. Fetch the track page and the home page of the venue. If a page does not exist, tell the user, and carry no fact over from an earlier edition.
2. Read the five service items nearest to the place of the new item in `nav/news.md`, and note the opening of each.
3. Choose a form from the two tables below whose condition holds and which none of the five uses.
4. Fill the form with facts. An item carries at most three facts, counting those that the form itself holds.
5. Add a closing sentence only where Closing sentences allows one.

The conditions refer to the news date. The reviewing has ended once the venue has notified its authors.

### Forms in use on the site

| Opening | Example | Condition |
| --- | --- | --- |
| "I am serving as a PC member for" | "I am serving as a PC member for Mining Software Repositories (MSR) Technical Papers 2027, the main research track of the conference." | The reviewing has not ended |
| "I joined the program committee of" | "I joined the program committee of AGENTVERIFY 2027, the International Workshop on Infrastructure for Trustworthy Software Agents at ICSE 2027. The workshop studies how harnesses and benchmarks shape the behavior of software agents. Full papers are due on November 6, 2026." | The reviewing has not ended |
| The name of the venue | "AISM 2026, the 2nd International Workshop on AI for Software Modernization, addresses the use of AI to understand and transform legacy systems, for example the migration of COBOL applications to Java. I served on its program committee. The workshop takes place at ASE 2026 in Munich, Germany." | None. The second sentence takes the tense that fits |
| "I served as a PC member for" | "I served as a PC member for ReSAISE 2026, the 4th IEEE International Workshop on Reliable and Secure AI for Software Engineering, co-located with ISSRE 2026 in Limassol, Cyprus." | The reviewing has ended |

The first opening begins nineteen items on the site, with a fact after the venue or without one. Choose it rarely.

### Further forms

| Opening | Pattern | Condition |
| --- | --- | --- |
| "I accepted an invitation to" | "I accepted an invitation to the program committee of [Venue], [fact]." | The reviewing has not ended |
| "I return to" | "I return to the program committee of [Venue] for a [third] year. [Fact]." | `_data/services.yml` lists the same conference or workshop, in any track, in each of the preceding years that the number counts |
| "[Venue] meets in" | "[Venue] meets in [City] in [Month Year]. I am a member of its program committee." | A venue page states the place and the dates |
| "Submissions to" | "Submissions to [Venue or track] are due on [date]. I serve on its program committee, and the call covers [subject]." | The deadline of that track is still ahead |
| "For [Venue], I review in" | "For [Venue], I review in the [Track] track, which [what the track does]." | The role belongs to one track of a conference |
| "I was selected as" | "I was selected as one of [X] junior PC members out of [Y] nominations for [Venue]." | The venue reports the numbers |

The link covers the name of the venue, together with the track where the two stand side by side.

### Facts

Take each fact from a venue page or from `_data/services.yml`, and state only what the source states. Leave out a fact that a page states in two conflicting ways.

- The subject that the venue or the track studies
- The place of the track within the venue, such as the main research track
- The edition
- The host conference, the place, and the dates
- A deadline that is still ahead
- The number of years served, counted in `_data/services.yml`
- The numbers of a selection

### Closing sentences

Two closing sentences are in use on the site.

| Closing | Condition |
| --- | --- |
| "Looking forward to reviewing the papers!" | The role reviews papers, and the reviewing has not ended |
| "Have a look at the CfP and consider submitting your research!" | The call is open, and the item does not already state the deadline |

Use a closing only when none of the five nearest service items carries one.

### Words to avoid

Do not open an item with Excited, Thrilled, Delighted, or Honored, and do not call a venue top-tier, flagship, or prestigious. Such a word reports a feeling or a rank, and the reader learns nothing about the venue from it. A fact does that work: the subject, the edition, the place, or the position of the track.

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

- NEVER infer or guess a date - ask the user for the news date, and take the dates and deadlines of a venue from its pages only
- ALWAYS vary the news wording - choose a form that none of the five nearest service items uses
- ONLY add news for conferences/workshops, NOT for journals
- ALWAYS emphasize prestigious venues (ASE, ICSE, FSE), through a fact where the venue pages provide one
- Maintain chronological order in news (newest first within each year)
- Maintain the service organization (prestigious venues first in services.yml)

## Error Handling

- Check if service already exists before adding
- Verify URLs are valid format, and fetch each one to confirm that the page exists
- Ensure dates are in correct format (Month Year)
- Confirm year matches between service and news entry

Remember: The goal is to automate the repetitive task while maintaining variety and accuracy in the announcements!