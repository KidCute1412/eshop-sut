# [23127404][FR-10] Shipping order remains cancellable after rejected Admin cancellation

## Summary

Shipping order remains cancellable after rejected Admin cancellation.

## Affected requirements and cases

- Requirement: FR-10
- Case ID: FR10-11
- Candidate ID: HW04-CAND-008

## Environment

- SUT revision: 6b884900be153b5af78a4865c9cca98cedcd9fc9
- Browser: Firefox 141.0 headless
- Execution command: `npx playwright test tests/fr10-order-state-machine.spec.ts --project=firefox --grep FR10-11`
- SUT URL: http://localhost:5173 (web) / http://localhost:3000 (API)

## Preconditions

Use the seeded database and the credentials/data defined by the external JSON case.

## Steps to reproduce

1. Start the SUT using the documented HW04 setup.
2. Execute case `FR10-11` with the command above.
3. Observe the response or UI state described by the case.

## Expected result

The behavior must satisfy the FR-10 requirement and the expected oracle in the external test-data row.

## Actual result

Shipping order remains cancellable after rejected Admin cancellation.

## Reproducibility

The failure was observed by the automated rerun; see the attached evidence metadata and Playwright report.

## Severity

**Medium** — The terminal/role restriction is explicit and the invalid UI action recurs across browsers.

## Evidence

- Screenshot: `bugs/evidence/HW04-CAND-008/screenshot.png`
- Trace: `bugs/evidence/HW04-CAND-008/trace.zip`
- Case evidence: `bugs/evidence/HW04-CAND-008/evidence.json`

## Scope

This Issue has been filed from the HW04 runtime candidate. Before final packaging, confirm that the public Issue and its screenshot attachment are visible to a logged-out viewer and contain no sensitive data.
