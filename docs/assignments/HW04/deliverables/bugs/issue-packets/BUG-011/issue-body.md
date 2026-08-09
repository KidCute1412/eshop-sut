# [23127404][FR-12] Anonymous product creation returns HTTP 200

## Summary

Anonymous product creation returns HTTP 200.

## Affected requirements and cases

- Requirement: FR-12
- Case ID: FR12-08
- Candidate ID: HW04-CAND-013

## Environment

- SUT revision: 6b884900be153b5af78a4865c9cca98cedcd9fc9
- Browser: Firefox 141.0 headless
- Execution command: `npx playwright test tests/fr12-access-control.spec.ts --project=firefox --grep FR12-08`
- SUT URL: http://localhost:5173 (web) / http://localhost:3000 (API)

## Preconditions

Use the seeded database and the credentials/data defined by the external JSON case.

## Steps to reproduce

1. Start the SUT using the documented HW04 setup.
2. Execute case `FR12-08` with the command above.
3. Observe the response or UI state described by the case.

## Expected result

The behavior must satisfy the FR-12 requirement and the expected oracle in the external test-data row.

## Actual result

Anonymous product creation returns HTTP 200.

## Reproducibility

The failure was observed by the automated rerun; see the attached evidence metadata and Playwright report.

## Severity

**Critical** — Unauthenticated data mutation must be rejected; the endpoint creates data without a JWT.

## Evidence

- Screenshot: `bugs/evidence/HW04-CAND-013/screenshot.png`
- Trace: `bugs/evidence/HW04-CAND-013/trace.zip`
- Case evidence: `bugs/evidence/HW04-CAND-013/evidence.json`

## Scope

This Issue was prepared from the HW04 runtime candidate and should be filed only after confirming the attached evidence is visible and contains no sensitive data.
