# [23127404][FR-06] Quantity 0 remains HTML-valid

## Summary

Quantity `0` remains HTML-valid.

## Affected requirements and cases

- Requirement: FR-06
- Case ID: FR06-13
- Candidate ID: HW04-CAND-005

## Environment

- SUT revision: 6b884900be153b5af78a4865c9cca98cedcd9fc9
- Browser: Firefox 141.0 headless
- Execution command: `npx playwright test tests/fr06-product-detail.spec.ts --project=firefox --grep FR06-13`
- SUT URL: http://localhost:5173 (web) / http://localhost:3000 (API)

## Preconditions

Use the seeded database and the credentials/data defined by the external JSON case.

## Steps to reproduce

1. Start the SUT using the documented HW04 setup.
2. Execute case `FR06-13` with the command above.
3. Observe the response or UI state described by the case.

## Expected result

The behavior must satisfy the FR-06 requirement and the expected oracle in the external test-data row.

## Actual result

Quantity `0` remains HTML-valid.

## Reproducibility

The failure was observed by the automated rerun; see the attached evidence metadata and Playwright report.

## Severity

**High** — The requirement rejects non-positive quantities; native validity is deterministic across browsers.

## Evidence

- Screenshot: `bugs/evidence/HW04-CAND-005/screenshot.png`
- Trace: `bugs/evidence/HW04-CAND-005/trace.zip`
- Case evidence: `bugs/evidence/HW04-CAND-005/evidence.json`

## Scope

This Issue was prepared from the HW04 runtime candidate and should be filed only after confirming the attached evidence is visible and contains no sensitive data.
