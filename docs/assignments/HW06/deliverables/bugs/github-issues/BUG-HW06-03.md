# [BUG-HW06-03] Successful login response exposes plaintext password

**Severity:** Critical  
**Endpoint:** `POST /api/login`  
**Requirement:** SEC-01

## Steps to reproduce

1. Send `POST /api/login` with valid credentials for `test@eshop.com`.
2. Inspect the JSON response body.

## Expected result

The response returns only safe user fields and never returns a password.

## Actual result

The response serializes `user.password` in plaintext.

## Evidence

- Newman case: `EXT-LOGIN-04`
- Raw result: `docs/assignments/HW06/deliverables/newman-reports/pool-a/cases/EXT-LOGIN-04.json`
