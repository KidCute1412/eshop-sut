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
- Review Date and Time: 2026-06-23 19:30 GMT+7
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

---

## AI Interaction

- AI Tool: ChatGPT 5.5
- Date and Time: 2026-06-23 / 20:47
- Feature ID: FR-01
- Task: FR-01 Phase 4 Boundary Value Analysis for Account Registration

### Prompt Reference

- Prompt file: [phase-04-prompt.md](../evidence/agent-skill/FR-01/phase-04-prompt.md)

### AI Output References

- AI output file: [phase-04-bva-ai-output.md](../evidence/agent-skill/FR-01/phase-04-bva-ai-output.md)
- Generated report: [reports/FR-01/boundary-value-analysis.md](../reports/FR-01/boundary-value-analysis.md)

### AI Output Summary

- Created a Boundary Value Analysis report for FR-01 Account Registration.
- Used only the approved black-box requirement analysis, human-reviewed Domain Testing report, and approved BVA method.
- Assessed 26 candidate domains and variables for BVA applicability.
- Classified password length as the only domain with a documented numeric boundary.
- Classified full-name length, email length, and registration Step Indicator applicability as undetermined because no approved numeric limits or step count were documented.
- Classified the remaining categorical, relational, structural, state-based, UI, response, outcome, and navigation domains as not applicable to BVA.
- Created one inclusive lower-boundary model for the minimum password length of 8 characters.
- Derived the following concrete values:
  - `Abcd1!x`: 7 characters, `min-1`, expected Invalid.
  - `Abcd1!xy`: 8 characters, `min`, expected Valid.
  - `Abcd1!xyz`: 9 characters, `min+1`, expected Valid.
  - `ValidPass1!`: 11 characters, nominal internal value, expected Valid.

- Kept uppercase, lowercase, digit, special-character, email, full-name, actor, and request-shape conditions nominal so that password length was the only changing factor.
- Did not create an upper-boundary model because no maximum password length was documented.
- Did not create test cases.
- Did not execute the application or send HTTP requests.
- Did not capture screenshots or execution evidence.
- Did not assign Actual Results or Pass/Fail statuses.
- Did not infer or report bugs.
- Did not create GitHub Issues.
- Did not inspect implementation source code, database schema, controllers, services, routes, middleware, models, or internal tests.

### Human Review

- Reviewer: Nguyen Thanh Tien
- Review Date and Time: 2026-06-23 19:30 GMT+7
- Review Scope: Boundary Value Analysis for FR-01 Account Registration
- Human Review Status: Completed
- Missing Boundaries Added: None
- Incorrect Boundaries Removed: None
- Approved for Test-Case Derivation: Yes
- Approved for Test Execution: No

### Human Corrections

- Verified that BVA is applicable only to the documented password minimum-length boundary.
- Confirmed that the selected password values contain exactly 7, 8, 9, and 11 displayed ASCII characters.
- Standardized abbreviated requirement references to feature-scoped IDs, including `FR01-API01` through `FR01-API05`, `FR01-SF01` through `FR01-SF05`, and `FR01-R01` through `FR01-R14`.
- Expanded the ambiguous reference `FR01-R06-R10` into the explicit rule IDs `FR01-R06`, `FR01-R07`, `FR01-R08`, `FR01-R09`, and `FR01-R10`.
- Added explicit Domain Testing partition references:
  - `PASSWORD-LENGTH-I01` for the 7-character invalid value.
  - `PASSWORD-LENGTH-V01` for the 8-, 9-, and 11-character valid values.

- Clarified the nominal API request conditions used for each boundary value.
- Clarified that UI execution assumes the Confirm Password control exists and contains the same selected password.
- Clarified that a missing Confirm Password control belongs to Domain Testing partition `CONFIRM-CONTROL-I01`, not to the password-length BVA model.
- Expanded the boundary derivation to explain why password length is the only factor that changes classification.
- Clarified that the 11-character value is a nominal internal value and not a boundary point.
- Confirmed that no maximum password length is documented, so no `max-1`, `max`, or `max+1` values were created.
- Removed the redundant Black-box Test Basis Summary from the final reviewed report.
- Confirmed that Phase 4 contains no test cases, execution results, evidence, bug reports, or GitHub Issues.

---

## AI Interaction

- AI Tool: ChatGPT 5.5
- Date and Time: 2026-06-24 / 12:45
- Feature ID: FR-01
- Task: FR-01 Phase 5 Test-Case Design for Account Registration

### Prompt Reference

- Prompt file: [phase-05-prompt.md](../evidence/agent-skill/FR-01/phase-05-prompt.md)

### AI Output References

- AI output file: [phase-05-test-case-design-ai-output.md](../evidence/agent-skill/FR-01/phase-05-test-case-design-ai-output.md)
- Generated report: [reports/FR-01/test-cases.md](../reports/FR-01/test-cases.md)

### AI Output Summary

- Created black-box test cases for FR-01 Account Registration.
- Generated 21 Domain Testing cases and 8 BVA cases.
- Covered valid and invalid UI/API partitions.
- Created separate UI and API BVA cases for password lengths 7, 8, 9, and 11.
- Added an Exploratory Backlog for four candidates without approved oracles.
- Added a preliminary coverage summary.
- Kept all cases as `Not Executed`.
- Did not inspect implementation source code.
- Did not execute tests or create evidence.
- Did not report bugs or create GitHub Issues.

### Human Review

- Reviewer: Nguyen Thanh Tien
- Review Date and Time: 2026-06-24 13:08
- Review Scope: FR-01 Test-Case Design
- Human Review Status: Completed
- Test Cases Before Review: 21 DT and 8 BVA
- Test Cases After Review: 29 DT and 8 BVA
- Missing Cases Added: 8
- Duplicate Cases Removed: None
- Incorrect Cases Removed: None
- Approved for Validation: Yes
- Approved for Traceability and Quality Review: Yes
- Approved for Test Execution: No

### Human Corrections

- Replaced nominal placeholders with concrete test data.
- Rewrote unclear or duplicated test steps.
- Standardized Rule IDs and test-basis references.
- Removed `Source Code Reference` from black-box cases.
- Added UI and API password-length cases using `Ab1!`.
- Added missing API cases for invalid email and duplicate email.
- Added missing API cases for passwords without uppercase, lowercase, digit, or special character.
- Updated the coverage table for the new cases.
- Kept undocumented API status codes and messages outside the oracle.
- Updated the validator to accept partition IDs, boundary IDs, and nominal BVA IDs.
- Updated the validator to stop before Human Review sections.
- Updated duplicate detection to distinguish different partitions and boundaries.
- Confirmed that all cases remain unexecuted.

## Manual Activity - 2026-06-24

- Feature ID: FR-01
- Phase: Phase 6 Human Review and Black-box Test Execution; Phase 7 Evidence Capture and Bug Reporting
- Performer: Nguyen Thanh Tien
- AI Tool: None
- Work Type: Manual human review, manual black-box execution, manual evidence capture, and manual bug reporting

### Manual Work Summary

- Reviewed the 37 human-approved FR-01 test cases before execution.
- Executed the cases through only the public registration UI and public registration API.
- Updated `reports/FR-01/test-cases.md` with real Actual Results, Status values, blocking reasons, and evidence references.
- Recorded final execution metrics:
  - 37 total test cases
  - 5 Pass
  - 14 Fail
  - 18 Blocked
  - 0 Not Executed
- Captured 37 real evidence PNG files under `reports/FR-01/evidence/`.
- Created `reports/FR-01/bug-report.md` with 7 confirmed bug records.
- Left GitHub Issue links as `Pending` because real GitHub Issues had not yet been created.
- Did not inspect implementation source code to determine expected results.
- Did not fabricate execution results, screenshots, bugs, evidence paths, or GitHub Issue links.

---

### Manual Review Notes

- UI-dependent cases requiring the Confirm Password control were marked `Blocked` when the public registration UI did not provide that control.
- The Confirm Password control-conformance case itself was marked `Fail`.
- API failures were recorded only when the public API response contradicted a documented expected result.
- Evidence files were manually checked against their corresponding test cases.

## AI Interaction - 2026-06-24T20:18:47+07:00

- AI Tool: ChatGPT 5.5
- Date and Time: 2026-06-24T20:18:47+07:00
- Feature ID: FR-01
- Task: Phase 8 AI Gap Analysis for Account Registration
- Prompt file: [phase-08-ai-gap-analysis-prompt.md](../evidence/agent-skill/FR-01/phase-08-ai-gap-analysis-prompt.md)
- AI output file: [phase-08-ai-gap-analysis-ai-output.md](../evidence/agent-skill/FR-01/phase-08-ai-gap-analysis-ai-output.md)
- Generated report: [reports/FR-01/ai-gap-analysis.md](../reports/FR-01/ai-gap-analysis.md)
- AI Output Summary: Compared preserved Phase 3-5 AI outputs with reviewed reports, 37 execution results, 37 evidence files, and 7 confirmed bug records. Identified 14 supported gaps/findings while distinguishing eight AI-missed cases, human improvements, and runtime bugs exposed by AI-generated tests.
- Human Review: Completed by Nguyen Thanh Tien on 2026-06-26 7:14
