# AI Audit

## AI Interaction

- AI Tool: ChatGPT 5.5
- Date and Time: 2026-06-23 20:11
- Feature ID: FR-01
- Task: FR-01 Phase 1 Feature Intake and Phase 2 Black-box Test Basis Collection

### Prompt Reference

- Prompt file: [phase-01-02-blackbox-prompt.md](../../evidence/ai-audit-artifacts/FR-01/phase-01-02-blackbox-prompt.md)

### AI Output References

- AI output file: [phase-01-02-blackbox-ai-output.md](../../evidence/ai-audit-artifacts/FR-01/phase-01-02-blackbox-ai-output.md)
- Final report: [requirement-analysis.md](../../reports/FR-01/requirement-analysis.md)

### Human Review

- Reviewer: Nguyen Thanh Tien
- Review Date and Time: 2026-06-22 21:18
- Review Scope: Feature Intake and Black-box Test Basis Collection
- Corrections Made:
  - Added API Base URL `http://localhost:3000` from `api_specification.md`.
  - Clarified that no public UI observation was used because the application was not started.
- Missing Rules or Test Bases: None identified after comparison with `README.md`, `api_specification.md`, and `2026.HW02.Domain Testing_En.pdf`.
- Status: Completed
- Approved for Domain Modeling: Yes
- Approved for Test Execution: No

---

## AI Interaction

- AI Tool: ChatGPT 5.5
- Date and Time: 2026-06-23 19:03
- Feature ID: FR-01
- Task: FR-01 Phase 3 Domain Modeling for Account Registration

### Prompt Reference

- Prompt file: [phase-03-domain-modeling-prompt.md](../../evidence/ai-audit-artifacts/FR-01/phase-03-domain-modeling-prompt.md)

### AI Output References

- AI output file: [phase-03-domain-modeling-ai-output.md](../../evidence/ai-audit-artifacts/FR-01/phase-03-domain-modeling-ai-output.md)
- Final report: [domain-testing.md](../../reports/FR-01/domain-testing.md)

## Human Review

- Reviewer: Nguyen Thanh Tien
- Review Date and Time: 2026-06-23 19:30
- Review Scope: Domain Modeling for FR-01 Account Registration
- Corrections Made:
  - Split the original `CONFIRM-PRESENCE-V01/I01` partitions into separate control-existence, value-presence, and matching-relation partitions.
  - Clarified that missing Confirm Password control is a UI structure issue, while an empty Confirm Password field is a user-entered value issue.
  - Updated dependencies for `CONFIRM-VALUE-V01/I01` to require `CONFIRM-CONTROL-V01`.
  - Updated dependencies for `CONFIRM-MATCH-V01/I01` to require both `CONFIRM-CONTROL-V01` and `CONFIRM-VALUE-V01`.
  - Updated Step 1, Step 2, Step 3, Partition Derivation, and Coverage Decisions to reflect the separated Confirm Password domains.
- Missing Partitions Added:
  - `CONFIRM-CONTROL-V01`
  - `CONFIRM-CONTROL-I01`
  - `CONFIRM-VALUE-V01`
  - `CONFIRM-VALUE-I01`
- Duplicate Partitions Removed:
  - `CONFIRM-PRESENCE-V01`
  - `CONFIRM-PRESENCE-I01`
- Status: Completed

---

## AI Interaction

- AI Tool: ChatGPT 5.5
- Date and Time: 2026-06-23 20:47
- Feature ID: FR-01
- Task: FR-01 Phase 4 Boundary Value Analysis for Account Registration

### Prompt Reference

- Prompt file: [phase-04-prompt.md](../../evidence/ai-audit-artifacts/FR-01/phase-04-prompt.md)

### AI Output References

- AI output file: [phase-04-bva-ai-output.md](../../evidence/ai-audit-artifacts/FR-01/phase-04-bva-ai-output.md)
- Final report: [boundary-value-analysis.md](../../reports/FR-01/boundary-value-analysis.md)

### Human Review

- Reviewer: Nguyen Thanh Tien
- Review Date and Time: 2026-06-23 21:00
- Review Scope: Boundary Value Analysis for FR-01 Account Registration
- Corrections Made:
  - Verified that BVA is applicable only to the documented password minimum length boundary.
  - Confirmed that password values have exact lengths of 7, 8, 9, and 11 characters.
  - Expanded the test basis reference from `FR01-R06-R10` to explicit rule IDs `FR01-R06`, `FR01-R07`, `FR01-R08`, `FR01-R09`, and `FR01-R10`.
  - Clarified that UI execution of password-length BVA assumes the Confirm Password control exists and its value matches the selected password.
  - Clarified that if the UI does not provide a Confirm Password control, that issue belongs to Domain Testing, not BVA.
  - Confirmed that no maximum password length is documented, so no upper-bound BVA is created.

- Missing Boundaries Added: None
- Incorrect Boundaries Removed: None
- Status: Completed

---

## AI Interaction

- AI Tool: ChatGPT 5.5
- Date and Time: 2026-06-24 / 12:45
- Feature ID: FR-01
- Task: FR-01 Phase 5 Test-Case Design for Account Registration

### Prompt Reference

- Prompt file: [phase-05-prompt.md](../../evidence/ai-audit-artifacts/FR-01/phase-05-prompt.md)

### AI Output References

- AI output file: [phase-05-test-case-design-ai-output.md](../../evidence/ai-audit-artifacts/FR-01/phase-05-test-case-design-ai-output.md)
- Final report: [test-cases.md](../../reports/FR-01/test-cases.md)

## Human Review

- Reviewer: Nguyen Thanh Tien
- Review Date and Time: 2026-06-24 13:08
- Review Scope: FR-01 Test-Case Design

- Corrections Made:
  - Replaced nominal placeholders with concrete test data.
  - Rewrote unclear and duplicated test steps.
  - Standardized Rule IDs and test-basis references.
  - Added exact partition and boundary IDs.
  - Removed `Source Code Reference` from black-box cases.
  - Added UI and API cases for the invalid password-length partition using `Ab1!`.
  - Added missing API cases for invalid email, duplicate email, and missing password character classes.
  - Kept each invalid case focused on one invalid condition.
  - Avoided undocumented API status codes and error messages.
  - Updated the coverage table for all new cases.
  - Confirmed that all eight BVA cases remain covered.
  - Confirmed that all cases were unexecuted at the time of the Phase 5 design review.

- Missing Cases Added: 8
  - `FR01-DT-022`: Short password through UI.
  - `FR01-DT-023`: Invalid email through API.
  - `FR01-DT-024`: Duplicate email through API.
  - `FR01-DT-025`: Short password through API.
  - `FR01-DT-026`: Missing uppercase through API.
  - `FR01-DT-027`: Missing lowercase through API.
  - `FR01-DT-028`: Missing digit through API.
  - `FR01-DT-029`: Missing special character through API.

- Test Cases Before Review: 21 DT and 8 BVA
- Test Cases After Review: 29 DT and 8 BVA
- Duplicate Cases Removed: None
- Incorrect Cases Removed: None
- Status: Completed
- Approved for Validation: Yes
- Approved for Test Execution: Yes

## AI Interaction

- AI Tool: ChatGPT 5.5
- Date and Time: 2026-06-24 20:30
- Feature ID: FR-01
- Task: Phase 8 AI Gap Analysis for Account Registration
- Prompt file: [phase-08-ai-gap-analysis-prompt.md](../../evidence/ai-audit-artifacts/FR-01/phase-08-ai-gap-analysis-prompt.md)
- AI output file: [phase-08-ai-gap-analysis-ai-output.md](../../evidence/ai-audit-artifacts/FR-01/phase-08-ai-gap-analysis-ai-output.md)
- Final report: [reports/FR-01/ai-gap-analysis.md](../../reports/FR-01/ai-gap-analysis.md)
- AI Output Summary: Compared preserved Phase 3-5 AI outputs with reviewed reports, 37 execution results, 37 evidence files, and 7 confirmed bug records. Identified 14 supported gaps/findings while distinguishing eight AI-missed cases, human improvements, and runtime bugs exposed by AI-Final tests.
- Human Review: Completed by Nguyen Thanh Tien on 2026-06-26 7:14
