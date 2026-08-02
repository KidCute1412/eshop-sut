# HW03 - GUI & Usability — Submission README

- Student: Nguyen Thanh Tien, Student ID 23127539, nttien232@clc.fitus.edu.vn
- SUT: EShop (`https://github.com/ttbhanh/eshop-sut`)
- Full report: [main-report.md](main-report.md)
- AI Critique: [ai-critique.md](ai-critique.md)

## Self-Assessment

| No.       | Criteria                                                              |   Grade | Self-Assessed Grade |
| --------- | --------------------------------------------------------------------- | ------: | ------------------: |
| 1         | Task 1 — GUI Checklist (design + execution + bug report)              |      30 |                  30 |
| 2         | Task 2 — Usability Evaluation (task scenario + 7 sessions + analysis) |      40 |                  40 |
| 3         | Task 3 — Cross-Browser / Cross-Platform (≥ 3 platforms)               |      20 |                  10 |
| 4         | Agent Skills                                                          |      10 |                  10 |
| **Total** |                                                                       | **100** |              **90** |

## Test Summary Report

- **Screens / flows tested:**
  - Task 1 / Task 3 (GUI Checklist): 2 screens — Register (Đăng Ký), Login (Đăng Nhập)
  - Task 2 (Usability Evaluation): 1 end-to-end flow — Register -> Login -> Update Profile
- **Checklist items:**
  - Designed: **41** (22 Register + 19 Login), covering all 4 interface aspects (IA-01..IA-04)
  - Executed (Task 1 baseline, Coc Coc): **41 / 41**
  - Passed: **10**
  - Failed: **31**
- **Cross-platform re-execution (Task 3):**
  - Coc Coc (Platform 1, reused from Task 1 baseline): 41/41 executed, 10 Passed / 31 Failed
  - Firefox (Platform 2): 41/41 executed, 10 Passed / 31 Failed (no new platform-specific bugs)
  - Safari via BrowserStack / Android Chrome (Platform 3): not yet executed
- **Bugs found:**
  - Task 1: **21 confirmed bugs** (4 High, 7 Medium, 10 Low severity), all filed as real GitHub
    Issues — see [gui-checklist/bug-report.md](gui-checklist/bug-report.md)
  - Task 2: **1 new bug** not covered by Task 1 (`BUG-USE-001`, Update Profile phone validation),
    plus 3 findings that independently reproduce Task 1 bugs through real user behavior — see
    [usability-evaluation/bug-report.md](usability-evaluation/bug-report.md)
  - Total unique confirmed bugs across the assignment: **22**
- **Participants (Task 2):** **7 real participants**, recruited outside the class, each with a
  completed session (Observation Log, SUS responses, probe-question answers) — see
  [usability-evaluation/participants.md](usability-evaluation/participants.md). No separate pilot
  session was required for this cohort per the lecturer's in-class clarification.
- **SUS result:** Mean SUS = **26.1** / 100 (well below the ~68 average benchmark) — see
  [usability-evaluation/sus-scoring.md](usability-evaluation/sus-scoring.md).
- **Demo videos:**
  - Agent Skill demonstration: [link](https://youtu.be/9FRgbmL1g7Q)
  - Session recordings (Task 2): see
    [usability-evaluation/evidence/record-evidece.txt](usability-evaluation/evidence/record-evidece.txt)
    for the recordings folder link

## Deliverables Index

- Main report: [main-report.md](main-report.md)
- AI Critique: [ai-critique.md](ai-critique.md)
- Task 1 — GUI Checklist: [gui-checklist/](gui-checklist/) (`checklist.md`, `checklist.xlsx`,
  `ai-gap-analysis.md`, `bug-report.md`, `ai-audit.md`, `github-issues.md`)
- Task 2 — Usability Evaluation: [usability-evaluation/](usability-evaluation/)
  (`usability-plan.md`, `participants.md`, `session-notes/`, `sus-scoring.md`, `findings.md`,
  `bug-report.md`, `ai-audit.md`)
- Task 3 — Cross-Platform: [cross-platform/](cross-platform/) (`matrix.md`, `coc-coc/`,
  `firefox/`, `safari-browserstack/`)
- Agent Skill: `.agents/skills/gui-usability/`
- Git commit log: TODO (`git-commit-log.txt`, not yet exported)

## Known Open Items

- Task 3: Safari (via BrowserStack) or Android Chrome execution still pending (Platform 3 of 3).
