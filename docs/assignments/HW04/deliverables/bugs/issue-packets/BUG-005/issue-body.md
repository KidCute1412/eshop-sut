# [23127404][FR-10] Customer UI exposes cancellation after confirmed -> shipping

## Summary

Customer UI exposes cancellation after `confirmed -> shipping`.

## Affected requirements and cases

- Requirement: FR-10
- Case ID: FR10-06
- Candidate ID: HW04-CAND-007

## Environment

- SUT revision: 6b884900be153b5af78a4865c9cca98cedcd9fc9
- Browser: Firefox 141.0 headless
- Execution command: `npx playwright test tests/fr10-order-state-machine.spec.ts --project=firefox --grep FR10-06`
- SUT URL: http://localhost:5173 (web) / http://localhost:3000 (API)

## Preconditions

Use the seeded database and the credentials/data defined by the external JSON case.

## Steps to reproduce

1. Start the SUT using the documented HW04 setup.
2. Execute case `FR10-06` with the command above.
3. Observe the response or UI state described by the case.

## Expected result

The behavior must satisfy the FR-10 requirement and the expected oracle in the external test-data row.

## Actual result

Customer UI exposes cancellation after `confirmed -> shipping`.

## Reproducibility

The failure was observed by the automated rerun; see the attached evidence metadata and Playwright report.

## Severity

**Medium** — The state-machine requirement forbids cancellation after shipping; the UI exposes an invalid action.

## Evidence

- Screenshot: `bugs/evidence/HW04-CAND-007/screenshot.png`
- Trace: `bugs/evidence/HW04-CAND-007/trace.zip`
- Case evidence: `bugs/evidence/HW04-CAND-007/evidence.json`

## Scope

This Issue has been filed from the HW04 runtime candidate. Before final packaging, confirm that the public Issue and its screenshot attachment are visible to a logged-out viewer and contain no sensitive data.
