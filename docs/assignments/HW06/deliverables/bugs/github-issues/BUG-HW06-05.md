# [BUG-HW06-05] Customer token can change an admin order

**Severity:** Critical  
**Endpoint:** `PUT /api/admin/orders/:id/status`  
**Requirement:** SEC-03 / FR-18

## Steps to reproduce

1. Authenticate as a regular customer and obtain a user JWT.
2. Send `PUT /api/admin/orders/{id}/status` with that JWT and a valid status payload.
3. Inspect the HTTP response and order state.

## Expected result

The route rejects non-admin tokens with `403 Forbidden`.

## Actual result

The route checks only whether the JWT is valid; a customer token successfully changes the order.

## Evidence

- Newman case: `EXT-ADM-01`
- Raw result: `docs/assignments/HW06/deliverables/newman-reports/pool-c/report.json`
