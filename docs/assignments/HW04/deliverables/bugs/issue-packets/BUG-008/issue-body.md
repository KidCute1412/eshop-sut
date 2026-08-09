# [23127404][FR-10] Canceled order accepts transition to delivered

## Summary

Canceled order accepts transition to delivered.

## Affected requirements and cases

- Requirement: FR-10
- Case ID: FR10-16
- Candidate ID: HW04-CAND-010

## Environment

- SUT revision: 6b884900be153b5af78a4865c9cca98cedcd9fc9
- Browser: Firefox 141.0 headless
- Execution command: `npx playwright test tests/fr10-order-state-machine.spec.ts --project=firefox --grep FR10-16`
- SUT URL: http://localhost:5173 (web) / http://localhost:3000 (API)

## Preconditions

Use the seeded database and the credentials/data defined by the external JSON case.

## Steps to reproduce

1. Start the SUT using the documented HW04 setup.
2. Execute case `FR10-16` with the command above.
3. Observe the response or UI state described by the case.

## Expected result

The behavior must satisfy the FR-10 requirement and the expected oracle in the external test-data row.

## Actual result

Canceled order accepts transition to delivered.

## Reproducibility

The failure was observed by the automated rerun; see the attached evidence metadata and Playwright report.

## Severity

**High** — Canceled is a terminal state under FR-10; accepting delivery is a direct contract violation.

## Evidence

- Screenshot: `bugs/evidence/HW04-CAND-010/screenshot.png`
- Trace: `bugs/evidence/HW04-CAND-010/trace.zip`
- Case evidence: `bugs/evidence/HW04-CAND-010/evidence.json`

## Scope

This Issue was prepared from the HW04 runtime candidate and should be filed only after confirming the attached evidence is visible and contains no sensitive data.
