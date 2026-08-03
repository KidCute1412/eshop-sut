# Test Case Design — FR-03 Forgot Password & Reset Password (2 steps)

Spec reference: `README.md` FR-03 (root of `eshop-sut`), routes `POST /api/forgot-password`, `POST /api/reset-password`, UI `frontend-web/src/pages/ForgotPassword.jsx`.

Data file: `tests/data/fr03-forgot-password.json`

| TC ID | Type | Description | Input (email / otp / newPassword) | Expected Result |
|---|---|---|---|---|
| FR03-TC01 | Positive | Request OTP with a registered email | `test@eshop.com` | 200, response contains a `resetToken` |
| FR03-TC02 | Negative | Request OTP with unregistered email | `nouser@eshop.com` | 404, error "User not found" |
| FR03-TC03 | Negative | Request OTP with empty email | `""` | 4xx / validation error |
| FR03-TC04 | Edge | Request OTP with malformed email (no @) | `testeshop.com` | 4xx or same as not-found (documents actual backend behavior — no format validation server-side) |
| FR03-TC05 | Positive | Reset password with correct email + correct OTP + valid new password | valid OTP, `NewPass1!` | 200, "Password reset successfully" |
| FR03-TC06 | Negative | Reset password with correct email + wrong OTP | wrong 4-digit OTP | 400, "Invalid token or email" |
| FR03-TC07 | Negative | Reset password with OTP from a different user's request | OTP issued for another email | 400 (OTP must not be reusable across accounts) |
| FR03-TC08 | Edge | Reuse an OTP a second time after it was already consumed | previously-used OTP | 400 (token cleared after first use) |
| FR03-TC09 | Boundary (BVA) | Real strong password: 8 chars, upper/lower/digit/special char (`!`) | `Aa1!aaaa` | Should be accepted per spec (FR-01 rule) — **known bug**: client regex's char class `[A-Za-z\d\s]` excludes `!` entirely, so this valid password is wrongly *rejected* |
| FR03-TC10 | Negative | Weak password containing a space instead of a special character | `Aa1 aaaa` | Should be rejected (no real special char) — **known bug**: client regex requires `\s` (whitespace) instead of a special char, so this weak password is wrongly *accepted* |
| FR03-TC11 | Negative | No special character, no whitespace | `Aaaaaaa1` | Rejected — correct outcome, but for the wrong reason (fails the `\s` group, not a real special-char check) |
| FR03-TC12 | UI/Negative | Missing confirm-password field entirely | n/a | Spec requires a confirm-password field on reset step — **known bug**: field does not exist in the UI |
| FR03-TC13 | UI | OTP step indicator visible ("Bước 1/2" style) | n/a | Step indicator/label shown |
| FR03-TC14 | UI | OTP field is documented as 6 digits by spec | n/a | **known bug**: UI label says "Mã OTP (4 số)" and backend generates a 4-digit token, not 6 |
| FR03-TC15 | Negative | Reset password after account already reset once (old password no longer works) | old password on `/api/login` | 401 Invalid email or password |
| FR03-TC16 | E2E | Full happy path: request OTP → read token from response → submit new password → login with new password | full flow | Ends with 200 login success |
| FR03-TC17 | Edge | Request OTP twice in a row for the same email | 2x forgot-password calls | Second call overwrites the first `reset_token`; only the latest OTP is valid |

Total: **17 test cases** (≥ 12 required). Automated subset selected for the Playwright suite: all of the above except FR03-TC03/TC04 which are merged into a single data-driven negative-input case (kept in the data file as extra rows to preserve ≥12 automated assertions).
