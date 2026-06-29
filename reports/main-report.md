# HW02 - Domain Testing Main Report

## Submission Scope

This report summarizes the Domain Testing and Boundary Value Analysis work for HW02 on the EShop SUT. The report includes the selected four-pool feature set and the additional completed FR-01 Pool A artifact.

| Pool | Selected Feature | Feature Name                     | Main Artifacts                                                                                                                                                                                                                                                                                     |
| ---- | ---------------- | -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A    | FR-01            | Account registration             | [requirement-analysis.md](FR-01/requirement-analysis.md), [domain-testing.md](FR-01/domain-testing.md), [boundary-value-analysis.md](FR-01/boundary-value-analysis.md), [test-cases.md](FR-01/test-cases.md), [bug-report.md](FR-01/bug-report.md), [ai-gap-analysis.md](FR-01/ai-gap-analysis.md) |
| A    | FR-02            | Login and account lockout        | [requirement-analysis.md](FR-02/requirement-analysis.md), [domain-testing.md](FR-02/domain-testing.md), [boundary-value-analysis.md](FR-02/boundary-value-analysis.md), [test-cases.md](FR-02/test-cases.md), [bug-report.md](FR-02/bug-report.md), [ai-gap-analysis.md](FR-02/ai-gap-analysis.md) |
| B    | FR-07            | Shopping cart                    | [requirement-analysis.md](FR-07/requirement-analysis.md), [domain-testing.md](FR-07/domain-testing.md), [boundary-value-analysis.md](FR-07/boundary-value-analysis.md), [test-cases.md](FR-07/test-cases.md), [bug-report.md](FR-07/bug-report.md), [ai-gap-analysis.md](FR-07/ai-gap-analysis.md) |
| C    | FR-17            | Coupon management CRUD           | [requirement-analysis.md](FR-17/requirement-analysis.md), [domain-testing.md](FR-17/domain-testing.md), [boundary-value-analysis.md](FR-17/boundary-value-analysis.md), [test-cases.md](FR-17/test-cases.md), [bug-report.md](FR-17/bug-report.md), [ai-gap-analysis.md](FR-17/ai-gap-analysis.md) |
| D    | FR-20            | Login and account lockout mobile | [requirement-analysis.md](FR-20/requirement-analysis.md), [domain-testing.md](FR-20/domain-testing.md), [boundary-value-analysis.md](FR-20/boundary-value-analysis.md), [test-cases.md](FR-20/test-cases.md), [bug-report.md](FR-20/bug-report.md), [ai-gap-analysis.md](FR-20/ai-gap-analysis.md) |

## Method Summary

For each selected feature, the work followed the same black-box testing structure:

1. Collect the feature requirements and public test basis from the assignment PDF, SUT README, API specification, and observable UI/API behavior.
2. Derive Domain Testing partitions for valid, invalid, missing, state-based, actor-based, and output-contract conditions where applicable.
3. Apply Boundary Value Analysis only to ordered or bounded domains, such as failed login count, lockout duration, quantity, discount value, minimum order amount, and max uses per user.
4. Generate and review DT/BVA test cases with traceable expected results.
5. Execute test cases through public UI/API surfaces, capture evidence, and record Pass/Fail/Blocked status.
6. Report discovered bugs in Markdown and preserve AI gap analysis for review.

Detailed derivation is kept in the per-feature files linked in the submission scope table.

## Test Summary

| Feature | Test Cases | Passed | Failed | Blocked | Not Executed | Bugs Recorded | Evidence Files |
| ------- | ---------: | -----: | -----: | ------: | -----------: | ------------: | -------------: |
| FR-01   |         37 |      5 |     14 |      18 |            0 |             7 |             37 |
| FR-02   |         34 |     22 |      9 |       0 |            0 |             6 |             38 |
| FR-07   |         20 |      6 |     14 |       0 |            0 |            10 |             11 |
| FR-17   |         22 |     13 |      9 |       0 |            0 |             4 |             22 |
| FR-20   |         19 |      9 |      3 |       7 |            0 |             3 |             11 |
| Total   |        132 |     55 |     49 |      25 |            0 |            30 |            119 |

## Self-Assessment

| No.   | Criteria                              | Grade | Self-Assessed Grade |
| ----- | ------------------------------------- | ----: | ------------------: |
| 1     | Feature A (Domain + Boundary)         |    25 |                  25 |
| 2     | Feature B (Domain + Boundary)         |    25 |                  25 |
| 3     | Feature C (Domain + Boundary)         |    25 |                  25 |
| 4     | Feature D (Mobile, Domain + Boundary) |    15 |                  15 |
| 5     | Agent Skills                          |    10 |                  10 |
| Total |                                       |   100 |                 100 |

## Feature Details

### FR-01 - Account Registration

FR-01 covers account registration through UI/API surfaces, required fields, email format, duplicate email, password complexity, confirm-password behavior, successful registration response, and invalid registration inputs.

- Requirement analysis: [FR-01/requirement-analysis.md](FR-01/requirement-analysis.md)
- Domain Testing report: [FR-01/domain-testing.md](FR-01/domain-testing.md)
- Boundary Value Analysis report: [FR-01/boundary-value-analysis.md](FR-01/boundary-value-analysis.md)
- Test cases and execution results: [FR-01/test-cases.md](FR-01/test-cases.md)
- Bug report: [FR-01/bug-report.md](FR-01/bug-report.md)
- AI gap analysis: [FR-01/ai-gap-analysis.md](FR-01/ai-gap-analysis.md)
- AI audit: [ai-audit/FR01/ai-audit.md](../ai-audit/FR01/ai-audit.md)
- Intake/test-basis prompt file: [phase-01-02-blackbox-prompt.md](../evidence/ai-audit-artifacts/FR-01/phase-01-02-blackbox-prompt.md)
- Intake/test-basis AI output file: [phase-01-02-blackbox-ai-output.md](../evidence/ai-audit-artifacts/FR-01/phase-01-02-blackbox-ai-output.md)
- Domain-modeling prompt file: [phase-03-domain-modeling-prompt.md](../evidence/ai-audit-artifacts/FR-01/phase-03-domain-modeling-prompt.md)
- Domain-modeling AI output file: [phase-03-domain-modeling-ai-output.md](../evidence/ai-audit-artifacts/FR-01/phase-03-domain-modeling-ai-output.md)
- BVA prompt file: [phase-04-prompt.md](../evidence/ai-audit-artifacts/FR-01/phase-04-prompt.md)
- BVA AI output file: [phase-04-bva-ai-output.md](../evidence/ai-audit-artifacts/FR-01/phase-04-bva-ai-output.md)
- Test-case design prompt file: [phase-05-prompt.md](../evidence/ai-audit-artifacts/FR-01/phase-05-prompt.md)
- Test-case design AI output file: [phase-05-test-case-design-ai-output.md](../evidence/ai-audit-artifacts/FR-01/phase-05-test-case-design-ai-output.md)
- Gap-analysis prompt file: [phase-08-ai-gap-analysis-prompt.md](../evidence/ai-audit-artifacts/FR-01/phase-08-ai-gap-analysis-prompt.md)
- Gap-analysis AI output file: [phase-08-ai-gap-analysis-ai-output.md](../evidence/ai-audit-artifacts/FR-01/phase-08-ai-gap-analysis-ai-output.md)

### FR-02 - Login and Account Lockout

FR-02 covers login form/API behavior, valid login, invalid credentials, failed-attempt counting, account lockout threshold, lockout duration, authorization token behavior, and password field visibility.

- Requirement analysis: [FR-02/requirement-analysis.md](FR-02/requirement-analysis.md)
- Domain Testing report: [FR-02/domain-testing.md](FR-02/domain-testing.md)
- Boundary Value Analysis report: [FR-02/boundary-value-analysis.md](FR-02/boundary-value-analysis.md)
- Test cases and execution results: [FR-02/test-cases.md](FR-02/test-cases.md)
- Bug report: [FR-02/bug-report.md](FR-02/bug-report.md)
- AI gap analysis: [FR-02/ai-gap-analysis.md](FR-02/ai-gap-analysis.md)
- AI audit: [ai-audit/FR02/ai-audit.md](../ai-audit/FR02/ai-audit.md)
- Prompt file: [phase-01-05-design-prompt.md](../evidence/ai-audit-artifacts/FR-02/phase-01-05-design-prompt.md)
- AI output file: [phase-01-05-design-ai-output.md](../evidence/ai-audit-artifacts/FR-02/phase-01-05-design-ai-output.md)
- Gap-analysis prompt file: [phase-08-ai-gap-analysis-prompt.md](../evidence/ai-audit-artifacts/FR-02/phase-08-ai-gap-analysis-prompt.md)
- Gap-analysis AI output file: [phase-08-ai-gap-analysis-ai-output.md](../evidence/ai-audit-artifacts/FR-02/phase-08-ai-gap-analysis-ai-output.md)

### FR-07 - Shopping Cart

FR-07 covers empty cart behavior, authenticated cart access, add-to-cart behavior, duplicate products, quantity controls, delete confirmation, navigation from cart, API authorization, and invalid API request bodies.

- Requirement analysis: [FR-07/requirement-analysis.md](FR-07/requirement-analysis.md)
- Domain Testing report: [FR-07/domain-testing.md](FR-07/domain-testing.md)
- Boundary Value Analysis report: [FR-07/boundary-value-analysis.md](FR-07/boundary-value-analysis.md)
- Test cases and execution results: [FR-07/test-cases.md](FR-07/test-cases.md)
- Bug report: [FR-07/bug-report.md](FR-07/bug-report.md)
- AI gap analysis: [FR-07/ai-gap-analysis.md](FR-07/ai-gap-analysis.md)
- AI audit: [ai-audit/FR07/ai-audit.md](../ai-audit/FR07/ai-audit.md)
- Prompt file: [phase-01-07-design-execution-prompt.md](../evidence/ai-audit-artifacts/FR-07/phase-01-07-design-execution-prompt.md)
- AI output file: [phase-01-07-design-execution-ai-output.md](../evidence/ai-audit-artifacts/FR-07/phase-01-07-design-execution-ai-output.md)

### FR-17 - Coupon Management CRUD

FR-17 covers coupon listing, create/update/delete behavior, admin and non-admin access, required fields, coupon type validation, numeric boundaries, and API response behavior.

- Requirement analysis: [FR-17/requirement-analysis.md](FR-17/requirement-analysis.md)
- Domain Testing report: [FR-17/domain-testing.md](FR-17/domain-testing.md)
- Boundary Value Analysis report: [FR-17/boundary-value-analysis.md](FR-17/boundary-value-analysis.md)
- Test cases and execution results: [FR-17/test-cases.md](FR-17/test-cases.md)
- Bug report: [FR-17/bug-report.md](FR-17/bug-report.md)
- AI gap analysis: [FR-17/ai-gap-analysis.md](FR-17/ai-gap-analysis.md)
- AI audit: [ai-audit/FR17/ai-audit.md](../ai-audit/FR17/ai-audit.md)
- Prompt file: [phase-01-07-design-execution-prompt.md](../evidence/ai-audit-artifacts/FR-17/phase-01-07-design-execution-prompt.md)
- AI output file: [phase-01-07-design-execution-ai-output.md](../evidence/ai-audit-artifacts/FR-17/phase-01-07-design-execution-ai-output.md)

### FR-20 - Login and Account Lockout Mobile

FR-20 covers the mobile login capability, shared login API behavior, invalid mobile/API login inputs, failed-attempt lockout, lockout duration, and mobile-runtime availability constraints.

- Requirement analysis: [FR-20/requirement-analysis.md](FR-20/requirement-analysis.md)
- Domain Testing report: [FR-20/domain-testing.md](FR-20/domain-testing.md)
- Boundary Value Analysis report: [FR-20/boundary-value-analysis.md](FR-20/boundary-value-analysis.md)
- Test cases and execution results: [FR-20/test-cases.md](FR-20/test-cases.md)
- Bug report: [FR-20/bug-report.md](FR-20/bug-report.md)
- AI gap analysis: [FR-20/ai-gap-analysis.md](FR-20/ai-gap-analysis.md)
- AI audit: [ai-audit/FR20/ai-audit.md](../ai-audit/FR20/ai-audit.md)
- Prompt file: [phase-01-08-design-execution-prompt.md](../evidence/ai-audit-artifacts/FR-20/phase-01-08-design-execution-prompt.md)
- AI output file: [phase-01-08-design-execution-ai-output.md](../evidence/ai-audit-artifacts/FR-20/phase-01-08-design-execution-ai-output.md)

## Bug Report Summary

The detailed bug descriptions, reproduction steps, expected results, actual results, severity, and evidence references are maintained in each feature's bug report:

- FR-01 bug report: [FR-01/bug-report.md](FR-01/bug-report.md)
- FR-02 bug report: [FR-02/bug-report.md](FR-02/bug-report.md)
- FR-07 bug report: [FR-07/bug-report.md](FR-07/bug-report.md)
- FR-17 bug report: [FR-17/bug-report.md](FR-17/bug-report.md)
- FR-20 bug report: [FR-20/bug-report.md](FR-20/bug-report.md)

GitHub Issue links should be completed in the bug reports after the real issues are created on the group GitHub Issues page. No fake issue links are included.

## AI Use Declaration

I use AI tools for the following tasks: requirement extraction, Domain Testing partition modeling, Boundary Value Analysis derivation, test-case drafting, report structuring, execution-result formatting, bug-report drafting, and AI gap analysis. The prompts, AI outputs, and final human-reviewed artifacts are recorded in the AI audit files.

AI audit files:

- FR-01 AI audit: [ai-audit/FR01/ai-audit.md](../ai-audit/FR01/ai-audit.md)
- FR-02 AI audit: [ai-audit/FR02/ai-audit.md](../ai-audit/FR02/ai-audit.md)
- FR-07 AI audit: [ai-audit/FR07/ai-audit.md](../ai-audit/FR07/ai-audit.md)
- FR-17 AI audit: [ai-audit/FR17/ai-audit.md](../ai-audit/FR17/ai-audit.md)
- FR-20 AI audit: [ai-audit/FR20/ai-audit.md](../ai-audit/FR20/ai-audit.md)

## AI Critique

The AI was useful for creating a disciplined first version of the Domain Testing and Boundary Value Analysis artifacts, especially when the feature involved many input conditions, invalid partitions, and cross-surface checks. However, the AI was not fully reliable as a final authority. It sometimes mixed setup conditions with feature requirements, treated ambiguous behavior as if it were normative, or produced links to files that later had to be verified manually. In several features, the runtime failures were not AI-missed test ideas: the AI had generated the negative cases, but the real defects only became visible after executing them against the public UI or API. This showed an important distinction between design quality and execution evidence. The AI also needed human correction for scope control, such as keeping only one Pool A feature in the final submission set and separating mobile-runtime blockers from product defects. The main lesson is that AI can accelerate systematic testing, but it must be constrained by explicit test bases, traceability, and evidence rules. Good collaboration with AI means asking it to expose assumptions, then checking every requirement, expected result, execution status, evidence path, and bug claim before submission.

## Agent Skill

The reusable Agent Skill is included at [.agents/skills/domain-testing-bva/](../.agents/skills/domain-testing-bva/). The skill contains the workflow instructions, templates, references, helper scripts, and validation tests used to structure the black-box DT/BVA process.

The skill is designed to run one feature at a time and to keep the work auditable from feature intake through AI gap analysis. It enforces black-box discipline: expected results must come from requirements, API specifications, observable public behavior, or explicit assumptions, not from implementation source code.
| Phase | Name | Purpose |
| ----- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Feature Intake | Select and record the feature ID, pool, actor, surface, requirement source, public endpoint/UI location, output directory, and environment. The skill also checks whether the selected feature appears consistent with the pool rule. |
| 2 | Black-box Test Basis Collection | Collect only approved public test bases: assignment PDF, README requirements, API specification, setup notes, observable UI/API behavior, public messages, and real execution evidence. |
| 3 | Domain Modeling | Derive valid/invalid partitions for inputs, states, actors, output contracts, missing values, format, length, range, uniqueness, and cross-field relationships. The skill requires a surface matrix so UI/API coverage is explicit. |
| 4 | Boundary Value Analysis | Apply BVA only to ordered or bounded domains, such as password minimum length, failed-attempt count, lockout duration, quantity, discount value, minimum order amount, and max uses per user. |
| 5 | AI Test-Case Generation | Generate DT and BVA cases from approved partitions and boundaries, with test data, steps, expected result, traceability, and initial `Not Executed` status before execution. |
| 6 | Human Review and Black-box Test Execution | Require human review before execution. After approval, execute only through public UI/API surfaces and record actual result, Pass/Fail/Blocked status, environment, and blocking reason when needed. |
| 7 | Human-verified Evidence and Bug Reporting | Capture evidence for each executed or blocked case, verify it manually, and create bug records only for reproduced observable contradictions with documented expected results. |
| 8 | AI Gap Analysis | Compare initial AI output with human corrections, execution findings, missed cases, reclassifications, and runtime bugs. The skill distinguishes AI-missed cases from bugs discovered by AI-generated tests. |

The skill also includes reusable assets and scripts:

- Skill instructions: [.agents/skills/domain-testing-bva/SKILL.md](../.agents/skills/domain-testing-bva/SKILL.md)
- Templates: [.agents/skills/domain-testing-bva/assets/](../.agents/skills/domain-testing-bva/assets/)
- Method references: [.agents/skills/domain-testing-bva/references/](../.agents/skills/domain-testing-bva/references/)
- Helper scripts: [.agents/skills/domain-testing-bva/scripts/](../.agents/skills/domain-testing-bva/scripts/)
- Script tests: [.agents/skills/domain-testing-bva/tests/](../.agents/skills/domain-testing-bva/tests/)

## Link Video Demonstration

- [HW02 Domain Testing Video Demonstration](https://www.youtube.com/watch?v=q7ZQzRcub8Q)

## Github link

- [HW02 Github Repository](https://github.com/KidCute1412/eshop-sut/tree/23127539-NguyenThanhTien)
