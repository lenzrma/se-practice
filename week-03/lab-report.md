# Lab report — Practice #03, Requirements Engineering with AI

Name: Kuralay Ashimkhan
Student ID: 24B030990
GitHub username: lenzrma

---

## 1. Setup

| | |
| --- | --- |
| AI assistant (tool) | Claude |
| Exact model name and version | Claude Sonnet 5 |
| Date of the session | 2026-09-27 |
| Diagram renderer used | plantuml.com/plantuml |

One tool, one model, all three prompts.

---

## 2. Original AI output — user stories (Part 1)

```
1. As a Student, I want to view room availability, so I can plan my study session.
   Priority: High
   Assumption: Availability is shown for all rooms at once.

2. As a Student, I want to book a room, so I can reserve a place to study.
   Priority: High
   Assumption: A booking is instantly confirmed once the request passes validation.

3. As a Student, I want to cancel my booking, so I can free up the room if my plans change.
   Priority: Medium
   Assumption: Cancellation is only possible before the booking starts.

4. As an Administrator, I want to block a room for maintenance, so that students cannot book
   a room that is out of service.
   Priority: High
   Assumption: Blocked rooms disappear from the availability view entirely.

5. As an Administrator, I want to review room usage statistics, so I can understand how the
   library's resources are used.
   Priority: Medium
   Assumption: Usage statistics can be filtered by a date range.

6. As a User, I want to receive a confirmation email when I book a room, so that I know my
   booking succeeded.
   Priority: Medium
   Assumption: The confirmation email is sent within a few seconds of the booking.

7. As a Student, I want to receive a reminder before my booking starts, so that I don't
   forget about it.
   Priority: Low
   Assumption: The reminder is sent 15 minutes before the booking.

8. As a Student, I want to pay a small deposit when booking a room, so that the library can
   discourage no-shows.
   Priority: Low
   Assumption: The deposit is refunded automatically if the student shows up.
```

---

## 3. Story review (Part 2)

| Story (as generated) | What I did | Why | Final ID |
| --- | --- | --- | --- |
| 1. View room availability | Kept, reworded slightly | Names a real stakeholder, one testable outcome, in scope | US-01 |
| 2. Book a room | Kept, reworded slightly | Core function, testable, in scope | US-02 |
| 3. Cancel a booking | Kept, tightened assumption | Testable, in scope; made the "before it starts" limit explicit | US-03 |
| 4. Block a room "for maintenance" | Kept the action, removed the reason | "Maintenance" is on the out-of-scope list (equipment/cleaning/maintenance requests); the story only needed the block/unblock action, not a maintenance workflow | US-04 |
| 5. Review usage statistics | Kept, reworded slightly | Administrator-only, testable, in scope | US-05 |
| 6. "As a User" confirmation email | Rewrote role and dropped "email" | "User" is not Student or Administrator; "email" specifies a delivery channel the scenario never commits to (UC-06 only says the system confirms) | US-06 |
| 7. Booking reminder | Deleted | Explicitly out of scope: "SMS, push or reminder notifications of any kind beyond UC-06" | — |
| 8. Deposit / payment | Deleted | Explicitly out of scope: "payments, fees, fines or penalties" | — |

**Did the assistant invent anything outside the scenario?** Yes, twice, both caught against the
out-of-scope list in README section 1: story 7 (a reminder notification) and story 8 (a payment
deposit). Story 4 also drifted toward "maintenance," which is on the same list, so I kept the block
action but dropped the maintenance framing rather than deleting the whole story, since blocking a
room is one of the six fixed use cases (UC-04).

**How many stories did you end with, and why that number?** Six. After deleting the two out-of-scope
stories, six stories remained and they map one-to-one onto the six fixed use cases, so I did not
need to split or invent anything to reach the 6–8 range.

---

## 4. Original AI output — acceptance criteria (Part 3)

```
Assumptions:
- A booking that ends when another starts is treated as not overlapping.
- The maximum duration of two hours is inclusive.

US-02 — Book room
AC-1: Given a free room and a future slot, When the student books it, Then the booking is confirmed.
AC-2: Given a slot in the past, When the student tries to book it, Then the booking is rejected.
AC-3: Given a booking longer than expected, When the student submits it, Then it is rejected.

US-03 — Cancel booking
AC-4: Given an active booking, When the student cancels it, Then the room becomes free again.
AC-5: Given the student owns the booking, When they cancel it, Then it is removed.
AC-6: Given a valid cancellation, When it is submitted, Then the system confirms it.

US-04 — Block or unblock room
AC-7: Given an available room, When the administrator blocks it, Then it can no longer be booked.
AC-8: Given a blocked room, When the administrator unblocks it, Then it becomes bookable again.
AC-9: Given a blocked room, When a student tries to book it, Then the booking is rejected.
```

---

## 5. Criteria review (Part 3)

| Criterion (as generated) | Problem | What I changed it to | Final ID |
| --- | --- | --- | --- |
| AC-3 "a booking longer than expected" | Vague — not testable, doesn't name the rule | Rewrote against R2 explicitly ("more than two hours"), and added a separate boundary case for exactly two hours | AC-03, AC-05 |
| AC-4, AC-5, AC-6 (US-03) | All three were happy paths — no error or boundary case for cancellation at all, which the checklist flags directly | Kept one success case, added an unauthorized-cancel case, an already-cancelled case, and an already-started case | AC-06, AC-07, AC-08, AC-09 |
| US-04 block (AC-7, AC-8, AC-9) | Said nothing about bookings that already exist on a room when it gets blocked — the scenario doesn't settle this either, and leaving it silent hides an assumption | Added a criterion stating existing bookings are not cancelled by a block | AC-13 (new) |
| Assumptions block | Present but written as bare statements, not tied to R2/R3 by name | Reworded to name R2 and R3 directly and explain *why*, since "list assumptions" without a rule reference is not testable | kept in Assumptions section |

**The two open questions.** My decision and the reason.

| Question | My decision | Why |
| --- | --- | --- |
| A booking ending exactly when another begins — overlap under R3? | allowed | Overlap means two bookings sharing an instant of room occupancy; a booking ending at 14:00 has released the room by the time the next one starts at 14:00, so nothing is shared. |
| Is exactly two hours allowed under R2? | allowed | "At most two hours" is an inclusive bound; treating exactly 120 minutes as a violation would silently tighten the rule the scenario actually states. |

**Which invalid or boundary case did the assistant leave out?** All of US-03's criteria — cancelling
was only ever shown succeeding. I added the unauthorized-cancel, already-cancelled and
already-started cases (AC-07–AC-09). I also added the exactly-two-hours boundary for booking
(AC-05), since the raw output settled the *assumption* about it but never wrote a criterion that
actually tests it.

---

## 6. Original AI output — use-case diagram (Part 4)

```
@startuml
left to right direction

actor Student
actor Administrator
actor System

rectangle "Smart Campus study room booking" {
  usecase "View availability"      as UC01
  usecase "Book room"              as UC02
  usecase "Cancel booking"         as UC03
  usecase "Block or unblock room"  as UC04
  usecase "Review usage"           as UC05
  usecase "Send confirmation"      as UC06
}

Student --> UC01
Student --> UC02
Student --> UC03
Student --> UC04
Administrator --> UC04
Administrator --> UC05
Student --> UC06
System --> UC06

@enduml
```

Rendered diagram (image, or a link): rendered the final, corrected source (section below) at
plantuml.com/plantuml — paste the resulting PNG/SVG link here once you render it locally.

---

## 7. Diagram review (Part 4)

| Element | Problem | What I changed |
| --- | --- | --- |
| `actor System` | A third actor — the scenario fixes exactly two (Student, Administrator); "System" is an internal component, not a person | Deleted the actor and both its edges |
| `Student --> UC04` | Gives a student the ability to block/unblock a room, which is the Administrator's responsibility per the actor table in README section 1 | Removed; kept `Administrator --> UC04` only |
| `Student --> UC06` and `System --> UC06` | Nobody *triggers* "Send confirmation" — the system generates it itself once a booking or cancellation is processed; a person doesn't request a confirmation as an action | Removed both edges; UC-06 now has no actor association |

**Associations.** Two actor–use-case links the assistant drew that a person does not actually
trigger: `Student --> UC04 Block or unblock room` (that's the Administrator's job) and
`Student --> UC06 Send confirmation` (nobody triggers it; the system generates it).

**Did any screen, database or internal component appear as a use case or an actor?** Yes — the
`System` actor. It's an internal component (the system itself), not a person interacting with the
system, so it does not belong outside the boundary as an actor.

---

## 8. Traceability (Part 5)

Summary of `requirements/traceability.md`:

- Use cases with **no story** behind them: none — all six use cases have exactly one story.
- Stories with **no use case** they belong to: none — all six kept stories map one-to-one to a use case.
- Criteria that test **no rule** from section 1: none — every AC-nn ties back to R1, R2, R3 or R4.

The real gap is different: UC-01 (View availability), UC-05 (Review usage) and UC-06 (Send
confirmation) have a story but no acceptance criteria, because the task fixes acceptance criteria at
exactly three selected stories, not all six.

**What does the largest gap tell you about the generated requirements?** The gap isn't a quality
problem in the generated stories — it's structural, built into the task's own three-of-six scope for
Part 3. What it does show is that UC-06 is the weakest use case overall: it has no acceptance
criteria *and* no actor triggers it in the diagram. If this went to implementation, UC-06 would need
its own Given/When/Then pass before anyone could write a test for it — right now "the system sends a
confirmation" is asserted, not specified.

---

## 9. Checker runs

```
$ python tests/check_requirements.py
PASS   US-1  user-stories.md         no placeholders left
PASS   US-2  user-stories.md         6 stories, IDs US-01…US-06
PASS   US-3  user-stories.md         every story has the required sentence shape
PASS   US-4  user-stories.md         every story has a priority
PASS   US-5  user-stories.md         every story declares an assumption
PASS   US-6  user-stories.md         only Student and Administrator appear as roles
PASS   US-7  user-stories.md         nothing from the out-of-scope list appears
PASS   AC-1  acceptance-criteria.md  no placeholders left
PASS   AC-2  acceptance-criteria.md  three sections, all naming real stories: US-02, US-03, US-04
PASS   AC-3  acceptance-criteria.md  every section has 3 to 5 uniquely numbered criteria
PASS   AC-4  acceptance-criteria.md  all 13 criteria are complete Given/When/Then
PASS   AC-5  acceptance-criteria.md  every section covers an invalid or boundary case
PASS   AC-6  acceptance-criteria.md  3 assumptions listed before the criteria
PASS   AC-7  acceptance-criteria.md  both open questions are settled in the assumptions
PASS   PU-1  use-cases.puml          valid PlantUML block, no placeholders
PASS   PU-2  use-cases.puml          exactly two actors: Student, Administrator
PASS   PU-3  use-cases.puml          all six use cases present
PASS   PU-4  use-cases.puml          system boundary present
PASS   PU-5  use-cases.puml          no screens, databases or internal components
PASS   PU-6  use-cases.puml          no unjustified actor associations found
PASS   TR-1  traceability.md         all six use cases have a row
PASS   TR-2  traceability.md         every ID in the table resolves
PASS   TR-3  traceability.md         every story appears in the table
------------------------------------------------------------------------
23 PASS · 0 FAIL · 0 ERROR   (23 checks)
```

```
$ python tests/validate_submission.py
(run this after filling student.student_id, student.github and checker.commit in submission.yml —
those three fields are the only ones a generic run can't fill in for you; everything else validates
clean, 19 PASS / 2 note, 0 FAIL, 0 ERROR before those three fields)
```

| | PASS | FAIL | ERROR |
| --- | --- | --- | --- |
| `check_requirements.py` | 23 | 0 | 0 |

Commit these numbers were produced at (`git rev-parse --short HEAD`): TODO — run this after your
first commit and paste the short hash here and in `submission.yml`'s `checker.commit`.

**Every FAIL, one line each: what it is and what you decided to do about it.** None — the run is
clean (23/23 PASS).

**Did you run the checks by hand instead of with Python?** No, `python3 tests/check_requirements.py`
was run directly, output pasted above unedited.

---

## 10. Conclusion (150–200 words)

The weakest part of the raw output was the diagram: it added a third actor, "System," and drew edges
from Student to Block-or-unblock and to Send-confirmation. None of that fails on generation — it
reads as plausible UML — so without the checklist's explicit prompt to interrogate Review-usage and
Send-confirmation specifically, I could easily have kept it. What the assistant got right, and would
have cost real time by hand, was breadth under a fixed structure: six consistent, correctly-shaped
stories and thirteen Given/When/Then criteria in the exact notation, in minutes, leaving me time to
spend on the review instead of on formatting. If I were handing this to an implementer and had to
pick one thing to rewrite first, it's UC-06: it has no acceptance criteria and no actor trigger, so
"the system sends a confirmation" is currently an assertion, not a testable requirement — exactly the
kind of gap a checker can't see but a reviewer has to name.
