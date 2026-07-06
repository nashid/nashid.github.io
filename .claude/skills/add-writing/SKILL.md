---
name: add-writing
description: Author a new long-form Writings post in the site's exact house style and journal-offprint formatting. Use when adding an essay or guide to _writings/ (e.g. "add a writing", "write a new blog post", "draft a Writings piece"). Enforces the writing style guide (no em-dashes, no contractions, simple formal academic wording) and the established typographic components.
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash
  - AskUserQuestion
  - WebFetch
  - WebSearch
---

# Add a Writing

You are helping author a new long-form post in the `_writings/` collection of this academic site. Every piece must read as if written by the same person and be typeset with the same components as the existing posts. This skill encodes both.

Three companion documents are authoritative and must be followed:
- **`WRITING-STYLE-GUIDE.md`** (repo root) governs voice, punctuation, and emphasis. Read it before drafting.
- **`references/components.md`** (in this skill folder) holds the exact copy-paste HTML for every formatting component. Read it before formatting.
- **`references/template.md`** (in this skill folder) is the canonical post skeleton. Copy it into `_writings/<slug>.md` and fill it in; keep the section order so every post is consistent.

The supporting CSS already lives in `_sass/_layout.scss`; do not add new styles. Reuse the existing classes so a new post looks identical to the first.

## The Page Style (why every post looks the same)

Consistency is not optional; it is the point. Every Writings post is typeset as a **journal offprint** and shares one fixed visual system. Do not redesign per post. The system is:

- **Family**: IBM Plex Serif body, IBM Plex Sans for labels/kickers, IBM Plex Mono for transcripts. One accent colour, deep crimson `#96172E`, used sparingly. Warm off-white page.
- **Fixed page furniture** (applied by the `post` layout and stylesheet, never hand-coded): the "Writings · <Month Year>" kicker, the serif title over a hairline rule, the crimson drop cap on the first paragraph, a crimson rule above every `##`, ink-coloured links with a quiet crimson underline, and the end-of-article mark ∎.
- **A fixed component palette** for everything else (epigraph, correspondence specimen, step/interval timeline, booktabs table, drawn-square checklist, revision history). Use these and only these; see `references/components.md`.
- **What is banned**, because it reads as generic: emoji in the prose or components, coloured callout cards, left-bar blockquotes, sidebars, rounded image corners, margin-note "Source" apparatus, and any new bespoke styling. These were each tried and removed.

If a post seems to need a component that does not exist, prefer restraint (plain prose) over inventing one. Raise it with the user before adding any new style to `_sass/_layout.scss`.

## Task Overview

When invoked with `/add-writing`, you will:
1. Gather the topic, sources, and shape of the piece
2. Verify any process or factual claims against primary sources
3. Draft the post in the house style, saved to `_writings/<slug>.md`
4. Format it with the established components
5. Optimize any images and wire the hero as the social-card image
6. Build, verify style compliance, and open a PR

## Step 1: Gather Information

Use AskUserQuestion to collect what you cannot infer. Ask only what you need:

- **Topic and working title**: what is the piece about?
- **Type**: is it a *process/how-to guide* (needs a caveat epigraph and a "last verified" posture, and its facts must be verified against primary sources) or a *reflection/essay* (no caveat needed)?
- **Source material**: does the user have notes, emails, a PDF, or links to draw from? These become the spine and the provenance. Ask them to point you to files or paste text.
- **Hero image**: is there one, should the user generate one, or none? If they want to generate one, offer detailed prompts (see Images below).
- **Audience**: who is it for? This sets how much to explain.

Do not ask about mechanics you can decide yourself (slug, date, file location).

## Step 2: Verify Facts (process/guide posts)

If the piece states processes, deadlines, numbers, or institutional rules, verify each against the authoritative source with WebFetch before writing it down. Link that source inline in the prose. Never state a policy number from memory. Add a caveat epigraph ("checked against X as of <Month Year>") and keep the piece evergreen.

Provenance rule: attribution goes **inline in the sentence, with a hyperlink** to the source. Do not use margin notes, footnote apparatus, or "Source ·" labels; that approach was tried and removed.

## Step 3: Start From the Template

Copy `references/template.md` into `_writings/<slug>.md`, where `<slug>` is short, kebab-case, and descriptive. The template already carries the front matter and the canonical section order; fill it in rather than composing structure from scratch. Front matter fields:

```yaml
---
title: "Full Title in Sentence Case With Key Terms"
date: YYYY-MM-DD
summary: "One or two sentences. Shown on the /writings/ listing and used as the og:description and meta description. Follow the style guide here too (no em-dashes, no contractions)."
image: /resources/images/<slug>-hero.jpg   # optional; enables the hero + social card
version: 1                                  # optional; arXiv-style, shown only in the revision-history block
---
```

The `post` layout is applied automatically (via `_config.yml` defaults), which renders the kicker, serif title, drop cap, and end-of-article mark. You do not add those.

## Step 4: Write in the House Style

Read `WRITING-STYLE-GUIDE.md` and follow it exactly. The non-negotiables:

- Simple formal academic wording. First person. Direct, not stilted ("I think", not "One might consider").
- **No em-dashes.** Use a comma, colon, period, or parentheses. En-dashes in numeric ranges (6–7 weeks) are fine.
- **No contractions.** Write "do not", "it is", "you are". Possessives ("the examiner's report") are correct and required.
- Mix short and long sentences. Bold only load-bearing facts, sparingly. Italics for a word you would stress aloud or a term used as a term.
- Trust the reader; do not explain the obvious, preach, or pad with generic advice. State uncertainty plainly.
- Never include confidential material (names under embargo, private deliberations, personal contact details of others).

## Step 5: Format With the Components

Read `references/components.md` for exact, copy-paste HTML. The palette, in the order it typically appears:

1. **Hero figure** (`figure.writing-hero`) right after the front matter, before the first paragraph.
2. **Opening paragraph** in plain prose. The drop cap and small-caps are automatic; write normally.
3. **Caveat epigraph** (`div.post-epigraph`) for process posts: an indented italic headnote under a small-caps label. Replaces any "disclaimer" blockquote.
4. **Body** in `##`/`###` sections. Each `##` automatically gets a crimson rule above it.
5. **Correspondence specimen** (`div.inbox-note`) to quote an email or document verbatim: small-caps label, a "From:" line, and the transcript in mono. No emoji.
6. **Step/interval timeline** (`ul.exam-timeline`) for a sequential chain with intervals between steps. (The class name is historical; reuse it for any timeline.)
7. **Tables**: plain Markdown tables, automatically styled as booktabs (horizontal rules only).
8. **Checklist**: plain Markdown task list (`- [ ]`), automatically rendered with drawn squares.
9. **Revision history** (`div.post-revisions`) as end matter, linking to the post's real GitHub commit history.
10. **Closing line**: a direct invitation to email corrections, which fits the evergreen posture.

Provenance stays inline with links (Step 2). Do not reintroduce margin notes.

## Step 6: Images

If a hero or figure image is provided:
1. Optimize it into `resources/images/`: roughly 1400px wide, JPEG quality ~82, target under ~200KB. Example: `sips -s format jpeg -s formatOptions 82 --resampleWidth 1400 <src>.png --out resources/images/<slug>-hero.jpg`
2. Set `image: /resources/images/<slug>-hero.jpg` in the front matter so it becomes the hero and the `og:`/Twitter card.
3. Write descriptive alt text.

If the user wants an AI-generated image, offer detailed prompts: flat minimalist editorial illustration, warm off-white (#FDFDFD) background, deep crimson (#96172E) as the sole accent, muted greys, no text/letters/watermark in the image, 2:1 for a hero. Ask them to generate and drop the file in the repo; you place and optimize it. Do not use two similar images in one post.

## Step 7: Verify

1. Build: `bundle exec jekyll build` and confirm it completes cleanly.
2. Style check the rendered article body. Both counts must be zero:
   - em-dashes: `grep -o "—" _site/writings/<slug>/index.html | wc -l`
   - contractions: `grep -oE "’(t|re|ll|ve|s|m|d)\b|n’t" _site/writings/<slug>/index.html | wc -l` (inspect any hits; possessive `'s` is allowed, contractions are not)
3. Confirm the post appears on `/writings/` and every link resolves.

## Step 8: Publish

Follow the repo's git conventions (see `CLAUDE.md`):
- Branch: `add-writing-<slug>` (or a short descriptive name).
- Commit message: describe the post; **never** add "Generated with Claude Code" or "Co-Authored-By: Claude".
- **Never** add "Closes #XX" / "Fixes #XX" unless the user explicitly asks.
- Push and open a PR summarizing the piece and its components.

Note the Writings nav tab stays hidden until `_writings/` holds at least 3 posts (threshold in `_includes/header.html`); the post URL is live and shareable regardless. Mention this to the user if this post does not yet cross the threshold.

## Important Rules

- Read `WRITING-STYLE-GUIDE.md` and `references/components.md` before drafting and formatting; do not work from memory.
- Reuse existing CSS classes; do not invent new styles or components.
- Verify every process fact against a primary source and link it inline.
- Evergreen over timely. Never publish confidential material.
- Show the draft locally (`./preview.sh`) and let the user review before you commit.
