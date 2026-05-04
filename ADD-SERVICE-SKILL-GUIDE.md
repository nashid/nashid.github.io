# 🚀 Add-Service Skill Guide

## Overview
The `/add-service` skill automates adding academic service roles to both your services page and news timeline, with creative varied announcements.

## How to Use

### Step 1: Invoke the Skill
Simply type:
```
/add-service
```

### Step 2: Answer Questions
The skill will ask you for:
1. **Service type** (Conference PC, Journal Reviewer, etc.)
2. **Venue name** (e.g., "ASE 2026 Tools and Datasets Track")
3. **Year** (e.g., 2026)
4. **Website URL**
5. **For conferences only:**
   - When it should appear in news (e.g., "May 2026")
   - Any special track information

### Step 3: Review & Approve
The skill will:
- Add the service to `_data/services.yml`
- Create a creative news announcement (for conferences only)
- Generate a PR for you to review

## Features

### 🎯 Smart Detection
- **Prestigious venues** (ASE, ICSE, FSE) get special emphasis
- **Journal reviews** are added to services only (no news)
- **Conference PCs** get both service entry and news announcement

### 🎨 Creative Variations
The skill uses varied templates to keep announcements fresh:
- "I am honored to join the PC of..."
- "Excited to serve as a PC member for..."
- "Looking forward to reviewing submissions for..."
- And many more!

### 🏆 Special Recognition
For distinguished roles, it uses special wording and trophy icons

### 📅 No Date Guessing
The skill will ALWAYS ask you for the news date - never assumes

## Examples

### Example 1: Conference PC
```
/add-service
> Service type? Conference PC Member
> Venue? ASE 2026 Tools and Datasets Track
> Year? 2026
> Website? https://conf.researchr.org/track/ase-2026/...
> News date? May 2026
> Special info? Tools and Datasets Track
```

Result:
- Services.yml: Added at top (prestigious venue)
- News: "I am honored to serve as a PC member for ASE 2026 Tools and Datasets Track, one of the premier venues in software engineering."

### Example 2: Journal Review
```
/add-service
> Service type? Journal Reviewer
> Venue? IEEE Transactions on Software Engineering
> Year? 2026
> Website? https://www.computer.org/tse
```

Result:
- Services.yml: Added to journal section
- News: Nothing added (journals don't get news)

## Directory Structure
```
nashid.github.io/
├── .claude/
│   └── commands/
│       └── add-service.md    # The skill definition
├── _data/
│   └── services.yml          # Where services are stored
└── nav/
    └── news.md               # Where news is displayed
```

## Customization

To modify the skill behavior, edit `.claude/commands/add-service.md`:
- Add new templates in the "News Entry Templates" section
- Add venues to the "Prestigious Venue Detection" list
- Modify icons in the "Icon Selection" section

## Benefits

✅ **Saves time**: No more manual dual updates
✅ **Prevents errors**: No forgotten news announcements
✅ **Maintains consistency**: Proper formatting and ordering
✅ **Adds variety**: Creative, varied announcements
✅ **Smart filtering**: Skips journals automatically

## Tips

1. **Be specific** about tracks (e.g., "Industry Track", "Tools Demo")
2. **Use full names** for conferences on first mention
3. **Include month and year** for news dates (e.g., "March 2026")
4. **Check the PR** before merging to ensure everything looks good

## Troubleshooting

- **Skill not found?** Make sure you're in the repo root directory
- **Duplicate service?** The skill checks for existing entries
- **Wrong position?** Prestigious venues (ASE, ICSE, FSE) go to the top

---

Happy automating! 🎉 This skill will save you time and keep your website consistently updated.