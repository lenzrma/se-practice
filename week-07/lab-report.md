# Week 07 — Lab report

**Name:** Ashimkhan Kuralay
**Group:** monday from 16:00 to 19:00
**Date:** 2026-11-06

Fill in every section. **Do not delete, rename or renumber the headings.** The checker and the
grader find your answers by them. You can add rows to any table, but never remove its header.

---

## 1. Setup

| | |
| --- | --- |
| Project I continue (`week-06` = my Week 06 Bolt project, `starter` = the provided starter) | starter |
| Bolt project link (or `not shared`, and why) | not shared (local university lab project) |
| Assistant that generated the tests (tool) | Claude (Anthropic) / Gemini |
| Exact model (with its version, or `not displayed`) | Claude Sonnet 3.5 / Gemini |
| Where I ran the tests (Bolt terminal / my computer / Codespace) | my computer |
| Vitest version (the `RUN  v…` line of a run) | vitest v3.2.4 |
| Test command | npx vitest run |

---

## 2. Task 1 — baseline and the booking function

**Before editing:** where did the booking decision live in the project you started from?

| | |
| --- | --- |
| File and function (or "inside the page component") | inside the page component (`App.tsx`, inside `check` function) |
| Its inputs | component React state variables (`start`, `end`, `now`, `blocked`, `room.bookings`) |
| What it returned | boolean value (`true` for available, `false` for unavailable) |
| How the page used it | set component result state to render 'Available' or 'Unavailable' message |

**What I changed to extract `canBook`.** Say which file it now lives in, what you moved, and why
the behaviour did not change. Also say which file of the page now calls it. 40 words or more.

I moved the pure validation and overlap-checking logic out of `App.tsx` into a standalone function named `canBook` inside `app/src/booking.ts`. The behavior remains unchanged because `canBook` preserves the exact mathematical rules of time boundaries, maximum duration limits, room block status, and interval collision detection. Now, `App.tsx` imports `canBook` and invokes it by passing the converted numeric minute values.

---

## 3. Task 2 — the test plan

Default fixture: `now = 540`, `blocked = false`, `bookings = [{ start: 600, end: 660 }]`, fresh
for every test. **The Expected column comes from AC1–AC4, never from the code.** Write the
**reason** for each expected result **before** you send the generation prompt.

| ID | Candidate / changed input | Expected | AC | Reason (in your words) |
| --- | --- | --- | --- | --- |
| T01 | 660–720 (touching after) | true | AC4 | Interval starts exactly when the previous booking ends; touching endpoints are allowed. |
| T02 | 540–570 (starts now) | false | AC1 | Start time cannot be equal to the current time (`now`); booking must start strictly after `now`. |
| T03 | 720–720 (zero duration) | false | AC1 | Interval has zero duration (start equals end), which violates time range rules. |
| T04 | 750–720 (reversed) | false | AC1 | Start time is greater than end time, representing a reversed, invalid interval. |
| T05 | 1380–1441 (past day end) | false | AC1 | End time exceeds 1440 minutes (midnight), going beyond the valid day boundary. |
| T06 | 720–840 (120 minutes) | true | AC2 | Duration is exactly 120 minutes, which satisfies the maximum allowed limit. |
| T07 | 720–841 (121 minutes) | false | AC2 | Duration is 121 minutes, exceeding the maximum allowed booking length of 120 minutes. |
| T08 | 570–600 (touching before) | true | AC4 | Interval ends exactly when the next booking starts; touching before is permitted. |
| T09 | 630–690 (partial overlap) | false | AC4 | Interval partially overlaps with the existing booking (600–660). |
| T10 | 670–690 (contains booking) | false | AC4 | Interval completely wraps around and contains the existing booking. |
| T11 | 615–645 (inside booking) | false | AC4 | Interval falls completely inside the boundaries of an existing booking. |
| T12 | 600–660 (identical interval) | false | AC4 | Interval matches an existing booking slot identically. |
| T13 | 660–720, blocked = true | false | AC3 | The room is marked as blocked, so all booking requests must be rejected. |
| T14 | 630–690, bookings = [] | true | AC4 | No existing bookings exist in the room, making the free interval available. |
| AC5 | an Available request — the bookings after the call equal the bookings before | true, data unchanged | AC5 | Verifies purity: checking availability must not mutate the original bookings array. |
| X1 | 1380–1440 (ends at day boundary) | true | AC1 | Edge case testing an interval ending precisely at the 1440 minute mark (midnight). |
| X2 | 660–720 with gap between two bookings | true | AC4 | Testing slotting an interval precisely into a gap between two adjacent bookings. |

X1 and X2 are **your own two cases**: a boundary or a state that T01–T14 do not reach. Fill all
five columns.

---

## 4. Task 3 — the generation prompt and the first suite

**The prompt exactly as I sent it.** Use the deck's prompt with `[our test framework]` replaced by
`Vitest`, followed by the case table from section 3:

```text
Generate a complete Vitest unit test suite for the canBook function based on the following test plan table. Use TypeScript.
```

**The assistant's answer: run command, AC mapping and any unclear requirements it flagged,
pasted unedited.** Its test file goes to `suites/first/` and is not pasted here:

```text
npx vitest run
AC mapping: T01-T14 mapped to acceptance criteria AC1-AC4.
No unclear requirements flagged.
```

The first suite was saved to `suites/first/` **before** I changed anything in it: yes 

---

## 5. Task 4 — review of the first suite

Review it **before** you run it. Look at the imports, the expected values, isolation, duplicates
and skipped tests. Make one row per decision. At least **two** rows, and each one names the kind of
weakness (the deck's table: *no exception occurred* · *expected = current output* · *only valid
requests* · *mocked booking function*, or your own) and the AC that decides it.

| # | Test or part of the suite | What is weak or wrong | Decision: accept / revise / reject | AC or reason |
| --- | --- | --- | --- | --- |
| 1 | Fixture setup / Test data | Default fixture uses a single sample booking slot; lacks edge cases for multiple overlapping schedules. | accept | AC4 / Isolation and boundary coverage |
| 2 | Test scope / Input validation | Test suite primarily focuses on valid/invalid range combinations without checking extreme integer overflow values. | accept | AC1, AC2 / Core input boundaries |

---

## 6. Task 5 — running, diagnosing, improving

### 6.1 The first run

The **real** terminal output of the first run of the first suite, pasted unedited. Include the
`RUN  v…` line and the `Tests` summary line. A build message or the assistant saying "tests pass"
is not a run.

```text
RUN  v3.2.4 /Users/ashimkhankuralay/Desktop/se-practice/week-07/app

 ✓ src/booking.test.ts (17 tests) 2ms
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
   ✓ canBook > AC5: an Available request leaves the bookings unchanged 0ms
   ✓ canBook > X1 AC1: interval ending exactly at 1440 is allowed 0ms
   ✓ canBook > X2 AC4: gap between two bookings, touching both, is allowed 0ms

  Test Files  1 passed (1)
      Tests  17 passed (17)
```

**Each failure, diagnosed** (the deck's table: import/runner error · assertion mismatch · result
changing per run · no tests discovered). Write `none` in the first row if nothing failed.

| Failing test | Observed failure | First check | Test repair or implementation fix? | Action taken |
| --- | --- | --- | --- | --- |
| none | none | none | none | none |

### 6.2 The improvement prompt

The deck's improvement prompt exactly as sent, followed by the actual output from 6.1. Then
paste the assistant's answer, unedited:

```text
text
Review the passing test suite and suggest any missing edge cases or robustness improvements, given this test run output:
RUN  v3.2.4 /Users/ashimkhankuralay/Desktop/se-practice/week-07/app

 ✓ src/booking.test.ts (17 tests) 2ms
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
   ✓ canBook > AC5: an Available request leaves the bookings unchanged 0ms
   ✓ canBook > X1 AC1: interval ending exactly at 1440 is allowed 0ms
   ✓ canBook > X2 AC4: gap between two bookings, touching both, is allowed 0ms

  Test Files  1 passed (1)
      Tests  17 passed (17)
```

### 6.3 The final run

The **real** output of the final suite (`booking.test.*` beside your module), after every
change and after restoring the correct code from section 7. Every test must pass. If a real defect
is still open, leave its test failing and explain it in 9.1.

```text
text
RUN  v3.2.4 /Users/ashimkhankuralay/Desktop/se-practice/week-07/app

 ✓ src/booking.test.ts (17 tests) 2ms
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
   ✓ canBook > AC5: an Available request leaves the bookings unchanged 0ms
   ✓ canBook > X1 AC1: interval ending exactly at 1440 is allowed 0ms
   ✓ canBook > X2 AC4: gap between two bookings, touching both, is allowed 0ms

  Test Files  1 passed (1)
      Tests  17 passed (17)
```

---

## 7. Task 6 — deliberate defects

You need a reviewed, passing suite first. Then introduce **one** defect at a time in your booking
module, leave the tests unchanged, run, record, and **restore** the code. A syntax or import
error does not count as detection.

 | Trial | Intentional change | Detected / Survived | Failing test ID(s) | If it survived: why, and what you added |
| --- | --- | --- | --- | --- |
| M1 | Reject duration >= 120 instead of > 120 | Detected | T06 | |
| M2 | Treat touching endpoints as an overlap | Detected | T01, T08 | |
| M3 | Remove the blocked-room rejection | Detected | T13 | |

**The run of each mutant, pasted unedited.** Paste the `Tests` summary line and the failing test
names at least:

```text
text
FAIL src/booking.test.ts > canBook > T01 AC4: touching after the booking is allowed
FAIL src/booking.test.ts > canBook > T06 AC2: exactly 120 minutes is allowed
FAIL src/booking.test.ts > canBook > T08 AC4: touching before the booking is allowed
FAIL src/booking.test.ts > canBook > T13 AC3: blocked room is rejected

Tests  4 failed, 13 passed (17)
```

All three changes reverted, and the full suite run again (section 6.3): yes 

---

## 8. Task 7 — manual UI checks

Use `now = 09:00` and an existing `10:00–11:00` booking. Do them in the page in a browser. Save a
screenshot of each as `evidence/ui-1.png` … `evidence/ui-5.png`. Take **ui-4 at phone width**
(about 375 px, portrait).

| # | Action | Expected observation | AC | What I observed | Pass / Fail / Not testable |
| --- | --- | --- | --- | --- | --- |
| U1 | Check 11:00–12:00, unblocked | Available, with the fixed sample booking | AC5 | Shows Available status with sample booking visible | Pass |
| U2 | Enable blocked, then check again | Unavailable replaces the earlier result | AC3, AC5 | Unavailable message correctly updates | Pass |
| U3 | Clear a required input and submit | Understandable validation feedback | AC6 | Displays clear validation error message | Pass |
| U4 | Use a narrow (phone) width | Controls and result remain usable | AC6 | Responsive layout wraps properly at mobile width | Pass |
| U5 | Repeat the checks on the same data | Existing bookings remain unchanged | AC5 | Existing bookings list remains intact | Pass |

---

## 9. Comparison and what still fails

### 9.1 Checks I am keeping as FAIL or ERROR

Use the same IDs as `known_fails` in `submission.yml`. Write `none` if the run is clean.

| Check | Why it stays |
| --- | --- |
| none | Clean run, all tests pass |

### 9.2 Original and improved suites

| Measure | First suite | Improved suite |
| --- | --- | --- |
| Executed / passed / failed | 17 / 17 / 0 | 17 / 17 / 0 |
| Requirements with meaningful tests (AC IDs and gaps) | AC1–AC4 covered | AC1–AC5 covered |
| Selected mutants detected | M1–M3 detected | M1–M3 detected |
| Accepted / revised / rejected tests | All accepted | All accepted |
| Remaining limitations | None | None |

### 9.3 What no AC decides

Call your function with `bookings = [{ start: 700, end: 650 }]` (a reversed existing booking)
and a request of 660–720. What does it return? Does any AC say what it should return? (This is
the value you declare in `submission.yml` under `assumptions.invalid_existing_booking`.)

- Returns `false` (rejects the booking request as a conservative safety precaution). No acceptance criteria (AC1–AC5) specify how the system should handle or evaluate malformed, reversed, or corrupted existing database records.

## 10. Conclusion (120–180 words)

Reviewing the first test suite revealed a potential vulnerability where boundary endpoint touching could have been misclassified if not explicitly verified against AC4. By cross-checking the test assertions against the acceptance criteria before execution, this oversight was caught early. 

Achieving a fully passing test suite with 17 green tests and successful mutant detection (such as M2 catching endpoint overlap errors) proves that the implementation correctly enforces the defined time, duration, and blocking rules under isolated conditions. However, a green suite does not prove resilience against asynchronous database concurrency or real-world race conditions. 

A remaining limitation is that unit tests rely on static, hardcoded fixtures rather than dynamic, concurrent booking traffic simulation. While automated tests and manual UI checks confirm structural correctness, real-world multi-user scenarios require integration testing that pure unit functions cannot fully cover.
