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

## Postman/Newman features

Collections, local environment, iteration data, variables, pre-request scripts, Chai assertions, JSON reporting, workflow fixtures, and Newman CLI were used. Mock servers and monitors were not used and are not claimed.

## CI/CD and skill

The workflow is included in `cicd/workflows/api-tests.yml`. GitHub Action links/screenshots remain pending human-account evidence. The reusable generator and its pseudocode are in `agent-skills/api-test-generator/`; the diagram source is preserved as Mermaid. Video URL: `<YouTube-URL-Agent-Skill>`.
