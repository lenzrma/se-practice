# AI Usage Disclosure — SIS #03

Required by the course academic policy (Generative AI use level **D — AI-integrated**).
You are responsible for the accuracy, testing and integrity of everything you submit,
including anything an AI tool produced.

| Tool | Exact model / plan | Used for | Which files it touched | Reused from |
| --- | --- | --- | --- | --- |
| Cursor | Claude 3.5 Sonnet | the plan (stage A) | `report.md` | this SIS |
| Cursor | Claude 3.5 Sonnet | Python v1 (stage B) | `code/original/booking_v1.py` | this SIS |
| Bolt.new | Claude 3.5 Sonnet | web prototype v1 (stage B) | `web/original/` | this SIS |
| Cursor | Claude 3.5 Sonnet | critique (stage C) | `report.md` | this SIS |
| Cursor | Claude 3.5 Sonnet | repair (stage D) | `code/booking.py` | this SIS |

**The assistant wrote, or helped write, my tests in `code/`:** yes
The assistant helped generate test templates for T1–T12 in `code/test_booking.py`. I manually verified every expected `True`/`False` return value against the exact requirements in AC1–AC5 (especially boundary durations and touching endpoint conditions) before accepting them into the suite.

**`code/original/` and `web/original/` hold the AI's first versions exactly as returned:** yes

**Every result in report.md section 5 was actually run or seen, not assumed:** yes

**Everything I submitted, I can explain and defend in class — including the overlap condition and what the agent did in section 9:** yes

**Anything I accepted from the AI without fully understanding it:**
None. All interval logic in `code/booking.py` and report analyses were fully reviewed and verified.

Signed: Ashimkhan Kuralay
Date: 2026-10-30