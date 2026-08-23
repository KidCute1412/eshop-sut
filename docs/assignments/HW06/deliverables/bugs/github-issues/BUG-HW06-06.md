# [BUG-HW06-06] Canceled order can transition to delivered

**Severity:** High  
**Endpoint:** `PUT /api/admin/orders/:id/status`  
**Requirement:** FR-10

## Steps to reproduce

1. Prepare an order whose current status is `canceled`.
2. Authenticate as an administrator.
3. Send `PUT /api/admin/orders/{id}/status` with `{ "status": "delivered" }`.

## Expected result

Canceled is terminal; the transition is rejected with a client error.

## Actual result

The API accepts `canceled → delivered` and returns success.

## Evidence

- Newman case: `EXT-ADM-02`
- Raw result: `docs/assignments/HW06/deliverables/newman-reports/pool-c/report.json`
