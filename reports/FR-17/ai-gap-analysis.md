# AI Gap Analysis - FR-17 Coupon Management CRUD

## Scope and Sources

This Phase 8 AI Gap Analysis compares the preserved FR-17 AI output in `evidence/ai-audit-artifacts/FR-17/phase-01-07-design-execution-ai-output.md` with the current human-reviewed and executed FR-17 artifacts.

Sources reviewed:

- `evidence/ai-audit-artifacts/FR-17/phase-01-07-design-execution-ai-output.md`
- `reports/FR-17/requirement-analysis.md`
- `reports/FR-17/domain-testing.md`
- `reports/FR-17/boundary-value-analysis.md`
- `reports/FR-17/test-cases.md`
- `reports/FR-17/bug-report.md`
- `reports/FR-17/evidence/`
- `ai-audit/FR17/ai-audit.md`

No implementation source code, database schema, controllers, services, routes, middleware, models, or internal tests were inspected. This report is based on the preserved AI summary, the reviewed FR-17 reports, and the execution evidence referenced by those reports.

## Verified Current Baseline

| Metric                                  | Preserved AI Output | Current FR-17 Files |
| --------------------------------------- | ------------------- | ------------------- |
| Test cases                              | 18                  | 22                  |
| Domain Testing cases                    | 13                  | 13                  |
| BVA cases                               | 5                   | 9                   |
| Pass                                    | 2                   | 13                  |
| Fail                                    | 3                   | 9                   |
| Blocked                                 | 13                  | 0                   |
| Not Executed                            | 0                   | 0                   |
| Confirmed bug records                   | 3                   | 4                   |
| Evidence files referenced in test cases | 18                  | 22                  |

## Initial AI Output vs Current Human-Reviewed State

| Area                          | Preserved Initial AI Output                                                                       | Current Human-Reviewed State                                                                                                  | Classification    |
| ----------------------------- | ------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| Admin authentication coverage | Included a standalone admin-login test case and treated admin credentials as part of FR-17 scope. | Removed the standalone admin-login test case; admin token availability is now treated as test setup, not a FR-17 requirement. | Human correction  |
| Requirement scoping           | Setup credentials appeared as normative rule references in the test suite.                        | Setup credential references were removed from the normative requirement set and test cases.                                   | Human correction  |
| Test feasibility              | Many cases were marked Blocked because valid admin access was not yet available.                  | After execution evidence was collected, all cases were reclassified to actual Pass or Fail results.                           | Human correction  |
| Numeric BVA coverage          | BVA covered only the original lower-bound set, without the later `min+1` in-points.               | Additional `min+1` cases were added for `discount_value: 2`, `min_order_amount: 1`, and `max_uses_per_user: 2`.               | Human improvement |
| Missing-field traceability    | Missing required fields were grouped more broadly.                                                | Missing `code` and missing `expired_at` were split into separate test cases for clearer traceability.                         | Human improvement |
| Final bug count               | 3 confirmed bug records.                                                                          | 4 confirmed bug records.                                                                                                      | Human improvement |

## Gap Register

| Gap ID       | Category                                | Initial AI Output                                                                                                  | Human Correction or Runtime Finding                                                                | Why AI Missed or Mishandled It                                                                                         | Corrective Action                                                             | Related Requirement / Partition / Boundary / Test / Evidence / Bug |
| ------------ | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| GAP-FR17-001 | Human correction - scope separation     | AI treated admin login access as a feature test case.                                                              | Admin authentication is now setup only; FR-17 tests focus on coupon CRUD behaviour.                | The AI blurred environment setup with feature behaviour.                                                               | Keep credential acquisition out of FR-17 normative coverage.                  | `requirement-analysis.md`, `domain-testing.md`, `test-cases.md`    |
| GAP-FR17-002 | Human correction - requirement hygiene  | Setup credentials were mixed into FR-17 requirements and test references.                                          | Setup credential references were removed from the normative requirement-rule table and test cases. | The AI did not clearly separate test basis from execution setup.                                                       | Use credentials only as preconditions where needed.                           | `requirement-analysis.md`, `test-cases.md`                         |
| GAP-FR17-003 | Human correction - execution status     | Many test cases remained Blocked in the preserved AI baseline.                                                     | Final report shows 22 total cases with 13 Pass and 9 Fail, no blocked cases.                       | The AI summary reflected an earlier environment state, not the final executed baseline.                                | Update execution status after evidence is collected.                          | `test-cases.md`, `bug-report.md`                                   |
| GAP-FR17-004 | Human improvement - boundary coverage   | Preserved AI output did not include later `min+1` BVA cases.                                                       | Human review added `discount_value: 2`, `min_order_amount: 1`, and `max_uses_per_user: 2`.         | The AI stopped at the minimum and immediate invalid value.                                                             | Add adjacent valid in-points for every documented lower-bound numeric domain. | `boundary-value-analysis.md`, `test-cases.md`                      |
| GAP-FR17-005 | Human improvement - traceability        | Missing-field coverage was broader and less explicit.                                                              | The current suite splits missing `code` and missing `expired_at` into separate cases.              | The AI grouped distinct required-field failures too coarsely.                                                          | Keep one invalid condition per case.                                          | `test-cases.md` - `FR17-DT-010`, `FR17-DT-012`                     |
| GAP-FR17-006 | Runtime bug from AI-generated test      | Non-admin token access control for coupon create/delete was part of the initial suite.                             | Current execution confirms non-admin create/delete are accepted with HTTP 200.                     | The AI generated the right negative access-control tests and the runtime behaviour exposed the defect.                 | Preserve the cases and bug grouping.                                          | `FR17-DT-003`, `FR17-DT-004`, `BUG-FR17-001`                       |
| GAP-FR17-007 | Runtime bug from AI-generated test      | Missing `code` and missing `expired_at` were tested in the suite.                                                  | Current execution shows both are accepted with HTTP 200.                                           | The AI did not miss the cases; the runtime API behaviour is wrong.                                                     | Keep the separate required-field cases and bug records.                       | `FR17-DT-010`, `FR17-DT-012`, `BUG-FR17-002`                       |
| GAP-FR17-008 | Runtime bug from AI-generated test      | Unsupported `type: bogus` was included as an invalid partition.                                                    | Current execution confirms the API accepts the unsupported type.                                   | The AI generated the relevant invalid-class test, so this is a runtime discovery rather than a missed case.            | Retain the invalid enum case and bug record.                                  | `FR17-DT-011`, `BUG-FR17-003`                                      |
| GAP-FR17-009 | Runtime bug from AI-generated BVA       | Lower-bound numeric invalid cases were included for `discount_value`, `min_order_amount`, and `max_uses_per_user`. | Current execution confirms the API accepts values below the documented lower bounds.               | The AI generated the correct boundary tests; the runtime defect is on the application side.                            | Keep the BVA cases and consolidate the numeric acceptance defect.             | `FR17-BVA-001`, `FR17-BVA-004`, `FR17-BVA-007`, `BUG-FR17-004`     |
| GAP-FR17-010 | Runtime finding - duplicate coupon code | Duplicate code was included as a negative partition.                                                               | Current execution returns a SQLite uniqueness failure and the duplicate is rejected.               | The AI surfaced the correct behaviour; the response detail is implementation-specific but still rejects the duplicate. | Treat this as a passing rejection, not a bug.                                 | `FR17-DT-009`                                                      |

## Runtime Findings vs AI-Missed Cases

The FR-17 issues are primarily runtime bugs exposed by AI-generated tests, plus a few human corrections to scope and traceability. They should not be described as AI-missed cases when the preserved suite already contained the relevant test.

| Finding                                             | Current Related Bug | Exposed By                                            | Classification                      |
| --------------------------------------------------- | ------------------- | ----------------------------------------------------- | ----------------------------------- |
| Non-admin user can create coupons                   | BUG-FR17-001        | FR17-DT-003                                           | Runtime bug from AI-generated test  |
| Non-admin user can delete coupons                   | BUG-FR17-001        | FR17-DT-004                                           | Runtime bug from AI-generated test  |
| Missing required `code` is accepted                 | BUG-FR17-002        | FR17-DT-010                                           | Runtime bug from AI-generated test  |
| Missing required `expired_at` is accepted           | BUG-FR17-002        | FR17-DT-012                                           | Runtime bug from AI-generated test  |
| Unsupported coupon type is accepted                 | BUG-FR17-003        | FR17-DT-011                                           | Runtime bug from AI-generated test  |
| Negative or zero numeric coupon values are accepted | BUG-FR17-004        | FR17-DT-013, FR17-BVA-001, FR17-BVA-004, FR17-BVA-007 | Runtime bug from AI-generated tests |
| Duplicate coupon code is rejected                   | no bug              | FR17-DT-009                                           | Runtime finding, not a bug          |

## AI Gap Summary

- The main AI issue was not missing coverage, but an earlier separation problem between setup data and FR-17 functional requirements.
- Human review corrected the test basis by removing the standalone admin-login case and treating admin credentials as setup only.
- Human review added `min+1` BVA coverage for all three documented lower-bound numeric domains.
- The final suite expanded from 18 to 22 cases and from 5 to 9 BVA cases.
- Final execution changed from the preserved blocked-heavy baseline to a fully executed baseline with 13 Pass and 9 Fail cases.
- The final bug report contains 4 confirmed bug records, not 3.
- No AI-missed FR-17 case is currently evident from the reviewed artifacts; the meaningful findings were already represented by the generated tests.

## Lessons Learned

- Keep environment setup separate from feature rules when the credential or token is only used to enable testing.
- Add adjacent valid BVA points, not only boundary and invalid values, when the domain is a documented lower-bound numeric constraint.
- Split required-field negatives into separate cases when each field is independently normative.
- Do not convert execution blockage into feature failure; update the execution state after evidence becomes available.
- Treat runtime defects as results of good negative tests, not as AI-missed cases, when the suite already contained the right coverage.
