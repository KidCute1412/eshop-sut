# [23127404][FR-06] Quantity input lacks the required min=1 constraint

## Summary

Quantity input lacks the required `min=1` constraint.

## Affected requirements and cases

- Requirement: FR-06
- Case ID: FR06-09
- Candidate ID: HW04-CAND-002

## Environment

- SUT revision: 6b884900be153b5af78a4865c9cca98cedcd9fc9
- Browser: Firefox 141.0 headless
- Execution command: `npx playwright test tests/fr06-product-detail.spec.ts --project=firefox --grep FR06-09`
- SUT URL: http://localhost:5173 (web) / http://localhost:3000 (API)

## Preconditions

Use the seeded database and the credentials/data defined by the external JSON case.

## Steps to reproduce

1. Start the SUT using the documented HW04 setup.
2. Execute case `FR06-09` with the command above.
3. Observe the response or UI state described by the case.

## Expected result

The behavior must satisfy the FR-06 requirement and the expected oracle in the external test-data row.

## Actual result

Quantity input lacks the required `min=1` constraint.

## Reproducibility

The failure was observed by the automated rerun; see the attached evidence metadata and Playwright report.

## Severity

**Medium** — FR-06 requires a positive integer quantity with minimum one; the missing native constraint is deterministic.

## Evidence

- Screenshot: `bugs/evidence/HW04-CAND-002/screenshot.png`
- Trace: `bugs/evidence/HW04-CAND-002/trace.zip`
- Case evidence: `bugs/evidence/HW04-CAND-002/evidence.json`

## Scope

This Issue has been filed from the HW04 runtime candidate. Before final packaging, confirm that the public Issue and its screenshot attachment are visible to a logged-out viewer and contain no sensitive data.
