# AI Usage Disclosure — Week 02

Required by the course academic policy (Generative AI use level D — AI-integrated). AI use is the subject of this lab, not a shortcut in it. You remain responsible for the accuracy, testing and integrity of everything you submit, including everything an AI produced.

## 1. The tool under test

| | |
| --- | --- |
| Assistant | GPT-5.6 Luna |
| Exact model name | GPT-5.6 Luna |
| Plan (free / paid) | free |
| Dates of the four runs | 2026-09-20 |

## 2. What it produced

| Prompt | File it produced | Edited by me afterwards? |
| --- | --- | --- |
| A | `week-02/code/prompt_a.py` | no |
| B | `week-02/code/prompt_b.py` | no |
| C | `week-02/code/prompt_c.py` | no |
| D | `week-02/code/prompt_d.py` | no |



Note: I removed a duplicated main() call at the end of my copy of tests/test_analyze_marks.py (it printed every run twice). Test cases and logic were not changed.



## 3. Any other AI use in this lab

| Tool | Used for | Which file or section |
| --- | --- | --- |
| Claude (Anthropic) | Explaining the task, helping structure the report, drafting wording for sections 2–5, 7, 8 and 9 from my real test output and code, which I then checked | lab-report.md |

## 4. Declarations

- **Every prompt was sent in a fresh chat, and the outputs were saved before any editing:** yes
- **The test results in section 6 of `lab-report.md` are real output from real runs:** yes
- **Everything I submitted, I can explain and defend in class:** yes


**Anything I accepted from the AI without fully understanding it:** 
code/prompt_d.py: I did not notice until reviewing that it accepts True/False as marks, because my Prompt D said "non-numeric (int/float)" and bool is a subclass of int.

Signed: Ashimkhan Kuralay
Date: 2026-09-20