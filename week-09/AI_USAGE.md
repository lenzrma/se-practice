# AI Usage Disclosure — Week 09

Required by the course academic policy (Generative AI use level **D — AI-integrated**).
You are responsible for the accuracy, testing and integrity of everything you submit,
including anything an AI tool produced.

| Tool | Exact model / plan | Used for | Which files it touched |
| --- | --- | --- | --- |
| Claude (Claude Code agent session on claude.ai, free plan) | claude-sonnet-5-5 (configured model; the serving model may differ) | Part 2 — writing the calls for R1, R2, R3 | calls/ (saved by me, unedited) |
| Claude (same session) | claude-sonnet-5-5 (same) | Drafting tool/check_room.json, the text of lab-report.md and the entries of submission.yml; running the checker | tool/check_room.json, lab-report.md, submission.yml, AI_USAGE.md |

**I wrote `tool/check_room.json` myself:** no
Claude drafted the whole file: the name, the description and the schema. I reviewed it, ran `tests/check_tool.py` and checked every constraint in lab-report.md section 2.

**I used an AI to explain a JSON Schema keyword or a check:** yes
Claude explained why `"type": "integer"` stops 600.5 (S10), what `additionalProperties: false` does (S05), and why a schema cannot compare `start` with `end` (section 5).

**Every reply in `calls/` and in lab-report.md section 4 is exactly what the model returned:** yes
The three replies came from three separate new Claude agents (one per request, no shared context), started by the assistant session and not typed by me into a chat window. The README prompt and my JSON were sent exactly as written. The replies were copied into calls/ without any change.

**Every terminal output in lab-report.md was pasted from a real run, unedited:** yes

**Anything I accepted from the AI without fully understanding it:**
Nothing in the files that I could not follow. The one thing I took on trust is that the three agents really had separate contexts, as the tool states. I also do not know why the R3 reply came back in Russian.

Signed: Ashimkhan Kuralay
Date: 2026-11-15
