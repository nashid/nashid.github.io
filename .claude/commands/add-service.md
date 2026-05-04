# Add Academic Service Role

You are a skilled assistant helping to add academic service roles (PC memberships, reviewerships) to both the services page and news timeline of an academic website.

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

For these, add phrases like "one of the premier venues in software engineering" or "top-tier software engineering conference"

## News Entry Templates

Randomly select from these templates to keep variety:

### Standard Templates:
- "I am serving as a PC member for [Conference]."
- "I joined the PC of [Conference]. Have a look at the CfP and consider submitting your research!"
- "Excited to serve on the program committee for [Conference]."
- "Looking forward to reviewing submissions for [Conference] as a PC member."
- "Honored to be part of the [Conference] program committee."
- "I will be serving as a PC member for [Conference]."
- "Delighted to join the program committee of [Conference]."

### Prestigious Venue Templates:
- "I am honored to serve as a PC member for [Conference], one of the premier venues in software engineering."
- "Thrilled to join the PC of [Conference], a top-tier software engineering conference."
- "Excited to be part of [Conference], one of the flagship conferences in our field."

### Special Recognition Templates (if applicable):
- "Selected as one of [X] junior PC members out of [Y] nominations for [Conference]."
- "Invited to serve as distinguished reviewer for [Journal]."

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
   - Add creative news entry with appropriate template
   - Use special emphasis for prestigious venues
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
- ALWAYS vary the news wording - don't use the same template repeatedly
- ONLY add news for conferences/workshops, NOT for journals
- ALWAYS emphasize prestigious venues (ASE, ICSE, FSE) with special wording
- Maintain chronological order in news (newest first within each year)
- Maintain the service organization (prestigious venues first in services.yml)

## Error Handling

- Check if service already exists before adding
- Verify URLs are valid format
- Ensure dates are in correct format (Month Year)
- Confirm year matches between service and news entry

Remember: The goal is to automate the repetitive task while maintaining creativity and accuracy in the announcements!