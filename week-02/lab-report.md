# Lab report — Practice #02: The Prompt Is an Engineering Input

**Name:** Ashimkhan Kuralay
**Group:** SE-2401 (KBTU)
**Date:** September 20, 2026

> Fill in every section. **Do not delete or renumber the headings** — the grading pass reads them
> by number. If something did not happen, write "did not happen" and why; an empty section and a
> fabricated one are graded the same way.

---

## 1. The frozen experiment

| | |
| --- | --- |
| AI assistant | GPT-5.6 Luna |
| Exact model name | GPT-5.6 Luna |
| Implementation language | Python |
| Date of the runs | September 20, 2026 |

**Non-Python students only** — paste your substituted Prompt B text here, so the substitution can
be checked:
n/a — used Python.





**Confirmations:**

- Each prompt was sent in a **fresh chat**: yes
- No follow-up questions were asked before Part 7: yes
- Every output was saved **before** any editing: yes

---

## 2. Prompt A — minimal

**Prompt sent** (should be exactly one sentence):
Write Python code to analyze student marks.




**Assumptions the AI made that I never gave it** — list them, one per line. A data format, a pass
threshold, a rounding rule, an input method, an invented feature all count.
1. The input is a list of numbers, and the function is called analyze_marks(marks, pass_mark=50).
2. The pass threshold is 50 by default, and a mark equal to it passes (>=).
3. pass_rate is a percentage (0–100), with no rounding.
4. Marks must be between 0 and 100, and invalid input raises ValueError.



**Questions it should have asked and did not:**
1. Should pass_rate be rounded, and to how many decimals?
2. Does a mark equal to the pass mark pass (>= or >)?


**Is the function named analyze_marks with the required signature?** 
yes



**First impression before testing (one sentence — you will compare this with section 6 later):**
A minimal prompt leaves critical architectural decisions entirely to the AI's stochastic guesswork, creating high risk of interface mismatch with a strict test harness.







## 3. Prompt B — structured context

**Prompt sent** (paste it in full, including any substitutions):
You are a Python developer. Implement analyze_marks(marks, pass_mark=50). Return average, highest, lowest, and pass_rate in a dictionary. Accept marks from 0 to 100; raise ValueError for an empty list, non-numeric values, or out-of-range values. Use no external libraries. Return code plus a short explanation. 

**What B fixed compared to A:**

1. The exact keys, signature and validation rules are given, so the output is predictable.
2. B rejects True/False as marks; A treats True as the number 1.

**What B still leaves open:**

1. Rounding of pass_rate: B returned 66.66666666666666 for case 1.
2. >= versus > for a mark equal to pass_mark, and whether pass_mark itself is validated.

---




## 4. Prompt C — examples and tests

**What I appended to Prompt B:**

Example: analyze_marks([40, 60, 80], 50) → average 60, highest 80, lowest 40,
pass_rate 66.67. Include tests for: one mark, decimals, custom pass_mark, empty list,
text value, and marks below 0 or above 100. State any remaining assumptions before
the code.









Tests the AI wrote for itself — how many, and which situations do they cover?

7 asserts/checks in prompt_c.py, plus one print of the example.




| Situation | Covered by the AI's tests? |
| --- | --- |
| one mark | yes |
| decimals | yes |
| custom pass_mark | yes |
| empty list | yes |
| text value | yes |
| below 0 / above 100 | yes (two separate tests) |








**Do the AI's own tests pass against the AI's own code?** 
yes

**Do they agree with the harness in section 6?** 
yes 

**Assumptions C stated explicitly before the code:**
None before the code. The explanation came after the code and named no assumptions, although the prompt asked for them before it.








## 5. Prompt D — my combined prompt

**The complete prompt I wrote** (one message, sent to a fresh chat):
You are an expert Python developer. Implement a robust function `analyze_marks(marks, pass_mark=50)`.
Requirements:
1. Accept a list of numeric marks (integers or floats) and an optional pass_mark defaulting to 50.
2. Return a dictionary with exact keys: 'average', 'highest', 'lowest', 'pass_rate'.
3. Calculations: average (float), highest (max mark), lowest (min mark), pass_rate (percentage of marks >= pass_mark, rounded explicitly to 2 decimal places using round(val, 2)). Note that a mark exactly equal to pass_mark counts as passing.
4. Validation: raise ValueError if `marks` is empty, if any element is non-numeric (int/float), or if any mark is out of the 0 to 100 range.
5. Constraints: Use standard library only, no external packages. Include clean implementation and brief documentation.
Example: analyze_marks([40, 60, 80], 50) -> {'average': 60.0, 'highest': 80, 'lowest': 40, 'pass_rate': 66.67}




**What I deliberately added that A, B and C did not have:**

1. An explicit rounding rule: round(val, 2) for pass_rate.
2. An explicit rule that a mark equal to pass_mark passes (>=).
3. Exact key names, pass_rate defined as a percentage, and the allowed types (int/float).

**The ambiguity I found in the specification, and how I resolved it inside Prompt D:**
The task says case 1 must give pass_rate 66.67 but never says to round. A and B returned 66.66666666666666; the harness accepts both only because its tolerance is 0.01. I resolved it in point 3 of Prompt D with "rounded explicitly to 2 decimal places using round(val, 2)" and added that a mark equal to pass_mark counts as passing.

What Prompt D still lacks: I did not ask for the required tests, and I did not say to reject True/False.






## 6. Test results — the evidence

Six cases × four prompts. Verdicts are **PASS**, **FAIL** or **ERROR** only.

| # | Call | Required | A | B | C | D |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `analyze_marks([40, 60, 80], 50)` | avg 60 · high 80 · low 40 · rate 66.67 | PASS | PASS | PASS | PASS |
| 2 | `analyze_marks([100], 50)` | avg 100 · high 100 · low 100 · rate 100 | PASS | PASS | PASS | PASS |
| 3 | `analyze_marks([49.5, 50], 50)` | avg 49.75 · high 50 · low 49.5 · rate 50 | PASS | PASS | PASS | PASS |
| 4 | `analyze_marks([], 50)` | raises ValueError | PASS | PASS | PASS | PASS |
| 5 | `analyze_marks([40, "60"], 50)` | raises ValueError | PASS | PASS | PASS | PASS |
| 6 | `analyze_marks([-1, 50, 101], 50)` | raises ValueError | PASS | PASS | PASS | PASS |
| | **Totals** | | 6/6 | 6/6 | 6/6 | 6/6 |

**For every FAIL and ERROR above, one line: what was returned or raised instead.**

No FAIL and no ERROR for any prompt. Case 1 for A and B returned `pass_rate=66.66666666666666`, for C and D `66.67`; the 0.01 tolerance makes both PASS.

Note: my copy of the harness called `main()` twice at the end, which printed every run twice. I removed the duplicate call; the test cases and logic were not changed.

| Prompt | Case | What actually happened |
| --- | --- | --- |
| | | |
| | | |
| | | |

### Pasted terminal output — all four runs

> This is the part that makes the table above count. Paste the **whole** output, unedited,
> including the header lines. A table with nothing behind it is not accepted.

**Prompt A**

```
========================================================================
analyze_marks harness — code/prompt_a.py
tolerance for numeric comparison: 0.01
========================================================================
SIGNATURE: ok
------------------------------------------------------------------------
case 1  PASS   analyze_marks([40, 60, 80], 50)
          expect: average=60.0, highest=80, lowest=40, pass_rate=66.67
          got   : average=60.0, highest=80, lowest=40, pass_rate=66.66666666666666
------------------------------------------------------------------------
case 2  PASS   analyze_marks([100], 50)
          expect: average=100.0, highest=100, lowest=100, pass_rate=100.0
          got   : average=100.0, highest=100, lowest=100, pass_rate=100.0
------------------------------------------------------------------------
case 3  PASS   analyze_marks([49.5, 50], 50)
          expect: average=49.75, highest=50, lowest=49.5, pass_rate=50.0
          got   : average=49.75, highest=50, lowest=49.5, pass_rate=50.0
------------------------------------------------------------------------
case 4  PASS   analyze_marks([], 50)
          expect: ValueError
          got   : raised ValueError: Marks list cannot be empty.
------------------------------------------------------------------------
case 5  PASS   analyze_marks([40, '60'], 50)
          expect: ValueError
          got   : raised ValueError: All marks must be numeric.
------------------------------------------------------------------------
case 6  PASS   analyze_marks([-1, 50, 101], 50)
          expect: ValueError
          got   : raised ValueError: Marks must be between 0 and 100.
------------------------------------------------------------------------
RESULT  6 PASS · 0 FAIL · 0 ERROR   (code/prompt_a.py)
========================================================================
```

**Prompt B**

```
========================================================================
analyze_marks harness — code/prompt_b.py
tolerance for numeric comparison: 0.01
========================================================================
SIGNATURE: ok
------------------------------------------------------------------------
case 1  PASS   analyze_marks([40, 60, 80], 50)
          expect: average=60.0, highest=80, lowest=40, pass_rate=66.67
          got   : average=60.0, highest=80, lowest=40, pass_rate=66.66666666666666
------------------------------------------------------------------------
case 2  PASS   analyze_marks([100], 50)
          expect: average=100.0, highest=100, lowest=100, pass_rate=100.0
          got   : average=100.0, highest=100, lowest=100, pass_rate=100.0
------------------------------------------------------------------------
case 3  PASS   analyze_marks([49.5, 50], 50)
          expect: average=49.75, highest=50, lowest=49.5, pass_rate=50.0
          got   : average=49.75, highest=50, lowest=49.5, pass_rate=50.0
------------------------------------------------------------------------
case 4  PASS   analyze_marks([], 50)
          expect: ValueError
          got   : raised ValueError: Marks list cannot be empty.
------------------------------------------------------------------------
case 5  PASS   analyze_marks([40, '60'], 50)
          expect: ValueError
          got   : raised ValueError: All marks must be numeric.
------------------------------------------------------------------------
case 6  PASS   analyze_marks([-1, 50, 101], 50)
          expect: ValueError
          got   : raised ValueError: Marks must be between 0 and 100.
------------------------------------------------------------------------
RESULT  6 PASS · 0 FAIL · 0 ERROR   (code/prompt_b.py)
========================================================================
```

**Prompt C**

```
{'average': 60.0, 'highest': 80, 'lowest': 40, 'pass_rate': 66.67}
========================================================================
analyze_marks harness — code/prompt_c.py
tolerance for numeric comparison: 0.01
========================================================================
SIGNATURE: ok
------------------------------------------------------------------------
case 1  PASS   analyze_marks([40, 60, 80], 50)
          expect: average=60.0, highest=80, lowest=40, pass_rate=66.67
          got   : average=60.0, highest=80, lowest=40, pass_rate=66.67
------------------------------------------------------------------------
case 2  PASS   analyze_marks([100], 50)
          expect: average=100.0, highest=100, lowest=100, pass_rate=100.0
          got   : average=100.0, highest=100, lowest=100, pass_rate=100.0
------------------------------------------------------------------------
case 3  PASS   analyze_marks([49.5, 50], 50)
          expect: average=49.75, highest=50, lowest=49.5, pass_rate=50.0
          got   : average=49.75, highest=50, lowest=49.5, pass_rate=50.0
------------------------------------------------------------------------
case 4  PASS   analyze_marks([], 50)
          expect: ValueError
          got   : raised ValueError: marks cannot be empty
------------------------------------------------------------------------
case 5  PASS   analyze_marks([40, '60'], 50)
          expect: ValueError
          got   : raised ValueError: all marks must be numeric
------------------------------------------------------------------------
case 6  PASS   analyze_marks([-1, 50, 101], 50)
          expect: ValueError
          got   : raised ValueError: marks must be between 0 and 100
------------------------------------------------------------------------
RESULT  6 PASS · 0 FAIL · 0 ERROR   (code/prompt_c.py)
========================================================================
```

**Prompt D**

```
{'average': 60.0, 'highest': 80, 'lowest': 40, 'pass_rate': 66.67}
========================================================================
analyze_marks harness — code/prompt_d.py
tolerance for numeric comparison: 0.01
========================================================================
SIGNATURE: ok
------------------------------------------------------------------------
case 1  PASS   analyze_marks([40, 60, 80], 50)
          expect: average=60.0, highest=80, lowest=40, pass_rate=66.67
          got   : average=60.0, highest=80, lowest=40, pass_rate=66.67
------------------------------------------------------------------------
case 2  PASS   analyze_marks([100], 50)
          expect: average=100.0, highest=100, lowest=100, pass_rate=100.0
          got   : average=100.0, highest=100, lowest=100, pass_rate=100.0
------------------------------------------------------------------------
case 3  PASS   analyze_marks([49.5, 50], 50)
          expect: average=49.75, highest=50, lowest=49.5, pass_rate=50.0
          got   : average=49.75, highest=50, lowest=49.5, pass_rate=50.0
------------------------------------------------------------------------
case 4  PASS   analyze_marks([], 50)
          expect: ValueError
          got   : raised ValueError: marks cannot be empty
------------------------------------------------------------------------
case 5  PASS   analyze_marks([40, '60'], 50)
          expect: ValueError
          got   : raised ValueError: all marks must be numeric
------------------------------------------------------------------------
case 6  PASS   analyze_marks([-1, 50, 101], 50)
          expect: ValueError
          got   : raised ValueError: marks must be between 0 and 100
------------------------------------------------------------------------
RESULT  6 PASS · 0 FAIL · 0 ERROR   (code/prompt_d.py)
========================================================================
```

---










## 7. Scoring

0–2 per criterion, using the rubric in `README.md` Part 7.

| Criterion | A | B | C | D |
| --- | --- | --- | --- | --- |
| Correctness (cases passed) | 2 | 2 | 2| 2 |
| Requirement coverage | 2 | 2 | 2 | 2 |
| Verifiability (tests) | 0 | 0 | 2  | 0 |
| Assumptions stated | 1 | 1 | 1 | 1 |
| Noise (2 = none) | 2 | 2 | 1 | 2 |
| **Total / 10** | 7 | 7 | 8 | 7 |

**Prompt length, in words:** A __7__ · B __44__ · C __84__ · D __132__

**Words added per point gained** — B over A, C over B, D over C. One line on what that ratio says:
B over A: +37 words, 0 points. C over B: +40 words, +1 point net (+2 for tests, −1 for noise), 40 words per point. D over C: +48 words, −1 point. Extra words paid off only when they added tests, not when they added detail.
---







## 8. Conclusion — 150–200 words

Prompt C scored best (8/10) and is the one I would use at work, because it is the only one that shipped tests. All four prompts got 6/6 on the harness, so correctness did not separate them. The only visible difference is case 1: A and B returned pass_rate=66.66666666666666, while C and D returned 66.67. Both pass only because the tolerance is 0.01. That is the ambiguity: the task states 66.67 but never says to round. I resolved it in Prompt D with round(val, 2) and by stating that a mark equal to pass_mark passes. The single addition that changed the output was the worked example in C, after which case 1 returned 66.67 instead of 66.66666666666666. Pure noise: C's unrequested pass_mark range check. D also regressed: B and C rejected True and False, but D, told "non-numeric (int/float)", accepts them, and my Prompt D forgot the required tests, so Verifiability fell from 2 to 0. D added 48 words over C and lost 1 point, so longer was not better.

Word count: 171



## 9. Two questions for the debrief

Written before class, answered in class.

1. Why did the harness with tolerance 0.01 not distinguish a rounded pass_rate (66.67) from an unrounded one (66.66666666666666)?
2. Why did D, where I wrote "non-numeric (int/float)", start accepting True/False, while B and C rejected them without being asked?