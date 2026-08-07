# Bug Report - FR-01

## BUG-HW04-FR01-001 - Duplicate email registration is accepted

- Feature: FR-01 Account registration
- Severity: High
- Status: Confirmed by automation
- GitHub Issue: Pending real issue creation
- Affected browsers: Chromium, Firefox, WebKit
- Failing test: `FR01-DT-011 Negative registration`

### Steps to Reproduce

1. Register a user with a unique email address.
2. Open the registration page again.
3. Submit another registration with the same email address.

### Expected Result

The system rejects the duplicate email and keeps the user on the registration page with an error.

### Actual Result

The system returns HTTP 200 and redirects to Login, meaning the duplicate account is accepted.

### Evidence

- Chromium screenshot: `test-results/FR-01-tests-fr-01-register-9f816-T-011-Negative-registration-chromium/test-failed-1.png`
- Firefox screenshot: `test-results/FR-01-tests-fr-01-register-9f816-T-011-Negative-registration-firefox/test-failed-1.png`
- WebKit screenshot: `test-results/FR-01-tests-fr-01-register-9f816-T-011-Negative-registration-webkit/test-failed-1.png`
- HTML report: `reports/html-23127539/index.html`

## BUG-HW04-FR01-002 - Registration rejects documented special characters in strong passwords

- Feature: FR-01 Account registration
- Severity: High
- Status: Confirmed by automation
- GitHub Issue: Pending real issue creation
- Affected browsers: Chromium, Firefox, WebKit
- Failing tests: `FR01-DT-006`, `FR01-BVA-009`, `FR01-BVA-010`

### Requirement

`README.md` states that a strong password must have at least 8 characters, at least one uppercase letter, one lowercase letter, one digit, and one special character from `@`, `$`, `!`, `%`, `*`, `?`, `&`.

### Steps to Reproduce

1. Open the registration page.
2. Enter valid name and unique email.
3. Enter a password such as `Aa1!aaaa`, `Aa1@aaaa`, or a 20-character password `Aa1!aaaaaaaaaaaaaaaa`.
4. Submit the form.

### Expected Result

Registration succeeds and redirects to Login because the password satisfies the documented strong-password rule.

### Actual Result

Registration is blocked on the client side. No `POST /api/register` request is sent, and the UI shows the weak-password error. A 20-character password using a whitespace character (`Aa1 aaaaaaaaaaaaaaaa`) succeeds, confirming that the failure is caused by the special-character validation rule rather than by password length.

### Evidence

- `FR01-DT-006` (`Aa1!aaaa`) failed on Chromium, Firefox, and WebKit.
- `FR01-BVA-009` (`Aa1@aaaa`) failed on Chromium, Firefox, and WebKit.
- `FR01-BVA-010` (`Aa1!aaaaaaaaaaaaaaaa`, 20 characters) failed on Chromium, Firefox, and WebKit.
- `FR01-BVA-011` (`Aa1 aaaaaaaaaaaaaaaa`, 20 characters with whitespace) passed on Chromium as a control check.
