# OpenAPI supporting-material audit

Student ID: `23127404`  
Artifact: `eshop-openapi.yaml`  
Status: **YAML syntax parsed successfully on 2026-08-23.**

This optional OpenAPI file describes the intended contract for the three selected APIs. It is not runtime evidence and must not be used to override observed SUT behavior.

| Check | Result |
|---|---|
| OpenAPI version declared | 3.0.3 |
| YAML parser | Pass |
| Selected paths documented | `/api/login`, `/api/checkout`, `/api/admin/orders/{id}/status` |
| `X-Student-Id` parameter | Present on all selected paths |
| Bearer security | Declared for checkout and admin status update |
| Runtime conformance | Not claimed; verified separately by raw Newman evidence |

Known runtime deviations are documented in `bugs/bug-report.md`, including password exposure, cart bypass, missing RBAC, and an illegal terminal-state transition.
