# [BUG-HW06-01] Login failure counter increments by two instead of one

**Severity:** High  
**Endpoint:** `POST /api/login`  
**Requirement:** FR-02

## Steps to reproduce

1. Start the EShop backend with a fresh account fixture.
2. Send one login request with that account's email and an incorrect password.
3. Inspect the recorded login attempt count.

## Expected result

One failed login increments `login_attempts` from `0` to `1`.

## Actual result

The count changes from `0` to `2`, so the lockout threshold is reached earlier than specified.

## Evidence

- Newman cases: `EXT-LOGIN-01`, `EXT-LOGIN-02`
- Raw result: `docs/assignments/HW06/deliverables/newman-reports/pool-a/cases/EXT-LOGIN-01.json`
