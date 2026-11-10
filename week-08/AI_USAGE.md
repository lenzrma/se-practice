
# AI Usage Disclosure — Week 08

Required by the course academic policy (Generative AI use level **D — AI-integrated**).
You are responsible for the accuracy, testing and integrity of everything you submit,
including anything an AI tool produced.

| Tool | Exact model / plan | Used for | Which files it touched |
| --- | --- | --- | --- |
| Gemini (web) | not displayed | diagnosis without the skill (Task 4) | none — "Do not edit code" |
| Gemini (web) | not displayed, SKILL.md pasted as the first message (prompt-only simulation) | diagnosis with bug-detector (Task 5) | none — "Do not edit code" |
| Claude (claude.ai) | Claude Sonnet 5.5, free plan | help with the rework on 10 Nov: git recovery, shell and Python commands, the two regression tests, a first draft of the analysis text in lab-report.md | app/src/booking.test.ts, lab-report.md, submission.yml, AI_USAGE.md |

**`skills/bug-detector/SKILL.md` was typed by me from the deck's text, not generated:** no
<!-- CHECK: my first version was typed by me but reworded; the checker failed it (K5), and I replaced it with the deck's exact text that Claude quoted from the README. The text itself is the deck's. Change this line if it is not what happened. -->
The text is the deck's. My first version was reworded; I replaced it with the deck's exact wording, which Claude quoted from the README.

**I applied the patches myself, one minimal change per bug, after reviewing what the assistant
proposed:** yes
Neither Gemini patch was usable (wrong signature, wrong field names), so I did not use them. I made one change per bug (`<=` to `<`, then deleting `bookings.push`) with commands Claude suggested, ran them myself and checked the `git diff` of each.

**I used another assistant as well (to explain a failure, to draft text in lab-report.md, …):** yes
Claude Sonnet 5.5. It suggested the shell and git commands, wrote the BUG-A and BUG-B regression tests, and drafted the text of sections 3 (line numbers), 4, 7, 9.2 and 10 of lab-report.md from the real outputs. I reviewed and rewrote sections 9.2 and 10 in my own words.
<!-- CHECK: only keep the last sentence if you really rewrote 9.2 and 10 yourself. Do it before you submit. -->

**Every terminal output in lab-report.md was pasted from a real run, unedited:** yes
All outputs were re-run on 10 Nov 2026, after the deadline. I only removed colour escape codes. In the two assistant answers I removed the code-fence lines so the checker could read them.
My submission of 8 Nov contained outputs that did not come from real runs (for example "21 tests") and `evidence/install.png` was a generated placeholder, not a screenshot. I replaced all of it with real runs and a real screenshot of the Gemini chat.

**I can explain both bugs and both fixes — which line, why it was wrong, which test proves the
fix — without the assistant:** yes
<!-- CHECK: say yes only if you can. BUG-A: line 17, <= treats touching as overlap. BUG-B: line 20, push mutates the array; it stayed hidden behind BUG-A because AC5 used a touching request. -->

**Anything I accepted from the AI without fully understanding it:**
The shell and Python scripts Claude gave me for pasting test outputs into lab-report.md and for building the input file for Gemini. I ran them and checked the result in the report, but I did not read every line of the scripts.

Signed: Ashimkhan Kuralay
Date: 10.11.2026