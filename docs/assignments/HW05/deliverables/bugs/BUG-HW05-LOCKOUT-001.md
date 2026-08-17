# BUG-HW05-LOCKOUT-001 — Account locks after two invalid passwords

**GitHub Issue URL:**

| Field | Value |
| --- | --- |
| Severity | High — an otherwise valid account is denied before the configured threshold |
| Environment | Local EShop backend, Node.js/Express + SQLite, Windows 11, 17 August 2026 |
| Endpoint | `POST /api/login` |
| Test account | Local seeded account `test@eshop.com` only |
| Precondition | Fresh backend/database state |

## Steps to reproduce

1. Send `POST /api/login` with the seeded email and an invalid password.
2. Repeat step 1 once with the same email.
3. Immediately send `POST /api/login` with the correct seeded password.

## Expected result

The first two invalid requests should return HTTP 401 and the correct password should still authenticate. The account should become locked only after the third failed password attempt.

## Actual result

The observed sequence is HTTP 401, HTTP 401, then HTTP 403 for the valid-password request. Runtime verification was performed on 17 August 2026 after a fresh backend start.

## Evidence and likely cause

- `evidence/lockout-reset/EV-LOCKOUT-INVALID-LOGIN-SEQUENCE.png` records the invalid-login sequence.
- `evidence/lockout-reset/EV-LOCKOUT-RESET-VALID-LOGIN.png` records reset followed by valid HTTP 200.
- Controlled follow-up result: first invalid attempt = HTTP 401; second invalid attempt = HTTP 401; valid login after the second invalid attempt = HTTP 403.
- `backend/server.js` increments `login_attempts` by two for one invalid password; the lock threshold is three.

## Impact

Users who mistype a password twice are blocked even when they subsequently provide valid credentials. The behavior also makes authentication-heavy automated scenarios fail unpredictably when account state is reused.
