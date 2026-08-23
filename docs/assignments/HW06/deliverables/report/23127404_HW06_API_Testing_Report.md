# HW06 — API Testing Report

## Scope and method

Three APIs were selected from distinct pools: `POST /api/login` (FR-02), `POST /api/checkout` (FR-08), and `PUT /api/admin/orders/:id/status` (FR-10/FR-18). Every pool contains 35 AI-generated cases reviewed by a human and 5 human extensions. The final matrix records a contract oracle separately from the observed-SUT oracle; this prevents a known defect reproducer from being misreported as a conforming result.

## Verified execution

| Pool | Cases | Requests | Assertions | Failures | Raw result |
|---|---:|---:|---:|---:|---|
| A | 40 | 40 | 167 | 0 | `newman-reports/pool-a/cases/` |
| B | 40 | 160 | 281 | 0 | `newman-reports/pool-b/report.json` |
| C | 40 | 120 | 240 | 0 | `newman-reports/pool-c/report.json` |

All requests inject `X-Student-Id: 23127404`; the Newman console records this with `[HW06 EVIDENCE]`. Pool A runs one isolated fixture per row to prevent lockout state leakage. Pool B uses login → cart → checkout → cart-query workflow. Pool C uses individually seeded fixture orders, then authenticates both roles before the status update.

## Human audit and extensions

All AI-generated rows were marked `VALID` after reconciliation with the requirement and live response. The extension set focuses on weaknesses an initial single-request prompt missed: persistent lockout state, password exposure, cart-to-order integrity, terminal state immutability, and role authorization. Full per-row rationale is in the Excel workbook.

## Verified defects

The six reproducible root defects are listed in `bugs/bug-report.md`. The checkout defects are one root cause (the endpoint does not consult cart state) with multiple demonstrated consequences: empty checkout, amount tampering, and cart not cleared.

The corresponding public GitHub Issues are [#162](https://github.com/KidCute1412/eshop-sut/issues/162), [#163](https://github.com/KidCute1412/eshop-sut/issues/163), [#164](https://github.com/KidCute1412/eshop-sut/issues/164), [#165](https://github.com/KidCute1412/eshop-sut/issues/165), [#166](https://github.com/KidCute1412/eshop-sut/issues/166), and [#167](https://github.com/KidCute1412/eshop-sut/issues/167). Their authentic page captures are stored in `bugs/screenshots/`.

## Postman/Newman features

Collections, local environment, iteration data, variables, pre-request scripts, Chai assertions, JSON reporting, workflow fixtures, and Newman CLI were used. Mock servers and monitors were not used and are not claimed.

## CI/CD and skill

The workflow is included in `cicd/workflows/api-tests.yml`. The baseline all-pass evidence is commit [`d07a9b1`](https://github.com/KidCute1412/eshop-sut/commit/d07a9b1) and its [GitHub Actions run](https://github.com/KidCute1412/eshop-sut/actions/runs/32665200965/job/97257113623). The required intentional red evidence is commit [`aa32d91`](https://github.com/KidCute1412/eshop-sut/commit/aa32d91) and its [GitHub Actions run](https://github.com/KidCute1412/eshop-sut/actions/runs/32665781240/job/97258816558): it intentionally expected `999` for `TC-LOGIN-01` and received `200`. The restoration commit must be pushed and its resulting green run captured before submission; authentic captures are in `cicd/screenshots/`. The reusable generator and its pseudocode are in `agent-skills/api-test-generator/`; the diagram source is preserved as Mermaid. Video URL: `<YouTube-URL-Agent-Skill>`.
