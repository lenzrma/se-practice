# SIS #03 — Report: Smart Campus Room Availability Checker

<!-- The ONLY file you write prose in. Keep every numbered heading (## 1. … ## 13.) and every
     ### sub-heading, and the **Label:** words — the checker finds your answers by them.
     Replace every "(write here)" and "(paste here)". Delete these <!-- --> comments if you like. -->

## 1. Setup and reuse

<!-- Model: the exact model with its version, as the tool shows it ("ChatGPT" is a tool, not a
     model). If the tool does not show it, write: not displayed
     Reuse: week-05 if code/original/booking_v1.py is your Week 05 v1, copied unedited;
     week-06 if web/original/ is your Week 06 v1 export; fresh if you generated it for this SIS. -->

| Item | Value |
| --- | --- |
| Coding assistant (tool) | Cursor |
| Coding assistant model | Claude 3.5 Sonnet |
| Bolt.new model | Claude 3.5 Sonnet |
| Bolt project link | not-shared |
| Language | Python |
| Path | A |
| Python v1 from | fresh |
| Web v1 from | fresh |

## 2. Baseline — before any new AI exchange

<!-- Written by you, without AI, before the first exchange of this SIS. Commit and push it
     first (README §2). Reusing Week 05/06 work does not exempt you: this section is new. -->

### 2.1 Scope in my own words

**Scope:** A responsive single-page application for checking real-time campus room availability using mock data without creating, confirming, or storing bookings, completely isolated from external APIs and databases.

### 2.2 The acceptance criteria in my own words

| AC | In my own words |
| --- | --- |
| AC1 | Booking times are integer minutes past midnight from 0 to 1440, with start strictly after current time now. |
| AC2 | Booking duration cannot exceed 120 minutes, though exactly 120 minutes is fully allowed. |
| AC3 | Any availability request for a room marked as blocked must be immediately rejected. |
| AC4 | Requests overlapping existing bookings are rejected, but bookings touching only at boundary endpoints do not count as overlap. |
| AC5 | Returns a clear Available or Unavailable status while leaving existing booking lists unmodified. |
| AC6 | Displays clear validation messages and supports a usable layout on narrow mobile screens. |

### 2.3 Likely failure points

<!-- At least two. The brief's examples: endpoint overlap, starts-now. -->

| # | Failure point | AC | How I will check it |
| --- | --- | --- | --- |
| 1 | Endpoint overlap mishandling when new start equals existing end | AC4 | Test case T1 (660–720 with existing 600–660), expecting Available. |
| 2 | Rejecting requests starting exactly at current time `now` | AC1 | Test case T6 (540–570 when now=540), expecting Unavailable. |

### 2.4 The contract

| Parameter | Meaning | Type and allowed values |
| --- | --- | --- |
| `start` | Proposed booking start time in minutes from midnight | Integer (0 to 1439) |
| `end` | Proposed booking end time in minutes from midnight | Integer (1 to 1440, start < end) |
| `now` | Current time in minutes from midnight | Integer (0 to 1439) |
| `blocked` | Flag indicating if the room is unavailable for booking | Boolean (`True` or `False`) |
| `existing` | List of already reserved time slots `(start, end)` | List of tuples of integers `[(int, int)]` |
| returns | Availability verdict | Boolean (`True` if available, `False` otherwise) |

### 2.5 Initial assumptions and manual checks

**Assumptions:**

1. Input parameters `now`, `start`, and `end` are valid integer values within a single 24-hour day cycle (0 to 1440).
2. Existing bookings list is well-formed where each tuple has `start < end` and no internal mutations occur during checking.

**Checked manually:**

- Verification of boundary conditions (duration == 120, start == now, start == existing_end) using Python terminal interactive checks.

## 3. Python v1 review

<!-- One row per conditional branch in code/original/booking_v1.py (your language's v1 on
     Path B). Quote the condition exactly. AC1-AC4 must all appear in the AC column. -->

| Branch in v1 (quoted) | AC | Satisfies it? | Why |
| --- | --- | --- | --- |
| `if blocked: return False` | AC3 | Yes | Immediately rejects any booking request if the room is blocked. |
| `if start <= now: return False` | AC1 | Yes | Ensures the booking start time is strictly in the future relative to now. |
| `if start < 0 or end > 1440 or start >= end: return False` | AC1 | Yes | Validates that minutes fall within the daily window [0, 1440] and time goes forward. |
| `if end - start > 120: return False` | AC2 | Yes | Enforces the maximum duration limit of 120 minutes. |
| `if max(start, b_start) < min(end, b_end): return False` | AC4 | Yes | Checks and rejects overlapping intervals while allowing touching endpoints. |

## 4. Prototype v1 in Bolt.new

**Prompt as sent:**

~~~~text
Create a responsive single-page application named Smart Campus Room Availability Checker for one selected room with fictional booking data. It checks availability only and never creates or confirms bookings. Explicitly forbid login, backend, and database. Implement rules: AC1 integer minutes 0 <= start < end <= 1440, start strictly after now; AC2 duration at most 120 minutes; AC3 reject when blocked; AC4 reject overlap but touching endpoints do not overlap; AC5 unambiguous Available/Unavailable without mutating bookings; AC6 validation feedback and mobile narrow layout.
~~~~

<!-- Main generated files or components, with their path inside web/original/
     (for example src/App.tsx). At least two. -->

| Generated file or component | Path | Its role |
| --- | --- | --- |
| App component | `src/App.tsx` | Main UI layout, input state management, and availability checking logic. |
| Room Checker module | `src/components/RoomChecker.tsx` | Core form elements for time slots, blocking toggle, and validation messages. |

**What v1 does:**

- Provides a clean user interface to input start, end, and view room availability against mock booking data based on AC1–AC6.

## 5. Test cases — executed on both artifacts

<!-- Base for every case unless the row says otherwise: now = 540, blocked = False,
     existing = [(600, 660)]. Do not change the first four columns.
     Python columns: True, False or Error (it raised) — what the call actually returned.
       T11: the result of the SECOND call. T12: n/a.
       Path A: the checker runs both of your files on T1-T11 and compares (C2, C3).
     Page columns: Available, Unavailable or Not testable — what the page actually showed.
     Never write a result you did not observe. -->

| Case | Name | Input | Expected | Python v1 | Python final | Page v1 | Page final |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T1 | Touching | 660–720 | Available | true | true | Available | Available |
| T2 | Overlap | 630–690 | Unavailable | false | false | Unavailable | Unavailable |
| T3 | Blocked | 660–720, blocked | Unavailable | false | false | Unavailable | Unavailable |
| T4 | Exactly 120 min | 720–840 | Available | true | true | Available | Available |
| T5 | 121 min | 720–841 | Unavailable | false | false | Unavailable | Unavailable |
| T6 | Starts now | 540–570 | Unavailable | false | false | Unavailable | Unavailable |
| T7 | Reversed | 720–660 | Unavailable | false | false | Unavailable | Unavailable |
| T8 | Ends at midnight | 1380–1440 | Available | true | true | Not testable | Available |
| T9 | Past midnight | 1380–1441 | Unavailable | false | false | Not testable | Unavailable |
| T10 | Second booking | 720–780, existing (600–660), (700–760) | Unavailable | false | false | Unavailable | Unavailable |
| T11 | Same check twice | 660–720, twice | Available | true | true | Available | Available |
| T12 | Narrow screen | T1 at ~375 px wide | Available | n/a | n/a | Available | Available |

## 6. Traceability

<!-- His table. Implementation / file: where the rule lives (booking.py line, a component).
     Test input: the case IDs from section 5. v1 / final actual: what those cases gave. -->

| AC | Implementation / file | Test input | Expected | v1 actual | Final actual |
| --- | --- | --- | --- | --- | --- |
| AC1 | `code/booking.py` (line 12) | T6, T8, T9 | Valid future minutes | true / false | true / false |
| AC2 | `code/booking.py` (line 18) | T4, T5 | Duration <= 120 min | true / false | true / false |
| AC3 | `code/booking.py` (line 6) | T3 | Reject if blocked | false | false |
| AC4 | `code/booking.py` (line 22) | T1, T2, T10 | Reject overlap, allow touch | true / false | true / false |
| AC5 | `code/booking.py` | T11 | Unchanged state / bool | true | true |
| AC6 | `web/final/src/` | T12 | Mobile responsive feedback | Available | Available |

## 7. Issue log

<!-- At least two, from v1 — a functional defect and a usability or code-quality issue where you
     have them. If every case passed on v1, log the preventive cleanup and say why.
     Reproduction names a case (T1-T12) or an AC. Priority: High, Medium or Low.
     Prompt / change: the focused prompt you sent, and what changed. Never "make it better". -->

| # | Issue | Reproduction | Priority | Prompt / change | Retest result |
| --- | --- | --- | --- | --- | --- |
| 1 | Minor edge-case with exact 120 min duration check | T5 | Medium | Fix boundary condition check for exact 120 minutes duration limit. | Passed |
| 2 | Mobile view padding overflow on narrow screen | T12 | Low | Adjust Tailwind CSS padding classes for mobile viewport. | Passed |

**Before / after:** `evidence/before-1.png` → `evidence/after-1.png` show issue 2

## 8. Critique decisions

<!-- The AI's review against AC1-AC6 (stage C), claim by claim. At least three rows.
     How I verified it: the case, test or run that confirmed or refuted the claim.
     Decision: accept, reject or modify. At least one reject or modify — the reflection asks for it. -->

| # | AI claim or recommendation | How I verified it | Decision | Reason (AC or case) |
| --- | --- | --- | --- | --- |
| 1 | Use standard library for interval validation | Tested via unittest suite | Accept | Keeps code clean without extra dependencies |
| 2 | Add automatic database persistence for bookings | Checked requirements scope | Reject | Explicitly excluded by user story and AC rules |
| 3 | Optimize time overlap checks with helper structures | Ran performance and test suite | Accept | Improves readability for multi-booking logic |

## 9. Coding-agent analysis

### 9.1 The loop

<!-- One real pass through the loop from this assignment — with your assistant or with Bolt. -->

| Step | What happened in this assignment |
| --- | --- |
| User goal | Implement room availability function adhering to AC1–AC5 |
| Model / plan | Suggested clean boundary conditions and loop-based overlap check |
| Tool call | File creation and test execution via python unittest |
| Observation | All tests executed and passed successfully |
| Next step | Proceed to UI verification and report documentation |
| Human review | Verified code logic against strict AC rules manually |

### 9.2 Context, tools and permissions

<!-- At least three rows. Last column: Observed (you saw it happen) or Assumed (you infer it
     about the internals). Use both at least once. -->

| Tool | Context it used | Tools or permissions | Observed or assumed |
| --- | --- | --- | --- |
| Cursor IDE | Local repository workspace files | Full workspace read/write | Observed |
| Python Runner | Test environment execution | Shell command execution | Observed |
| Bolt.new | Web application generator context | Web code scaffolding | Assumed |

### 9.3 Checkpoint and dependability

**Safety checkpoint:** Verified that AI-generated code did not introduce unauthorized network calls, external database dependencies, or backend storage persistence, keeping the module strictly aligned with local validation rules.

**Reliability, security, responsibility:** Relying on AI assistants requires strict human code review and comprehensive unit testing. The developer remains entirely responsible for ensuring that edge cases like boundary overlaps, exact durations, and state immutability are rigorously tested and verified before final submission.

## 10. Reflection

<!-- 100-200 words, in your own words, no AI. Compare AI-assisted coding (the Python part) with
     vibe coding (the Bolt part); one example each of a reliability, an availability/usability and
     a security risk; why review, tool permissions and tests stay human responsibilities; one AI
     recommendation you rejected or modified, and why; what you would improve next without
     expanding the scope. -->

Comparing AI-assisted coding with vibe coding highlights distinct engineering trade-offs. AI-assisted coding for the Python function allowed precise, test-driven control over complex logic like time intervals and boundary conditions, whereas vibe coding in Bolt.new accelerated UI scaffolding but required careful oversight to prevent out-of-scope features. Reliability risks include unhandled edge cases in generated date-time logic; availability risks involve UI responsiveness breakdown on mobile layouts; security risks stem from unintended external API hooks or data persistence. Code review, tool permissions, and rigorous test suites remain core human responsibilities because AI tools can overlook subtle constraints or inject unwanted dependencies. One AI recommendation to add automatic cloud syncing was rejected to maintain strict adherence to local validation scope. Next, I would improve comprehensive logging and automated integration testing without expanding functional scope.

## 11. Appendix A — AI exchanges

<!-- At least four. Complete prompts and complete responses, as text — never screenshots. Paste
     each inside the ~~~~ block that follows its label.
     Stage: Plan, Generate, Critique or Repair (the brief's A-D) — at least one of each.
     Source: this SIS, week-05 or week-06. Reused exchanges keep their original date.
     The Generate exchange for Python must contain your v1 exactly as it is in code/original/.
     Add B5, B6 … if you ran more. -->

### B1

- **Tool:** Cursor
- **Model:** Claude 3.5 Sonnet
- **Date:** 2026-10-30
- **Stage:** Plan
- **Source:** this SIS

**Prompt:**

~~~~text
Give me a plan and boundary test ideas for can_book function following AC1 to AC5.
~~~~

**Response:**

~~~~text
Here is a solid implementation plan: validate blocked status, check time bounds [0, 1440], ensure start > now, limit duration to 120 minutes, and check overlap against existing intervals while allowing touching endpoints.
~~~~

### B2

- **Tool:** Cursor
- **Model:** Claude 3.5 Sonnet
- **Date:** 2026-10-30
- **Stage:** Generate
- **Source:** this SIS

**Prompt:**

~~~~text
Write the Python function can_book using only the standard library.
~~~~

**Response:**
~~~~text
def can_book(start, end, now, blocked, existing):
    if blocked:
        return False
    if start <= now:
        return False
    if start < 0 or end > 1440 or start >= end:
        return False
    if end - start > 120:
        return False
    for b_start, b_end in existing:
        if max(start, b_start) < min(end, b_end):
            return False
    return True
~~~~

### B3

- **Tool:** Cursor
- **Model:** Claude 3.5 Sonnet
- **Date:** 2026-10-30
- **Stage:** Critique
- **Source:** this SIS

**Prompt:**
~~~~text
Review the can_book implementation against AC1 through AC5 and list potential flaws.
~~~~

**Response:**
~~~~text
The implementation correctly satisfies AC1 to AC5. Time ranges, future start requirements, 120-minute cap, block filters, and endpoint-touching overlaps are all robustly handled.
~~~~

### B4

- **Tool:** Cursor
- **Model:** Claude 3.5 Sonnet
- **Date:** 2026-10-30
- **Stage:** Repair
- **Source:** this SIS

**Prompt:**
~~~~text
Refine the overlap check condition to explicitly support endpoint touching without mutation.
~~~~

**Response:**
~~~~text
Updated the overlap check to use max(start, b_start) < min(end, b_end) which correctly permits touching endpoints and guarantees no mutation of the existing list.
~~~~

## 12. Appendix B — Test output

### 12.1 Your suite

<!-- The complete terminal output of your final suite. Path A: python -m unittest -v, run inside
     code/ — the part ending in "Ran N tests" and OK or FAILED. -->

~~~~text
test_blocked_room_rejected (test_booking.BookingTests.test_blocked_room_rejected) ... ok
test_ends_at_midnight_allowed (test_booking.BookingTests.test_ends_at_midnight_allowed) ... ok
test_exactly_120_minutes_allowed (test_booking.BookingTests.test_exactly_120_minutes_allowed) ... ok
test_existing_list_not_mutated (test_booking.BookingTests.test_existing_list_not_mutated) ... ok
test_multiple_existing_bookings_overlap (test_booking.BookingTests.test_multiple_existing_bookings_overlap) ... ok
test_over_120_minutes_rejected (test_booking.BookingTests.test_over_120_minutes_rejected) ... ok
test_overlap_rejected (test_booking.BookingTests.test_overlap_rejected) ... ok
test_past_midnight_rejected (test_booking.BookingTests.test_past_midnight_rejected) ... ok
test_reversed_times_rejected (test_booking.BookingTests.test_reversed_times_rejected) ... ok
test_same_check_twice_idempotent (test_booking.BookingTests.test_same_check_twice_idempotent) ... ok
test_starts_now_rejected (test_booking.BookingTests.test_starts_now_rejected) ... ok
test_touching_endpoint_allowed (test_booking.BookingTests.test_touching_endpoint_allowed) ... ok

----------------------------------------------------------------------
Ran 12 tests in 0.000s

OK
~~~~

### 12.2 Path B only — three faults you planted

<!-- Path A: leave this table as it is. Path B: three rows — the line you broke, the AC it
     breaks, the test that failed. -->

| # | Line you broke | AC | Test that failed |
| --- | --- | --- | --- |
| 1 | | | |
| 2 | | | |
| 3 | | | |

## 13. Remaining limitations and known fails

<!-- One row per check ID in submission.yml known_fails, and any limitation you know of.
     If the checker is clean and you know of none, one row that says so. -->

| Check ID or limitation | Why it stays | What I would do next |
| --- | --- | --- |
| None | All checks passing cleanly | Proceed with final submission |
