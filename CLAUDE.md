# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Jekyll-based academic personal website hosted on GitHub Pages for Nashid Noor, a Ph.D. candidate at UBC. The site showcases research publications, academic services, CV, and professional information.

## Git Conventions

**CRITICAL**: Never add "Generated with Claude Code" or "Co-Authored-By: Claude" attribution in commit messages or pull requests.

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
- **`nav/`**: Navigation pages (awards, papers, teaching, service, CV, news)
- **`resources/`**: Static assets (PDFs, images)
- **`preview.sh`**: Local development helper script with auto-reload

### Content Flow

1. **Publications**: Defined in `_data/papers.yml` and rendered via `nav/papers.md` using Liquid loops
2. **Awards & Talks**: Defined in `_data/awards.yml` and `_data/talks.yml`, rendered via `nav/awards.md` with two sections
3. **Services**: Defined in `_data/services.yml` and rendered similarly
4. **Home Page**: `index.md` contains the about section and news timeline with direct HTML/Markdown content
5. **Navigation**: Pages in `nav/` directory are linked via the header and use YAML front matter for layout and metadata

### Key Conventions

- All pages use YAML front matter to specify layout, title, weight (for ordering), and group
- The `weight` parameter controls navigation order in the header:
  - About (weight: 1)
  - Awards (weight: 2)
  - Papers (weight: 3)
  - Teaching (weight: 4)
  - Service (weight: 5)
  - CV (weight: 6)
  - News (weight: 7)
- PDF files are stored in `resources/papers/` and referenced by paper ID from `papers.yml`
- Images are stored in `resources/images/`

## Content Updates

### Adding a New Publication
1. Edit `_data/papers.yml`
2. Add a new entry with: `id`, `title`, `authors`, `venue`, `year`
3. Optional fields: `award`, `doi`, `code`, `video`, `pages`
4. Place the PDF in `resources/papers/{id}.pdf`

### Adding News Items
Edit `index.md` and add a new `<tr>` entry to the news table with date, icon, and description.

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

## Important Notes

- The site is deployed via GitHub Pages, so only GitHub Pages-compatible plugins work
- Changes to `_config.yml` require a full site rebuild (restart `jekyll serve`)
- The site uses Liquid templating for dynamic content generation
- News items on the home page are manually curated in HTML format within `index.md`

## Future Improvements for Academic Job Hunting

### High Priority

- [ ] **Research Statement/Vision** - Add a dedicated section or expand research description with:
  - Clear research vision and future directions
  - What problems to solve in the next 5-10 years
  - How work fits into the broader SE landscape

- [ ] **Research Artifacts** - Add links to:
  - GitHub repositories for tools/frameworks
  - Datasets, benchmarks, or artifacts
  - Shows reproducibility and impact beyond papers

- [ ] **Talks/Presentations** - Add a section listing:
  - Conference presentations
  - Invited talks at other universities
  - Workshop presentations
  - Shows visibility and communication skills

### Medium Priority

- [ ] **Teaching Philosophy** - Expand the teaching page with:
  - Brief teaching statement or philosophy
  - More detail about TA responsibilities (e.g., "Led lab sections for 50+ students")
  - Any innovative teaching approaches or materials

- [ ] **Featured Projects** - Highlight 2-3 key research projects with:
  - Brief description
  - Impact/outcomes
  - Links to papers, code, demos

- [ ] **Contact Information** - Make it very prominent:
  - Email clearly visible on every page (header/footer?)
  - Links to Twitter/X, GitHub, Google Scholar
  - Currently might be buried in CV

### Lower Priority

- [ ] **Collaborators/Network** - Mention key collaborators or research group
- [ ] **Students Supervised** - Expand with thesis topics or outcomes
- [ ] **Grants/Funding** - If involved in any grant proposals
- [ ] **Diversity Statement** - Some positions require this (can be separate PDF)
- [ ] **Professional Photo** - Consider adding if comfortable
- [ ] **Research Highlights** - Add section on home page
- [ ] **Google Scholar Profile** - Link prominently
- [ ] **Citation Metrics** - Add h-index/citation count if strong
