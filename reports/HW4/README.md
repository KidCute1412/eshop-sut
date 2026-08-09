# HW04 - Automation Testing - Submission README

- Student: Nguyen Thanh Tien, Student ID 23127539, nttien232@clc.fitus.edu.vn
- SUT: EShop (`https://github.com/ttbhanh/eshop-sut`)
- Working repository / branch: [KidCute1412/eshop-sut - 23127539-NguyenThanhTien](https://github.com/KidCute1412/eshop-sut/tree/23127539-NguyenThanhTien)
- Framework: Playwright
- Browsers: Chromium, Firefox, WebKit
- Full report: [main-report.md](main-report.md)
- AI Critique: [ai-critique.md](ai-critique.md)
- Final HTML report: [reports/html-23127539/index.html](reports/html-23127539/index.html)
- Demo video: [https://youtu.be/mN1KJbr8aFo](https://youtu.be/mN1KJbr8aFo)
- Agent Skill demo video: [https://youtu.be/k_f_I4ccgjo](https://youtu.be/k_f_I4ccgjo)

## Self-Assessment

| No. | Criteria | Grade | Self-Assessed Grade |
| --- | --- | ---: | ---: |
| 1 | Task 1 - Feature A (FR-01 Account registration) | 25 | 25 |
| 1 | Task 1 - Feature B (FR-07 Shopping cart) | 25 | 25 |
| 1 | Task 1 - Feature C (FR-17 Coupon management) | 25 | 25 |
| 2 | Task 2 - Demo video | 15 | 15 |
| 3 | Agent Skills | 10 | 10 |
| **Total** | | **100** | **100** |

## Test Summary Report

- **Features automated:** 3 - FR-01, FR-07, FR-17
- **Design-time test cases automated:** 41 (15 FR-01 + 14 FR-07 + 12 FR-17)
- **Browser executions:** 123 (Chromium, Firefox, WebKit)
- **Passed:** 84
- **Failed:** 39
- **Bugs confirmed:** 9 (`BUG-HW04-FR01-001`, `BUG-HW04-FR01-002`, `BUG-HW04-FR07-001` through `BUG-HW04-FR07-005`, `BUG-HW04-FR17-001`, `BUG-HW04-FR17-002`)
- **HTML report validation:** Passed; report shows `Run by: 23127539` with ISO timestamp.

## Feature Results

| Feature | Test Cases | Browser Executions | Passed | Failed | Main Findings |
| --- | ---: | ---: | ---: | ---: | --- |
| FR-01 Account registration | 15 | 45 | 33 | 12 | Duplicate email is accepted; documented special-character passwords using `!` or `@` are rejected by the UI. |
| FR-07 Shopping cart | 14 | 42 | 21 | 21 | Duplicate product rows, missing delete confirmation, wrong header/total labels, and missing quantity controls. |
| FR-17 Coupon management | 12 | 36 | 30 | 6 | Coupon creation accepts `discount_value = 0` and `min_order_amount = -1`. |

## Deliverables Index

- Main report: [main-report.md](main-report.md)
- AI Critique: [ai-critique.md](ai-critique.md)
- Git commit log: [git-commit-log.txt](git-commit-log.txt)
- Working repository / branch: [KidCute1412/eshop-sut - 23127539-NguyenThanhTien](https://github.com/KidCute1412/eshop-sut/tree/23127539-NguyenThanhTien)
- Playwright config: [playwright.config.js](playwright.config.js)
- Playwright runner/stamper: [scripts/run-with-report-stamp.js](scripts/run-with-report-stamp.js)
- HTML report: [reports/html-23127539/](reports/html-23127539/)
- FR-01: [FR-01/](FR-01/) (`test-cases.md`, `data/`, `tests/`, `ai-audit.md`, `ai-gap-analysis.md`, `bug-report.md`)
- FR-07: [FR-07/](FR-07/) (`test-cases.md`, `data/`, `tests/`, `ai-audit.md`, `ai-gap-analysis.md`, `bug-report.md`)
- FR-17: [FR-17/](FR-17/) (`test-cases.md`, `data/`, `tests/`, `ai-audit.md`, `ai-gap-analysis.md`, `bug-report.md`)
- Agent Skill: `.agents/skills/automation-testing/`

## Agent Skill Summary

The custom `automation-testing` Agent Skill guided this submission through HW04-specific phases: reuse HW02 cases, generate data-driven Playwright specs, review selectors and assertions, run multi-browser tests, validate data/report artifacts, preserve AI audit logs, and document real bugs. Its integrity rules were used to keep expected results tied to requirements instead of changing oracles to match buggy SUT behavior. The Agent Skill demo video is available at [https://youtu.be/k_f_I4ccgjo](https://youtu.be/k_f_I4ccgjo).
