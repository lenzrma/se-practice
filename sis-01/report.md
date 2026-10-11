# SIS #01 — Software Engineering Fundamentals, With an AI in the Loop

**Topic:** 1.1

---

## 1. Scenario

**Question:** What does a customer require for professional software delivery beyond functional source code?

**Users:** University students who book equipment and computer lab assistants who manage it.

**Problem:** Manual equipment booking in paper logbooks causes scheduling conflicts, lost devices and administrative chaos in the lab.

**Constraints:** 1) The system must run on the existing local university servers. 2) Implementation is limited to one strict two-month semester sprint.

**Risk:** Complete system failure during peak examination weeks, caused by a missing maintenance plan, backup routine and clear documentation.

**Assumptions:** [Fictional: all room names, laboratory equipment models and user accounts are invented for this case study.] The customer is the university lab department. The exam-week demand spike is an assumption, not a measured figure.

## 2. Analysis

Professional software delivery means handing the customer a system they can run, support and keep running, not only source code. Lecture slides (IARE ACS008, slide 11) describe a working program as one part of a software configuration with many elements, with documentation as the foundation for support. For the lab department, delivery therefore has to include the means to operate the booking system after the student team has left.

The central trade-off is time. One two-month sprint cannot hold both a wide feature set and a complete operations package. I chose a small core: booking with conflict checking, and device check-out and return with a due date. These map to the two named problems, scheduling conflicts and lost devices. Notifications and reports wait for a later sprint because no named problem needs them yet. The second trade-off comes from the local-server constraint: the team does not control the hardware, so the delivery must state what it needs and who hosts it.

Decision 1: a handover package that leads with maintenance, backups and documentation, because the stated risk is a missing maintenance plan, backup routine and documents, not slow code. University IT hosts the system and a trained lab assistant is first-line support. This owner is my assumption, since the Code of Ethics (clause 3.15) asks for maintenance to be treated as seriously as new development but does not say who owns it. Backups run nightly, with a copy kept off the application server and a restore drill before handover; these are design assumptions, not sourced rules. Student, assistant and administrator guides cover booking, returns, installation, configuration and recovery, and record problems found with the solutions adopted (clause 3.11).

Decision 2: a testing and fallback set matched to the risk. Evidence includes double-booking tests, an acceptance check with a lab assistant, a restore drill and a load test against an assumed exam-week spike, for which I give no number (clause 3.10). A documented downtime procedure switches the lab to the paper logbook and explains how to enter those records afterwards, so the logbook is the planned fallback rather than the disaster. Logs help administrators find what went wrong and tests reduce the chance of failure, but neither guarantees that failure will not happen.

## 3. Review

I treated the Prompt B critique as claims to judge, not as evidence. Point 1 (my risk and the draft's load-testing emphasis did not match) I accepted, so maintenance, backups and documentation now lead. Point 2 (the arbitrary number of five items) I qualified: slide 11 gives no count, so the number is gone. Points 3, 4, 7 and 8 (backup detail, downtime fallback, owner, testing evidence) I accepted and answered with labelled assumptions. Point 5 I qualified by tying each feature to a named problem. Point 6 I accepted: I could not verify the draft's claim that local servers avoid hosting cost and keep data on campus, so I removed it. Point 9 I qualified by defining the customer and labelling the exam spike. I rejected point 10: it said my claim that logs and tests prevent failures never appeared, but my outline point 4 says exactly that, so the claim was mine and I softened it.

Source checks: verification row 1 checked "a customer typically needs five things" against slide 11 and qualified it. Row 2 checked that maintenance continues after delivery against slides 10 and 14 and kept it, quoting no percentage because the slide figure is general, not specific to small projects. Row 3 checked the maintenance owner against Code clauses 3.10, 3.11 and 3.15; the Code supports testing, documentation and maintenance but names no owner, so I qualified it.

Three substantive changes appear in the final text: features mapped to named problems (change-log row 1), the unverified hosting claim deleted (row 2), and a downtime fallback added in place of a bare user-count figure (row 3). Remaining gap: I did not open the course textbook, so only lecture slides and the Code were checked.

## 4. Conclusion

I recommend delivering the booking system as a package, not a program: a small core of booking and device check-out, plus student, assistant and administrator guides, nightly off-server backups with a tested restore, a testing record, a downtime procedure and a named owner at handover. The sprint should spend its time on these items before adding extra features. The main limitation is thin evidence. The argument rests on lecture slides and the ethics code, not on the course textbook, and the owner, backup schedule and exam-week load are my assumptions. The system also depends on the university's servers and IT staff, so recovery fails if the hardware or the hosting agreement fails.

## 5. Reflection

Engaging in this assignment transformed my perspective on software development lifecycle priorities. Previously, I viewed the absence of code bugs at the repository submission stage as the ultimate measure of project success. Analyzing professional delivery made me realize the critical value of comprehensive documentation, test coverage, and operational readiness. Utilizing the AI assistant through structured steps—drafting, critical review, evidence verification, and revision—helped me critically evaluate generated insights against academic sources. The most valuable takeaway was learning to independently verify every key claim rather than blindly trusting AI outputs. A concrete moment: the critique said my claim about logs and tests preventing failures was missing, but my own outline point 4 contained it, so I rejected that point. Another: I could not verify the hosting cost claim, so I removed it. I also learned that a clean-looking draft can answer a different problem than my stated risk, which critique point 1 showed.

## 6. References

- IARE. (n.d.). Software Engineering, course ACS008, Unit I lecture slides (software products, software myths). Institute of Aeronautical Engineering, Hyderabad. https://www.iare.ac.in/sites/default/files/PPT/IARE_SE_PPTs.pdf. Accessed 2026-10-11.
- ACM/IEEE-CS Joint Task Force. (1999). Software Engineering Code of Ethics and Professional Practice, Version 5.2, full version (copy hosted by Linköping University). https://www.ida.liu.se/~TDDI82/etik/SW_Engr_Code_of_Ethics.pdf. Accessed 2026-10-11.

## 7. Appendix A — Initial outline

1. Defining professional software delivery as a comprehensive package combining code, documentation, and operational support.
2. Analyzing the practical needs of university students and laboratory assistants within a shared facility.
3. Accounting for local infrastructure limitations when deploying university applications.
4. Implementing automated logging and testing mechanisms to prevent critical system failures during high-load periods.
5. Emphasizing the long-term importance of software maintenance and evolution after initial release.

## 8. Appendix B — AI exchanges

### B1 — Draft (Prompt A)

- **Tool:** Claude.ai
- **Model:** Claude Sonnet 5.5
- **Date:** 2026-10-11
- **Purpose:** contextual draft

**Prompt:**

```text
Act as a software engineering tutor. Help me analyze topic 1.1 Professional software delivery: what does a customer require for professional software delivery beyond functional source code? for a first-year-level university assignment.

My scenario is Users: university students and computer lab assistants. Problem: manual equipment booking via paper logbooks causes scheduling conflicts, lost devices, and administrative chaos. Constraints: 1) the system must be deployed on existing local university servers; 2) implementation is restricted to a strict two-month semester sprint. Risk: complete system failure during peak examination load due to the lack of a maintenance plan, backup routines, and clear documentation. Assumptions: all room names, laboratory equipment models, and user accounts are fictional. My initial ideas are 1. Defining professional software delivery as a comprehensive package combining code, documentation, and operational support. 2. Analyzing the practical needs of university students and laboratory assistants within a shared facility. 3. Accounting for local infrastructure limitations when deploying university applications. 4. Implementing automated logging and testing mechanisms to prevent critical system failures during high-load periods. 5. Emphasizing the long-term importance of software maintenance and evolution after initial release. Draft a 400–500 word explanation using these details.

Separate facts from assumptions. Explain trade-offs and identify claims I should verify. Do not invent quotations, references or page numbers.
```

**Response:**

```text
**Draft (about 425 words)**

Professional software delivery means handing a customer something they can run, trust and keep running, not just source code. A customer judges a delivery by whether the lab can operate it, not by how elegant the code is. In this scenario the customer is the university, and the users are students who book equipment and lab assistants who manage it. Code alone would not solve the problem of scheduling conflicts and lost devices, because the system has to keep working after the developer leaves.

Beyond working code, a customer typically needs five things. First, documentation: a user guide for students and assistants, and an administrator guide covering installation, configuration and recovery. Students need quick booking with visible availability. Assistants need to see who holds which device, record returns and report faults, so each group needs its own instructions. Second, deployment support: the system must run on the existing local university servers, so the delivery should include installation steps and a list of required software and versions. Third, a backup and restore routine, so booking records and device history survive a disk failure. Fourth, testing evidence, including a check of how the system behaves when many students book at once. Fifth, a maintenance plan that names who fixes bugs, who applies updates, and how changes are made safely.

These needs follow from the stated risk. Examination weeks bring a sudden spike in demand, so the delivery should state how many simultaneous users the system was tested for. If the system fails during that period, the lab returns to paper logbooks and the original problems come back. Logging helps administrators find out what went wrong, and testing reduces the chance of failure, but neither guarantees it.

Trade-offs matter because the sprint lasts only two months. Time spent on documentation, backups and load testing is time not spent on features such as notifications or reports. A reasonable choice is a small core feature set (booking, conflict checking, device check-in and check-out) delivered with a simple but complete operations package. Running on local servers avoids hosting costs and keeps data on campus, but the team may lack control over hardware, software versions and uptime, and the university's IT staff must agree to support it.

Maintenance continues after release. Exam periods, new equipment types and changing policies will require updates, so the design should be easy to modify and the handover should say who owns the system. Without an owner, small problems such as a full disk or an expired account build up until the next peak.

**Facts vs assumptions**

- Given in your scenario (treat as facts for the assignment): users are students and lab assistants; the current process is paper logbooks; the system runs on local university servers; there is a two-month sprint; the main risk is failure at peak exam load.
- General software engineering knowledge, not specific to your case: customers need more than code (documentation, deployment, support, maintenance). Say this without citing anyone unless you find a source.
- Assumptions I made: the university IT team will host and support the system; the project team hands over after the sprint; the peak is many simultaneous bookings; the core feature set is the right minimum. The room names, equipment and accounts are fictional, as you stated.
- Your claim that logs and tests "prevent" failures is too strong. I changed it to "help find" and "reduce the chance".

**Trade-offs to mention**

- Features vs operations package, within a fixed two months.
- Local servers (cheap, data stays on campus) vs limited control and dependence on IT staff.
- Backups and load tests cost time but directly address your stated risk.

**Claims to verify before submitting**

1. The exact definition and any list of "delivery requirements" your course or textbook uses. Align my five items with it, and cite only sources you have actually read.
2. Whether your course expects specific terms, such as "non-functional requirements" or "operational readiness".
3. Whether your university has rules on data storage, backups or server access that apply to your fictional scenario.
4. Whether the peak load claim needs a number. I gave none, because inventing one would be a fabricated figure.
5. Whether the assignment wants word-count rules to include headings. My draft has none.

I added no quotations, references or page numbers.
```

### B2 — Critique (Prompt B)

- **Tool:** Claude.ai
- **Model:** Claude Sonnet 5.5
- **Date:** 2026-10-11
- **Purpose:** critical review of the draft

**Prompt:**

```text
Review the draft below against my chosen question and scenario. Identify inaccuracies, missing reasoning, vague claims and unsupported assumptions.
For each concern, explain why it matters and how I could check it. Include a counterexample or alternative interpretation. Do not rewrite the answer yet.
Question: Topic 1.1 Professional software delivery: what does a customer require for professional software delivery beyond functional source code?. Scenario: Users: university students and computer lab assistants. Problem: manual equipment booking via paper logbooks causes scheduling conflicts, lost devices, and administrative chaos. Constraints: 1) the system must be deployed on existing local university servers; 2) implementation is restricted to a strict two-month semester sprint. Risk: complete system failure during peak examination load due to the lack of a maintenance plan, backup routines, and clear documentation. Assumptions: all room names, laboratory equipment models, and user accounts are fictional. Draft: **Draft (about 425 words)**

Professional software delivery means handing a customer something they can run, trust and keep running, not just source code. A customer judges a delivery by whether the lab can operate it, not by how elegant the code is. In this scenario the customer is the university, and the users are students who book equipment and lab assistants who manage it. Code alone would not solve the problem of scheduling conflicts and lost devices, because the system has to keep working after the developer leaves.

Beyond working code, a customer typically needs five things. First, documentation: a user guide for students and assistants, and an administrator guide covering installation, configuration and recovery. Students need quick booking with visible availability. Assistants need to see who holds which device, record returns and report faults, so each group needs its own instructions. Second, deployment support: the system must run on the existing local university servers, so the delivery should include installation steps and a list of required software and versions. Third, a backup and restore routine, so booking records and device history survive a disk failure. Fourth, testing evidence, including a check of how the system behaves when many students book at once. Fifth, a maintenance plan that names who fixes bugs, who applies updates, and how changes are made safely.

These needs follow from the stated risk. Examination weeks bring a sudden spike in demand, so the delivery should state how many simultaneous users the system was tested for. If the system fails during that period, the lab returns to paper logbooks and the original problems come back. Logging helps administrators find out what went wrong, and testing reduces the chance of failure, but neither guarantees it.

Trade-offs matter because the sprint lasts only two months. Time spent on documentation, backups and load testing is time not spent on features such as notifications or reports. A reasonable choice is a small core feature set (booking, conflict checking, device check-in and check-out) delivered with a simple but complete operations package. Running on local servers avoids hosting costs and keeps data on campus, but the team may lack control over hardware, software versions and uptime, and the university's IT staff must agree to support it.

Maintenance continues after release. Exam periods, new equipment types and changing policies will require updates, so the design should be easy to modify and the handover should say who owns the system. Without an owner, small problems such as a full disk or an expired account build up until the next peak.

**Facts vs assumptions**

- Given in your scenario (treat as facts for the assignment): users are students and lab assistants; the current process is paper logbooks; the system runs on local university servers; there is a two-month sprint; the main risk is failure at peak exam load.
- General software engineering knowledge, not specific to your case: customers need more than code (documentation, deployment, support, maintenance). Say this without citing anyone unless you find a source.
- Assumptions I made: the university IT team will host and support the system; the project team hands over after the sprint; the peak is many simultaneous bookings; the core feature set is the right minimum. The room names, equipment and accounts are fictional, as you stated.
- Your claim that logs and tests "prevent" failures is too strong. I changed it to "help find" and "reduce the chance".

**Trade-offs to mention**

- Features vs operations package, within a fixed two months.
- Local servers (cheap, data stays on campus) vs limited control and dependence on IT staff.
- Backups and load tests cost time but directly address your stated risk.

**Claims to verify before submitting**

1. The exact definition and any list of "delivery requirements" your course or textbook uses. Align my five items with it, and cite only sources you have actually read.
2. Whether your course expects specific terms, such as "non-functional requirements" or "operational readiness".
3. Whether your university has rules on data storage, backups or server access that apply to your fictional scenario.
4. Whether the peak load claim needs a number. I gave none, because inventing one would be a fabricated figure.
5. Whether the assignment wants word-count rules to include headings. My draft has none.

I added no quotations, references or page numbers.
```

**Response:**

```text
I'm treating the draft's own text as the thing under review. Ordered roughly by how much each concern could cost you.

**1. The stated risk and the draft's emphasis don't match.**
- *Concern:* The scenario attributes failure to a missing maintenance plan, backup routines and documentation. The draft's strongest concrete requirement is load testing and a concurrent-user figure, and it assumes "the peak is many simultaneous bookings."
- *Why it matters:* The answer can look well-argued while addressing a different cause than the one you were given.
- *Check:* Re-read the risk sentence and mark which draft items map to each named cause (maintenance plan, backups, documentation). Count how much text each gets.
- *Alternative:* Peak-week failure could come from a full disk, an expired certificate or account, a server reboot, or nobody knowing how to restart the service. None of those is a concurrency problem, and load testing wouldn't catch them.

**2. "Five things" is presented as a typical list with no basis.**
- *Concern:* "A customer typically needs five things" is asserted, and the number looks arbitrary. The draft admits it is "general knowledge" and cites nothing.
- *Why it matters:* A grader may read it as invented structure. It also leaves out items that plausibly matter more.
- *Check:* Compare it with the list in your course material or textbook. If you cite a standard, confirm the wording yourself. ISO/IEC 25010 (quality characteristics) and ISO/IEC/IEEE 12207 (lifecycle processes) exist, but don't cite either until you've checked that it supports the specific point.
- *Counterexample:* Missing items include user and admin training, migration of existing paper-logbook data, access control and security, acceptance criteria and sign-off, a rollback plan for deployment, monitoring or alerting, and a support or response-time agreement. For a handover to non-developers, training arguably matters more than "testing evidence."

**3. Backups are named but not specified.**
- *Concern:* "A backup and restore routine" gives no frequency, retention, storage location or restore test.
- *Why it matters:* A backup kept on the same server, or never restored, doesn't protect against the stated risk.
- *Check:* Ask what the acceptable data loss and downtime are, and whether a restore drill is part of the deliverable.
- *Alternative:* Booking data changes slowly, so nightly backups might be enough. Or the university IT team may already back up its servers, which would shift the deliverable from "build backups" to "confirm and document existing ones."

**4. Missing downtime fallback, and an unsupported causal claim.**
- *Concern:* "The lab returns to paper logbooks and the original problems come back" is stated as certain. The draft never proposes a planned fallback.
- *Why it matters:* Professional delivery usually includes what to do when the system is down, and the paper return might be the planned fallback rather than the disaster.
- *Check:* Ask whether a degraded-mode procedure (a printed sheet, a read-only export) would be a stronger answer to the risk.

**5. The core-feature recommendation is unjustified.**
- *Concern:* "A reasonable choice is a small core feature set" has no reasoning. The three features are picked by assumption, and the draft itself lists the choice as an assumption.
- *Why it matters:* It is the key trade-off decision and it is asserted, not argued.
- *Check:* Map each feature to a named problem in the scenario (conflicts, lost devices, admin chaos). Sketch rough effort for each against two months.
- *Counterexample:* Overdue-return reminders are the kind of "notification" feature the draft defers, yet they directly address lost devices. Deferring them could undermine the problem the system exists to solve.

**6. Local servers are framed as a choice and given unsupported benefits.**
- *Concern:* The scenario lists local deployment as a constraint, but the draft treats it as a trade-off. "Avoids hosting costs" and "keeps data on campus" are claims, not facts.
- *Why it matters:* University servers still cost staff time, and "on campus" doesn't by itself mean compliant or secure.
- *Check:* Reframe it as "what this constraint forces into the delivery" (a version list, firewall and access requests, IT sign-off). Verify any cost or privacy claim against your course material or drop it.

**7. Ownership and timing after the sprint are unresolved.**
- *Concern:* The draft says the handover "should say who owns the system" but never says who. It also assumes IT staff will host and support it.
- *Why it matters:* A student team will have left after two months, so "who fixes bugs" is the crux of the maintenance plan.
- *Check:* Decide and state a default owner, such as university IT, the lab supervisor or a trained lab assistant, and say what that owner needs (a runbook, credentials, a contact).
- *Alternative:* Lab assistants may be the only realistic day-to-day maintainers, which changes what the documentation must contain.
- *Related gap:* The draft never places delivery before exam week. If the sprint ends at the peak, there is no burn-in period.

**8. "Testing evidence" is vague, and conflict correctness is untested.**
- *Concern:* The only test named is a many-users check. Nothing covers double-booking races, user acceptance with real lab assistants, or restore testing.
- *Why it matters:* Scheduling conflicts are the headline problem. A system that handles load but still double-books doesn't solve it.
- *Check:* List what evidence would convince the customer. A test log, an acceptance checklist signed by an assistant and a documented restore drill are all candidates.

**9. Smaller vague claims.**
- "A customer judges a delivery by whether the lab can operate it" is rhetoric with no support. It is also unclear whether the "customer" is the university, the lab department or the students, who are users, not customers.
- Check: Define the customer and user roles once and keep them consistent.
- "Examination weeks bring a sudden spike" is plausible but is an assumption.
- Check: Label it as one.

**10. The surrounding notes contradict the body or reference things that aren't there.**
- *Concern:* The notes say "Your claim that logs and tests 'prevent' failures... I changed it," but no such claim of yours appears in your question. Check item 5 says "My draft has none" about headings, yet the draft uses bold headings.
- *Why it matters:* Both read as confused, and the first implies a prior version you can't verify.
- *Check:* Read the notes against the actual text, then confirm the word count (about 425) with a counter, and whether your rules count headings and the notes sections.

**Overall:** The draft is coherent, but it relies on unsourced assertions and unjustified choices (five items, the core feature set, the assumed load pattern). It doesn't tie each requirement to a named cause in the risk statement.
```

### B3 — Revision (Prompt C)

- **Tool:** Claude.ai
- **Model:** Claude Sonnet 5.5
- **Date:** 2026-10-11
- **Purpose:** revision using my review decisions and source notes

**Prompt:**

```text
Revise the draft using my review decisions and source notes below. Keep the answer relevant to my scenario and preserve uncertainty where evidence is limited.

My decisions: (1) Accepted: the draft stressed load testing but my risk names a missing maintenance plan, backups and documentation, so these must lead and load testing becomes one test among several. (2) Qualified: the number "five things" has no basis, so I drop it and present a scenario-driven set instead. (3) Accepted: backups need specifics; I decide nightly backup, a copy kept off the application server, and a restore drill before handover (these are my design assumptions, not sourced facts). (4) Accepted: add a documented downtime fallback; the paper logbook becomes the planned fallback, not the disaster. (5) Qualified: the feature set must be justified by mapping each feature to a named problem; I keep booking with conflict checking and device check-out and return with a due date, because lost devices are a named problem. (6) Accepted: local servers are a constraint, not a choice; I could not verify the claims about hosting cost and data staying on campus, so I remove them. (7) Accepted: name a default owner; university IT hosts the system and a trained lab assistant is first-line support (fictional assumption). (8) Accepted: testing evidence must include double-booking tests, an acceptance check with a lab assistant, and a restore drill. (9) Qualified: define the customer as the university lab department and the users as students and assistants; label the exam-week spike as an assumption. (10) Rejected: the note that my claim about logs and tests preventing failures never appeared is wrong, because my outline point 4 says mechanisms to prevent critical system failures; the claim is still too strong and I keep the softer wording. Verified evidence: (a) IARE lecture slides ACS008, slide 11 (Software Myths): a working program is only one part of a software configuration that includes many elements, and documentation is the foundation for support; the slide gives no count of five. (b) Same slides, slide 10 and slide 14: a large share of effort and cost comes after delivery; slide 10 gives a 60 to 80 percent figure that is a general claim not specific to small projects, so I use it only qualitatively. (c) ACM/IEEE-CS Software Engineering Code of Ethics v5.2, full version, Principle 3, clause 3.10 (adequate testing, debugging and review), clause 3.11 (adequate documentation including problems found and solutions adopted) and clause 3.15 (treat all forms of maintenance with the same professionalism as new development); the code does not say who owns maintenance, so the owner is my scenario decision. Draft: **Draft (about 425 words)**

Professional software delivery means handing a customer something they can run, trust and keep running, not just source code. A customer judges a delivery by whether the lab can operate it, not by how elegant the code is. In this scenario the customer is the university, and the users are students who book equipment and lab assistants who manage it. Code alone would not solve the problem of scheduling conflicts and lost devices, because the system has to keep working after the developer leaves.

Beyond working code, a customer typically needs five things. First, documentation: a user guide for students and assistants, and an administrator guide covering installation, configuration and recovery. Students need quick booking with visible availability. Assistants need to see who holds which device, record returns and report faults, so each group needs its own instructions. Second, deployment support: the system must run on the existing local university servers, so the delivery should include installation steps and a list of required software and versions. Third, a backup and restore routine, so booking records and device history survive a disk failure. Fourth, testing evidence, including a check of how the system behaves when many students book at once. Fifth, a maintenance plan that names who fixes bugs, who applies updates, and how changes are made safely.

These needs follow from the stated risk. Examination weeks bring a sudden spike in demand, so the delivery should state how many simultaneous users the system was tested for. If the system fails during that period, the lab returns to paper logbooks and the original problems come back. Logging helps administrators find out what went wrong, and testing reduces the chance of failure, but neither guarantees it.

Trade-offs matter because the sprint lasts only two months. Time spent on documentation, backups and load testing is time not spent on features such as notifications or reports. A reasonable choice is a small core feature set (booking, conflict checking, device check-in and check-out) delivered with a simple but complete operations package. Running on local servers avoids hosting costs and keeps data on campus, but the team may lack control over hardware, software versions and uptime, and the university's IT staff must agree to support it.

Maintenance continues after release. Exam periods, new equipment types and changing policies will require updates, so the design should be easy to modify and the handover should say who owns the system. Without an owner, small problems such as a full disk or an expired account build up until the next peak.

**Facts vs assumptions**

- Given in your scenario (treat as facts for the assignment): users are students and lab assistants; the current process is paper logbooks; the system runs on local university servers; there is a two-month sprint; the main risk is failure at peak exam load.
- General software engineering knowledge, not specific to your case: customers need more than code (documentation, deployment, support, maintenance). Say this without citing anyone unless you find a source.
- Assumptions I made: the university IT team will host and support the system; the project team hands over after the sprint; the peak is many simultaneous bookings; the core feature set is the right minimum. The room names, equipment and accounts are fictional, as you stated.
- Your claim that logs and tests "prevent" failures is too strong. I changed it to "help find" and "reduce the chance".

**Trade-offs to mention**

- Features vs operations package, within a fixed two months.
- Local servers (cheap, data stays on campus) vs limited control and dependence on IT staff.
- Backups and load tests cost time but directly address your stated risk.

**Claims to verify before submitting**

1. The exact definition and any list of "delivery requirements" your course or textbook uses. Align my five items with it, and cite only sources you have actually read.
2. Whether your course expects specific terms, such as "non-functional requirements" or "operational readiness".
3. Whether your university has rules on data storage, backups or server access that apply to your fictional scenario.
4. Whether the peak load claim needs a number. I gave none, because inventing one would be a fabricated figure.
5. Whether the assignment wants word-count rules to include headings. My draft has none.

I added no quotations, references or page numbers.

Show what you changed and why. Use only the sources I supplied. Flag remaining gaps instead of inventing details.
```

**Response:**

```text
**Revised draft (about 470 words)**

Professional software delivery means handing the customer something they can run, support and keep running, not only source code. Here the customer is the university lab department. The users are students, who book equipment, and lab assistants, who manage it. Lecture slides (IARE ACS008, slide 11) describe a working program as only one part of a software configuration, with documentation as the foundation for support. The system runs on local university servers, which is a constraint of this scenario, and the sprint lasts two months.

The main risk is that the lab cannot keep the system running after handover: no maintenance plan, no backups, no documentation. The delivery therefore leads with these.

**Maintenance and ownership.** The slides (10 and 14) indicate that a large share of effort and cost comes after delivery, so I treat maintenance as part of the project. The ACM/IEEE-CS Code (clause 3.15) asks for the same professionalism in maintenance as in new development. The Code does not say who owns maintenance. My scenario assumption is that university IT hosts the system and a trained lab assistant is first-line support. The handover names both.

**Backups.** I assume a nightly backup, a copy kept off the application server, and a restore drill before handover. These are my design assumptions, not sourced requirements.

**Documentation.** There is a student guide for booking and an assistant guide for check-out, returns and faults. An administrator guide covers installation, configuration and recovery. Following clause 3.11, it also records problems found and solutions adopted.

**Downtime fallback.** If the system is down, a documented procedure switches the lab to the paper logbook and says how to enter those records afterwards. The logbook is the planned fallback, not the disaster.

**Features tied to named problems.** Booking with conflict checking addresses scheduling conflicts. Device check-out and return with a due date addresses lost devices. Features with no named problem, such as notifications or reports, wait for a later sprint.

**Testing evidence** (clause 3.10, adequate testing) covers:
- double-booking tests;
- an acceptance check with a lab assistant;
- a restore drill;
- a load test against an assumed exam-week spike. This is an assumption, and I give no number.

Logs help administrators find what went wrong, and tests reduce the chance of failure. Neither guarantees that critical failures will not happen.

**What changed and why**

| # | Change | Reason |
|---|---|---|
| 1 | Maintenance, backups and documentation now lead. Load testing is one test among several. | Matches your risk. |
| 2 | "Five things" removed. The set is scenario-driven. | No source gives a count. Slide 11 gives none. |
| 3 | Backups specified: nightly, off-server copy, restore drill. Labelled as design assumptions. | Your decision. |
| 4 | Downtime fallback added. | Your decision. |
| 5 | Each feature mapped to a named problem. Notifications and reports dropped. | They had no named problem. |
| 6 | Hosting-cost and data-on-campus claims removed. Local servers framed as a constraint. | Unverified. |
| 7 | Default owner named and marked as an assumption. | Clause 3.15 does not assign ownership. |
| 8 | Testing evidence rewritten. | Your decision. |
| 9 | Customer and users defined. Exam-week spike labelled an assumption. | Your decision. |
| 10 | Softer wording on logs and tests kept. | Your decision. The earlier review note was wrong. |
| 11 | The 60 to 80 percent figure is not quoted. The point is made only qualitatively. | It is a general claim, not specific to small projects. |

**Remaining gaps**
- I have not seen the slides or the Code myself. Slide numbers and clauses 3.10, 3.11 and 3.15 rest on your notes. Recheck the wording before submitting.
- The 60 to 80 percent figure is from your notes on slide 10. I left it out.
- No peak-load number is given. Pick one only if your course supplies a basis.
- The "trained" lab assistant is unspecified: who trains them, and on what.
- Backup retention, restore-drill pass criteria and the trigger for switching to the paper logbook are undefined. Add them only as labelled assumptions.
- University IT's agreement to host is assumed, not confirmed.
- Check which citation format your course expects. I added no page numbers or quotations.
```

## 9. Appendix C — Evidence tables

### Verification table

| AI claim | Source and locator | Evidence found | Decision |
| --- | --- | --- | --- |
| Beyond working code, a customer typically needs five things. | IARE ACS008 lecture slides, Unit I, slide 11 (Software Myths), https://www.iare.ac.in/sites/default/files/PPT/IARE_SE_PPTs.pdf, accessed 2026-10-11 | The slide says a working program is only one part of a software configuration that includes many elements, and that documentation is the foundation for support. It gives no count of five, so the number is the AI's own. | qualify |
| Maintenance continues after release. | IARE ACS008 lecture slides, Unit I, slides 10 and 14, https://www.iare.ac.in/sites/default/files/PPT/IARE_SE_PPTs.pdf, accessed 2026-10-11 | Slide 14 says that for most systems the majority of costs come from changing the software after it is in use. Slide 10 gives a 60 to 80 percent figure for effort after first delivery, a general claim not specific to small projects. | keep |
| A maintenance plan that names who fixes bugs, who applies updates, and how changes are made safely. | ACM/IEEE-CS Software Engineering Code of Ethics v5.2, full version, Principle 3, clauses 3.10, 3.11 and 3.15, https://www.ida.liu.se/~TDDI82/etik/SW_Engr_Code_of_Ethics.pdf, accessed 2026-10-11 | The Code asks for adequate testing and review (3.10), adequate documentation including problems and solutions (3.11), and maintenance treated as professionally as new development (3.15). It does not say who owns maintenance, so the owner is a scenario decision. | qualify |

### Change log

| AI wording | Final wording | Reason (evidence or constraint) |
| --- | --- | --- |
| A reasonable choice is a small core feature set (booking, conflict checking, device check-in and check-out) delivered with a simple but complete operations package. | The core is booking with conflict checking, and device check-out and return with a due date, each mapped to a named problem; notifications and reports wait for a later sprint. | Critique point 5 and the scenario problem: scheduling conflicts and lost devices are the named problems. |
| Running on local servers avoids hosting costs and keeps data on campus. | Local servers are treated as a constraint, and the delivery states what the team needs from university IT. | I could not verify the cost and data claims in any source I opened; scenario constraint 1 is local deployment. |
| The delivery should state how many simultaneous users the system was tested for. | A documented downtime procedure switches the lab to the paper logbook, and the load test uses an assumed spike with no invented number. | Critique points 1 and 4 and the scenario risk: failure can come from missing backups, owner or documents, not only load. |
