# [BUG-HW06-02] Login lock duration is 180 seconds instead of 30 seconds

**Severity:** Medium  
**Endpoint:** `POST /api/login`  
**Requirement:** FR-02

## Steps to reproduce

1. Trigger the configured login lockout for a test account.
2. Wait 30 seconds.
3. Retry a login with valid credentials.

## Expected result

The account unlocks after the specified 30-second lock period.

## Actual result

The account remains locked; the implementation uses a 180-second lock duration.

## Evidence

- Newman case: `EXT-LOGIN-03`
- Raw result: `docs/assignments/HW06/deliverables/newman-reports/pool-a/cases/EXT-LOGIN-03.json`
