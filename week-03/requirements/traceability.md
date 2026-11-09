# Traceability — use cases → stories → criteria

| Use case | Stories (US-nn) | Criteria (AC-nn) | Gap? |
| --- | --- | --- | --- |
| UC-01 View availability | US-01 | none | Gap: US-01 was not one of the three stories selected for acceptance criteria (the task fixes that at 3), so UC-01 has no AC-nn behind it. |
| UC-02 Book room | US-02 | AC-01, AC-02, AC-03, AC-04, AC-05 | |
| UC-03 Cancel booking | US-03 | AC-06, AC-07, AC-08, AC-09 | |
| UC-04 Block or unblock room | US-04 | AC-10, AC-11, AC-12, AC-13 | |
| UC-05 Review usage | US-05 | none | Gap: same reason as UC-01 — US-05 was not selected for the acceptance-criteria pass. |
| UC-06 Send confirmation | US-06 | none | Gap: same reason, and UC-06 also has no actor association in the diagram — the confirmation is system-triggered, not person-triggered. |

**Stories that belong to no use case:** none — every kept story (US-01…US-06) maps to exactly one use case.

**What the gaps tell you:** the gaps are all the same shape — they come from the acceptance-criteria step being scoped to 3 of 6 stories by the task itself, not from a missing requirement. If this went to implementation, UC-01, UC-05 and UC-06 would need their own Given/When/Then pass before anyone could test them.
