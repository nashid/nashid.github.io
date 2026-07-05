---
title: "A Practical Guide to the UBC PhD Thesis Submission and Examination Process"
date: 2026-07-05
summary: "The tacit timeline behind a UBC doctoral defence — the departmental exam, the external examiner, the final oral defence, and the final submission — written down so the next student doesn't have to reverse-engineer it."
---

Every few months a labmate or colleague asks me how the final stretch of the UBC PhD actually works, and every time I find myself reconstructing the same timeline from memory and old emails. I defended in April 2026, so the process is still fresh. This post writes it down once, properly.

A theme of [my mentoring](/mentorship/) is that the biggest barriers in academia are often not ability but *access* — including access to the tacit knowledge that nobody writes down. The thesis endgame is full of exactly that: unwritten lead times, forms with long processing queues, and scheduling realities that can quietly cost you a graduation cycle. Consider this my attempt to make those norms explicit.

> **Before you rely on this:** policies change and programs differ. This reflects my experience as a PhD student in **Electrical and Computer Engineering (ECE)**, checked against the [Faculty of Graduate and Postdoctoral Studies (G+PS) pages](https://www.grad.ubc.ca/current-students/final-doctoral-exam) as of **July 2026**. The G+PS pages and your program assistant are authoritative — when in doubt, trust them over this post.

## The big picture

Between "my thesis is mostly written" and "I am officially done" there are four gates:

1. **The departmental exam** — an internal defence within your department (ECE requires one; the name and format vary by program).
2. **The external examination** — your dissertation is reviewed by an external examiner outside UBC.
3. **The final oral defence** — the university-level exam run by G+PS.
4. **The final submission** — the approved dissertation goes into [cIRcle](https://circle.ubc.ca/), UBC's open-access repository.

The single most useful planning fact: G+PS wants the **external examiner nomination roughly 8 weeks before** you submit the dissertation for external examination, and everything else stacks up behind that. G+PS publishes [suggested deadlines for each graduation cycle](https://www.grad.ubc.ca/current-students/final-doctoral-exam/doctoral-deadlines) — find your target cycle and work backwards from it on day one.

| Milestone | Typical lead time | Who drives it |
|---|---|---|
| Departmental exam | book ~4–6 weeks ahead; thesis to committee ≥1 week before | You + program |
| External examiner nomination | ~8 weeks before dissertation submission | Supervisor + grad advisor (you draft the list) |
| External review | about a month for the report | G+PS + examiner |
| Final oral defence | ~1–2 months after the dissertation goes out | G+PS |
| Final acceptance in cIRcle | submit ≥5 business days before your deadline | You |

## Step 0: Write in the right template from the start

UBC does **not** provide an official thesis template — only [formatting requirements](https://www.grad.ubc.ca/current-students/dissertation-thesis-preparation), which are checked strictly at final submission. There are community-maintained templates, offered without guarantees:

- **LaTeX**: [Michael Forbes' `ubcthesis` class](https://alum.mit.edu/www/mforbes/projects/ubcthesis/), an [updated Overleaf version by Jeremy Wong](https://www.overleaf.com/read/zxbgknhvbsts), and [Brian de Alwis' `ubcdiss`](https://github.com/briandealwis/ubcdiss)
- **Word**: the Koerner Library Research Commons template (linked from the [style guides and tools page](https://www.grad.ubc.ca/current-students/dissertation-thesis-preparation/style-guides-computer-tools))
- **R Markdown**: [`ubcdown`](https://github.com/jepa/ubcdown)

Pick one early and write in it from the beginning. Retrofitting a formatting-compliant document in the final month, while also handling committee revisions, is avoidable misery. You will also need a style guide (APA, Chicago, etc.) — that choice is made **with your supervisor**, not unilaterally.

## Step 1: The departmental exam

In ECE, before anything goes to G+PS, you defend internally. Mechanically it looks like a smaller version of the real defence:

- **Committee**: your advisor, two members of your supervisory committee, and a chair.
- **Scheduling is the hard part.** You need a slot where four busy academics are simultaneously available — start ~4–6 weeks out, and be extra generous in summer when everyone travels. In my case, scheduling started in mid-July for a late-August exam.
- **The thesis goes to the committee at least one week before the exam.** In practice, aim for more; a committee member who hasn't read it helps nobody.

Treat this exam as a genuine asset rather than a hurdle: it is the last round of substantive feedback before your dissertation is read by someone who has never met you. The revisions that come out of it are what make the external examination boring — which is what you want.

## Step 2: The external examiner (start earlier than feels necessary)

This is the step with the longest invisible lead time and the strictest rules, so it deserves the most care.

**How it works.** Your supervisor and the graduate program advisor nominate **at least two, preferably three** candidates using the [Nominations for External Examiner form](https://www.grad.ubc.ca/current-students/final-doctoral-exam/selecting-external-examiner), due roughly **8 weeks before** the dissertation is submitted for external examination. In practice, you draft a shortlist together with your supervisor well before that — for me this conversation happened in mid-July for a late-fall submission.

**Who is eligible.** An external examiner must hold the rank of full, associate, or emeritus professor at a comparable university, have an established reputation in the dissertation's research area, have prior experience supervising and examining doctoral students, and must not have acted as external examiner for a student of any of your committee members in the past three years.

**Who is *not* eligible (arm's length).** No co-authors or research collaborators from the past 6 years, no institutional colleagues from the past 6 years, no close friends or relatives, no former supervisors or prospective employers. Before proposing anyone, check your own co-author list — after years of collaboration it is longer than you remember.

**The confidentiality rules matter.** You may not contact potential examiners, and you are not supposed to know who the external examiner is until after the dissertation has been submitted. Nobody on your side may discuss your work with the examiner before the defence. Concretely: keep the shortlist between you, your supervisor, and the program — don't mention names in talks, on social media, or anywhere public. A leaked name can disqualify an examiner and cost you months.

## Step 3: The dissertation goes out

Once your supervisory committee approves the dissertation for external examination, G+PS sends it to the appointed examiner, who has **about a month** to read it and write a report. This is the quiet phase — a good time to prepare the defence talk and, frankly, to rest. Working backwards: if you want a spring program-end date, the dissertation typically needs to go out around **November/December**, which is why the examiner conversation starts in the summer.

## Step 4: The final oral defence

G+PS schedules the defence roughly **1–2 months after** the dissertation goes out, once the external's report is in. The examining committee combines your own committee with university examiners and a G+PS-appointed chair; the external's report is part of the record whether or not they attend. The [Doctoral Exam Guide](https://www.grad.ubc.ca/current-students/final-doctoral-exam) covers the mechanics, room, and format — read it once end-to-end the week you submit.

## Step 5: Final submission to cIRcle

After the defence you incorporate any required revisions, collect committee approval, and upload the final PDF to cIRcle. Details that surprise people:

- The PDF must be unsecured (no password protection), and **a scan is not acceptable**.
- G+PS reviews the formatting *after* you submit — **your program is not closed and you are not eligible to graduate until they approve it**, and corrections are common. G+PS itself recommends submitting **at least 5 business days before** your deadline; the deadline is for *approval*, not submission.
- Once accepted, **no changes are permitted** — proofread the final version as if it is permanent, because it is. It goes online within 3–4 days.

## The cadence, end to end

Roughly my own calendar, as one concrete instantiation:

- **Mid-July** — external examiner shortlist drafted with my supervisor; departmental exam scheduling begins
- **Late August** — departmental exam (thesis to the committee a week or more before)
- **September–October** — revisions from committee feedback; external examiner nomination submitted
- **November/December** — committee approves; dissertation submitted for external examination
- **+ ~1 month** — external report comes back
- **Late winter / spring** — final oral defence, revisions, cIRcle submission, done

## Checklist

- [ ] Writing in a formatting-compliant template from day one; style guide agreed with supervisor
- [ ] Target graduation cycle picked; worked backwards from the [G+PS deadlines](https://www.grad.ubc.ca/current-students/final-doctoral-exam/doctoral-deadlines)
- [ ] Departmental exam booked 4–6 weeks out; thesis to committee ≥1 week before
- [ ] External shortlist (2–3+ names) drafted with supervisor; arm's-length rules checked; kept confidential
- [ ] Nomination form in ~8 weeks before planned dissertation submission
- [ ] Defence talk prepared while the external reads
- [ ] Final PDF proofread; submitted to cIRcle ≥5 business days before the deadline

If you're navigating this at UBC — or anywhere, since most universities have an isomorphic process with different names — and something here doesn't match what you're seeing, [email me](mailto:nashid@ece.ubc.ca). I'd rather update this post than have you reverse-engineer it from scratch like I did.
