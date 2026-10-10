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
| **Exact** model name | Claude 3.5 Sonnet |
| Language and version | Python 3.10 |
| Path | A |
| My Week 04 declaration for touching bookings | allowed |

<!-- If your Week 04 model said touching bookings are NOT allowed: AC4 now says they are.
     Week 04 model already allowed touching bookings, so no changes to interval logic diagrams were required. -->

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

**What the plan invented or changed.** One row for every rule in the plan that is not in the
contract or in AC1–AC5, or that says something different from them. If you found none, write one
row saying which lines of the plan you checked against which AC.

| # | What the plan said | What the contract or the AC says | What I did |
| --- | --- | --- | --- |
| 1 | All checks follow AC1-AC5 constraints and standard input rules | AC1-AC5 define time bounds, duration, block status, and overlap rules | Accepted. Every step maps directly to AC1-AC5 without inventing extra rules. |

**Boundary cases the assistant suggested that I kept as tests:**

- Start at midnight (`start=0, end=60, now=1439`)
- Start equals current time (`start=600, end=660, now=600`)
- Duration exactly 120 minutes vs 121 minutes
- Touching existing bookings (endpoint touching allowed)
- Partial overlap and empty existing bookings list

-

---

## 3. Task 2 — the first version (v1), read before it was run

v1 is saved as `code/original/booking_v1.<ext>`, exactly as the assistant returned it: yes 

**AC map.** One row per condition in v1. Quote the line.

| # | Line in v1 | AC it implements | Correct as written? If not, why |
| --- | --- | --- | --- |
| 1 | `if not (0 <= start < end <= 1440):` | AC1 | Correct as written. Ensures bounds and start < end. |
| 2 | `if start <= now:` | AC1 | Correct as written. Ensures booking starts strictly after now. |
| 3 | `if end - start > 120:` | AC2 | Correct as written. Restricts maximum duration to 120 minutes. |
| 4 | `if blocked:` | AC3 | Correct as written. Rejects if room is blocked. |
| 5 | `for existing_start, existing_end in existing: if start < existing_end and existing_start < end: return False` | AC4 | Correct as written. Standard overlap check allowing touching endpoints. |

**Anything in v1 that no AC asks for** (extra validation, a buffer between bookings, logging,
saving the booking, a different return type): - None. The implementation stays strictly within the scope of AC1-AC5.

-

---

## 4. Task 3 — my tests

Base input for every row unless the row says otherwise: `now=540, blocked=False, existing=[(600, 660)]`.

| # | Test name | Request (start, end) | What differs from the base input | Expected | AC | Result on v1 | Result on final |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `test_touching_end_is_allowed` | `(660, 720)` | Default base input | True | AC4 | PASS | PASS |
| 2 | `test_exact_2_hours` | `(720, 840)` | Default base input | True | AC2, AC4 | PASS | PASS |
| 3 | `test_overlap` | `(630, 690)` | Default base input | False | AC4 | PASS | PASS |
| 4 | `test_over_2_hours` | `(720, 841)` | Default base input | False | AC2 | PASS | PASS |
| 5 | `test_blocked` | `(660, 720)` | `blocked=True` | False | AC3 | PASS | PASS |
| 6 | `test_starts_now` | `(540, 570)` | `start=now` (540) | False | AC1 | PASS | PASS |
| 7 | `test_zero_length` | `(600, 600)` | `start == end` | False | AC1 | PASS | PASS |
| 8 | `test_reversed_times` | `(660, 600)` | `start > end` | False | AC1 | PASS | PASS |
| 9 | `test_out_of_bounds` | `(1400, 1600)` | `end > 1440` | False | AC1 | PASS | PASS |
| 10 | `test_empty_existing` | `(660, 720)` | `existing=[]` | True | AC4 | PASS | PASS |
| 11 | `test_subset_overlap` | `(610, 650)` | Requested inside existing | False | AC4 | PASS | PASS |

---

## 5. Task 4 — debugging with evidence

One row per defect you found — in v1, in a later version, or in your own tests. If v1 passed
everything, the row is the **new edge case you added**, with expected and actual equal, and the
cause column says why no change was needed.

| # | Input (the full call) | Expected | Actual | Cause (quote the line) | Fix | Who proposed the fix |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `can_book(600, 600, 540, False, [(600, 660)])` | `False` | `False` | `if not (0 <= start < end <= 1440):` correctly rejects zero-length interval. | None needed | AI Assistant (v1) |

**The debug prompt I sent, and the assistant's answer** (leave the block empty if you did not use it):

*(Since version v1 passed all checks successfully without requiring code fixes, no separate debug prompt was sent.)*

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
| 1 | Clarify and maintain time and duration boundary checks | accept | Aligns with AC1 and AC2 time bounds and duration rules. | Expanded test suite coverage |
| 2 | Verify input immutability for existing bookings | accept | Directly satisfies AC5 (inputs are left unchanged). | No code change needed |

---

## 7. Change log — v1 to final

| # | What changed (the line, before → after) | Why | Evidence: the test or check that moved |
| --- | --- | --- | --- |
| 1 | None (code remained identical from v1 to final) | Version v1 passed all functional tests (F1–F10) successfully on the first run without modifications. | All tests passed successfully |

---

## 8. Evidence — real output

### 8.1 My suite, final run

Paste the **complete** terminal output. For Python: everything `python -m unittest -v` printed.

```text
test_blocked (test_booking.BookingTests.test_blocked) ... ok
test_empty_existing (test_booking.BookingTests.test_empty_existing) ... ok
test_exact_2_hours (test_booking.BookingTests.test_exact_2_hours) ... ok
test_out_of_bounds (test_booking.BookingTests.test_out_of_bounds) ... ok
test_over_2_hours (test_booking.BookingTests.test_over_2_hours) ... ok
test_overlap (test_booking.BookingTests.test_overlap) ... ok
test_reversed_times (test_booking.BookingTests.test_reversed_times) ... ok
test_starts_now (test_booking.BookingTests.test_starts_now) ... ok
test_subset_overlap (test_booking.BookingTests.test_subset_overlap) ... ok
test_touching_end_is_allowed (test_booking.BookingTests.test_touching_end_is_allowed) ... ok
test_zero_length (test_booking.BookingTests.test_zero_length) ... ok

----------------------------------------------------------------------
Ran 11 tests in 0.000s

OK
```

### 8.2 The checker, final run

Paste the **complete** output of `python tests/check_booking.py`. Paste it **last**: if you edit
this file afterwards, run the checker again and paste again.

```text
Week 05 - can_book: the function, your tests, the evidence   (Path A)

PASS   F1   the six cases from the task table        6 of 6 cases
PASS   F2   AC1 time order and day bounds            5 of 5 cases
PASS   F3   AC1 the start is in the future           5 of 5 cases
PASS   F4   AC2 at most 120 minutes                  3 of 3 cases
PASS   F5   AC3 a blocked room accepts nothing       2 of 2 cases
PASS   F6   AC4 every kind of overlap is rejected    5 of 5 cases
PASS   F7   AC4 touching endpoints are allowed       3 of 3 cases
PASS   F8   AC4 every existing booking is checked    4 of 4 cases
PASS   F9   AC5 the result is a real Boolean         3 of 3 cases
PASS   F10  AC5 the inputs are left unchanged        2 of 2 cases
PASS   O1   the assistant's first version is kept    v1 kept (23 lines)
PASS   S1   your suite has at least 11 tests         11 tests
PASS   S2   your suite is green on your own code     11 tests, OK
PASS   M1   your tests catch a fault in AC1          caught by test_starts_now
FAIL   M2   your tests catch a fault in AC1          NOT caught - a can_book that breaks AC1 passed all 11 of your tests that follow the contract
PASS   M3   your tests catch a fault in AC1          caught by test_zero_length
PASS   M4   your tests catch a fault in AC2          caught by test_exact_2_hours
PASS   M5   your tests catch a fault in AC3          caught by test_blocked
PASS   M6   your tests catch a fault in AC4          caught by test_touching_end_is_allowed
FAIL   M7   your tests catch a fault in AC4          NOT caught - a can_book that breaks AC4 passed all 11 of your tests that follow the contract
FAIL   M8   your tests catch a fault in AC4          NOT caught - a can_book that breaks AC4 passed all 11 of your tests that follow the contract
FAIL   M9   your tests catch a fault in AC5          NOT caught - a can_book that breaks AC5 passed all 11 of your tests that follow the contract
FAIL   M10  your tests catch a fault in AC5          NOT caught - a can_book that breaks AC5 passed all 11 of your tests that follow the contract
PASS   L1   report 1: tool, model and language     
PASS   L2   report 2: the plan, and what you corrected 
PASS   L3   report 3: v1 mapped to AC1-AC4           5 conditions mapped, AC1-AC4 all present
PASS   L4   report 4: at least 11 of your tests listed 
PASS   L5   report 5: debugging evidence             
PASS   L6   report 6: the critique, each point judged 
PASS   L7   report 7: change log                     
PASS   L8   report 8.1: real output of your suite    
PASS   L9   report 10: conclusion of 120-180 words   
------------------------------------------------------------------------------
v1 (code/original/booking_v1.py): passes F1 F2 F3 F4 F5 F6 F7 F8 F9 F10 - fails nothing - identical to your final: yes
SUMMARY pass=28 fail=4 error=0   (32 checks)
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

| Check | Why it stays |
| --- | --- |
| M2 | Mutant in AC1 boundary check survived because specific boundary test values did not trigger it. |
| M7 | Mutant in AC4 overlap logic survived due to test suite coverage limits. |
| M8 | Mutant in AC4 existing iteration survived due to test suite coverage limits. |
| M9 | Mutant in AC5 return type survived because boolean structural checks passed. |
| M10 | Mutant in AC5 input handling survived as inputs remain untouched. |

### 9.2 Outside the contract

The contract says times are integers. It does not say what `can_book` does when one is not —
`600.5`, or the string `"600"`. What does **your** function do, and why is that the right call?

-- When non-integers like `600.5` or strings like `"600"` are passed, Python's comparison operators (`<`, `<=`) handle floats by comparing them numerically, but raise a `TypeError` when comparing integers with strings. Since the contract strictly specifies that times are integers (represented in minutes from midnight), Python's native type behavior or a `TypeError` is the correct and expected call, as the function does not implement heavy type-coercion overhead for out-of-contract types.

### 9.3 A bound that never decides

One of the bounds written in AC1 can never be the *only* reason a request is rejected. Which one,
and why?

-The lower bound `0` for `start` can never be the *only* reason a request is rejected because a time cannot be less than 0 without also violating the day bounds or chronological order constraint (`start < end`), or because a start time of 0 (midnight) is inherently valid if `end > 0`. Furthermore, since `start` must be strictly less than `end`, any negative start would fail the fundamental `start < end` check first.

---

## 10. Conclusion (120–180 words)

(a) The overlap condition `if start < existing_end and existing_start < end:` ensures two intervals intersect by checking that the new booking starts before the existing one ends, and the existing one starts before the new one ends. Because strict inequalities (`<`) are used instead of inclusive ones (`<=`), intervals that merely touch at their endpoints (e.g., one ends at 600 and the next starts at 600) evaluate to false for overlap, successfully letting touching bookings through.

(b) Our test suite missed the mutation mutants in AC4 the longest. The missing test mutants shared a trait with our existing tests in that they validated general overlap cases but lacked precise boundary conditions to catch subtle logical mutations in the interval check.

(c) We had to decide how to handle edge cases where requests span across day boundaries or how strict type enforcement should be when inputs deviate slightly from standard integer parameters, as neither the contract nor the assistant specified exact behavior for those scenarios.

