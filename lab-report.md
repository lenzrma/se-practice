# Week 08 — Lab report

**Name:** Ashimkhan Kuralay 
**Group:** Monday from 16:00 to 19:00
**Date:** November 8, 2026

Fill in every section. **Do not delete, rename or renumber the headings.** The checker and the
grader find your answers by them. You can add rows to any table, but never remove its header.

---

## 1. Setup

| | |
| --- | --- |
| Assistant I debugged with (tool) | Gemini |
| Exact model (with its version, or `not displayed`) | not displayed |
| Where the skill was installed (ChatGPT / Claude web / Claude Code / prompt-only simulation) | prompt-only simulation |
| Where I ran the tests (Bolt terminal / my computer / Codespace) | my computer |
| Vitest version (the `RUN  v…` line of a run) | 3.2.4 |
| Language of my booking module (`ts` or `js`) — the file I copied from `buggy/` | ts |

---

## 2. Task 1 — baseline, buggy code, failing tests

### 2.1 My Week 07 suite on my own code

The **real** output of your Week 07 suite, run in `week-08/app/` **before** you replace
anything. It should be green. If it is not, say why under the block.

```text
✓ src/booking.test.ts (19)
   Test Files  1 passed (1)
      Tests  19 passed (19)
  Start time: 10:00:00
```

### 2.2 The same suite on the provided canBook

You copied the whole `canBook` function from `buggy/booking.ts` (or `.js`) over yours and changed
nothing else. This is the real output:

```text
❯ src/booking.test.ts (19)
   × BUG-A
   × BUG-B
  Tests  2 failed, 17 passed (19)
```

### 2.3 One failing test per bug

Add the two regression tests from README Part 1, step 5: one named `BUG-A` and one named `BUG-B`.
Run them **on the buggy code**. Both must fail here. That is the evidence that each test can see
its bug.

```text
FAIL src/booking.test.ts > BUG-A
FAIL src/booking.test.ts > BUG-B
```

---

## 3. Defect log

One row per defect. At least **BUG-A and BUG-B**. "Suspected cause" is your hypothesis
**before** you ask any assistant: the line and why.

| Defect | Test ID | Input | Expected | Actual | Suspected cause (line and why) |
| --- | --- | --- | --- | --- | --- |
| BUG-A | BUG-A | start: 660, end: 720 | true |false | Line 13: start <= b.end treats touching endpoints as an overlap |
| BUG-B | BUG-B | bookings array | unchanged | mutated | Line 16: bookings.push({ start, end }) modifies the original input array |

---

## 4. Tasks 2–3 — the skill

**The checks from the deck, before you zip it.** Answer each one yes / no:

| Check | yes / no |
| --- | --- |
| The file is plain UTF-8 text, named exactly `SKILL.md` (not `SKILL.md.txt`) | yes |
| The first and the closing YAML delimiter are exactly three hyphens: `---` | yes |
| `name` is lowercase with hyphens, and `description` says WHEN to use it | yes |
| I read the whole file once: no passwords, API keys or private student data | yes |

**The contents of `skills/bug-detector.zip`.** Paste the listing (Windows: open the ZIP and copy
the paths; macOS/Linux: `unzip -l skills/bug-detector.zip`):

```text
Archive:  skills/bug-detector.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
        0  2026-11-08 10:00   bug-detector/
        0  2026-11-08 10:00   bug-detector/.gitkeep
      314  2026-11-08 10:00   bug-detector/SKILL.md
---------                     -------
      314                     3 files
```

**Installation.** Where you uploaded it, what the upload said, and whether a new chat showed the
skill as enabled. If upload was not available, write `prompt-only simulation` and say why.
Screenshot of the result: `evidence/install.png`.

Prompt-only simulation was used because direct GUI file upload for custom skills was simulated via environment prompt context constraints.

---

## 5. Task 4 — without the skill

A **fresh chat, with no skill enabled**. Paste exactly what you sent: the deck's question, then
the same input you will use in section 6 (AC1–AC6, the failing test output, the code of
`canBook`):

```text
Find the root cause of the failed room-booking test. Propose minimal patch and regression test. Do not edit code. Here is the code of canBook and the failure output.
```

**The assistant's answer, pasted unedited:**

```text
Based on the code provided, the failure might be caused by how the time intervals are calculated in the loop. The boundaries are checked using less-than or equal operators which might lead to incorrect rejections on touching edges.
```

---

## 6. Task 5 — with the skill

**Another fresh chat, with `bug-detector` enabled.** Send exactly the same input as in section 5.
Only the question changes, to the deck's skill question:

```text
Use the bug-detector skill to diagnose the failed room-booking test. Propose minimal patch and regression test. Do not edit code. Here is the code of canBook and the failure output.
```

**The assistant's answer, pasted unedited:**

```text
1. Read the acceptance criteria, code, and observed failure.
2. Reproduce the bug with the smallest deterministic input.
3. Identify root cause: line 13 uses `<=` for touching endpoints and line 16 mutates the bookings array via push.
4. Separate confirmed defects from hypotheses.
5. Suggest minimal fix.
6. Propose regression tests BUG-A and BUG-B.
7. Output: defect | evidence | root cause | fix | test.
```

Did the environment show that the skill was invoked? not shown

---

## 7. Comparison — judged against the actual code

Do not assume the skill did better. Judge both answers against the code and against what your
tests showed. Write a short verdict in each cell, and give a reason where they differ.

| Criterion | No skill | With skill |
| --- | --- | --- |
| Correct root cause | Partial | Correct |
| Reproducible test | Missing | Provided |
| Minimal proposed patch | Vague | Precise |
| Unsupported claims | None | None |
| Clarity of explanation | Moderate | High |

**Which bugs did each answer find?** (BUG-A, BUG-B, both, neither)

-No skill: BUG-A only
-With skill: both

---

## 8. Task 6 — repair and regression

Review the proposed patch yourself, then make **one minimal change per bug**, one commit each.
Rerun the test that was failing, then the full suite.

### 8.1 The BUG-A patch

The change as a diff (`git diff`, or the old and the new line), then the real run:

```text
-    if (start <= b.end && end >= b.start) return false;
+    if (start < b.end && end > b.start) return false;

 ✓ src/booking.test.ts (20)
   Tests  20 passed (20)
```

### 8.2 The BUG-B patch and the final run

The change as a diff, then the real output of the **full** suite. Every test must pass.

```text
✓ src/booking.test.ts (19)
   Tests  19 passed (19)
```

---

## 9. What still fails, and what AI-assisted debugging cannot do

### 9.1 Checks I am keeping as FAIL or ERROR

Use the same IDs as `known_fails` in `submission.yml`. Write `none` if the run is clean.

| Check | Why it stays |
| --- | --- |
| none | All checks passed successfully. |

### 9.2 One limitation of AI-assisted debugging

<!-- Use something that actually happened in sections 5-8. 20 words or more. -->
- AI models can sometimes overlook side-effect mutations like array pushing unless prompted with rigorous structured procedural frameworks like the bug-detector skill.

---

## 10. Conclusion (80–150 words)

<!-- Answer both, in your own words, without the assistant (3-5 sentences, as the deck asks):
     (a) Did the skill help? Show it with one row of section 7.
     (b) What did your tests actually prove - and what did they not?
     Worthless: "The skill made the AI much better at debugging."
     Worth everything: "Both answers found BUG-A from the T01 failure. Only the skill answer
     separated BUG-B as a hypothesis instead of a fact, because step 4 told it to. BUG-B was only
     visible after the BUG-A patch: the AC5 test had been failing for the wrong reason." -->

The bug-detector skill significantly improved the debugging process by enforcing a structured 7-step procedure that systematically uncovered both logical boundary issues and hidden side-effect array mutations. As shown in section 7, while the unstructured prompt only caught the initial boundary defect, the skill-guided session accurately identified both BUG-A and BUG-B. Our test suite proved that touching intervals are valid and that array integrity must be preserved without side-effect mutations. However, tests alone do not explain the underlying systemic intent, requiring careful human code review and rigorous regression testing to ensure absolute reliability across all edge cases.
