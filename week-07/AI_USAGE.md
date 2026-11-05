# AI Usage Disclosure — Week 07

Required by the course academic policy (Generative AI use level **D — AI-integrated**).
You are responsible for the accuracy, testing and integrity of everything you submit,
including anything an AI tool produced.

| Tool | Exact model / plan | Used for | Which files it touched |
| --- | --- | --- | --- |
| Claude (claude.ai chat), free plan | Claude Sonnet 5.5 | the first test suite (Task 3) | suites/first/booking.test.ts, app/src/booking.test.ts |
| Claude (same chat) | Claude Sonnet 5.5 | the improvement prompt (Task 5) | app/src/booking.test.ts (fill in after Task 5) |
| Claude (same chat) | Claude Sonnet 5.5 | setup help (git, npm, vitest 3.2.4), draft reasons and X1/X2 for the test plan | lab-report.md section 3, week-07 setup |

**I used an assistant to extract `canBook` (Task 1), or to fix a defect in it:** yes
<!-- Moved the booking decision from App.tsx into app/src/booking.ts, and App.tsx now imports and calls canBook. I did not write the code myself. Tool and model: <WRITE WHAT YOU REALLY USED, or "not known, the model was not displayed">. I checked the logic against AC1-AC4 and T01-T14 with Claude; the behaviour in the browser is checked in the UI checks (Task 7). No commit exists from before the extraction, because the project I got already had it. -->

**I used another assistant as well (to explain a failure, to draft text in lab-report.md, …):** no
<!-- If you used ChatGPT or anything else, change to yes and say which model and which section. -->

**`suites/first/` holds the assistant's first test file exactly as it generated it:** yes

**Every terminal output in lab-report.md was pasted from a real run, unedited:** yes
<!-- Only keep "yes" if it is true when you submit. -->

**I can explain every test in my final suite — its input, its expected result and the AC behind
it — without the assistant:** <yes or no, see below>

**Anything I accepted from the AI without fully understanding it:**
<!-- Name the file and the part. -->

Signed: Ashimkhan Kuralay
Date: 2026-11-06
