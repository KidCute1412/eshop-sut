# HW04 - Automation Testing - Submission README

- Student: Nguyen Thanh Tien, Student ID 23127539, nttien232@clc.fitus.edu.vn
- SUT: EShop (`https://github.com/ttbhanh/eshop-sut`)
- Full report: [main-report.md](main-report.md)
- AI Critique: [ai-critique.md](ai-critique.md)
- Final HTML report: [reports/html-23127539/index.html](reports/html-23127539/index.html)

## Self-Assessment

| No. | Criteria | Grade | Self-Assessed Grade |
| --- | --- | ---: | ---: |
| 1 | Task 1 - Feature A (FR-01 Account registration) | 25 | 21 |
| 1 | Task 1 - Feature B (FR-07 Shopping cart) | 25 | 25 |
| 1 | Task 1 - Feature C (FR-17 Coupon management) | 25 | 25 |
| 2 | Task 2 - Demo video | 15 | 0 |
| 3 | Agent Skills | 10 | 10 |
| **Total** | | **100** | **81** |

## Test Summary Report

- **Features automated:** 3 - FR-01, FR-07, FR-17
- **Design-time test cases automated:** 39 (15 FR-01 + 12 FR-07 + 12 FR-17)
- **Browser executions:** 117 (Chromium, Firefox, WebKit)
- **Passed:** 105
- **Failed:** 12
- **Bugs confirmed:** 2 (`BUG-HW04-FR01-001`, `BUG-HW04-FR01-002`)
- **HTML report validation:** Passed; report shows `Run by: 23127539` with ISO timestamp
- **Demo video link:** Pending recording/upload by the student

## Deliverables Index

- Main report: [main-report.md](main-report.md)
- Automation report: [automation-report.md](automation-report.md)
- AI Critique: [ai-critique.md](ai-critique.md)
- FR-01: [FR-01/](FR-01/) (`test-cases.md`, `data/`, `tests/`, `ai-audit.md`, `ai-gap-analysis.md`, `bug-report.md`)
- FR-07: [FR-07/](FR-07/) (`test-cases.md`, `data/`, `tests/`, `ai-audit.md`, `ai-gap-analysis.md`, `bug-report.md`)
- FR-17: [FR-17/](FR-17/) (`test-cases.md`, `data/`, `tests/`, `ai-audit.md`, `ai-gap-analysis.md`, `bug-report.md`)
- Playwright config and runner: [playwright.config.js](playwright.config.js), [scripts/run-with-report-stamp.js](scripts/run-with-report-stamp.js)
- HTML report: [reports/html-23127539/](reports/html-23127539/)
- Git commit log: [git-commit-log.txt](git-commit-log.txt)
- Demo video script: [demo-video-script.md](demo-video-script.md)
- Agent Skill: `.agents/skills/automation-testing/`

## Known Open Items

- Record and upload the required Vietnamese demo video.
- Create the real GitHub Issue for `BUG-HW04-FR01-001` and replace the pending link.
- Build a public Git history with at least 8 commits touching `.spec.js` files across at least 4 days.
- Export Markdown reports to PDF for final Moodle packaging.
