# HW04 - Automation Testing Main Report

- Student: Nguyen Thanh Tien, Student ID 23127539
- SUT: EShop (`https://github.com/ttbhanh/eshop-sut`)
- Scope: Automate the same HW02 web features from Pools A/B/C: FR-01 Account registration, FR-07 Shopping cart, and FR-17 Coupon management.

## Submission Scope

| Feature | Selected Scope | Main Artifacts |
| --- | --- | --- |
| FR-01 | Account registration | [test-cases.md](FR-01/test-cases.md), [data/register-cases.json](FR-01/data/register-cases.json), [tests/fr-01-register.spec.js](FR-01/tests/fr-01-register.spec.js), [ai-gap-analysis.md](FR-01/ai-gap-analysis.md), [bug-report.md](FR-01/bug-report.md), [ai-audit.md](FR-01/ai-audit.md) |
| FR-07 | Shopping cart | [test-cases.md](FR-07/test-cases.md), [data/cart-cases.json](FR-07/data/cart-cases.json), [tests/fr-07-cart.spec.js](FR-07/tests/fr-07-cart.spec.js), [ai-gap-analysis.md](FR-07/ai-gap-analysis.md), [bug-report.md](FR-07/bug-report.md), [ai-audit.md](FR-07/ai-audit.md) |
| FR-17 | Coupon management | [test-cases.md](FR-17/test-cases.md), [data/coupon-cases.json](FR-17/data/coupon-cases.json), [tests/fr-17-coupons.spec.js](FR-17/tests/fr-17-coupons.spec.js), [ai-gap-analysis.md](FR-17/ai-gap-analysis.md), [bug-report.md](FR-17/bug-report.md), [ai-audit.md](FR-17/ai-audit.md) |

## Method Summary

1. Reused the HW02 feature selection: FR-01 from Pool A, FR-07 from Pool B, and FR-17 from Pool C.
2. Selected 12 test cases per feature and mapped each case to an external JSON data row.
3. Built Playwright automation in `reports/HW4`, with Chromium, Firefox, and WebKit projects.
4. Reviewed and corrected AI-generated/first-pass automation for fragile selectors, weak waits, missing SPA-state handling, and incorrect assumptions.
5. Ran the full suite against real local backend, web frontend, and admin frontend servers.
6. Generated a Playwright HTML report with an automated `Run by: 23127539` plus ISO timestamp stamp.

## Task 1 - AI-Generated Automation Scripts

- Total design-time cases automated: **39**
- Total browser executions: **117**
- Final result: **105 Passed / 12 Failed**
- Data-driven validation: Passed for FR-01, FR-07, and FR-17 using `validate_test_data.py`.
- HTML report validation: Passed using `validate_html_report.py`.

### FR-01 - Account Registration

- Cases automated: 15
- Browser executions: 45
- Result: **33 Passed / 12 Failed**
- Failures: `FR01-DT-006`, `FR01-DT-011`, `FR01-BVA-009`, and `FR01-BVA-010` on Chromium, Firefox, and WebKit.
- Confirmed bugs: duplicate email registration is accepted; documented special-character passwords using `!` or `@` are rejected by client-side validation.

### FR-07 - Shopping Cart

- Cases automated: 12
- Browser executions: 36
- Result: **36 Passed / 0 Failed**
- Human review highlight: initial reload-based navigation lost React cart context; final test uses SPA link navigation.

### FR-17 - Coupon Management

- Cases automated: 12
- Browser executions: 36
- Result: **36 Passed / 0 Failed**
- Human review highlight: final fixture uses the actual seeded admin password `Admin123!`; no edit coupon flow is automated because the UI does not implement one.

## Automation Report

See [automation-report.md](automation-report.md) for the browser matrix, assertion pattern coverage, and final failure summary.

## Bug Report

Two bugs were confirmed:

- `BUG-HW04-FR01-001`: duplicate email registration is accepted. See [FR-01/bug-report.md](FR-01/bug-report.md).
- `BUG-HW04-FR01-002`: documented special-character passwords are rejected by registration UI. See [FR-01/bug-report.md](FR-01/bug-report.md).

The GitHub Issue link is pending because no authenticated GitHub issue creation was available in this local run.

## Task 2 - Demo Video

The required YouTube demo video is still pending recording/upload by the student. A Vietnamese narration script is prepared in [demo-video-script.md](demo-video-script.md). The script includes the required `whoami` and `hostname` authorship evidence step, multi-browser run, HTML report walkthrough, and one real fix from human review.

## Agent Skill

- Skill location: `.agents/skills/automation-testing/`
- The skill provides the HW04 workflow, assignment references, templates, validators, and helper scripts.
- This run used that skill's workflow and validators.

## AI Audit Report

Per-feature AI audit logs:

- [FR-01/ai-audit.md](FR-01/ai-audit.md)
- [FR-07/ai-audit.md](FR-07/ai-audit.md)
- [FR-17/ai-audit.md](FR-17/ai-audit.md)

## AI Critique

See [ai-critique.md](ai-critique.md).

## Git Commit Log

See [git-commit-log.txt](git-commit-log.txt). The current local work does not yet satisfy the assignment's 8 spec-touching commits over 4 days rule; this must be completed with real commits over real dates before final submission.

## Self-Assessment

| No. | Criteria | Grade | Self-Assessed Grade |
| --- | --- | ---: | ---: |
| 1 | Task 1 - Feature A | 25 | 21 |
| 1 | Task 1 - Feature B | 25 | 25 |
| 1 | Task 1 - Feature C | 25 | 25 |
| 2 | Task 2 - Demo video | 15 | 0 |
| 3 | Agent Skills | 10 | 10 |
| **Total** | | **100** | **81** |

## Github Link

- Pending public repository link / branch confirmation.
