# AI Audit

## AI Interaction

- AI Tool: ChatGPT 5.5
- Date and Time: 2026-06-23 / 20:11
- Feature ID: FR-01
- Task: FR-01 Phase 1 Feature Intake and Phase 2 Black-box Test Basis Collection

### Prompt Reference

- Prompt file: [phase-01-02-blackbox-prompt.md](../evidence/agent-skill/FR-01/phase-01-02-blackbox-prompt.md)

### AI Output References

- AI output file: [phase-01-02-blackbox-ai-output.md](../evidence/agent-skill/FR-01/phase-01-02-blackbox-ai-output.md)
- Generated report: [reports/FR-01/requirement-analysis.md](../reports/FR-01/requirement-analysis.md)

### AI Output Summary

- Created a black-box requirement analysis report for FR-01 Account Registration.
- Identified the feature scope, actor, public UI/API surfaces, and testable registration behaviour.
- Identified 14 FR-01 requirement rules.
- Identified 5 registration API specification rules.
- Identified 5 shared form rules applicable to the registration form.
- Recorded requirement ambiguities, assumptions, and coverage gaps.
- Did not create domain partitions, Boundary Value Analysis, test cases, execution results, screenshots, bug reports, or GitHub Issues.
- Did not start or execute the application.
- Did not inspect implementation source code, database schema, controllers, services, routes, middleware, models, or internal tests.

### Human Review

- Reviewer: Nguyen Thanh Tien
- Review Date and Time: 2026-06-22 21:18 GMT+7
- Review Scope: Feature Intake and Black-box Test Basis Collection
- Human Review Status: Completed
- Approved for Domain Modeling: Yes
- Approved for Test Execution: No

### Human Corrections

- Added API Base URL `http://localhost:3000` from `api_specification.md`.
- Fixed the `Feature Intake` Markdown table so `Public API Endpoint` and `API Base URL` are separate rows.
- Clarified that no public UI observation was used because the application was not started.
- Confirmed no missing rules or test bases after comparison with `README.md`, `api_specification.md`, and `2026.HW02.Domain Testing_En.pdf`.

---

## AI Interaction

- AI Tool: ChatGPT 5.5
- Date and Time: 2026-06-23 / 19:03
- Feature ID: FR-01
- Task: FR-01 Phase 3 Domain Modeling for Account Registration

### Prompt Reference

- Prompt file: [phase-03-domain-modeling-prompt.md](../evidence/agent-skill/FR-01/phase-03-domain-modeling-prompt.md)

### AI Output References

- AI output file: [phase-03-domain-modeling-ai-output.md](../evidence/agent-skill/FR-01/phase-03-domain-modeling-ai-output.md)
- Generated report: [reports/FR-01/domain-testing.md](../reports/FR-01/domain-testing.md)

### AI Output Summary

- Created a Domain Testing report for FR-01 Account Registration.
- Identified input variables, output variables, state/condition items, UI form rules, and API contract elements using only the approved black-box requirement analysis.
- Identified normative equivalence classes for:
  - Full name presence.
  - Email presence, format, and uniqueness.
  - Password presence, length, uppercase, lowercase, digit, and special-character rules.
  - Confirm Password control existence, value presence, and matching relation.
  - API request shape and success response shape.
  - Shared form rules such as required-field marker, email input type, password input type, and error-message placement.
  - Registration success, redirect to Login page, guest actor state, and validation rejection.

- Identified 23 valid partitions and 20 invalid partitions after human correction.
- Identified 4 ambiguous or exploratory candidates:
  - Whitespace-only full name.
  - Email case sensitivity or normalization.
  - Undocumented special character such as `#`.
  - Step Indicator applicability for FR-01 registration.

- Did not create Boundary Value Analysis.
- Did not generate test cases.
- Did not execute the application.
- Did not capture screenshots or execution evidence.
- Did not infer or report bugs.
- Did not create GitHub Issues.
- Did not inspect implementation source code, database schema, controllers, services, routes, middleware, models, or internal tests.

### Human Review

- Reviewer: Nguyen Thanh Tien
- Review Date and Time: 2026-06-23 18:30 GMT+7
- Review Scope: Domain Modeling for FR-01 Account Registration
- Human Review Status: Completed
- Approved for BVA: Yes
- Approved for Test-Case Derivation: No
- Approved for Test Execution: No

### Human Corrections

- Split the original `CONFIRM-PRESENCE-V01/I01` partitions into separate control-existence, value-presence, and matching-relation partitions.
- Added `CONFIRM-CONTROL-V01` and `CONFIRM-CONTROL-I01` to represent whether the registration UI provides a Confirm Password control.
- Added `CONFIRM-VALUE-V01` and `CONFIRM-VALUE-I01` to represent whether the Confirm Password field has a provided or empty value.
- Kept `CONFIRM-MATCH-V01` and `CONFIRM-MATCH-I01` for the equality relation between Password and Confirm Password.
- Clarified that a missing Confirm Password control is a UI structure issue, while an empty Confirm Password field is a user-entered value issue.
- Updated dependencies for `CONFIRM-VALUE-V01/I01` to require `CONFIRM-CONTROL-V01`.
- Updated dependencies for `CONFIRM-MATCH-V01/I01` to require both `CONFIRM-CONTROL-V01` and `CONFIRM-VALUE-V01`.
- Removed duplicate or overloaded partitions:
  - `CONFIRM-PRESENCE-V01`
  - `CONFIRM-PRESENCE-I01`

- Updated Step 1, Step 2, Step 3, Partition Derivation, and Coverage Decisions in `reports/FR-01/domain-testing.md`.
- Confirmed that Phase 3 still contains no BVA, test cases, execution results, evidence, bug reports, or GitHub Issues.
