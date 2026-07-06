---
title: "A Practical Guide to the UBC PhD Thesis Submission and Examination Process"
date: 2026-07-05
summary: "The tacit timeline behind a UBC doctoral defence: the departmental exam, the external examiner, the final oral defence, and the final submission, written down so the next student does not have to reverse-engineer it."
image: /resources/images/ubc-road-to-thesis.jpg
version: 1
---

<figure class="writing-hero">
<img src="{{ "/resources/images/ubc-road-to-thesis.jpg" | prepend: site.baseurl }}" alt="Illustration of a winding road climbing a mountain past crimson research milestones toward a doctoral cap at the sunlit summit, with the UBC clock tower and campus below." />
</figure>

Every few months a labmate or colleague asks me how the final stretch of the UBC PhD actually works, and every time I find myself reconstructing the same timeline from memory and old emails. I defended in April 2026, so the process is still fresh. This post writes it down once, properly.

The thesis endgame is full of the tacit knowledge that nobody writes down: unwritten lead times, forms with long processing queues, and scheduling realities that can quietly cost you a graduation cycle. Consider this guide my attempt to make those norms explicit for the last stretch of the UBC PhD, from the departmental exam to the final approved dissertation.

<div class="post-epigraph">
<span class="post-epigraph-label">A note before you rely on this</span>
<p>Policies change and programs differ. This reflects my experience as a PhD student in Electrical and Computer Engineering (ECE), checked against the <a href="https://www.grad.ubc.ca/current-students/final-doctoral-exam">Faculty of Graduate and Postdoctoral Studies (G+PS) pages</a> as of July 2026. The G+PS pages and your program assistant are authoritative; when in doubt, trust them over this post.</p>
</div>

## The big picture

Between "my thesis is mostly written" and "I am officially done" there are four gates:

1. **The departmental exam**: an internal defence within your department (ECE requires one; the name and format vary by program).
2. **The external examination**: your dissertation is reviewed by an external examiner outside UBC.
3. **The final oral defence**: the university-level exam run by G+PS.
4. **The final submission**: the approved dissertation goes into [cIRcle](https://circle.ubc.ca/), UBC's open-access repository.

The single most useful planning fact: G+PS wants the **external examiner nomination roughly 8 weeks before** you submit the dissertation for external examination, and everything else stacks up behind that. G+PS publishes [suggested deadlines for each graduation cycle](https://www.grad.ubc.ca/current-students/final-doctoral-exam/doctoral-deadlines); find your target cycle and work backwards from it on day one.

Once the nomination form is in, the exam office's own interval chain takes over. These numbers come straight from the welcome packet G+PS sends candidates: <span class="mn">G+PS welcome packet, p. 1</span>

<ul class="exam-timeline">
<li>
<span class="exam-step-title">Nominations for External Examiner form submitted</span>
<span class="exam-step-note">G+PS confirms receipt by email and starts inviting. You are here.</span>
<span class="exam-interval">&darr;&nbsp; about 8 weeks</span>
</li>
<li>
<span class="exam-step-title">Dissertation submitted to the G+PS Doctoral Exams Office</span>
<span class="exam-step-note">The &ldquo;Dissertation Transmit&rdquo; email tells you and your supervisor the earliest possible defence date; booking opens now.</span>
<span class="exam-interval">&darr;&nbsp; minimum 6&ndash;7 weeks</span>
</li>
<li>
<span class="exam-step-title">Oral defence day</span>
<span class="exam-step-note">University Examiner form and booking request go in at least 4 weeks before this day.</span>
<span class="exam-interval">&darr;&nbsp; usually about 1 month</span>
</li>
<li>
<span class="exam-step-title">Final submission approved</span>
<span class="exam-step-note">Program closed, degree awarded, done.</span>
</li>
</ul>

And the wider logistics around that chain:

| Milestone | Typical lead time | Who drives it |
|---|---|---|
| Departmental exam | book ~4–6 weeks ahead; thesis to committee ≥1 week before | You + program |
| External examiner nomination | ~8 weeks before dissertation submission | Supervisor + grad advisor (you draft the list) |
| External review | about a month for the report | G+PS + examiner |
| University examiners + defence booking | form and booking request in ≥4 weeks before the defence | You + program |
| Final oral defence | minimum 6–7 weeks after the dissertation goes to G+PS | You + G+PS |
| Final acceptance in cIRcle | ~1 month after the defence; submit ≥5 business days before your deadline | You |

## Step 0: Write in the right template from the start

UBC does **not** provide an official thesis template, only [formatting requirements](https://www.grad.ubc.ca/current-students/dissertation-thesis-preparation), which are checked strictly at final submission.

**Start from mine.** I maintain the [LaTeX template I wrote my own dissertation in](https://github.com/nashid/ubc-dissertation-template). It builds on Brian de Alwis' public-domain `ubcdiss.cls`, follows the G+PS structure and formatting requirements, and is organized for a **manuscript-based dissertation**, with each research chapter corresponding to a published or submitted paper. It has been through the entire pipeline described in this guide, G+PS formatting review included, so you inherit a structure that is known to pass.

Adopt it early and write in it from the beginning. Retrofitting a formatting-compliant document in the final month, while also handling committee revisions, is avoidable misery. You will also need a style guide (APA, Chicago, or another approved guide); that choice is made **with your supervisor**, not unilaterally.

## Step 1: The departmental exam

In ECE, before anything goes to G+PS, you defend internally. Mechanically it looks like a smaller version of the real defence: <span class="mn">personal experience, ECE (2025); formats vary by program</span>

- **Committee**: your advisor, two members of your supervisory committee, and a chair.
- **Scheduling is the hard part.** You need a slot where four busy academics are simultaneously available. Start 4–6 weeks out, and be extra generous in summer when everyone travels. In my case scheduling started in mid-July for a late-August exam.
- **The thesis goes to the committee at least one week before the exam.** In practice, aim for more; a committee member who has not read it helps nobody.

Treat this exam as a genuine asset rather than a hurdle: it is the last round of substantive feedback before your dissertation is read by someone who has never met you. The revisions that come out of it are what make the external examination boring, which is what you want.

## Step 2: The external examiner (start earlier than feels necessary)

This is the step with the longest invisible lead time and the strictest rules, so it deserves the most care.

**How it works.** Your supervisor and the graduate program advisor nominate **at least two, preferably three** candidates using the [Nominations for External Examiner form](https://www.grad.ubc.ca/current-students/final-doctoral-exam/selecting-external-examiner), due roughly **8 weeks before** the dissertation is submitted for external examination. In practice, you draft a shortlist together with your supervisor well before that; for me this conversation happened in mid-July, months before the form went in. <span class="mn">G+PS, &ldquo;Selecting an External Examiner&rdquo;</span>

**Who is eligible.** An external examiner must hold the rank of full, associate, or emeritus professor at a comparable university, have an established reputation in the dissertation's research area, have prior experience supervising and examining doctoral students, and must not have acted as external examiner for a student of any of your committee members in the past three years.

**Who is *not* eligible (arm's length).** No co-authors or research collaborators from the past 6 years, no institutional colleagues from the past 6 years, no close friends or relatives, no former supervisors or prospective employers. Before proposing anyone, check your own co-author list; after years of collaboration it is longer than you remember.

**The confidentiality rules matter.** You may not contact potential examiners, and you are not supposed to know who the external examiner is until after the dissertation has been submitted. Nobody on your side may discuss your work with the examiner before the defence. Concretely: keep the shortlist between you, your supervisor, and the program. Do not mention names in talks, on social media, or anywhere public. A leaked name can disqualify an examiner and cost you months.

**After you press send.** Two things arrive. First, a short confirmation; here is the one I received, condensed and with the sender anonymized:

<div class="inbox-note">
<span class="inbox-note-eyebrow">What lands in your inbox</span>
<span class="inbox-note-from">From: the Doctoral Exams team, G+PS, after the nomination form goes in</span>
<p>&ldquo;Graduate and Postdoctoral Studies has received your Nominations for External Examiner (Doctoral Dissertation) form and will proceed to confirm an External Examiner for early February <b>as noted on the form</b>. Please let us know <b>immediately</b> if you will not be submitting your dissertation for external examination at that time. [&hellip;] More information about next steps will be provided once an External Examiner has been confirmed.&rdquo;</p>
</div>

Read that email the way G+PS means it: the anticipated submission date you wrote on the form is now the spine of your exam timeline. The exams office is explicit about the tolerances: **a few days late is fine; more than two weeks late** and they may have to go back to your examiner to check they are still available, and every downstream date moves with you. If you know you will slip, say so immediately rather than going quiet. <span class="mn">welcome packet, p. 2</span>

Second, G+PS sends a **doctoral exam welcome packet**, which, in the best tradition of bureaucracies with soul, introduces the doc exams team alongside photographs of their corgis. Behind the corgis it is genuinely load-bearing: the interval chain in the timeline above is theirs, and it warns you that everything from here on arrives from **graduate.doctoral@ubc.ca** and contains instructions, not just updates. Whitelist that address and read every message carefully. I have archived [the edition I received (December 2025)](/resources/docs/ubc-doctoral-exam-welcome-dec2025.pdf) as a specimen; get the current one from the exams office.

Then, usually: silence, while invitations go out. Do not panic; the next email is the one confirming an external has accepted.

## Step 3: The dissertation goes out

Once your supervisory committee approves the dissertation for external examination, you submit it to the G+PS Doctoral Exams Office, which transmits it to the examiner, who then has **about a month** to read it and write the report.

<div class="inbox-note">
<span class="inbox-note-eyebrow">What lands in your inbox</span>
<span class="inbox-note-from">From: the Doctoral Exams team, the &ldquo;Dissertation Transmit&rdquo; email</span>
<p>Sent to you and your supervisor the moment the dissertation goes out. It names the <b>earliest date your defence can be held</b>, which means booking starts <i>now</i>, not when the external&rsquo;s report arrives.</p>
</div>

This is otherwise the quiet phase: a good time to prepare the defence talk and, frankly, to rest. In my case the dissertation went out in **early February** for an April defence; the examiner conversation still happens the previous summer, because the 8-week nomination lead time sits in front of everything.

## Step 4: The final oral defence

Here is the fact most candidates get wrong, straight from the exams office: **you do not wait for the external examiner's report to book the defence.** Booking opens as soon as the dissertation is transmitted; the defence lands a **minimum of 6–7 weeks** after submission and should be booked **at least 4 weeks in advance**. With the booking request goes the **University Examiner form**, nominating the two UBC examiners who join the examining committee from outside your supervisory committee; G+PS appoints the chair. The external's report becomes part of the record whether or not they attend. The [Doctoral Exam Guide and planning tools](https://www.grad.ubc.ca/current-students/final-doctoral-exam) cover the room, format, and mechanics; read them end-to-end the week you submit.

## Step 5: Final submission to cIRcle

Usually about a month separates defence day from being fully done. You incorporate any required revisions, collect committee approval, and upload the final PDF to cIRcle. Details that surprise people:

- The PDF must be unsecured (no password protection), and **a scan is not acceptable**.
- G+PS reviews the formatting *after* you submit: **your program is not closed and you are not eligible to graduate until they approve it**, and corrections are common. G+PS itself recommends submitting **at least 5 business days before** your deadline; the deadline is for *approval*, not submission.
- Once accepted, **no changes are permitted**. Proofread the final version as if it is permanent, because it is. It goes online within 3–4 days. <span class="mn">G+PS, &ldquo;Final Dissertation Submission&rdquo;</span>

## The cadence, end to end

Roughly my own calendar, as one concrete instantiation: <span class="mn">my own timeline, 2025&ndash;2026</span>

- **Mid-July**: external examiner shortlist drafted with my supervisor; departmental exam scheduling begins
- **Late August**: departmental exam (thesis to the committee a week or more before)
- **September–October**: revisions from committee feedback
- **Late fall**: Nominations for External Examiner form submitted; G+PS confirms receipt and starts inviting
- **Early February**: dissertation submitted to the Doctoral Exams Office for external examination
- **April**: final oral defence, booked weeks earlier without waiting for the external's report
- **Late spring**: revisions incorporated, final version approved in cIRcle, program closed

## Quick answers to the questions everyone asks

**Can I email a potential external examiner to ask whether they would be willing?** No. You may not contact candidates, and you are not supposed to know who accepted until after the dissertation is submitted. Your supervisor and program handle every touchpoint.

**Do we wait for the external's report before booking the defence?** No. Booking opens with the Dissertation Transmit email. Waiting for the report is the most common self-inflicted delay.

**What if my dissertation is not ready on the date I put on the nomination form?** A few days late is fine. More than two weeks late and G+PS may need to re-confirm your examiner's availability, and every downstream date moves. Tell the exams office immediately rather than going quiet.

**Who is actually in the room at the defence?** Your supervisory committee, two university examiners nominated via the University Examiner form, and a G+PS-appointed chair. The external's report is part of the record whether or not they attend.

**How long after defending am I actually done?** Usually about a month: revisions, committee sign-off, cIRcle upload, and G+PS formatting approval. Your program closes only when the final version is approved; the dissertation goes public 3–4 days later.

**Which emails matter?** Everything about the exam arrives from [graduate.doctoral@ubc.ca](mailto:graduate.doctoral@ubc.ca). Whitelist it, and read each message as instructions rather than updates, because that is what they are.

## Checklist

- [ ] Writing in a formatting-compliant template from day one; style guide agreed with supervisor
- [ ] Target graduation cycle picked; worked backwards from the [G+PS deadlines](https://www.grad.ubc.ca/current-students/final-doctoral-exam/doctoral-deadlines)
- [ ] Departmental exam booked 4–6 weeks out; thesis to committee ≥1 week before
- [ ] External shortlist (2–3+ names) drafted with supervisor; arm's-length rules checked; kept confidential
- [ ] Nomination form in ~8 weeks before planned dissertation submission; submission date on the form treated as a commitment
- [ ] [graduate.doctoral@ubc.ca](mailto:graduate.doctoral@ubc.ca) whitelisted; every message from it read as instructions
- [ ] Defence booked as soon as the Dissertation Transmit email arrives (≥4 weeks ahead); University Examiner form in with the booking
- [ ] Defence talk prepared while the external reads
- [ ] Final PDF proofread; submitted to cIRcle ≥5 business days before the deadline

If you are navigating this at UBC (or anywhere, since most universities run an isomorphic process under different names) and something here does not match what you are seeing, [email me](mailto:nashid@ece.ubc.ca). I would rather update this post than have you reverse-engineer it from scratch like I did.

<div class="post-revisions">
<span class="post-revisions-label">Revision history</span>
<p>v1 &middot; July 5, 2026 &middot; First published.</p>
<p>Corrections are versioned like a preprint; the <a href="https://github.com/nashid/nashid.github.io/commits/main/_writings/ubc-phd-thesis-examination-guide.md">full source history</a> of this guide is public.</p>
</div>
