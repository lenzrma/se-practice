# Week 09 — Lab Report: canBook as a Tool

Fill in every section. Do not delete or renumber the headings: the README and the checker point at
them. Replace every `<!-- comment -->` with your own text (comments are ignored by the checker).

**Name:** Ashimkhan Kuralay
**Student ID:** 24B030990
**GitHub:** lenzrma

---

## 1. Setup

| | |
| --- | --- |
| Assistant (frozen for the whole lab) | Claude (Claude Code agent session on claude.ai) |
| Exact model (or "not displayed") | claude-sonnet-5-5 (the configured model of the session; the model that actually served a turn may differ) |
| Three fresh chats for R1, R2, R3? (yes / no) | yes. Each request went to its own new agent with an empty context and only the README prompt, my JSON and one request. |
| Python version (`python --version`) | Python 3.14.3 |

## 2. Your tool definition — a reason for every constraint

Paste your final `tool/check_room.json`, then fill the table: one row per constraint you wrote.

```json
{
  "name": "check_room",
  "description": "Checks whether a room can be booked for a requested time slot and answers Available or Unavailable. All times are whole minutes since midnight, from 0 to 1440 (10:00 is 600, 24:00 is 1440). It looks at the requested start and end, the current time, whether the room is blocked, and the existing bookings. It only checks: it does not save, create or change any booking, so calling it never reserves the room.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "start": {
        "type": "integer",
        "minimum": 0,
        "maximum": 1440,
        "description": "Requested start, in whole minutes since midnight (10:00 = 600)."
      },
      "end": {
        "type": "integer",
        "minimum": 0,
        "maximum": 1440,
        "description": "Requested end, in whole minutes since midnight (24:00 = 1440)."
      },
      "now": {
        "type": "integer",
        "minimum": 0,
        "maximum": 1440,
        "description": "The current time, in whole minutes since midnight."
      },
      "blocked": {
        "type": "boolean",
        "description": "true if the room is blocked (for example for maintenance), false if it is not."
      },
      "bookings": {
        "type": "array",
        "description": "Existing bookings of the room. Use an empty list if there are none.",
        "items": {
          "type": "object",
          "properties": {
            "start": {
              "type": "integer",
              "minimum": 0,
              "maximum": 1440,
              "description": "Booking start, in whole minutes since midnight."
            },
            "end": {
              "type": "integer",
              "minimum": 0,
              "maximum": 1440,
              "description": "Booking end, in whole minutes since midnight."
            }
          },
          "required": ["start", "end"],
          "additionalProperties": false
        }
      }
    },
    "required": ["start", "end", "now", "blocked", "bookings"],
    "additionalProperties": false
  }
}
```

| Field | Constraint (e.g. `"type": "integer"`, `"maximum": 1440`) | What goes wrong without it |
| --- | --- | --- |
| name | `"name": "check_room"` | The client looks tools up by name. Any other name and the model's call goes to a tool that does not exist (D3). |
| description | 25+ words that give the unit (minutes), the range 0–1440 and say it does not save a booking | The model has only the description to go on. Without the unit it may send "11:00" or hours. Without the "does not save" it may treat the tool as a booking action, or an agent may avoid calling it, thinking it reserves the room (AC5). |
| start, end, now | `"type": "integer"` | A string like "11:00" (S03) or a half minute like 600.5 (S10) would reach canBook, which does arithmetic on whole minutes. |
| start, end, now | `"minimum": 0` and `"maximum": 1440` | -30 (S06) or 1500 (S07) would pass as times, although the day only has minutes 0 to 1440. 1440 itself must stay allowed for end (S11). |
| blocked | `"type": "boolean"` | The string "false" (S09) would get through, and in many languages a non-empty string counts as true, so a free room would be treated as blocked. |
| bookings | `"type": "array"` with no `minItems` | Something that is not a list would get through. No `minItems`, because an empty list is a valid call (S02). |
| bookings items | `"type": "object"` with `"required": ["start", "end"]` | A booking with no end (S08) or a pair like [660, 720] (S12) would break the overlap check in AC4. |
| bookings items | `"additionalProperties": false` | A booking with invented fields would be accepted silently, and nobody would know which ones canBook ignores. |
| top level | `"required"`: all five fields | A call without `now` (S04) would make "start after now" (AC1) compare with undefined. The model must give every value or ask. |
| top level | `"additionalProperties": false` | The model can invent a field like `"room": "204"` (S05). canBook has no room, so the call would look right and mean nothing. |
| every field | a `description` with the unit | It is not a validation rule, but it is what the model reads when it fills the field (R1 and R2 converted times correctly). |

## 3. The twelve calls — first run and final run

Your **first** run's S verdicts (before any fix), and your final ones. For every case that changed,
say what you changed.

| Case | First run | Final run | What you changed |
| --- | --- | --- | --- |
| S01 | PASS | PASS | nothing |
| S02 | PASS | PASS | nothing |
| S03 | PASS | PASS | nothing |
| S04 | PASS | PASS | nothing |
| S05 | PASS | PASS | nothing |
| S06 | PASS | PASS | nothing |
| S07 | PASS | PASS | nothing |
| S08 | PASS | PASS | nothing |
| S09 | PASS | PASS | nothing |
| S10 | PASS | PASS | nothing |
| S11 | PASS | PASS | nothing |
| S12 | PASS | PASS | nothing |

My first run of the definition passed all twelve cases (D1–D6 passed too; the F and L checks were still ERROR and FAIL because
calls/ and this report did not exist yet). So I changed nothing in the schema between the first and the final run, and the number of S fails on the first run is 0. I am not claiming the schema
is perfect. The twelve cases test only one fault each, and a schema that passes them says nothing about R3 or about the meaning of the numbers.

## 4. Function calling — what the model wrote

For each request, paste the model's reply exactly, then judge it against the request.

### R1

```text
{"name": "check_room", "arguments": {"start": 600, "end": 660, "now": 540, "blocked": false, "bookings": [{"start": 660, "end": 720}]}}
```

F1, F2 and F3 all passed. The call matches the request: now 9:00 = 540, slot 10:00–11:00 = 600–660, "isn't blocked" = false, and the one booking 11:00–12:00 = 660–720. The model was right and so was the request. The model also called the tool for a yes/no question instead of answering "yes" itself. canBook should answer Available here, because AC4 allows bookings that only touch (660 = 660). That is the function's job, not the schema's.

### R2

```text
{"name": "check_room", "arguments": {"start": 840, "end": 990, "now": 810, "blocked": true, "bookings": []}}
```

F4, F5 and F6 all passed. 13:30 = 810, 14:00 = 840, and 16:30 = 16 × 60 + 30 = 990, so the model did not make the 16:30 → 960 mistake. It did not refuse to call, although the room is blocked: it passed `blocked: true` and left the verdict to the tool. It also turned "no other bookings" into `[]`, as the schema description said. The schema accepts this call, because it is well formed. canBook must answer Unavailable (AC3). A schema cannot do that.

### R3

```text
Какое сейчас время, заблокирована ли комната, какие уже есть брони, и на какие именно часы нужна комната (например, 14:00–16:00)?
```

The model asked and did not call, so it is `calls/r3.txt` and `calls.r3: asked`. The request gives no `now`, no `blocked`, no `bookings`, and no exact `start` and `end` ("tomorrow afternoon", "a couple of hours"). The model invented no values. The "14:00–16:00" in the question is only an example, not an argument. Three things I noticed: (1) it asked four things in one sentence, but the prompt said "one short question"; (2) it answered in Russian, although the prompt and request are in English, and I do not know why; (3) the real problem is in my tool: it has no date field, only minutes since midnight, so "tomorrow" cannot be expressed in the call at all, and even with every answer given, `now` would still refer to today. The model was right to ask. A model that called this would have had to invent at least four of the five values.

## 5. What the schema cannot check

AC1 is split. A schema can enforce the part that looks at one field alone: each of `start`, `end` and `now` is a whole number from 0 to 1440 (`type`, `minimum`, `maximum`, tested by S03, S06, S07, S10, S11). It cannot enforce the part that compares fields: `start < end` and "start after `now`". The allowed keywords (`minimum`, `maximum` and so on) take a fixed number, never another field, so `"start": 600, "end": 600` is a valid call but canBook must say Unavailable.

- **AC1 (start < end, start after now):** both compare two fields with each other, which these keywords cannot do.
- **AC2 (at most 120 minutes):** it needs the subtraction `end - start`. A schema can only limit `end` to a fixed number, so it cannot say "end is at most start + 120".
- **AC3 (not when blocked):** `blocked: true` is a valid boolean. The schema checks the shape of the value, not what it means for the answer (R2 is a call that should be made, and the answer is Unavailable).
- **AC4 (no overlap, touching allowed):** it compares `start` and `end` with every item in `bookings`, so it needs a loop over the list and comparisons across fields.
- **AC5 (does not change or save anything):** this is about what the function does, not about what goes into it. No input schema can express it. The only thing I can do is say it in the description (D4), and that is advice to the model, not enforcement.
- **AC6 (the page's feedback):** it is the text the user sees, so it is output. An input schema does not describe outputs.

So these rules stay in canBook: the schema is a first filter on shape, and the function is the only place that knows what the numbers mean.

## 6. Permissions — allow, ask or block

| # | Action | Decision (allow / ask / block) | Reason (the risk, in one sentence or more) |
| --- | --- | --- | --- |
| A1 | call `check_room` with the times the user just typed | allow | The tool only reads its arguments and saves nothing (AC5), the schema refuses malformed values before it runs, and the worst case is a wrong Available or Unavailable answer. |
| A2 | read `week-08/app/src/booking.ts` | allow | Reading a source file in the project the agent was given changes nothing, so the risk is close to zero, unless the file contains secrets, and a booking rule file should not. |
| A3 | edit `booking.ts` to raise the 120-minute limit to 180 | ask | It changes the business rule AC2 for every user because one user asked, it can break the week-08 tests and the graded work, and a chat message is not a spec change, so I want to see the diff and decide. |
| A4 | run `npm test` in `week-08/app` | allow | It runs only the project's own tests, writes nothing outside the folder and is easy to repeat, so the main risk is a slow run or a changed test script. I would not extend this to `npm install` or to commands that reach the network. |
| A5 | run `git reset --hard` to undo its own last three edits | ask | It permanently throws away uncommitted changes, including my own edits mixed with the agent's, and no later command brings back files that were never committed, so a human has to confirm what exactly will be lost. |
| A6 | `git commit` its change on the `week-09` branch | allow | A local commit on the feature branch is easy to undo (`git reset` or `git revert`) and is exactly the kind of small step the checkpoint relies on. I would check `git status` first so a `.env` file never gets committed. |
| A7 | `git push` to `main` | block | It publishes code to the shared branch without a pull request or review, it is hard to undo once others have it, and this course counts a commit on main as an automatic failure. Only the human pushes the week-09 branch and opens the PR. |
| A8 | send the contents of `.env` to an MCP server it found online | block | `.env` holds secrets and tokens, an unknown server can store and reuse them, sending them cannot be taken back, and "to configure it" is a typical prompt-injection trick. If it ever happened, I would rotate every key in the file. |

## 7. Checkpoint

Before I let an agent edit anything, I would commit a clean working tree on `week-09` with the message `checkpoint: clean tree before agent edits`.

- **SHA of that commit (from `git log --oneline`):** 98f5e11
- **Command that takes me back to it:** `git reset --hard 98f5e11`
- **What that command throws away:** every uncommitted change to tracked files (staged or not), and every commit made on this branch after the checkpoint (they stay reachable only through `git reflog` for a while). It does not delete untracked new files, but it also does not bring them back to a clean state. Because of this, if the agent has made edits I might want to look at, I would first save them with `git switch -c rescue` or `git stash`.

## 8. Checker output

Paste the **whole** output of your last `python tests/check_tool.py`, unedited.

```text
PASS  D1    tool/check_room.json exists and is valid JSON
PASS  D2    has name, description and inputSchema
PASS  D3    name is exactly "check_room"
PASS  D4    description: 25+ words, says minutes, 1440, and that it does not save
PASS  D5    inputSchema: an object with exactly the five fields, all required
PASS  D6    inputSchema uses only the keywords listed in README section 5
PASS  S01   the R1 call, valid -> accept
PASS  S02   no existing bookings: bookings = [] -> accept
PASS  S03   end as a string: "11:00" -> refuse
PASS  S04   now missing -> refuse
PASS  S05   an extra field: "room": "204" -> refuse
PASS  S06   start below the day: -30 -> refuse
PASS  S07   end beyond the day: 1500 -> refuse
PASS  S08   a booking with no end: {start: 660} -> refuse
PASS  S09   blocked as a string: "false" -> refuse
PASS  S10   start not a whole minute: 600.5 -> refuse
PASS  S11   end at the end of the day: 1440 -> accept
PASS  S12   a booking as a pair: [660, 720] -> refuse
PASS  F1    calls/r1.json: a call to check_room
PASS  F2    calls/r1.json: arguments valid against your schema
PASS  F3    calls/r1.json: arguments equal the expected ones (README section 5, Part 2)
PASS  F4    calls/r2.json: a call to check_room
PASS  F5    calls/r2.json: arguments valid against your schema
PASS  F6    calls/r2.json: arguments equal the expected ones (README section 5, Part 2)
PASS  F7    calls/r3: exactly one of r3.json (it called) or r3.txt (it asked), not empty
PASS  L1    section 5 names at least two acceptance criteria (AC1-AC6) the schema cannot check
PASS  L2    section 6: A1-A8 each have allow / ask / block and a reason of 5+ words
PASS  L3    section 7 names the checkpoint commit (a SHA)
PASS  L4    section 10: a conclusion of 80-150 words
PASS  L5    AI_USAGE.md filled in (a tool row, and signed)

SUMMARY: 30 PASS · 0 FAIL · 0 ERROR  (of 30 checks)
Paste this whole output into lab-report.md section 8, and these three numbers into submission.yml.
```

## 9. What still fails

None. All 30 checks pass at the commit named in `submission.yml`, so `known_fails` is empty.

Nothing was hidden or edited to make a check pass: the first run of S01–S12 was already all PASS (section 3), and calls/ holds the replies exactly as they came (F3 and F6 passed without any change from me). The things that are not checker failures but that I noticed are in section 4: the R3 question was asked in Russian and in four parts, and the tool has no date field.

## 10. Conclusion (80–150 words)

The schema checks shape and nothing more. It refused all nine bad calls on the first run (S03 string end, S05 invented `room`, S09 "false" as a string), but it accepts R2 without a problem: blocked true with 14:00–16:30 is a well-formed call, and only canBook can answer Unavailable under AC3. The model did the part I cannot enforce: it turned 16:30 into 990, and for R3 it asked instead of inventing `now`, `blocked` and `bookings`. The surprise was that my tool has no date, so "tomorrow afternoon" cannot even be written down. The same line decides the agent actions: checking (A1) is safe, but changing the 120-minute rule (A3) needs me, and pushing to main (A7) or sending `.env` out (A8) is blocked.
