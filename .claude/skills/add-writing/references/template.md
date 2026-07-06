<!--
  Writings post template. Copy this into _writings/<slug>.md and fill it in.
  This is the canonical skeleton: keep the section order so every post is consistent.
  Remove any optional block you do not use. HTML comments are guidance; delete them.
  Follow WRITING-STYLE-GUIDE.md for the prose and components.md for the components.
-->
---
title: "Full Title in Sentence Case"
date: YYYY-MM-DD
summary: "One or two sentences for the listing and social card. Style guide applies: no em-dashes, no contractions."
image: /resources/images/<slug>-hero.jpg   # optional; enables hero + og image. Remove if no image.
version: 1                                  # optional; shown only in the revision-history block below.
---

<!-- HERO (optional): first thing after front matter, before any prose. -->
<figure class="writing-hero">
<img src="{{ "/resources/images/<slug>-hero.jpg" | prepend: site.baseurl }}" alt="Concrete description of the illustration." />
</figure>

<!-- OPENING: a normal paragraph. The drop cap is automatic. State what this is and why it exists. -->
Opening paragraph.

Second paragraph, setting up the piece.

<!-- CAVEAT EPIGRAPH (process/guide posts only): replaces any "disclaimer" blockquote. -->
<div class="post-epigraph">
<span class="post-epigraph-label">A note before you rely on this</span>
<p>Policies change and circumstances differ. This reflects my experience, checked against <a href="https://authoritative-source">the authoritative source</a> as of <Month Year>. When in doubt, trust it over this post.</p>
</div>

## First section

Body prose. Verify any factual claim against a primary source and link it inline. Use `**bold**` only for load-bearing facts, and `*italics*` for a stressed word or a term used as a term.

<!-- Optional components, used where they fit (see references/components.md for exact markup):
     - div.inbox-note        quote an email or document verbatim, in mono, no emoji
     - ul.exam-timeline      a step chain with intervals between steps
     - a Markdown table      auto-styled as booktabs
-->

## Second section

More body prose.

## A quick-answers or checklist section (optional)

- [ ] Specific, personal, actionable item
- [ ] Another item

<!-- CLOSING: a direct line inviting corrections, consistent with the evergreen posture. -->
Closing paragraph. If something here does not match what you are seeing, [email me](mailto:nashid@ece.ubc.ca).

<!-- REVISION HISTORY: end matter. The version lives here, not in the kicker. -->
<div class="post-revisions">
<span class="post-revisions-label">Revision history</span>
<p>v1 &middot; <Month D, YYYY> &middot; First published.</p>
<p>Corrections are versioned like a preprint; the <a href="https://github.com/nashid/nashid.github.io/commits/main/_writings/<slug>.md">full source history</a> of this post is public.</p>
</div>
