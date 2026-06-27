# Bug Report - FR-20 Login and Account Lockout (Mobile)

## Confirmed Bugs

## BUG-FR20-001

- Bug ID: BUG-FR20-001
- Title: Account remains locked after documented 30-second demo lockout duration.
- Severity: High
- Status: Open
- Related Test Case: FR20-BVA-003
- Requirement or Rule Reference: FR20-R05
- Test Basis Reference: `README.md` - FR-02 Login and Account Lockout
- Preconditions:
  - Backend API is running at `http://localhost:3000`.
  - Disposable user exists with known password `Test1234!`.
  - Account has been locked by three consecutive wrong-password login attempts.
- Reproduction Steps:
  1. Send three consecutive `POST /api/login` requests for the same account with wrong password `Wrong123!`.
  2. Observe locked-account response on the third attempt.
  3. Wait 31 seconds.
  4. Send `POST /api/login` for the same account with correct password `Test1234!`.
  5. Retry after an additional wait to confirm the lock does not expire as documented.
- Expected Result: Because the documented demo lockout duration is 30 seconds, correct credentials after more than 30 seconds should authenticate and return a token.
- Actual Result: Correct credentials after 31 seconds returned HTTP `403 Forbidden` with `{"error":"Tài khoản đã bị khóa. Vui lòng thử lại sau."}`. A retry after roughly 66 seconds total also returned HTTP `403 Forbidden`.
- Evidence:
  - [FR20-BVA-003](./evidence/FR20-BVA-003.txt)
  - [FR20-BVA-003 retry after 66s](./evidence/FR20-BVA-003-retry-after-66s.txt)
- GitHub Issue Link: Pending

## Blocked / Not Bugs

- FR20-DT-007 through FR20-DT-010 are Blocked by unavailable mobile runtime. They are not product failures until the mobile UI is observable.
