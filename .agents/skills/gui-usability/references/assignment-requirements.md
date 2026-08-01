# HW03 Assignment Requirements Relevant to This Skill

Source: `2026.HW03.GUI Usability_En.pdf`. This working summary does not replace the official PDF.

## System Under Test

EShop — Vietnamese e-commerce demo. Requirements: `README.md` (FR-01..FR-24, Vietnamese SRS).
API contract: `api_specification.md`. Startup: `setup_guide.md` / `run_servers.sh`. Components:
Backend (`http://localhost:3000`), Frontend Web (`http://localhost:5173`), Web Admin
(`http://localhost:5174`), Mobile (Expo Go on LAN).

Interface aspects for this homework (not FR-numbered functional requirements, but checklist
categories):

- IA-01: General UI standards
- IA-02: Forms
- IA-03: Navigation
- IA-04: Feedback / state

The closest normative source for these is `README.md` §8 (FR-21 General UI, FR-22 Forms, FR-23
Navigation, FR-24 Feedback & State) plus general usability heuristics for anything the SRS does not
enumerate (accessibility, dark mode, RTL, etc.).

## Scope Selection (§5)

- Task 1/3 checklist: choose one or more screens (Home, Cart, Checkout, Admin Dashboard, a Mobile
  screen, ...). Minimum one screen; more screens are strongly encouraged because a single screen
  will not realistically yield 40 non-repetitive items.
- Task 2 usability flow: choose exactly one end-to-end flow (e.g. Sign-up → Add to cart → Checkout
  with a coupon). This becomes the task scenario.
- Never duplicate screen/flow selection with a groupmate if the cohort enforces that rule (see
  `instructor-clarifications.md` item 11).

## Task 1 — GUI Checklist (30 pts)

- Design a checklist of **more than 40 items** covering all four interface aspects.
- Use AI to generate an initial set, then critically review and add further human items.
- For every human-added item, explain **why the AI missed it** (prompt quality, model limitation,
  or characteristic of the chosen interface). Examples the AI tends to miss: accessibility, RTL
  layout, dark mode — not an exhaustive list.
- Execute the checklist against the real SUT: mark each item Passed/Failed, add a Notes column with
  the failure reason for every Failed item, and attach screenshots for Failed items only.
- Report all discovered bugs in the Markdown report **and** on GitHub Issues, with screenshots
  attached to each issue.

## Task 2 — Usability Evaluation (40 pts)

Moderated, small-sample evaluation of the single chosen flow with **7 real participants** (7
sessions, 1 per participant).

**Phase 1 — Plan & prepare:** define objectives; write a goal-oriented (not step-by-step) task
scenario; prepare SUS or UEQ-S (or a justified custom scale) plus probe questions covering at least
clarity, error recovery, speed, and trust; recruit 7 real participants outside this class with
verifiable contact details (Zalo/email/phone, middle four digits masked) — non-IT/non-tester
participants preferred but not required; run one pilot session first and refine.

**Phase 2 — Conduct (one session per participant):** set the stage (testing the product, not the
participant) and request think-aloud; observe neutrally, no leading hints, step in only if
completely stuck; capture screen (and audio with consent) plus structured notes on friction,
errors, hesitations, verbalized frustration; close with the SUS/UEQ-S scale then the probe
questions.

**Phase 3 — Analyse & report:** score SUS/UEQ-S across all 7 participants; synthesize notes into
grouped pain points, separating isolated bugs from systemic issues; prioritize by severity; report
genuine bugs in the Markdown report and on GitHub Issues with screenshots.

A TA may randomly call 2 participants to verify. Impersonation = 0 points for Task 2.

## Task 3 — Cross-Browser / Cross-Platform (20 pts)

- Re-run Task 1's checklist across **at least 3 platforms**.
- BrowserStack or LambdaTest trial strongly preferred; Sauce Labs, CrossBrowserTesting, or real
  physical devices are acceptable substitutes if the trial has expired, provided screenshots
  clearly show browser/OS/device name plus the SUT's localhost URL.
- Cover the web frontend on Chrome, Firefox, and Safari (or Android Chrome).
- Expo Go on a real phone is a valid platform and may replace one of the three required browsers
  (e.g. in place of Safari) — it satisfies a required slot, it is not bonus-only.
- Every screenshot must overlay the username in the form of the student email.

## Agent Skill (10 pts, §7)

Build an Agent Skill (this one) that applies the checklist and usability-evaluation activities so
it is reusable on future screens/flows. Submit it with a demonstration video (YouTube link) showing
end-to-end use on one complete screen or flow.

## Allowed Tools and Bloom-AI Level (§8)

Any AI tool (declared in the AI Audit Report); a BrowserStack or LambdaTest trial. Required level:
G9.3 (Analyse) and G9.4 (Collaborate).

## AI Audit Report (§9, mandatory appendix)

For every AI interaction: tool name, date/time, exact prompt, AI output. If AI was not used for
some part, that must still be stated explicitly ("I do not use any AI help in this exercise" only
applies if truly no AI was used anywhere).

## AI Critique (§10, mandatory, 200–300 words)

Address: where the AI was wrong/biased/incomplete; why it failed to catch the issue; what
collaboration principle was learned.

## Anti-AI-Cheat Constraints (§11)

The 7-participant list (name + masked Zalo/phone) and the cross-platform screenshots (student ID +
full name visible) must be genuine, not AI-generated or fabricated. TAs verify both.

## Git Commit Log (§12)

One commit per testing-procedure step (checklist design, checklist execution, bug logging, each
usability session, the analysis). Provide the log as a text file (e.g. `git log --stat`).

## Submission (§14)

Zip named `<StudentID>_HW03_AI_GUIUsability_<SelfAssessedGrade>.zip` containing: main report
(Markdown + PDF), bug report with GitHub Issue screenshots, AI Critique + AI Audit Report
(Markdown + PDF), Git commit log (text), Excel checklist (>40 items) + test summary, usability
session evidence + 7-participant table, cross-platform screenshots, and a `README.md` with the
self-assessment table and a test summary (screens/flows tested, items designed/executed/passed/
failed, bug count, participant count, demo videos).

## Integrity and Submission

Never fabricate execution, status, bugs, screenshots, participants, evidence, or GitHub Issue
links. Bug reporting requires an observable reproduced failure against a documented expected
result. Preserve AI prompts/outputs, human review/corrections, gap analysis, real evidence, commit
history, and required demo/submission materials. Late submission is not permitted; missing any
required document is 0 points; copying between students (including prompts) is 0 for both parties.
