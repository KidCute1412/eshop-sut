# HW04 - Automation Testing Main Report

- Student: Nguyen Thanh Tien, Student ID 23127539
- SUT: EShop (`https://github.com/ttbhanh/eshop-sut`)
- Working repository / branch: [KidCute1412/eshop-sut - 23127539-NguyenThanhTien](https://github.com/KidCute1412/eshop-sut/tree/23127539-NguyenThanhTien)
- Scope: Automate the same HW02 web features from Pools A/B/C: FR-01 Account registration, FR-07 Shopping cart, and FR-17 Coupon management.

## Submission Scope

| Feature | Selected Scope       | Main Artifacts                                                                                                                                                                                                                                                                               |
| ------- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| FR-01   | Account registration | [test-cases.md](FR-01/test-cases.md), [data/register-cases.json](FR-01/data/register-cases.json), [tests/fr-01-register.spec.js](FR-01/tests/fr-01-register.spec.js), [ai-gap-analysis.md](FR-01/ai-gap-analysis.md), [bug-report.md](FR-01/bug-report.md), [ai-audit.md](FR-01/ai-audit.md) |
| FR-07   | Shopping cart        | [test-cases.md](FR-07/test-cases.md), [data/cart-cases.json](FR-07/data/cart-cases.json), [tests/fr-07-cart.spec.js](FR-07/tests/fr-07-cart.spec.js), [ai-gap-analysis.md](FR-07/ai-gap-analysis.md), [bug-report.md](FR-07/bug-report.md), [ai-audit.md](FR-07/ai-audit.md)                 |
| FR-17   | Coupon management    | [test-cases.md](FR-17/test-cases.md), [data/coupon-cases.json](FR-17/data/coupon-cases.json), [tests/fr-17-coupons.spec.js](FR-17/tests/fr-17-coupons.spec.js), [ai-gap-analysis.md](FR-17/ai-gap-analysis.md), [bug-report.md](FR-17/bug-report.md), [ai-audit.md](FR-17/ai-audit.md)       |

## Method Summary

1. Reused the HW02 feature selection: FR-01 from Pool A, FR-07 from Pool B, and FR-17 from Pool C.
2. Selected at least 12 test cases per feature and mapped each case to an external JSON data row.
3. Built Playwright automation in `reports/HW4`, with Chromium, Firefox, and WebKit projects.
4. Reviewed and corrected AI-generated/first-pass automation for fragile selectors, weak waits, missing SPA-state handling, and incorrect assumptions.
5. Ran the full suite against real local backend, web frontend, and admin frontend servers.
6. Generated a Playwright HTML report with an automated `Run by: 23127539` plus ISO timestamp stamp.

## Task 1 - AI-Generated Automation Scripts

- Total design-time cases automated: **41**
- Total browser executions: **123**
- Final result: **84 Passed / 39 Failed**
- Data-driven validation: Passed for FR-01, FR-07, and FR-17 using `validate_test_data.py`.
- HTML report validation: Passed using `validate_html_report.py`.

### FR-01 - Account Registration

- Cases automated: 15
- Browser executions: 45
- Result: **33 Passed / 12 Failed**
- Failures: `FR01-DT-006`, `FR01-DT-011`, `FR01-BVA-009`, and `FR01-BVA-010` on Chromium, Firefox, and WebKit.
- Confirmed bugs: duplicate email registration is accepted; documented special-character passwords using `!` or `@` are rejected by client-side validation.

### FR-07 - Shopping Cart

- Cases automated: 14
- Browser executions: 42
- Result: **21 Passed / 21 Failed**
- Failures: `FR07-DT-004`, `FR07-DT-005`, `FR07-DT-006`, `FR07-DT-010`, `FR07-DT-011`, `FR07-BVA-002`, and `FR07-BVA-003` on Chromium, Firefox, and WebKit.
- Confirmed bugs: duplicate product rows are not consolidated, delete lacks confirmation, the header label is `Giá` instead of `Đơn giá`, the total label is `Tổng tạm tính` instead of `Tổng cộng`, and cart quantity `+` / `-` controls are missing.

### FR-17 - Coupon Management

- Cases automated: 12
- Browser executions: 36
- Result: **30 Passed / 6 Failed**
- Failures: `FR17-BVA-001` and `FR17-BVA-002` on Chromium, Firefox, and WebKit.
- Confirmed bugs: coupon creation accepts `discount_value = 0` and `min_order_amount = -1` even though the FR-17 requirement requires `discount_value > 0` and `min_order_amount >= 0`. `FR17-BVA-003` passes because the UI blocks `max_uses_per_user = 0` through native validation.

## Bug Report

Nine bugs were confirmed:

- `BUG-HW04-FR01-001`: duplicate email registration is accepted. See [FR-01/bug-report.md](FR-01/bug-report.md).
- `BUG-HW04-FR01-002`: documented special-character passwords are rejected by registration UI. See [FR-01/bug-report.md](FR-01/bug-report.md).
- `BUG-HW04-FR07-001` through `BUG-HW04-FR07-005`: shopping-cart requirement defects. See [FR-07/bug-report.md](FR-07/bug-report.md).
- `BUG-HW04-FR17-001` and `BUG-HW04-FR17-002`: coupon numeric lower-bound defects. See [FR-17/bug-report.md](FR-17/bug-report.md).

The GitHub Issue link is pending because no authenticated GitHub issue creation was available in this local run.

## Task 2 - Demo Videos

The required YouTube demo videos were recorded:

- [demo-video-link](https://youtu.be/mN1KJbr8aFo): main HW04 automation demo focused on FR-01 Account Registration
- [agent-skill-demo-link](https://youtu.be/k_f_I4ccgjo): Agent Skill demo for `.agents/skills/automation-testing/`

## Agent Skill

- Skill location: `.agents/skills/automation-testing/`
- Skill purpose: the `automation-testing` skill was created to guide AI-assisted HW04 work in an auditable way. It prevents the automation task from becoming a one-shot code generation request by separating the work into requirement review, test-case selection, data-driven script generation, human review, multi-browser execution, reporting, and final packaging.
- Workflow guidance: `SKILL.md` defines the phases used in this submission: reuse the selected HW02 cases, convert them into Playwright tests, keep test data in external JSON files, use multiple assertion patterns, run Chromium/Firefox/WebKit, preserve AI audit evidence, and document every human correction in `ai-gap-analysis.md`.
- Reference files: the skill includes focused reference documents under `.agents/skills/automation-testing/references/`, including assignment requirements, EShop-specific selector risks, data-driven/assertion guidance, multi-browser reporting rules, and a human-review checklist. These references were used to keep expected results tied to `README.md` and `api_specification.md` rather than to the current SUT behavior.
- Templates and assets: `.agents/skills/automation-testing/assets/` provides reusable report templates for test cases, automation report, bug report, AI gap analysis, AI critique, README, and main report. The HW04 report structure follows these templates while adapting content to FR-01, FR-07, and FR-17.
- Helper scripts: `.agents/skills/automation-testing/scripts/` contains validation and support scripts such as `validate_test_data.py`, `validate_html_report.py`, `compute_test_summary.py`, `check_commit_rule.py`, `append_ai_audit.py`, and `init_feature_workspace.py`.
- Validation use: `validate_test_data.py` was run for the feature folders to confirm that the Playwright specs use external JSON data instead of hardcoded inline test-data arrays. The HTML report workflow also uses `run-with-report-stamp.js` and the skill's report validation rule to ensure the generated report contains `Run by: 23127539` with an ISO timestamp.
- Human-review impact: the skill directly influenced several corrections. For FR-01, it helped preserve requirement-based password expectations and keep real failures for duplicate email and documented special characters. For FR-07, it led to stronger assertions for duplicate product quantity, delete confirmation, exact headers, total label, and quantity controls. For FR-17, it replaced weak BVA choices with lower-bound tests for `discount_value`, `min_order_amount`, and `max_uses_per_user`.
- Integrity rule: the most important rule enforced by the skill is that the AI may draft automation, but the human reviewer owns the final oracle. A test is not changed to match buggy SUT behavior just to pass; failing assertions are kept when they expose real requirement violations.
- Demo support: the Agent Skill demo is available at [agent-skill-demo-link](https://youtu.be/k_f_I4ccgjo), showing the skill folder, references, scripts, validators, and concrete review examples.

## AI Audit Report

Per-feature AI audit logs preserve prompt text and raw AI output in a consistent appendix format:

- [FR-01/ai-audit.md](FR-01/ai-audit.md)
- [FR-07/ai-audit.md](FR-07/ai-audit.md)
- [FR-17/ai-audit.md](FR-17/ai-audit.md)

## AI Critique

See [ai-critique.md](ai-critique.md).

## GitHub Link

- Working repository / branch: [KidCute1412/eshop-sut - 23127539-NguyenThanhTien](https://github.com/KidCute1412/eshop-sut/tree/23127539-NguyenThanhTien)

## Git Commit Log

See [git-commit-log.txt](git-commit-log.txt). 

## Self-Assessment

| No.       | Criteria            |   Grade | Self-Assessed Grade |
| --------- | ------------------- | ------: | ------------------: |
| 1         | Task 1 - Feature A  |      25 |                  25 |
| 1         | Task 1 - Feature B  |      25 |                  25 |
| 1         | Task 1 - Feature C  |      25 |                  25 |
| 2         | Task 2 - Demo video |      15 |                  15 |
| 3         | Agent Skills        |      10 |                  10 |
| **Total** |                     | **100** |             **100** |
