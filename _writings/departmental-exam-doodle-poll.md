---
title: "Scheduling a departmental exam with a Doodle poll"
date: 2026-07-12
summary: "The workflow I used to schedule an ECE departmental exam: agree the time with your advisor, cut the slots nobody can make, and let the poll confirm a decision rather than discover one."
version: 1
---

A colleague recently asked me how I ran the Doodle poll to schedule my ECE departmental exam. The tool is trivial and the question sounds trivial, but the way most people use it is what turns a fifteen-minute task into three weeks of silence. This post is the workflow I actually used, written down so the next person can copy it.

The failure mode is easy to name. A committee meeting means getting four or five busy academics into one room, and the tempting shortcut is to paste your whole calendar into a poll and let them sort it out. It does not work. Claus Wilke [warns against a 120-option poll](https://clauswilke.com/blog/2014/10/14/how-to-schedule-a-committee-meeting/); Eva Lefkowitz once [filled out one with 56](https://www.evalefkowitz.com/blog/how-to-set-up-a-doodle-poll) and, by her own account, stopped bothering to check whether the conflicts on her calendar could be moved. A long poll does not gather more information. It gathers less, because it invites people to answer carelessly. The fix is to make the poll as deterministic as you can: use it to *confirm* among times you have already vetted, not to *discover* a time from scratch.

<div class="post-epigraph">
<span class="post-epigraph-label">A note before you rely on this</span>
<p>This is a personal workflow, not a policy. What is stable here is the human discipline, deciding before you poll and offering only vetted slots; what changes is your department's scheduling norms and Doodle's interface, both as of July 2026. For what a departmental exam is and who sits on it, see my <a href="/writings/ubc-phd-thesis-examination-guide/#step-1-the-departmental-exam">guide to the UBC thesis examination process</a>. Your program assistant is authoritative; when in doubt, trust them over this post.</p>
</div>

## The poll confirms a decision, it does not make one

A departmental exam, the internal exam ECE requires before the university defence, needs your advisor, two committee members, and a chair in the same room. Your advisor and you are the two people whose presence is non-negotiable and whose calendars are the hardest to move. Fix those two first, and the poll only has to find agreement among the people who are left.

How many options should the poll hold? The advice splits, and the split is worth understanding. Wilke argues that more than about ten is doing it wrong, and that three to five well-chosen times is the target, because a quick turn-around beats complete information: a committee member who opens a short poll answers it at once. Lefkowitz argues for 10 to 20 carefully selected options, on the grounds that too few leaves no common time while too many makes people careless. They agree on far more than they dispute. Both say to talk to your advisor first, to remove the times that cannot possibly work before anyone sees the poll, and never to paste in a raw calendar.

My own rule sits at the deterministic end, which is also what a departmental exam rewards: the more you settle in advance, the fewer options you need. So I do the elimination first and the poll last, and I keep the list as short as the legwork allows. If you have done that work, a handful of times is enough. If you genuinely cannot pre-eliminate much, Lefkowitz's larger, carefully chosen slate is the safer bet. Either way the invariant holds: every option in the poll is one you have already checked is plausible. The steps below are just that principle made concrete.

## <span class="step-num">Step 1</span> Agree with your advisor, and cut the impossible times

Settle the two of you before anyone else is involved. A two-minute conversation, "which afternoons that month could you sit my exam?", collapses most of the uncertainty, because once the advisor is fixed the poll has a much smaller job. Do this privately, not through the poll; the poll is for the people you cannot simply ask.

Then spend a few minutes removing options rather than adding them. Take out anything your advisor cannot make, check the committee members' teaching schedules online and take out those hours, and if the exam falls in summer or near a holiday, ask each member whether they will be travelling. Wilke suggests going one step further and simply asking, in two lines, whether there are days they are away or times that generally do not work; a busy professor answers that in the time it takes to read it, and it saves you proposing a dozen slots they would have declined. Faculty calendars are tighter than students expect, so start at least a month out, and further if your committee travels a lot. What survives this pruning is your slate, and it should already be short.

## <span class="step-num">Step 2</span> Put a tentative hold on the calendar

Once you and your advisor have agreed on a front-runner and a backup or two, send a tentative calendar invite for those slots to the two of you, marked as a hold, before the poll goes out. It stops the advisor's slot from being booked over while the committee responds, and it gives you a real event to convert into the final invite once the poll resolves. Keep it tentative: you are reserving the time, not announcing it yet.

## <span class="step-num">Step 3</span> Build a short poll in one-hour blocks

Now create the Doodle with only the slots that survived Step 1. Title it so it is obvious whose exam it is, set the duration, and set your timezone. One refinement is worth the trouble, and I owe it to Lefkowitz: poll in one-hour blocks rather than the full length of the meeting, even for a two-hour exam. If I am free from 10 to 12 but the only options are 9 to 11 and 11 to 1, I will mark neither; offer one-hour blocks, then look for two adjacent hours everyone can make, and you capture the times a coarser grid hides. My own poll used two-hour blocks, and a finer grid would have collected more yeses. This is otherwise how I set mine up:

<div class="inbox-note">
<span class="inbox-note-meta"><b>How I set up the poll</b> &middot; reusable; swap in your own name</span>
<p>Title: <b>PhD Departmental Exam - [your name]</b>. Duration: <b>2 hours</b>. Timezone: your city. Description: &ldquo;I am reaching out to kindly ask about your availability for my PhD departmental exam. To that end, I would appreciate it if you could please fill out this Doodle poll with your available dates. Thank you, [your name].&rdquo;</p>
</div>

Do not reach for a paid account or an exotic feature. The discipline that makes this work is offering few, vetted slots and deciding first, not any particular setting.

## <span class="step-num">Step 4</span> Send one short email

The poll link goes out in a single email. Keep it warm and short: thank the committee, ask for their availability, and give the link. Send it to the members whose times you still need; your advisor, already aligned from Step 1, can simply be copied. I sent mine in early December for a January exam. This is close to what I sent, with the committee anonymized:

<div class="inbox-note">
<span class="inbox-note-meta"><b>The email that carries the poll</b> &middot; anonymized; swap the brackets</span>
<p>Subject: Scheduling ECE Departmental Exam &ndash; [your name]</p>
<p>&ldquo;Dear Committee Members, thank you for serving on my committee throughout my doctoral degree and for your continual guidance. I would like to kindly ask about your availability for my ECE Departmental Exam. To that end, please indicate your preferred dates using the Doodle poll below: [Doodle link]. Thank you very much for your time. Sincerely, [your name].&rdquo;</p>
</div>

## Once the poll closes

Pick the slot with full attendance, preferring your held front-runner if it survives, and email the whole committee the confirmed time straight away. Wilke and Lefkowitz make the same point here: wait too long and someone books over the slot you found, and you are back to a second poll. Convert the tentative hold into the final invite with the room and the video link, and cancel the other holds so nobody keeps a phantom event. If a member never answered the poll, do not send a third reminder into the void; catch them in person or by a direct message and ask about the one time you need. If two slots tie, your advisor's preference breaks the tie.

## Quick answers

**How many options should I offer?** As few as your legwork allows. Wilke would say three to five; Lefkowitz would accept 10 to 20 if they are carefully chosen. Everyone agrees that a poll with 50 or more options is the failure mode, because it makes people answer carelessly.

**Should I ask everyone for their availability first?** Talk to your advisor first, always. For the rest, a two-line email asking which days or times generally do not work is often faster than a poll, and it lets you build a shorter poll afterwards.

**What if none of the slots work?** Run a second short poll. Two polls of a handful of options each are far better than one poll of 50, and a failed first round is normal rather than a disaster.

**What if a committee member will not respond?** Ask them directly, in person or by message, about the single time you need. A small committee is small enough that one conversation beats another round for everyone.

## Checklist

- [ ] Started at least a month out, more if the committee travels
- [ ] Front-runner and a backup or two agreed with your advisor first
- [ ] Impossible times removed: advisor's conflicts, teaching schedules, travel weeks
- [ ] Calendar hold placed on the surviving slots before the poll goes out
- [ ] Doodle kept short, in one-hour blocks, with a clear title, duration, and timezone
- [ ] One warm, short email with the poll link, advisor copied
- [ ] Winning time emailed to everyone at once, final invite sent, other holds cancelled

This is the workflow that turned my own exam scheduling from a slow email thread into one poll and one email. If your department runs it differently, or you find a cleaner sequence, [email me](mailto:nashid@ece.ubc.ca) and I will update this.

<div class="post-revisions">
<span class="post-revisions-label">Revision history</span>
<p>v1 &middot; July 12, 2026 &middot; First published.</p>
<p>Corrections are versioned like a preprint; the <a href="https://github.com/nashid/nashid.github.io/commits/main/_writings/departmental-exam-doodle-poll.md">full source history</a> of this post is public.</p>
</div>
