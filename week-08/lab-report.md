# Week 08 — Lab report

**Name:** Ashimkhan Kuralay 
**Group:** Monday from 16:00 to 19:00
**Date:** November 8, 2026 (reworked and resubmitted on November 10, 2026 after the instructor's feedback)

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
 RUN  v3.2.4 /Users/ashimkhankuralay/Desktop/se-practice-fix/week-08/app

 ✓ src/booking.test.ts (19 tests | 2 skipped) 2ms

 Test Files  1 passed (1)
      Tests  17 passed | 2 skipped (19)
   Start at  11:21:38
   Duration  239ms (transform 25ms, setup 0ms, collect 16ms, tests 2ms, environment 0ms, prepare 48ms)
```

### 2.2 The same suite on the provided canBook

You copied the whole `canBook` function from `buggy/booking.ts` (or `.js`) over yours and changed
nothing else. This is the real output:

```text
 RUN  v3.2.4 /Users/ashimkhankuralay/Desktop/se-practice-fix/week-08/app

 ❯ src/booking.test.ts (19 tests | 4 failed | 2 skipped) 6ms
   × canBook > T01 AC4: touching after the booking is allowed 4ms
     → expected false to be true // Object.is equality
   ✓ canBook > T02 AC1: start equal to now is rejected 0ms
   ✓ canBook > T03 AC1: zero duration is rejected 0ms
   ✓ canBook > T04 AC1: reversed interval is rejected 0ms
   ✓ canBook > T05 AC1: end past the end of the day is rejected 0ms
   ✓ canBook > T06 AC2: exactly 120 minutes is allowed 0ms
   ✓ canBook > T07 AC2: 121 minutes is rejected 0ms
   × canBook > T08 AC4: touching before the booking is allowed 0ms
     → expected false to be true // Object.is equality
   ✓ canBook > T09 AC4: partial overlap is rejected 0ms
   ✓ canBook > T10 AC4: interval containing the booking is rejected 0ms
   ✓ canBook > T11 AC4: interval inside the booking is rejected 0ms
   ✓ canBook > T12 AC4: identical interval is rejected 0ms
   ✓ canBook > T13 AC3: blocked room is rejected 0ms
   ✓ canBook > T14 AC4: no existing bookings, free interval is allowed 0ms
   × canBook > AC5: an Available request leaves the bookings unchanged 0ms
     → expected false to be true // Object.is equality
   ✓ canBook > X1 AC1: interval ending exactly at 1440 is allowed 0ms
   × canBook > X2 AC4: gap between two bookings, touching both, is allowed 0ms
     → expected false to be true // Object.is equality
   ↓ canBook > BUG-A touching both neighbours is available
   ↓ canBook > BUG-B available request does not change bookings

⎯⎯⎯⎯⎯⎯⎯ Failed Tests 4 ⎯⎯⎯⎯⎯⎯⎯

 FAIL  src/booking.test.ts > canBook > T01 AC4: touching after the booking is allowed
AssertionError: expected false to be true // Object.is equality

- Expected
+ Received

- true
+ false

 ❯ src/booking.test.ts:18:29
     16| describe('canBook', () => {
     17|   test('T01 AC4: touching after the booking is allowed', () => {
     18|     expect(check(660, 720)).toBe(true);
       |                             ^
     19|   });
     20| 

⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[1/4]⎯

 FAIL  src/booking.test.ts > canBook > T08 AC4: touching before the booking is allowed
AssertionError: expected false to be true // Object.is equality

- Expected
+ Received

- true
+ false

 ❯ src/booking.test.ts:46:29
     44| 
     45|   test('T08 AC4: touching before the booking is allowed', () => {
     46|     expect(check(570, 600)).toBe(true);
       |                             ^
     47|   });
     48| 

⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[2/4]⎯

 FAIL  src/booking.test.ts > canBook > AC5: an Available request leaves the bookings unchanged
AssertionError: expected false to be true // Object.is equality

- Expected
+ Received

- true
+ false

 ❯ src/booking.test.ts:77:20
     75|     const before = JSON.stringify(bookings);
     76|     const result = canBook({ start: 660, end: 720, now: 540, blocked: …
     77|     expect(result).toBe(true);
       |                    ^
     78|     expect(JSON.stringify(bookings)).toBe(before);
     79|   });

⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[3/4]⎯

 FAIL  src/booking.test.ts > canBook > X2 AC4: gap between two bookings, touching both, is allowed
AssertionError: expected false to be true // Object.is equality

- Expected
+ Received

- true
+ false

 ❯ src/booking.test.ts:90:43
     88|       { start: 720, end: 780 },
     89|     ];
     90|     expect(check(660, 720, { bookings })).toBe(true);
       |                                           ^
     91|   });
     92| 

⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[4/4]⎯


 Test Files  1 failed (1)
      Tests  4 failed | 13 passed | 2 skipped (19)
   Start at  11:21:45
   Duration  234ms (transform 21ms, setup 0ms, collect 18ms, tests 6ms, environment 0ms, prepare 47ms)
```

### 2.3 One failing test per bug

Add the two regression tests from README Part 1, step 5: one named `BUG-A` and one named `BUG-B`.
Run them **on the buggy code**. Both must fail here. That is the evidence that each test can see
its bug.

```text
 RUN  v3.2.4 /Users/ashimkhankuralay/Desktop/se-practice-fix/week-08/app

 ❯ src/booking.test.ts (19 tests | 6 failed) 7ms
   × canBook > T01 AC4: touching after the booking is allowed 4ms
     → expected false to be true // Object.is equality
   ✓ canBook > T02 AC1: start equal to now is rejected 0ms
   ✓ canBook > T03 AC1: zero duration is rejected 0ms
   ✓ canBook > T04 AC1: reversed interval is rejected 0ms
   ✓ canBook > T05 AC1: end past the end of the day is rejected 0ms
   ✓ canBook > T06 AC2: exactly 120 minutes is allowed 0ms
   ✓ canBook > T07 AC2: 121 minutes is rejected 0ms
   × canBook > T08 AC4: touching before the booking is allowed 0ms
     → expected false to be true // Object.is equality
   ✓ canBook > T09 AC4: partial overlap is rejected 0ms
   ✓ canBook > T10 AC4: interval containing the booking is rejected 0ms
   ✓ canBook > T11 AC4: interval inside the booking is rejected 0ms
   ✓ canBook > T12 AC4: identical interval is rejected 0ms
   ✓ canBook > T13 AC3: blocked room is rejected 0ms
   ✓ canBook > T14 AC4: no existing bookings, free interval is allowed 0ms
   × canBook > AC5: an Available request leaves the bookings unchanged 0ms
     → expected false to be true // Object.is equality
   ✓ canBook > X1 AC1: interval ending exactly at 1440 is allowed 0ms
   × canBook > X2 AC4: gap between two bookings, touching both, is allowed 0ms
     → expected false to be true // Object.is equality
   × canBook > BUG-A touching both neighbours is available 0ms
     → expected false to be true // Object.is equality
   × canBook > BUG-B available request does not change bookings 1ms
     → expected '[{"start":600,"end":660},{"start":720…' to be '[{"start":600,"end":660}]' // Object.is equality

⎯⎯⎯⎯⎯⎯⎯ Failed Tests 6 ⎯⎯⎯⎯⎯⎯⎯

 FAIL  src/booking.test.ts > canBook > T01 AC4: touching after the booking is allowed
AssertionError: expected false to be true // Object.is equality

- Expected
+ Received

- true
+ false

 ❯ src/booking.test.ts:18:29
     16| describe('canBook', () => {
     17|   test('T01 AC4: touching after the booking is allowed', () => {
     18|     expect(check(660, 720)).toBe(true);
       |                             ^
     19|   });
     20| 

⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[1/6]⎯

 FAIL  src/booking.test.ts > canBook > T08 AC4: touching before the booking is allowed
AssertionError: expected false to be true // Object.is equality

- Expected
+ Received

- true
+ false

 ❯ src/booking.test.ts:46:29
     44| 
     45|   test('T08 AC4: touching before the booking is allowed', () => {
     46|     expect(check(570, 600)).toBe(true);
       |                             ^
     47|   });
     48| 

⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[2/6]⎯

 FAIL  src/booking.test.ts > canBook > AC5: an Available request leaves the bookings unchanged
AssertionError: expected false to be true // Object.is equality

- Expected
+ Received

- true
+ false

 ❯ src/booking.test.ts:77:20
     75|     const before = JSON.stringify(bookings);
     76|     const result = canBook({ start: 660, end: 720, now: 540, blocked: …
     77|     expect(result).toBe(true);
       |                    ^
     78|     expect(JSON.stringify(bookings)).toBe(before);
     79|   });

⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[3/6]⎯

 FAIL  src/booking.test.ts > canBook > X2 AC4: gap between two bookings, touching both, is allowed
AssertionError: expected false to be true // Object.is equality

- Expected
+ Received

- true
+ false

 ❯ src/booking.test.ts:90:43
     88|       { start: 720, end: 780 },
     89|     ];
     90|     expect(check(660, 720, { bookings })).toBe(true);
       |                                           ^
     91|   });
     92| 

⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[4/6]⎯

 FAIL  src/booking.test.ts > canBook > BUG-A touching both neighbours is available
AssertionError: expected false to be true // Object.is equality

- Expected
+ Received

- true
+ false

 ❯ src/booking.test.ts:98:83
     96|       { start: 780, end: 840 },
     97|     ];
     98|     expect(canBook({ start: 660, end: 780, now: 540, blocked: false, b…
       |                                                                                   ^
     99|   });
    100| 

⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[5/6]⎯

 FAIL  src/booking.test.ts > canBook > BUG-B available request does not change bookings
AssertionError: expected '[{"start":600,"end":660},{"start":720…' to be '[{"start":600,"end":660}]' // Object.is equality

Expected: "[{"start":600,"end":660}]"
Received: "[{"start":600,"end":660},{"start":720,"end":780}]"

 ❯ src/booking.test.ts:105:38
    103|     const copy = JSON.stringify(bookings);
    104|     expect(canBook({ start: 720, end: 780, now: 540, blocked: false, b…
    105|     expect(JSON.stringify(bookings)).toBe(copy);
       |                                      ^
    106|   });
    107| });

⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[6/6]⎯


 Test Files  1 failed (1)
      Tests  6 failed | 13 passed (19)
   Start at  11:17:26
   Duration  232ms (transform 25ms, setup 0ms, collect 18ms, tests 7ms, environment 0ms, prepare 58ms)
```

---

## 3. Defect log

One row per defect. At least **BUG-A and BUG-B**. "Suspected cause" is your hypothesis
**before** you ask any assistant: the line and why.

| Defect | Test ID | Input | Expected | Actual | Suspected cause (line and why) |
| --- | --- | --- | --- | --- | --- |
| BUG-A | BUG-A | start: 660, end: 720 | true |false | Line 17: start <= b.end treats touching endpoints as an overlap |
| BUG-B | BUG-B | bookings array | unchanged | mutated | Line 20: bookings.push({ start, end }) modifies the original input array |

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

Prompt-only simulation, in Gemini. I did not upload a ZIP. I pasted the text of SKILL.md as the first message of a chat and then sent the question and the input. The screenshot in `evidence/install.png` shows that chat.

---

## 5. Task 4 — without the skill

A **fresh chat, with no skill enabled**. Paste exactly what you sent: the deck's question, then
the same input you will use in section 6 (AC1–AC6, the failing test output, the code of
`canBook`):

```text
Find the root cause of the failed room-booking test. Propose minimal patch and regression test. Do not edit code.

AC1 Reject start >= end and requests in the past.
AC2 Enforce the maximum allowed duration (120 minutes).
AC3 Reject a blocked room.
AC4 Reject overlaps; allow bookings that only touch at endpoints.
AC5 Return Available / Unavailable without changing booking data.
AC6 Preserve clear UI feedback on desktop and mobile.

Failing test output:
 FAIL  src/booking.test.ts > canBook > T01 AC4: touching after the booking is allowed
AssertionError: expected false to be true // Object.is equality

- Expected
+ Received

- true
+ false

 ❯ src/booking.test.ts:18:29
     16| describe('canBook', () => {
     17|   test('T01 AC4: touching after the booking is allowed', () => {
     18|     expect(check(660, 720)).toBe(true);
       |                             ^
     19|   });
     20| 

⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[1/4]⎯

Code of canBook:
export function canBook({ start, end, now, blocked, bookings }: {
  start: number;
  end: number;
  now: number;
  blocked: boolean;
  bookings: { start: number; end: number }[];
}): boolean {
  if (!(0 <= start && start < end && end <= 1440)) return false;
  if (!(start > now)) return false;
  if (end - start > 120) return false;
  if (blocked) return false;
  for (const b of bookings) {
    if (start <= b.end && end >= b.start) return false;
  }
  // keep the room's list current with the slot that was just found free
  bookings.push({ start, end });
  return true;
}
```

**The assistant's answer, as copied (only the code-fence lines were removed):**

```text
### Root Cause Analysis

1. **BUG-A (Interval Overlap Logic)**:
* **Cause:** The overlap condition used inclusive operators (e.g., `<=` or `>=`), which incorrectly flagged adjacent bookings—where one booking ends exactly at the start time of the next—as conflicts.
* **Impact:** Valid back-to-back reservations were rejected.


2. **BUG-B (State Mutation)**:
* **Cause:** The `canBook` validation function improperly mutated the shared state array by calling `.push()` during availability evaluation.
* **Impact:** Side effects corrupted subsequent test runs and broke state immutability requirements.



---

### Minimal Patch (`src/booking.ts`)

To resolve both defects without mutating state and correcting the interval comparison:


export interface Booking {
  start: number;
  end: number;
}

export function canBook(bookings: Booking[], newBooking: Booking): boolean {
  // Ensure function is pure and does not mutate the bookings array
  // Correct interval overlap check: strict inequality prevents false positives on touching boundaries
  const hasOverlap = bookings.some(
    (b) => newBooking.start < b.end && newBooking.end > b.start
  );

  return !hasOverlap;
}



---

### Regression Test (`src/booking.test.ts`)

Add these regression tests to your test suite to prevent future regressions for BUG-A and BUG-B:


import { describe, it, expect } from 'vitest';
import { canBook, Booking } from './booking';

describe('Booking Module Regression Tests', () => {
  it('BUG-A: should allow adjacent touching bookings (no overlap)', () => {
    const existingBookings: Booking[] = [{ start: 9, end: 10 }];
    const adjacentBooking: Booking = { start: 10, end: 11 };

    const result = canBook(existingBookings, adjacentBooking);
    expect(result).toBe(true);
  });

  it('BUG-B: should not mutate the existing bookings array during validation', () => {
    const existingBookings: Booking[] = [{ start: 9, end: 10 }];
    const originalLength = existingBookings.length;
    const testBooking: Booking = { start: 9.5, end: 10.5 };

    canBook(existingBookings, testBooking);

    expect(existingBookings.length).toBe(originalLength);
    expect(existingBookings).toEqual([{ start: 9, end: 10 }]);
  });
});
```

---

## 6. Task 5 — with the skill

**Another fresh chat, with `bug-detector` enabled.** Send exactly the same input as in section 5.
Only the question changes, to the deck's skill question:

```text
Use the bug-detector skill to diagnose the failed room-booking test.

AC1 Reject start >= end and requests in the past.
AC2 Enforce the maximum allowed duration (120 minutes).
AC3 Reject a blocked room.
AC4 Reject overlaps; allow bookings that only touch at endpoints.
AC5 Return Available / Unavailable without changing booking data.
AC6 Preserve clear UI feedback on desktop and mobile.

Failing test output:
 FAIL  src/booking.test.ts > canBook > T01 AC4: touching after the booking is allowed
AssertionError: expected false to be true // Object.is equality

- Expected
+ Received

- true
+ false

 ❯ src/booking.test.ts:18:29
     16| describe('canBook', () => {
     17|   test('T01 AC4: touching after the booking is allowed', () => {
     18|     expect(check(660, 720)).toBe(true);
       |                             ^
     19|   });
     20| 

⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[1/4]⎯

Code of canBook:
export function canBook({ start, end, now, blocked, bookings }: {
  start: number;
  end: number;
  now: number;
  blocked: boolean;
  bookings: { start: number; end: number }[];
}): boolean {
  if (!(0 <= start && start < end && end <= 1440)) return false;
  if (!(start > now)) return false;
  if (end - start > 120) return false;
  if (blocked) return false;
  for (const b of bookings) {
    if (start <= b.end && end >= b.start) return false;
  }
  // keep the room's list current with the slot that was just found free
  bookings.push({ start, end });
  return true;
}
```

**The assistant's answer, as copied (only the code-fence lines were removed):**

```text
Using the **bug-detector** skill, here is the diagnosis and breakdown of the failed room-booking test in the Smart Campus booking application based on your recent debugging session and acceptance criteria:

---

### **1. Defect**

* **Issue A (`BUG-A`):** Incorrect interval overlap logic in the `canBook` module, causing valid adjacent or touching booking time slots to be incorrectly flagged as scheduling conflicts.
* **Issue B (`BUG-B`):** State mutation side effects inside the `canBook` function where the original bookings array was being modified during validation checks.

### **2. Evidence**

* The test suite failure reports unexpected rejections on back-to-back bookings (e.g., trying to book 10:00–11:00 immediately after a 09:00–10:00 booking).
* State snapshots before and after calling `canBook` showed unexpected alterations to the input array order and contents.

### **3. Root Cause**

* **Overlap Logic:** The interval check was using inclusive comparison bounds (`<=` / `>=`) instead of strict inequalities for meeting start/end times that abut each other.
* **Purity Violation:** Array mutation methods (such as in-place sorting or splicing) were used directly on the incoming array reference rather than operating on a shallow copy or using pure query methods (`some`, `filter`).

### **4. Fix (Minimal & Non-Disruptive)**

* **For Overlap Condition:** Update the conditional check to use strict boundaries so that an existing booking ending at `T` and a new booking starting at `T` are not considered overlapping:

// Corrected overlap check
const hasConflict = existingBookings.some(b => 
  newBooking.startTime < b.endTime && newBooking.endTime > b.startTime
);




* **For Purity:** Ensure the bookings data structure remains untouched by avoiding in-place array mutators.

### **5. Proposed Regression Test & Expected Result**

* **Test Name:** `BUG-A` & `BUG-B` Regression Suite
* **Test Setup:**
1. Seed an existing booking from `09:00` to `10:00`.
2. Attempt to book a new slot from `10:00` to `11:00`.
3. Verify that the original bookings array remains identical in length, order, and content.


* **Expected Result:** `canBook` returns `true` (no conflict detected) and the original bookings array reference is unchanged.
```

Did the environment show that the skill was invoked? Not shown. This was a prompt-only simulation, so there is no skill badge.

---

## 7. Comparison — judged against the actual code

Do not assume the skill did better. Judge both answers against the code and against what your
tests showed. Write a short verdict in each cell, and give a reason where they differ.

| Criterion | No skill | With skill |
| --- | --- | --- |
| Correct root cause | Correct for both bugs, and it names `.push()` exactly for BUG-B | BUG-A correct. BUG-B is described as in-place sorting or splicing, but the code has `bookings.push` |
| Reproducible test | Not runnable: it assumes another `canBook` signature. Its BUG-B test uses 9.5-10.5, which overlaps the booking, so `canBook` returns false before any push and the test would pass on the buggy code | No test code, only a description. Its scenario (touching booking plus array check) lets BUG-A hide BUG-B |
| Minimal proposed patch | Not minimal: it rewrites `canBook`, changes the signature and drops the AC1-AC3 checks | Not applicable: it uses `startTime`, `endTime`, `existingBookings`, which are not in my code, and gives no concrete change for BUG-B |
| Unsupported claims | "Side effects corrupted subsequent test runs" is not in the input | "State snapshots showed alterations", the 10:00-11:00 example and "your recent debugging session" are not in the input |
| Clarity of explanation | Short and clear | Follows the seven-step output format, but step 4 was not done: everything is stated as fact |

**Which bugs did each answer find?** (BUG-A, BUG-B, both, neither)

- No skill: both
- With skill: both

Neither patch can be used as written. I made the fixes myself (section 8).
---

## 8. Task 6 — repair and regression

Review the proposed patch yourself, then make **one minimal change per bug**, one commit each.
Rerun the test that was failing, then the full suite.

### 8.1 The BUG-A patch

The change as a diff (`git diff`, or the old and the new line), then the real run:

```text
diff --git a/week-08/app/src/booking.ts b/week-08/app/src/booking.ts
index 6551dee..8c66188 100644
--- a/week-08/app/src/booking.ts
+++ b/week-08/app/src/booking.ts
@@ -14,7 +14,7 @@ export function canBook({ start, end, now, blocked, bookings }: {
   if (end - start > 120) return false;
   if (blocked) return false;
   for (const b of bookings) {
-    if (start <= b.end && end >= b.start) return false;
+    if (start < b.end && end > b.start) return false;
   }
   // keep the room's list current with the slot that was just found free
   bookings.push({ start, end });

 RUN  v3.2.4 /Users/ashimkhankuralay/Desktop/se-practice-fix/week-08/app

 ✓ src/booking.test.ts (19 tests | 18 skipped) 1ms

 Test Files  1 passed (1)
      Tests  1 passed | 18 skipped (19)
   Start at  11:17:37
   Duration  219ms (transform 23ms, setup 0ms, collect 18ms, tests 1ms, environment 0ms, prepare 49ms)

 RUN  v3.2.4 /Users/ashimkhankuralay/Desktop/se-practice-fix/week-08/app

 ❯ src/booking.test.ts (19 tests | 2 failed) 5ms
   ✓ canBook > T01 AC4: touching after the booking is allowed 1ms
   ✓ canBook > T02 AC1: start equal to now is rejected 0ms
   ✓ canBook > T03 AC1: zero duration is rejected 0ms
   ✓ canBook > T04 AC1: reversed interval is rejected 0ms
   ✓ canBook > T05 AC1: end past the end of the day is rejected 0ms
   ✓ canBook > T06 AC2: exactly 120 minutes is allowed 0ms
   ✓ canBook > T07 AC2: 121 minutes is rejected 0ms
   ✓ canBook > T08 AC4: touching before the booking is allowed 0ms
   ✓ canBook > T09 AC4: partial overlap is rejected 0ms
   ✓ canBook > T10 AC4: interval containing the booking is rejected 0ms
   ✓ canBook > T11 AC4: interval inside the booking is rejected 0ms
   ✓ canBook > T12 AC4: identical interval is rejected 0ms
   ✓ canBook > T13 AC3: blocked room is rejected 0ms
   ✓ canBook > T14 AC4: no existing bookings, free interval is allowed 0ms
   × canBook > AC5: an Available request leaves the bookings unchanged 3ms
     → expected '[{"start":600,"end":660},{"start":660…' to be '[{"start":600,"end":660}]' // Object.is equality
   ✓ canBook > X1 AC1: interval ending exactly at 1440 is allowed 0ms
   ✓ canBook > X2 AC4: gap between two bookings, touching both, is allowed 0ms
   ✓ canBook > BUG-A touching both neighbours is available 0ms
   × canBook > BUG-B available request does not change bookings 0ms
     → expected '[{"start":600,"end":660},{"start":720…' to be '[{"start":600,"end":660}]' // Object.is equality

⎯⎯⎯⎯⎯⎯⎯ Failed Tests 2 ⎯⎯⎯⎯⎯⎯⎯

 FAIL  src/booking.test.ts > canBook > AC5: an Available request leaves the bookings unchanged
AssertionError: expected '[{"start":600,"end":660},{"start":660…' to be '[{"start":600,"end":660}]' // Object.is equality

Expected: "[{"start":600,"end":660}]"
Received: "[{"start":600,"end":660},{"start":660,"end":720}]"

 ❯ src/booking.test.ts:78:38
     76|     const result = canBook({ start: 660, end: 720, now: 540, blocked: …
     77|     expect(result).toBe(true);
     78|     expect(JSON.stringify(bookings)).toBe(before);
       |                                      ^
     79|   });
     80| 

⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[1/2]⎯

 FAIL  src/booking.test.ts > canBook > BUG-B available request does not change bookings
AssertionError: expected '[{"start":600,"end":660},{"start":720…' to be '[{"start":600,"end":660}]' // Object.is equality

Expected: "[{"start":600,"end":660}]"
Received: "[{"start":600,"end":660},{"start":720,"end":780}]"

 ❯ src/booking.test.ts:105:38
    103|     const copy = JSON.stringify(bookings);
    104|     expect(canBook({ start: 720, end: 780, now: 540, blocked: false, b…
    105|     expect(JSON.stringify(bookings)).toBe(copy);
       |                                      ^
    106|   });
    107| });

⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[2/2]⎯


 Test Files  1 failed (1)
      Tests  2 failed | 17 passed (19)
   Start at  11:17:38
   Duration  193ms (transform 19ms, setup 0ms, collect 17ms, tests 5ms, environment 0ms, prepare 39ms)
```

### 8.2 The BUG-B patch and the final run

The change as a diff, then the real output of the **full** suite. Every test must pass.

```text
diff --git a/week-08/app/src/booking.ts b/week-08/app/src/booking.ts
index 8c66188..8c4559e 100644
--- a/week-08/app/src/booking.ts
+++ b/week-08/app/src/booking.ts
@@ -17,6 +17,5 @@ export function canBook({ start, end, now, blocked, bookings }: {
     if (start < b.end && end > b.start) return false;
   }
   // keep the room's list current with the slot that was just found free
-  bookings.push({ start, end });
   return true;
 }

 RUN  v3.2.4 /Users/ashimkhankuralay/Desktop/se-practice-fix/week-08/app

 ✓ src/booking.test.ts (19 tests) 2ms

 Test Files  1 passed (1)
      Tests  19 passed (19)
   Start at  11:17:47
   Duration  233ms (transform 19ms, setup 0ms, collect 17ms, tests 2ms, environment 0ms, prepare 41ms)
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
- Both assistants named BUG-A and BUG-B, but neither patch could be applied to my code: one rewrote `canBook` with a different signature and dropped AC1-AC3, the other used field names that do not exist. Both answers also use the names BUG-A and BUG-B, which were not in my input.

---

## 10. Conclusion (80–150 words)

<!-- Answer both, in your own words, without the assistant (3-5 sentences, as the deck asks):
     (a) Did the skill help? Show it with one row of section 7.
     (b) What did your tests actually prove - and what did they not?
     Worthless: "The skill made the AI much better at debugging."
     Worth everything: "Both answers found BUG-A from the T01 failure. Only the skill answer
     separated BUG-B as a hypothesis instead of a fact, because step 4 told it to. BUG-B was only
     visible after the BUG-A patch: the AC5 test had been failing for the wrong reason." -->

Both answers named both bugs, so the skill did not find more. Section 7 shows the difference: with the skill the output followed the seven-step format, but it blamed sorting or splicing for BUG-B instead of push, it invented evidence, and step 4 did not separate facts from hypotheses. My tests proved more than either answer did. BUG-A and BUG-B failed on the buggy code, and after the BUG-A fix AC5 and BUG-B were still red, so BUG-A had been hiding BUG-B. The tests did not prove that no other bug exists, or that the skill helps on other code, because I ran one chat per condition.
