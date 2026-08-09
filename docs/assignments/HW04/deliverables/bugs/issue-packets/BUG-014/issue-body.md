# [23127404][FR-12] Regular user JWT deletes a product

## Summary

Regular user JWT deletes a product.

## Affected requirements and cases

- Requirement: FR-12
- Case ID: FR12-12
- Candidate ID: HW04-CAND-016

## Environment

- SUT revision: 6b884900be153b5af78a4865c9cca98cedcd9fc9
- Browser: Firefox 141.0 headless
- Execution command: `npx playwright test tests/fr12-access-control.spec.ts --project=firefox --grep FR12-12`
- SUT URL: http://localhost:5173 (web) / http://localhost:3000 (API)

## Preconditions

Use the seeded database and the credentials/data defined by the external JSON case.

## Steps to reproduce

1. Start the SUT using the documented HW04 setup.
2. Execute case `FR12-12` with the command above.
3. Observe the response or UI state described by the case.

## Expected result

The behavior must satisfy the FR-12 requirement and the expected oracle in the external test-data row.

## Actual result

Regular user JWT deletes a product.

## Reproducibility

The failure was observed by the automated rerun; see the attached evidence metadata and Playwright report.

## Severity

**Critical** — Product deletion must require an admin role; a regular JWT is accepted.

## Evidence

- Screenshot: `bugs/evidence/HW04-CAND-016/screenshot.png`
- Trace: `bugs/evidence/HW04-CAND-016/trace.zip`
- Case evidence: `bugs/evidence/HW04-CAND-016/evidence.json`

## Scope

This Issue was prepared from the HW04 runtime candidate and should be filed only after confirming the attached evidence is visible and contains no sensitive data.
