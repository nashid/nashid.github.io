# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Jekyll-based academic personal website hosted on GitHub Pages for Nashid Noor, a Postdoctoral Fellow in Software Engineering at UBC. The site showcases research publications, academic services, CV, and professional information.

## Git Conventions

**CRITICAL**: Never add "Generated with Claude Code" or "Co-Authored-By: Claude" attribution in commit messages or pull requests.

## GitHub Issues and Pull Requests

**CRITICAL**: Do NOT automatically close GitHub issues in commit messages or PR descriptions unless the user explicitly asks you to.

- **Never add** "Closes #XX" or "Fixes #XX" to commits or PRs unless specifically requested
- The user wants to examine changes on the live site before closing issues
- Let the user manually close issues after they verify the changes
- If unsure, ask the user if they want the issue auto-closed before adding the reference

## Technology Stack

- **Static Site Generator**: Jekyll (GitHub Pages)
- **Build Tool**: GitHub Pages automatically builds and deploys from the main branch
- **Markup**: Kramdown (Markdown processor)
- **Styling**: SASS/SCSS
- **Template Engine**: Liquid

## Development Commands

### Local Development
```bash
# Quick start with preview script (recommended)
./preview.sh

# OR manual commands:
# Install dependencies locally (requires Ruby and Bundler)
bundle install --path vendor/bundle

# Serve the site locally at http://localhost:4000
bundle exec jekyll serve

# Build the site (output to _site/)
bundle exec jekyll build
```

### Testing Changes
The site is automatically deployed to GitHub Pages when changes are pushed to the main branch. To preview locally before pushing, use `./preview.sh` or `bundle exec jekyll serve`.

## Architecture

### Site Structure

The website follows Jekyll's convention-based architecture:

- **`_config.yml`**: Site-wide configuration including personal information, social links, and Jekyll settings
- **`_data/`**: YAML files containing structured content:
  - `papers.yml`: Research publications organized by year
  - `awards.yml`: Awards and honors with highlighting support
  - `talks.yml`: Conference presentations and invited talks
  - `services.yml`: Academic service roles (PC member, reviewer positions)
  - `projects.yml`, `courses.yml`, `maplers.yml`: Additional structured data (currently empty)
- **`_layouts/`**: HTML templates that wrap content:
  - `default.html`: Base layout with header, footer, and SVG icons
  - `page.html`: Simple page wrapper
  - `post.html`: Blog post layout
- **`_includes/`**: Reusable HTML components:
  - `header.html`: Site navigation
  - `footer.html`: Footer content
  - `svg.html`: Icon definitions
  - `functions/`: Liquid template helper functions
- **`_sass/`**: SCSS stylesheets for site styling
- **`_writings/`**: Long-form essays/blog posts (Jekyll collection, rendered at `/writings/<filename>/` with the `post` layout)
- **`nav/`**: Navigation pages (awards, papers, teaching, mentorship, service, CV, writings, news)
- **`resources/`**: Static assets (PDFs, images)
- **`preview.sh`**: Local development helper script with auto-reload

### Site Header

The site header (`_includes/header.html`) displays:
- **Name**: `{{ site.title }}, Ph.D.` (displays as "Nashid Noor, Ph.D." in bold)
- **Position**: "Postdoctoral Fellow in Software Engineering"
- **Department**: Electrical and Computer Engineering
- **Institution**: University of British Columbia (linked)
- **Contact**: Email and location
- **Social Links**: LinkedIn, GitHub, Twitter, DBLP, Google Scholar

The `.large-name` class in `_sass/_layout.scss` makes the name bold and larger.

### Content Flow

1. **Publications**: Defined in `_data/papers.yml` and rendered via `nav/papers.md` using Liquid loops
2. **Awards & Talks**: Defined in `_data/awards.yml` and `_data/talks.yml`, rendered via `nav/awards.md` with two sections
3. **Services**: Defined in `_data/services.yml` and rendered similarly
4. **News**: Timeline format in `nav/news.md` with divs for different event types
5. **Home Page**: `index.md` contains the about section with bio and selected publications
6. **Navigation**: Pages in `nav/` directory are linked via the header and use YAML front matter for layout and metadata

### Key Conventions

- All pages use YAML front matter to specify layout, title, weight (for ordering), and group
- The `weight` parameter controls navigation order in the header:
  - About (weight: 1)
  - Awards (weight: 2)
  - Papers (weight: 3)
  - Teaching (weight: 4)
  - Mentorship (weight: 5)
  - Service (weight: 6)
  - CV (weight: 7)
  - Writings (weight: 8) — tab hidden until `_writings/` has at least 3 entries (see below)
  - News (weight: 9)
- PDF files are stored in `resources/papers/` and referenced by paper ID from `papers.yml`
- Images are stored in `resources/images/`

## Content Updates

### Adding a New Publication
1. Edit `_data/papers.yml`
2. Add a new entry with: `id`, `title`, `authors`, `venue`, `year`
3. Optional fields: `award`, `doi`, `code`, `video`, `pages`
4. Place the PDF in `resources/papers/{id}.pdf`

### Adding News Items
Edit `nav/news.md` and add a new timeline item div with appropriate class (service, award, paper, talk, travel), date, icon, and content. Structure:
```html
<div class="timeline-item [type]">
  <div class="timeline-icon">
    <img src="{{ "/resources/images/icon-[name].svg" | prepend: site.baseurl }}" alt="[Alt]">
  </div>
  <div class="timeline-date">[Month Year]</div>
  <div class="timeline-content">
    [Content here...]
  </div>
</div>
```
Available timeline item types: `service`, `award`, `paper`, `talk`, `travel`, `position`

### Adding a Writing (Essay/Blog Post)
**Preferred: run `/add-writing`**, which handles all of the below in house style. The manual steps, for reference:
1. Copy `.claude/skills/add-writing/references/template.md` to `_writings/<slug>.md`. Front matter: `title`, `date` (YYYY-MM-DD), `summary` (one-two sentences, shown on the listing page and as the og:description); optional `image` (og/social card + hero) and `version` (arXiv-style integer metadata; bump it on substantive revisions and add a matching line to the post's revision-history block at the bottom; the version is not shown in the kicker)
2. Write the body in Markdown; it renders with the `post` layout at `/writings/<slug>/`
3. The `/writings/` listing page (`nav/writings.md`) picks it up automatically, sorted newest first
4. Content guidelines: evergreen over timely; never include confidential details (e.g., external examiner names or committee deliberations); add a "last verified" note to process-dependent posts
5. **Follow `WRITING-STYLE-GUIDE.md`** for voice, punctuation, and emphasis rules (notably: no em-dashes, no contractions, simple formal academic wording)
6. **Scope rule (hard requirement)**: Writings styling lives exclusively in `_sass/_writings.scss`, compiled to `/css/writings.css` and loaded only on `/writings/` pages (conditional in `_includes/head.html`). Never style Writings work in `css/main.scss` or `_sass/_layout.scss`, and never let Writings changes affect any other page of the site

**Writings nav tab visibility**: The Writings tab is hidden from the header nav until `_writings/` contains at least 3 posts (threshold check in `_includes/header.html`). Individual post URLs and `/writings/` remain live and shareable regardless — only the nav tab is affected. The tab appears automatically when the 3rd post is added; no other change is needed.

### Adding Awards
1. Edit `_data/awards.yml`
2. Add a new entry with: `year`, `title`, `description`, `highlight` (true/false for gold styling), `website`
3. Awards with `highlight: true` are displayed in gold to emphasize distinguished achievements

### Adding Talks/Presentations
1. Edit `_data/talks.yml`
2. Add a new entry with: `year`, `title`, `location` (optional), `description`, `type` (conference/invited), `website`
3. Link to specific paper presentation pages, not general conference homepages
4. Talks are automatically sorted by year (newest first)

### Adding Service Roles
Edit `_data/services.yml` with: `name`, `role`, `year`, `website`

### Updating Teaching/Mentoring
Edit `nav/teaching.md` to add:
- Teaching Assistant experience (course code, name, institution, description)
- Research mentoring (student name, degree/role, year, advisor link)

### Updating Personal Information
Edit `_config.yml` to update contact info, affiliations, or social media links.

## Claude Code Automation Skills

The repository includes custom Claude Code skills to automate repetitive tasks. Skills are located in `.claude/skills/`.

### Available Skills

#### `/add-service` - Automate Service Role Addition
Streamlines adding academic service roles (PC memberships, reviewerships) to both the services page and news timeline.

**Usage**: Type `/add-service` and answer the interactive prompts.

**Features**:
- Automatically updates both `_data/services.yml` and `nav/news.md`
- Smart filtering: Adds news for conferences only, skips journals
- Prestigious venue detection: Special emphasis for ASE, ICSE, FSE
- Creative variations: 10+ templates to keep announcements fresh
- Never guesses dates: Always asks for confirmation
- Maintains proper ordering (prestigious venues first)

**Documentation**: See `ADD-SERVICE-SKILL-GUIDE.md` for detailed usage instructions.

#### `/add-writing` - Author a Writings Post in House Style
Drafts and formats a new long-form post in `_writings/` so every piece is written and typeset identically.

**Usage**: Type `/add-writing` and answer the interactive prompts.

**Guarantees consistency via three artifacts** (all version-controlled):
- `WRITING-STYLE-GUIDE.md` (repo root) - voice, punctuation, emphasis (no em-dashes, no contractions, simple formal academic wording)
- `.claude/skills/add-writing/references/components.md` - exact copy-paste HTML for every formatting component
- `.claude/skills/add-writing/references/template.md` - the canonical post skeleton to fill in

**Features**:
- Starts from a fixed template so section order and structure never drift
- Enforces the modernized journal-offprint page style (Plex Serif body in a 640px column, kicker row with reading time, standfirst, author chip, numbered step headings, booktabs tables, correspondence specimens, revision history)
- Verifies process facts against primary sources and links them inline
- Optimizes the hero image and wires it as the social-card image
- Builds, checks for style violations, and opens a PR

### Creating New Skills
To add a new automation skill:
1. Create a directory in `.claude/skills/` (e.g., `skill-name/`)
2. Add a `SKILL.md` file with YAML frontmatter and skill instructions
3. Test with `/skill-name` command
4. Document in this file and create a user guide

For detailed skill creation instructions, see [Claude Code Skills Documentation](https://code.claude.com/docs/en/skills)

## Important Notes

- The site is deployed via GitHub Pages, so only GitHub Pages-compatible plugins work
- Changes to `_config.yml` require a full site rebuild (restart `jekyll serve`)
- The site uses Liquid templating for dynamic content generation
- **Site Keywords**: Software Engineering, Software Testing, Program Analysis, Agentic AI, Large Language Models, Deep Learning
- **Excluded Files**: The following files are excluded from Jekyll processing via `_config.yml`:
  - `CLAUDE.md` - Claude Code instructions
  - `TODO.md` - Personal task list
  - `README.md` - Repository readme
  - `ADD-SERVICE-SKILL-GUIDE.md` - Skill documentation (internal use only)
  - Development files (Gemfile, vendor/, .bundle/, preview.sh)
