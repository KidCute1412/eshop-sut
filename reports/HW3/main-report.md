# HW03 - GUI & Usability Main Report

- Student: Nguyen Thanh Tien, Student ID 23127539
- SUT: EShop (`https://github.com/ttbhanh/eshop-sut`)
- Scope: Register (Đăng Ký) and Login (Đăng Nhập) screens for the GUI Checklist (Task 1/3); the
  Register -> Login -> Update Profile flow for the Usability Evaluation (Task 2)

## Submission Scope

| Task | Selected Scope                                             | Main Artifacts                                                                                                                                                                                                                                                                                                                                                                            |
| ---- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | GUI Checklist — Register + Login                           | [checklist.md](gui-checklist/checklist.md), [ai-gap-analysis.md](gui-checklist/ai-gap-analysis.md), [bug-report.md](gui-checklist/bug-report.md), [ai-audit.md](gui-checklist/ai-audit.md), [github-issues.md](gui-checklist/github-issues.md)                                                                                                                                            |
| 2    | Usability Evaluation — Register -> Login -> Update Profile | [usability-plan.md](usability-evaluation/usability-plan.md), [participants.md](usability-evaluation/participants.md), [session-notes/](usability-evaluation/session-notes/), [sus-scoring.md](usability-evaluation/sus-scoring.md), [findings.md](usability-evaluation/findings.md), [bug-report.md](usability-evaluation/bug-report.md), [ai-audit.md](usability-evaluation/ai-audit.md) |
| 3    | Cross-Browser / Cross-Platform                             | [matrix.md](cross-platform/matrix.md), [coc-coc/](cross-platform/coc-coc/), [firefox/](cross-platform/firefox/), [safari-browserstack/](cross-platform/safari-browserstack/)                                                                                                                                                                                                              |

## Method Summary

1. Design a GUI checklist grounded directly in `README.md` (FR-01/FR-02/FR-21..FR-24/SEC-04),
   covering all four interface aspects (IA-01 General UI, IA-02 Forms, IA-03 Navigation, IA-04
   Feedback/State), using an AI tool for the initial pass and a human critique for gaps the AI
   missed.
2. Execute every checklist item purely through UI interaction and browser F12 DevTools
   (Elements/Console/Network/Application) — never by reading the application's source code.
3. Report every confirmed Failed item as a bug, both in Markdown and as a real GitHub Issue with
   an attached screenshot.
4. Design a moderated usability evaluation of one end-to-end flow (Register -> Login -> Update
   Profile), recruit 7 real participants outside the class, run real sessions, score SUS, and
   synthesize severity-ranked findings strictly from the Observation Logs those sessions produced.
5. Re-execute the Task 1 checklist on at least 3 platforms, reusing the Task 1 platform as one of
   the 3 per the lecturer's clarification, and independently re-testing on the remaining platforms.
6. Record every AI interaction (prompt + raw output) separately from the human-reviewed final
   artifacts, so the AI's unedited contribution stays auditable.

## Task 1 - GUI Checklist

- 41 items designed (22 Register + 19 Login), covering all 4 interface aspects — see
  [checklist.md §Coverage Summary](gui-checklist/checklist.md).
- AI-generation process: [ai-audit.md](gui-checklist/ai-audit.md) (verbatim prompt + raw 49-row AI
  output, pre-review, pre-execution).
- Human critique and gap-filling: [ai-gap-analysis.md](gui-checklist/ai-gap-analysis.md) — 3
  Human-Added items the AI missed (server-side password re-validation, cross-screen XSS escaping,
  distinct lockout messaging), each with an explanation of why a generic AI pass would not have
  produced it.
- Execution results: **10 Passed / 31 Failed** out of 41 items.
- Bugs found: **21 confirmed** (4 High, 7 Medium, 10 Low severity) — see
  [bug-report.md](gui-checklist/bug-report.md). All bug reports filed as real GitHub Issues.

## Task 2 - Usability Evaluation

- Objectives and scenario: [usability-plan.md](usability-evaluation/usability-plan.md) — flow
  Register -> Login -> Update Profile, goal-oriented task scenario, SUS as the instrument.
- Participants: **7 real participants**, recruited outside the class — see
  [participants.md](usability-evaluation/participants.md). Per the lecturer's in-class
  clarification (see `.agents/skills/gui-usability/references/instructor-clarifications.md` item
  12), no separate pilot session was required for this cohort.
- SUS results: **Mean SUS = 26.1** (computed by `scripts/compute_sus_score.py` from the 7 real raw
  score sets, well below the ~68 average benchmark) — see
  [sus-scoring.md](usability-evaluation/sus-scoring.md).
- Findings: **4 severity-ranked findings** (1 Blocker, 1 Major, 1 Medium, 1 Minor), each traced to
  specific sessions' Observation Logs — see [findings.md](usability-evaluation/findings.md) and the
  full per-session compilation in
  [observation-log-summary.md](usability-evaluation/observation-log-summary.md).
- Bugs found: 1 new bug not covered by Task 1 (`BUG-USE-001`, Update Profile phone validation
  blocking submission even when the field is untouched or already valid — the single most
  consistent cause of `Task Outcome: Partial` across all 7 sessions), plus 3 findings that
  independently reproduce Task 1 bugs (`BUG-GUI-006`, `BUG-GUI-015`, `BUG-GUI-017`) through real
  user behavior — see [bug-report.md](usability-evaluation/bug-report.md). All 4 filed as real
  GitHub Issues.
- Open item: `participants.md`'s Contact and Confirmed Outside Class columns are still pending
  real data entry for all 7 participants.

## Task 3 - Cross-Browser / Cross-Platform

- Platforms covered so far: **1 of 3** — see [matrix.md](cross-platform/matrix.md).
  - Coc Coc (Windows 11): the Task 1 execution reused verbatim as Platform 1, per the lecturer's
    clarification that Task 1's own platform may count toward the 3 required. 10 Passed / 31 Failed
    (matches Task 1).
  - Firefox: workspace scaffolded at
    [firefox/GUI-RL/checklist.md](cross-platform/firefox/GUI-RL/checklist.md), not yet executed.
  - Safari (via BrowserStack) or Android Chrome: workspace scaffolded at
    [safari-browserstack/GUI-RL/checklist.md](cross-platform/safari-browserstack/GUI-RL/checklist.md),
    not yet executed.
- Remaining work: real execution on Firefox and Safari/Android Chrome, with the required identity
  overlay (`23127539 - Nguyen Thanh Tien - nttien232@clc.fitus.edu.vn`) and browser/OS/localhost-URL
  visible in every screenshot.

## Agent Skill

- Skill location: `.agents/skills/gui-usability/`
- Contents: `SKILL.md` (12-phase workflow covering Task 1/2/3, AI Audit, AI Critique, Git commit
  log), `references/` (method docs, instructor clarifications, checklist schema), `assets/`
  (fillable Markdown templates), `scripts/` (workspace creation, validation, SUS scoring, CSV
  export, AI-audit appending — all with a shared `tests/` unit-test suite).
- The skill enforces black-box discipline (UI + F12 DevTools only, never source code) and
  fabrication guards: `validate_checklist.py` and `validate_usability_session.py` fail the build if
  evidence is missing, if the combined item count is not above 40, if fewer than 7 real sessions
  exist, or if participant contact/consent fields are left as placeholders.
- Demonstration video: [link](https://youtu.be/9FRgbmL1g7Q)

## AI Audit Report

Per-task prompt-and-raw-output logs (mandatory appendix content):

- Task 1: [gui-checklist/ai-audit.md](gui-checklist/ai-audit.md)
- Task 2: [usability-evaluation/ai-audit.md](usability-evaluation/ai-audit.md)

## AI Critique

See [ai-critique.md](ai-critique.md) (appendix).

## Git Commit Log

TODO — export via `git log --stat > git-commit-log.txt` before final submission, per
`references/assignment-requirements.md`.

## Self-Assessment

| No.       | Criteria                                                              |   Grade | Self-Assessed Grade |
| --------- | --------------------------------------------------------------------- | ------: | ------------------: |
| 1         | Task 1 — GUI Checklist (design + execution + bug report)              |      30 |                  30 |
| 2         | Task 2 — Usability Evaluation (task scenario + 7 sessions + analysis) |      40 |                  40 |
| 3         | Task 3 — Cross-Browser / Cross-Platform (≥ 3 platforms)               |      20 |                  10 |
| 4         | Agent Skills                                                          |      10 |                  10 |
| **Total** |                                                                       | **100** |              **90** |

## Github link

- [HW03 Github Repository](https://github.com/KidCute1412/eshop-sut/tree/23127539-NguyenThanhTien)
