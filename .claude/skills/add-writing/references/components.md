# Writings Formatting Components

Exact, copy-paste HTML and Markdown for every component used in a Writings post. All supporting CSS already exists in `_sass/_layout.scss`; reuse these classes verbatim so a new post looks identical to the existing ones. Do not add new styles.

Raw HTML is allowed directly inside the Markdown body (kramdown passes it through). Keep the `<img>` `src` wrapped in the Liquid `prepend: site.baseurl` filter as shown.

---

## Automatic (you write nothing)

These are applied by the `post` layout and the stylesheet. Do not hand-code them:

- **Kicker and serif title**: rendered from front matter as "Writings · <Month Year>" above the title.
- **Drop cap**: the first letter of the first paragraph. Just start the post with a normal paragraph.
- **End-of-article mark (∎)**: appended to the last paragraph automatically.
- **Section rule**: a short crimson rule is drawn above every `##` heading.
- **Scholarly links**: body links render as ink text with a quiet crimson underline, crimson on hover.
- **Booktabs tables** and **drawn checklist squares**: any Markdown table or task list is styled automatically (see below).
- **Typographic detail**: oldstyle figures in prose, lining tabular figures in tables, soft hyphenation, crimson text selection.

---

## Hero image

Immediately after the front matter, before the first paragraph. No caption by convention.

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

## Caveat epigraph

For process/guide posts. An indented italic headnote under a small-caps label, no box and no rule. Use this instead of a Markdown blockquote for "before you rely on this" disclaimers.

```html
<div class="post-epigraph">
<span class="post-epigraph-label">A note before you rely on this</span>
<p>Policies change and programs differ. This reflects my experience as a ..., checked against the <a href="https://authoritative-source">authoritative source</a> as of <Month Year>. When in doubt, trust it over this post.</p>
</div>
```

---

## Correspondence specimen

To quote an email or document verbatim. Small-caps label, a "From:" attribution line, and the transcript set in mono. No emoji. Anonymize senders. Keep bold only on the load-bearing words inside the quote.

```html
<div class="inbox-note">
<span class="inbox-note-eyebrow">What lands in your inbox</span>
<span class="inbox-note-from">From: the sender, anonymized, with context</span>
<p>&ldquo;Quoted text, verbatim, with <b>key words</b> in bold and an ellipsis where trimmed [&hellip;].&rdquo;</p>
</div>
```

---

## Step / interval timeline

A vertical chain of steps with the interval between them called out. Each `<li>` may carry a title, an optional note, and an optional interval (omit the interval on the final step). The class name is historical; reuse it for any sequential timeline.

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

Plain Markdown. Rendered with a heavy rule top and bottom, a thin rule under a small-caps header row, and no vertical lines.

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

End matter, after the closing line. arXiv-style: the version lives here (not in the kicker). Link to the post's real commit history so corrections are auditable.

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
