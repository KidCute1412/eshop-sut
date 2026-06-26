# Bug Report - FR-02 Login and Account Lockout

### BUG-FR02-001 - Login Email input does not use HTML5 email control and malformed email is not rejected by browser email validation

- Severity: Medium
- Status: Confirmed from executed test evidence
- Related Test Cases: FR02-DT-005, FR02-DT-015
- Related Requirements / Rules: FR02-R13, FR02-SF02
- Test Basis: `requirement-analysis.md` - FR02-R13, FR02-SF02; `domain-testing.md` - LOGIN-EMAIL-FORMAT-I01, FORM-EMAIL-TYPE-V01/I01
- Preconditions: EShop User Web `/login` is available; actor is unauthenticated.
- Reproduction Steps:
  1. Open `/login`.
  2. Inspect the first login input intended for Email.
  3. Enter malformed Email `not-an-email` and Password `Test1234!`.
  4. Submit the form.
  5. Observe the input type, validation message, and authentication result.
- Expected Result: The Email input exposes `type="email"` and malformed email input is rejected by HTML5 email validation. Exact browser validation text is unspecified.
- Actual Result: The Email/first login input was observed as `type="text"`. For malformed Email `not-an-email`, the input state showed no HTML5 email validation message. Login did not produce a token, but the documented browser-level email control requirement was not satisfied.
- Evidence:
  - [FR02-DT-005](./evidence/FR02-DT-005.png)
  - [FR02-DT-015](./evidence/FR02-DT-015.png)
- GitHub Issue Link: Pending

### BUG-FR02-002 - Required-field asterisk markers are missing on the login form

- Severity: Low
- Status: Confirmed from executed test evidence
- Related Test Case: FR02-DT-014
- Related Requirements / Rules: FR02-SF01
- Test Basis: `requirement-analysis.md` - FR02-SF01; `domain-testing.md` - FORM-REQUIRED-MARKER-V01/I01
- Preconditions: EShop User Web `/login` is available; actor is unauthenticated.
- Reproduction Steps:
  1. Open `/login`.
  2. Observe the Email and Password labels.
  3. Check whether required fields display adjacent `*` markers.
- Expected Result: Required Email and Password labels display adjacent `*` markers.
- Actual Result: The login form text was inspected and no `*` required-field marker was present.
- Evidence:
  - [FR02-DT-014](./evidence/FR02-DT-014.png)
- GitHub Issue Link: Pending

### BUG-FR02-003 - Login Password field is visible text instead of masked password input

- Severity: High
- Status: Confirmed from executed test evidence
- Related Test Case: FR02-DT-016
- Related Requirements / Rules: FR02-SF03
- Test Basis: `requirement-analysis.md` - FR02-SF03; `domain-testing.md` - FORM-PASSWORD-TYPE-V01/I01
- Preconditions: EShop User Web `/login` is available; actor is unauthenticated.
- Reproduction Steps:
  1. Open `/login`.
  2. Inspect the login Password control.
  3. Enter Password `Test1234!`.
  4. Observe the input type and whether the value is exposed in clear text.
- Expected Result: The Password control uses `type="password"` and masks the entered value.
- Actual Result: The Password/second login input was observed as `type="text"` and the entered password value was visible as clear text.
- Evidence:
  - [FR02-DT-016](./evidence/FR02-DT-016.png)
- GitHub Issue Link: Pending

### BUG-FR02-004 - Login error message appears below the submit button instead of above it

- Severity: Low
- Status: Confirmed from executed test evidence
- Related Test Case: FR02-DT-017
- Related Requirements / Rules: FR02-SF04
- Test Basis: `requirement-analysis.md` - FR02-SF04; `domain-testing.md` - FORM-ERROR-PLACEMENT-V01/I01
- Preconditions: EShop User Web `/login` is available; actor is unauthenticated.
- Reproduction Steps:
  1. Open `/login`.
  2. Enter a valid existing Email with a wrong password.
  3. Submit the login form.
  4. Observe where the displayed login error appears relative to the `Sign In` submit button.
- Expected Result: Any displayed login error appears above the submit button. Exact error text is unspecified.
- Actual Result: The login form displayed `Đăng nhập thất bại. Vui lòng kiểm tra lại.`, but the error message appeared below the `Sign In` submit button.
- Evidence:
  - [FR02-DT-017](./evidence/FR02-DT-017.png)
- GitHub Issue Link: Pending

### BUG-FR02-005 - Account is locked or correct login is rejected after only 2 failed attempts

- Severity: High
- Status: Confirmed from executed test evidence
- Related Test Cases: FR02-BVA-001, FR02-BVA-005
- Related Requirements / Rules: FR02-R05, FR02-R06
- Test Basis: `boundary-value-analysis.md` - FR02-FAILED-ATTEMPTS-B01; `requirement-analysis.md` - FR02-R05, FR02-R06
- Preconditions: Account `test@eshop.com` exists, is initially usable for login, and has password `Test1234!`.
- Reproduction Steps:
  1. Perform two consecutive wrong-password login attempts for `test@eshop.com`.
  2. Immediately attempt login with the correct password `Test1234!`.
  3. Repeat through the UI and public `POST /api/login` surface.
- Expected Result: Two failures do not reach the documented 3-attempt lockout threshold; the correct login is not rejected solely due to lockout.
- Actual Result:
  - UI: after two wrong-password attempts, the correct-password login did not reach an authenticated state and no token was observed.
  - API: after two wrong-password attempts returning `401` and `401`, the correct-password request returned `403 Forbidden` with `{"error":"Tài khoản đã bị khóa. Vui lòng thử lại sau."}` and no token.
- Evidence:
  - [FR02-BVA-001](./evidence/FR02-BVA-001.png)
  - [FR02-BVA-005](./evidence/FR02-BVA-005.png)
- GitHub Issue Link: Pending
- Notes: This bug is recorded once because the UI and API failures describe the same threshold contradiction on the same account-lockout rule.

### BUG-FR02-006 - UI lockout does not expire at or after the documented 30-second duration

- Severity: High
- Status: Confirmed from executed test evidence
- Related Test Cases: FR02-BVA-010, FR02-BVA-011
- Related Requirements / Rules: FR02-R07
- Test Basis: `boundary-value-analysis.md` - FR02-LOCKOUT-DURATION-B02, FR02-LOCKOUT-DURATION-B03; `requirement-analysis.md` - FR02-R07
- Preconditions: Account `test@eshop.com` is locked through public failed login attempts.
- Reproduction Steps:
  1. Lock account `test@eshop.com` through consecutive failed UI login attempts.
  2. Wait approximately 30 seconds.
  3. Attempt UI login with the correct password `Test1234!`.
  4. Repeat with an approximately 31-second wait.
- Expected Result: At the documented 30-second duration, and after 31 seconds, the account is no longer rejected solely due to lockout. Exact timing precision is unspecified.
- Actual Result:
  - At approximately 30 seconds, the correct-password UI login remained unauthenticated, no token was observed, and the login error was displayed.
  - At approximately 31 seconds, the correct-password UI login still remained unauthenticated, no token was observed, and the login error was displayed.
- Evidence:
  - [FR02-BVA-010](./evidence/FR02-BVA-010.png)
  - [FR02-BVA-011](./evidence/FR02-BVA-011.png)
- GitHub Issue Link: Pending
- Notes: `FR02-DT-021` passed in the current merged test-case file for the general expired-lockout state. This bug is limited to the UI BVA observations at the documented 30-second and 31-second boundary points.

## Failed Test Cases to Bug Mapping

| Failed Test Case | Status | Bug ID       |
| ---------------- | ------ | ------------ |
| FR02-DT-005      | Fail   | BUG-FR02-001 |
| FR02-DT-014      | Fail   | BUG-FR02-002 |
| FR02-DT-015      | Fail   | BUG-FR02-001 |
| FR02-DT-016      | Fail   | BUG-FR02-003 |
| FR02-DT-017      | Fail   | BUG-FR02-004 |
| FR02-BVA-001     | Fail   | BUG-FR02-005 |
| FR02-BVA-005     | Fail   | BUG-FR02-005 |
| FR02-BVA-010     | Fail   | BUG-FR02-006 |
| FR02-BVA-011     | Fail   | BUG-FR02-006 |

## Non-Bug Notes

- Passing cases are not listed as bugs.
- No bug is recorded for removed or merged duplicate cases.
- No GitHub Issue links are invented; all issue links remain `Pending` until real issues are created.
- Runtime failures exposed by AI-generated or human-reviewed tests are recorded as runtime findings, not as automatically AI-missed bugs.

## Human Review

- Reviewer: Nguyen Thanh Tien
- Review Date and Time: 2026-06-26 15:02
- Human Review Status: Completed
- Human Corrections: Reviewed failed cases, merged duplicated failures, confirmed 6 bug records.
