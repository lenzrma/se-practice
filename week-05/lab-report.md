# Week 05 — Lab report

**Name:** Ashimkhan Kuralay
**Group:** Software Engineering (Monday 16:00–19:00)
**Date:** October 10, 2026

Fill in every section. **Do not delete, rename or renumber the headings** — the checker and the
grader find your answers by them. Add rows to any table; never remove its header.

---

## 1. Setup

| | |
| --- | --- |
| Assistant (tool) | Claude |
| **Exact** model name | Claude Sonnet 5.5 |
| Language and version | Python 3.14.3 |
| Path | A |
| My Week 04 declaration for touching bookings | allowed |

<!-- If your Week 04 model said touching bookings are NOT allowed: AC4 now says they are.
     One sentence here on what that changes in your Week 04 diagrams. This is a finding, not a penalty. -->

---

## 2. Task 1 — the plan

**The assistant's plan, pasted unedited:**

```text
Implementation plan for `can_book`:
1. Validate time order and day bounds (AC1): 0 <= start < end <= 1440.
2. Validate future start time (AC1): start > now.
3. Validate maximum duration of 120 minutes (AC2): end - start <= 120.
4. Check if the room is blocked (AC3): blocked is False.
5. Check for overlapping bookings (AC4): iterate over existing bookings using interval separation.
6. Return True if all checks pass, otherwise False.

 ### 2. Assumptions

- Python 3 is used.
- `start`, `end`, and `now` are integer minutes after midnight on the same date.
- `now` is valid and falls within `0–1439`.
- `blocked` is a Boolean.
- `existing` contains only valid `(start, end)` tuples representing active bookings for the selected room.
- The requested interval must start strictly in the future; `start == now` is invalid.
- An end time of `1440` is valid, representing midnight at the end of the date.
- Inputs are not changed, and no booking is saved or confirmed by this function.

 ### 3. Boundary cases to test

| Case                                       | Example                                       | Expected                     |
| ------------------------------------------ | --------------------------------------------- | ---------------------------- |
| Start at midnight                          | `start=0, end=60, now=1439`                   | `False`                      |
| Start equals current time                  | `start=600, end=660, now=600`                 | `False`                      |
| Start one minute in the future             | `start=601, end=660, now=600`                 | `True`, if other checks pass |
| Start equals end                           | `start=600, end=600`                          | `False`                      |
| Start greater than end                     | `start=700, end=600`                          | `False`                      |
| End exceeds midnight                       | `start=1380, end=1441`                        | `False`                      |
| End exactly at midnight                    | `start=1320, end=1440`                        | `True`, if other checks pass |
| Duration exactly 120 minutes               | `start=600, end=720`                          | `True`, if other checks pass |
| Duration 121 minutes                       | `start=600, end=721`                          | `False`                      |
| Room blocked                               | Valid interval, `blocked=True`                | `False`                      |
| Existing booking ends at requested start   | Requested `(600, 660)`, existing `(540, 600)` | `True`                       |
| Existing booking starts at requested end   | Requested `(600, 660)`, existing `(660, 720)` | `True`                       |
| Partial overlap                            | Requested `(600, 660)`, existing `(650, 700)` | `False`                      |
| Requested interval inside existing booking | Requested `(610, 650)`, existing `(600, 660)` | `False`                      |
| Existing booking inside requested interval | Requested `(600, 720)`, existing `(630, 660)` | `False`                      |
| Empty existing bookings                    | Valid interval, `existing=[]`                 | `True`, if other checks pass |

Note: Expected `True` values assume that all other acceptance criteria are satisfied.

 ### 4. Important implementation pitfalls

- Using `start >= now` instead of `start > now`.
- Allowing durations greater than 120 minutes.
- Treating touching endpoints as overlapping.
- Forgetting to check every existing booking.
- Checking overlap before validating the requested interval in a way that produces incorrect results.
- Sorting, removing, or otherwise modifying `existing`.

The implementation should be a simple decision function: reject invalid conditions early, then return `True` only after every check passes.
```

Only change to the plan text: I put one space before the `###` lines, so the checker does not read them as report headings.

**What the plan invented or changed.** One row for every rule in the plan that is not in the
contract or in AC1–AC5, or that says something different from them. If you found none, write one
row saying which lines of the plan you checked against which AC.

| # | What the plan said | What the contract or the AC says | What I did |
| --- | --- | --- | --- |
| 1 | Plan steps 1–6 (day bounds, start after now, 120 minutes, blocked, overlap, return) and the assumptions list | Steps 1–2 are AC1, step 3 is AC2, step 4 is AC3, step 5 is AC4, step 6 and the "inputs are not changed" assumption are AC5 | I checked every step against its AC and found no invented rule, so I changed nothing |

**Boundary cases the assistant suggested that I kept as tests:**

- Start equals now, and start one minute after now (`test_starts_now`, `test_table_starts_now`, `test_start_one_min_after_now`)
- End exactly at 1440 and end at 1441 (`test_end_of_day_inclusive`, `test_out_of_bounds_end`)
- Duration exactly 120 and 121 minutes (`test_exact_2_hours`, `test_over_2_hours`)
- Start equals end and start after end (`test_zero_length`, `test_reversed_times`)
- Blocked room (`test_blocked`)
- Touching on both sides (`test_touching_left_allowed`, `test_touching_right_allowed`)
- Partial overlap and an existing booking inside the request (`test_overlap_left`, `test_overlap_encloses`)
- Empty `existing` (used as `existing=[]` in most of the AC1–AC3 tests)

---

## 3. Task 2 — the first version (v1), read before it was run

v1 is saved as `code/original/booking_v1.py`, exactly as the assistant returned it: yes

**AC map.** One row per condition in v1. Quote the line.

| # | Line in v1 | AC it implements | Correct as written? If not, why |
| --- | --- | --- | --- |
| 1 | `if not (0 <= start < end <= 1440):` | AC1 | Correct as written. Checks the day bounds and that start is before end. |
| 2 | `if start <= now:` | AC1 | Correct as written. Rejects start equal to now, so start must be strictly after now. |
| 3 | `if end - start > 120:` | AC2 | Correct as written. Exactly 120 minutes passes, 121 is rejected. |
| 4 | `if blocked:` | AC3 | Correct as written. A blocked room accepts nothing. |
| 5 | `if start < existing_end and existing_start < end:` inside `for existing_start, existing_end in existing:` | AC4 | Correct as written. Strict comparisons, so touching endpoints are allowed. Every existing booking is checked. |

**Anything in v1 that no AC asks for** (extra validation, a buffer between bookings, logging,
saving the booking, a different return type):

- Nothing. v1 has no type checks, no buffer, no sorting, no logging and returns only True or False.

---

## 4. Task 3 — my tests

Base input for every row unless the row says otherwise: `now=540, blocked=False, existing=[(600, 660)]`.

| # | Test name | Request (start, end) | What differs from the base input | Expected | AC | Result on v1 | Result on final |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `test_end_of_day_inclusive` | `(1380, 1440)` | `existing=[]` | True | AC1 | PASS | PASS |
| 2 | `test_out_of_bounds_end` | `(1380, 1441)` | `existing=[]`; duration is 61, so only the day bound rejects it | False | AC1 | PASS | PASS |
| 3 | `test_start_one_min_after_now` | `(541, 571)` | `existing=[]` | True | AC1 | PASS | PASS |
| 4 | `test_start_in_past` | `(500, 530)` | `existing=[]` | False | AC1 | PASS | PASS |
| 5 | `test_starts_now` | `(540, 600)` | `existing=[]`, start equals now | False | AC1 | PASS | PASS |
| 6 | `test_exact_2_hours` | `(600, 720)` | `existing=[]`, duration 120 | True | AC2 | PASS | PASS |
| 7 | `test_over_2_hours` | `(600, 721)` | `existing=[]`, duration 121 | False | AC2 | PASS | PASS |
| 8 | `test_zero_length` | `(600, 600)` | `existing=[]`, start equals end | False | AC1 | PASS | PASS |
| 9 | `test_reversed_times` | `(660, 600)` | `existing=[]`, start after end | False | AC1 | PASS | PASS |
| 10 | `test_blocked` | `(600, 660)` | `existing=[]`, `blocked=True` | False | AC3 | PASS | PASS |
| 11 | `test_overlap_left` | `(570, 630)` | none (base) | False | AC4 | PASS | PASS |
| 12 | `test_overlap_encloses` | `(570, 690)` | none (base) | False | AC4 | PASS | PASS |
| 13 | `test_overlap_identical` | `(600, 660)` | none (base) | False | AC4 | PASS | PASS |
| 14 | `test_touching_left_allowed` | `(570, 600)` | none (base) | True | AC4 | PASS | PASS |
| 15 | `test_touching_right_allowed` | `(660, 720)` | none (base) | True | AC4 | PASS | PASS |
| 16 | `test_multiple_existing_overlap_second` | `(720, 780)` | `existing=[(600,660),(700,760)]` | False | AC4 | PASS | PASS |
| 17 | `test_unsorted_existing` | `(610, 650)` | `existing=[(900,960),(600,660)]` | False | AC4 | PASS | PASS |
| 18 | `test_window_between_three` | `(760, 800)` | `existing=[(600,660),(700,760),(800,860)]` | True | AC4 | PASS | PASS |
| 19 | `test_immutability` | `(780, 840)` and `(610, 650)` | `existing=[(900,960),(600,660),(700,760)]`, list compared with its copy after both calls | list unchanged | AC5 | PASS | PASS |
| 20 | `test_table_overlap` | `(630, 690)` | none (base) | False | AC4 | PASS | PASS |
| 21 | `test_table_blocked` | `(660, 720)` | `blocked=True` | False | AC3 | PASS | PASS |
| 22 | `test_table_exact_2_hours` | `(720, 840)` | none (base) | True | AC2 | PASS | PASS |
| 23 | `test_table_over_2_hours` | `(720, 841)` | none (base) | False | AC2 | PASS | PASS |
| 24 | `test_table_starts_now` | `(540, 570)` | none (base), start equals now | False | AC1 | PASS | PASS |

Expected values come from AC1–AC5 and the task table, not from running the code. v1 and the final `booking.py` are identical, so the two result columns are the same.

---

## 5. Task 4 — debugging with evidence

One row per defect you found — in v1, in a later version, or in your own tests. If v1 passed
everything, the row is the **new edge case you added**, with expected and actual equal, and the
cause column says why no change was needed.

| # | Input (the full call) | Expected | Actual | Cause (quote the line) | Fix | Who proposed the fix |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `can_book(1380, 1440, 540, False, [])` | `True` | `True` | `if not (0 <= start < end <= 1440):` lets `end == 1440` through, as AC1 says, so no change was needed | None needed | nobody, v1 was already correct |

v1 passed all my tests and all F checks, so I did not send the debug prompt.

**The debug prompt I sent, and the assistant's answer** (leave the block empty if you did not use it):

```text
```

---

## 6. Task 5 — the critique

**The assistant's critique, pasted unedited:**

```text
The implementation of can_book corresponds to AC1–AC5 according to the given contract. Here are two specific recommendations for improvement.
1. Clarify time and duration boundary checks
Current checks are correct:
- 0 <= start < end <= 1440 — allows start = 0 and end = 1440, but rejects end = 1441.
- start <= now — correctly rejects booking start exactly at the 'now' moment.
- end - start > 120 — allows exactly 120 minutes and rejects 121 minutes.
Suggestion: Keep these conditions unchanged and add boundary tests for start = now, start = now + 1, durations of 120 and 121 minutes, as well as end = 1440. This will help prevent errors during future modifications.
2. Verify overlaps and the immutability of existing
Current overlap check:
if start < existing_end and existing_start < end:    return False

It correctly allows touching intervals and detects partial and full overlaps. The time complexity is O(n) and auxiliary space complexity is O(1), where n is the number of existing bookings.
Suggestion: Add tests for partial overlap, nested intervals, and boundary touching. Additionally, compare existing before and after the call to confirm AC5 — inputs are not modified.
Conclusion: Rewriting the function is not required. The most useful improvements are strengthening boundary tests and explicitly verifying input immutability.
```

| # | Suggestion | accept / reject | Reason — cite the AC or the contract line | Suite after the change |
| --- | --- | --- | --- | --- |
| 1 | Keep the boundary conditions and add tests for start = now, start = now + 1, 120 and 121 minutes, end = 1440 | accept | AC1 and AC2 name exactly these boundaries; I added `test_start_one_min_after_now`, `test_end_of_day_inclusive` and the other boundary tests | Ran 24 tests, OK |
| 2 | Add tests for partial overlap, nested intervals and touching, and compare `existing` before and after the call | accept | AC4 (overlap and touching) and AC5 (never alter existing); I added the overlap tests and `test_immutability` | Ran 24 tests, OK |

---

## 7. Change log — v1 to final

| # | What changed (the line, before → after) | Why | Evidence: the test or check that moved |
| --- | --- | --- | --- |
| 1 | No code change: `booking.py` is identical to `booking_v1.py`. Only the suite changed, from 11 to 24 tests. | v1 already passed F1–F10. My first 11 tests were too weak: M2, M7, M8, M9 and M10 survived. | After adding the tests, M1–M10 all PASS and the suite runs 24 tests, OK |

---

## 8. Evidence — real output

### 8.1 My suite, final run

Paste the **complete** terminal output. For Python: everything `python -m unittest -v` printed.

```text
test_blocked (test_booking.BookingTests.test_blocked) ... ok
test_end_of_day_inclusive (test_booking.BookingTests.test_end_of_day_inclusive) ... ok
test_exact_2_hours (test_booking.BookingTests.test_exact_2_hours) ... ok
test_immutability (test_booking.BookingTests.test_immutability) ... ok
test_multiple_existing_overlap_second (test_booking.BookingTests.test_multiple_existing_overlap_second) ... ok
test_out_of_bounds_end (test_booking.BookingTests.test_out_of_bounds_end) ... ok
test_over_2_hours (test_booking.BookingTests.test_over_2_hours) ... ok
test_overlap_encloses (test_booking.BookingTests.test_overlap_encloses) ... ok
test_overlap_identical (test_booking.BookingTests.test_overlap_identical) ... ok
test_overlap_left (test_booking.BookingTests.test_overlap_left) ... ok
test_reversed_times (test_booking.BookingTests.test_reversed_times) ... ok
test_start_in_past (test_booking.BookingTests.test_start_in_past) ... ok
test_start_one_min_after_now (test_booking.BookingTests.test_start_one_min_after_now) ... ok
test_starts_now (test_booking.BookingTests.test_starts_now) ... ok
test_table_blocked (test_booking.BookingTests.test_table_blocked) ... ok
test_table_exact_2_hours (test_booking.BookingTests.test_table_exact_2_hours) ... ok
test_table_over_2_hours (test_booking.BookingTests.test_table_over_2_hours) ... ok
test_table_overlap (test_booking.BookingTests.test_table_overlap) ... ok
test_table_starts_now (test_booking.BookingTests.test_table_starts_now) ... ok
test_touching_left_allowed (test_booking.BookingTests.test_touching_left_allowed) ... ok
test_touching_right_allowed (test_booking.BookingTests.test_touching_right_allowed) ... ok
test_unsorted_existing (test_booking.BookingTests.test_unsorted_existing) ... ok
test_window_between_three (test_booking.BookingTests.test_window_between_three) ... ok
test_zero_length (test_booking.BookingTests.test_zero_length) ... ok

----------------------------------------------------------------------
Ran 24 tests in 0.000s

OK
```

### 8.2 The checker, final run

Paste the **complete** output of `python tests/check_booking.py`. Paste it **last**: if you edit
this file afterwards, run the checker again and paste again.

```text
Week 05 - can_book: the function, your tests, the evidence   (Path A)

PASS   F1   the six cases from the task table           6 of 6 cases
PASS   F2   AC1 time order and day bounds               5 of 5 cases
PASS   F3   AC1 the start is in the future              5 of 5 cases
PASS   F4   AC2 at most 120 minutes                     3 of 3 cases
PASS   F5   AC3 a blocked room accepts nothing          2 of 2 cases
PASS   F6   AC4 every kind of overlap is rejected       5 of 5 cases
PASS   F7   AC4 touching endpoints are allowed          3 of 3 cases
PASS   F8   AC4 every existing booking is checked       4 of 4 cases
PASS   F9   AC5 the result is a real Boolean            3 of 3 cases
PASS   F10  AC5 the inputs are left unchanged           2 of 2 cases
PASS   O1   the assistant's first version is kept       v1 kept (23 lines)
PASS   S1   your suite has at least 11 tests            24 tests
PASS   S2   your suite is green on your own code        24 tests, OK
PASS   M1   your tests catch a fault in AC1             caught by test_starts_now, test_table_starts_now
PASS   M2   your tests catch a fault in AC1             caught by test_out_of_bounds_end
PASS   M3   your tests catch a fault in AC1             caught by test_zero_length
PASS   M4   your tests catch a fault in AC2             caught by test_exact_2_hours, test_table_exact_2_hours
PASS   M5   your tests catch a fault in AC3             caught by test_blocked, test_table_blocked
PASS   M6   your tests catch a fault in AC4             caught by test_touching_left_allowed, test_touching_right_allowed, test_window_between_three
PASS   M7   your tests catch a fault in AC4             caught by test_multiple_existing_overlap_second, test_unsorted_existing
PASS   M8   your tests catch a fault in AC4             caught by test_overlap_encloses
PASS   M9   your tests catch a fault in AC5             caught by test_immutability
PASS   M10  your tests catch a fault in AC5             caught by test_immutability
PASS   L1   report 1: tool, model and language          tool, model and language recorded
PASS   L2   report 2: the plan, and what you corrected  plan pasted, 17 row(s) on what you corrected or verified
PASS   L3   report 3: v1 mapped to AC1-AC4              5 conditions mapped, AC1-AC4 all present
PASS   L4   report 4: at least 11 of your tests listed  24 tests listed
PASS   L5   report 5: debugging evidence                1 row(s) of input / expected / actual
PASS   L6   report 6: the critique, each point judged   critique pasted, 2 points judged
PASS   L7   report 7: change log                        1 change-log row(s)
PASS   L8   report 8.1: real output of your suite       suite output pasted
PASS   L9   report 10: conclusion of 120-180 words      150 words
------------------------------------------------------------------------------
v1 (code/original/booking_v1.py): passes F1 F2 F3 F4 F5 F6 F7 F8 F9 F10 - fails nothing - identical to your final: yes
SUMMARY pass=32 fail=0 error=0   (32 checks)
Behaviour and shape are clean. This says nothing about the quality of your review.

```

### 8.3 Path B only — three faults I planted myself

Break your own function on purpose, one line at a time, run your suite, restore the line.

| # | Line I changed (before → after) | AC it breaks | Test that failed |
| --- | --- | --- | --- |
| 1 | | | |
| 2 | | | |
| 3 | | | |

The three failing runs (Path A students leave this block empty):

```text
```

---

## 9. What still fails, and what the contract does not say

### 9.1 Checks I am keeping as FAIL or ERROR

The same IDs as `known_fails` in `submission.yml`. Write `none` if the run is clean.

none

| Check | Why it stays |
| --- | --- |
| none | The final run has no FAIL and no ERROR. With my first 11 tests M2, M7, M8, M9 and M10 survived; the extra tests (section 7) caught them. |

### 9.2 Outside the contract

The contract says times are integers. It does not say what `can_book` does when one is not —
`600.5`, or the string `"600"`. What does **your** function do, and why is that the right call?

- I ran both. `can_book(600.5, 660, 540, False, [])` returns `True`: Python compares a float with an int without complaint, so the function treats it as valid. `can_book("600", 660, 540, False, [])` raises `TypeError` on the line `if not (0 <= start < end <= 1440):`. I left it this way on purpose: the contract guarantees integers, and a type check would be a rule that no AC asks for. The price is that the string case raises an exception instead of returning False, but that input is outside the contract.

### 9.3 A bound that never decides

One of the bounds written in AC1 can never be the *only* reason a request is rejected. Which one,
and why?

- The lower bound `0 <= start`. The contract says `now` is 0–1439 and AC1 also requires `start > now`, so `start` is always at least 1. Any negative start is already rejected by `start > now`, so `0 <= start` never decides alone.

---

## 10. Conclusion (120–180 words)

(a) The overlap condition is `start < existing_end and existing_start < end`. A new booking overlaps only if it starts before the old one ends and the old one starts before the new one ends. Both comparisons are strict, so a booking that ends at 660 and another that starts at 660 do not overlap. That is how touching bookings get through, as AC4 requires.

(b) My first suite of 11 tests missed the faults in AC4 and AC5 the longest (M7–M10), plus M2 in AC1. Every test used one existing booking, and I never checked the list after the call. I added tests with several and unsorted bookings, an end of 1440 and 1441, and an immutability test.

(c) I had to decide what happens with 600.5 or "600". The contract says nothing, so I left it unhandled: a float returns True and a string raises TypeError.