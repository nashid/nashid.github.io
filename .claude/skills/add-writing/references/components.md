# Writings Formatting Components

Exact, copy-paste HTML and Markdown for every component used in a Writings post. All supporting CSS already exists in `_sass/_writings.scss` (compiled to `/css/writings.css`, loaded only on Writings pages); reuse these classes verbatim so a new post looks identical to the existing ones. Do not add new styles, and never style Writings work in `css/main.scss` or `_sass/_layout.scss`: the rest of the site must stay untouched.

Raw HTML is allowed directly inside the Markdown body (kramdown passes it through). Keep the `<img>` `src` wrapped in the Liquid `prepend: site.baseurl` filter as shown.

The design system is deliberately restrained: an 18.5px serif body in a 640px column, one crimson accent with a small set of fixed jobs (link underlines, kicker marks, step numerals, timeline marks, aside rules, specimen labels), and hierarchy from scale and space rather than ornament. Do not add decorative devices beyond the components below; at most one accent component per screenful.

---

## Automatic (you write nothing)

These are applied by the `post` layout and the stylesheet. Do not hand-code them:

- **Header stack**: rendered from front matter as a kicker row ("Writings · <Month D, YYYY> · <N> min read"), the serif title, and an italic standfirst taken from `summary`, closed by a hairline rule. No byline: the site header above already identifies the author.
- **"On this page" rail**: a sticky contents list of the `##` headings, hanging in the right margin on wide screens; built by the layout, appears automatically once a post has two or more `##` sections.
- **Scholarly links**: body links render as ink text with a quiet crimson underline, crimson on hover.
- **Section rhythm**: `##` headings carry their own space above and hug the text below; no rules or ornaments.
- **Booktabs tables** and **drawn checklist squares**: any Markdown table or task list is styled automatically (see below).
- **Crimson text selection.**

There is deliberately no drop cap, no end-of-article mark, and no rule above headings. Those ornaments were tried and removed in the July 2026 redesign; do not reintroduce them.

---

## Hero image

Immediately after the front matter, before the first paragraph. No caption and no border by convention (corners are rounded by the stylesheet). Prefer restrained, low-saturation artwork; the page around it is calm.

```html
<figure class="writing-hero">
<img src="{{ "/resources/images/<slug>-hero.jpg" | prepend: site.baseurl }}" alt="Concrete description of the illustration." />
</figure>
```

For an inline figure later in the body, use `writing-figure`. A caption is optional (italic, centered):

```html
<figure class="writing-figure">
<img loading="lazy" src="{{ "/resources/images/<name>.jpg" | prepend: site.baseurl }}" alt="..." />
<figcaption>Optional caption.</figcaption>
</figure>
```

---

## Numbered step headings (process posts only)

When a post describes a genuine sequence, number the sections with a small overline label inside the heading. Do not use it for essays or non-sequential sections (they take a plain `##` heading).

```markdown
## <span class="step-num">Step 2</span> The external examiner: start earlier than feels necessary
```

---

## Caveat aside

For process/guide posts. A roman aside behind a thin crimson rule, styled to be read rather than skipped. Use this instead of a Markdown blockquote for "before you rely on this" disclaimers.

```html
<div class="post-epigraph">
<span class="post-epigraph-label">A note before you rely on this</span>
<p>Policies change and programs differ. This reflects my experience as a ..., checked against the <a href="https://authoritative-source">authoritative source</a> as of <Month Year>. When in doubt, trust it over this post.</p>
</div>
```

---

## Correspondence specimen

To quote an email or document verbatim. One small uppercase source line (the component name in crimson, the attribution after a middot), then the transcript in the body serif. No emoji. Anonymize senders. Keep bold only on the load-bearing words inside the quote.

```html
<div class="inbox-note">
<span class="inbox-note-meta"><b>What lands in your inbox</b> &middot; from the sender, anonymized, with context</span>
<p>&ldquo;Quoted text, verbatim, with <b>key words</b> in bold and an ellipsis where trimmed [&hellip;].&rdquo;</p>
</div>
```

---

## Step / interval timeline

A vertical chain of steps on a crimson rail with the interval between them called out. Each `<li>` may carry a title, an optional note, and an optional interval (omit the interval on the final step). The class name is historical; reuse it for any sequential timeline.

```html
<ul class="exam-timeline">
<li>
<span class="exam-step-title">First step</span>
<span class="exam-step-note">An optional note under the step.</span>
<span class="exam-interval">&darr;&nbsp; about 8 weeks</span>
</li>
<li>
<span class="exam-step-title">Middle step</span>
<span class="exam-interval">&darr;&nbsp; minimum 6&ndash;7 weeks</span>
</li>
<li>
<span class="exam-step-title">Final step</span>
<span class="exam-step-note">No interval after the last step.</span>
</li>
</ul>
```

---

## Booktabs table

Plain Markdown. Rendered with a heavy rule top and bottom, a thin rule under the header row, and no internal or vertical rules, as in a typeset paper.

```markdown
| Milestone | Lead time | Who drives it |
|---|---|---|
| First | ~8 weeks | You |
| Second | about a month | The office |
```

---

## Checklist

Plain Markdown task list. Rendered with hand-drawn hollow squares (not OS checkboxes).

```markdown
- [ ] First actionable item, specific and personal
- [ ] Second item
```

---

## Revision history

End matter, after the closing line. arXiv-style: the version lives here, not in the kicker. Link to the post's real commit history so corrections are auditable.

```html
<div class="post-revisions">
<span class="post-revisions-label">Revision history</span>
<p>v1 &middot; <Month D, YYYY> &middot; First published.</p>
<p>Corrections are versioned like a preprint; the <a href="https://github.com/nashid/nashid.github.io/commits/main/_writings/<slug>.md">full source history</a> of this post is public.</p>
</div>
```

On a substantive later revision, bump `version` in the front matter and add a line here (for example, "v2 · <date> · Corrected the external-examiner timeline.").

---

## Provenance (inline, not a component)

Attribution goes in the sentence itself, with a hyperlink to the source:

> The exams office is explicit about the tolerances: a few days late is fine, more than two weeks late and they may need to re-confirm your examiner. [link the source on a natural phrase]

Do not use margin notes, "Source ·" labels, or a footnote apparatus. That approach was tried and deliberately removed.
