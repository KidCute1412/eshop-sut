# Bug Report - GUI Checklist (Register + Login)

## BUG-GUI-001: Register Page Uses `<h2>` Instead of Required `<h1>`

- Status: Confirmed
- Severity: Low
- Feature: Register Screen
- Requirement: `README.md` FR-21
- Related Checklist No.: [`1.2`](./checklist.md)
- URL: `http://localhost:5173/register`

### Steps to Reproduce

1. Open `http://localhost:5173/register`.
2. Inspect the page title element via F12 -> Elements.

### Expected Result

The page title is wrapped in an `<h1>` element.

### Actual Result

The page title "Đăng Ký Tài Khoản" is wrapped in an `<h2>` tag; no `<h1>` element exists anywhere
on the page.

### Evidence

- [1.2 screenshot](./evidence/1.2.png)

### GitHub Issue

- [Github Issue](https://github.com/KidCute1412/eshop-sut/issues/84)

## BUG-GUI-002: Register Required Field Labels Are Missing Asterisk Markers

- Status: Confirmed
- Severity: Low
- Feature: Register Screen
- Requirement: `README.md` FR-22
- Related Checklist No.: [`2.1`](./checklist.md)
- URL: `http://localhost:5173/register`

### Steps to Reproduce

1. Open `http://localhost:5173/register`.
2. Inspect the Full Name, Email, and Password labels.
3. Leave a field blank and submit to confirm it is actually required.

### Expected Result

Every required field label displays an adjacent `*` marker.

### Actual Result

None of the 3 labels (Full Name, Email, Password) shows an asterisk, even though leaving any of
them blank and submitting triggers a required-field prompt.

### Evidence

- [2.1 screenshot](./evidence/2.1.png)

### GitHub Issue

- [Github Issue](https://github.com/KidCute1412/eshop-sut/issues/85)

## BUG-GUI-003: Register Email Field Does Not Use Email Input Type or Validate Format

- Status: Confirmed
- Severity: Medium
- Feature: Register Screen
- Requirement: `README.md` FR-01
- Related Checklist No.: [`2.2`](./checklist.md), [`2.6`](./checklist.md)
- URL: `http://localhost:5173/register`

### Steps to Reproduce

1. Open `http://localhost:5173/register`.
2. Type `not-an-email` into the Email field.
3. Click Register.

### Expected Result

The browser shows a native email-format warning, or the form blocks submission with an
email-format error.

### Actual Result

No browser-native email-format warning appears; via F12 -> Elements the input's `type` attribute
is `text`, not `email`. The form does not block submission or show an email-format error — the
value is accepted as-is.

### Evidence

- [2.2 screenshot](./evidence/2.2.png)

### GitHub Issue

- [Github Issue](https://github.com/KidCute1412/eshop-sut/issues/86)

## BUG-GUI-004: Register Form Is Missing Confirm Password

- Status: Confirmed
- Severity: Medium
- Feature: Register Screen
- Requirement: `README.md` FR-01
- Related Checklist No.: [`2.5`](./checklist.md)
- URL: `http://localhost:5173/register`

### Steps to Reproduce

1. Open `http://localhost:5173/register`.
2. Count the password-type input fields on the form.

### Expected Result

The form displays a Confirm Password input and rejects submission when Password and Confirm
Password do not match.

### Actual Result

Only one password field is shown; there is no second "Confirm Password" field, so a typo in the
password cannot be caught before submitting.

### Evidence

- [2.5 note](./evidence/2.5.txt)

### GitHub Issue

- [Github Issue](https://github.com/KidCute1412/eshop-sut/issues/87)

## BUG-GUI-005: Registration API Accepts Duplicate Email Addresses

- Status: Confirmed
- Severity: High
- Feature: Register Screen
- Requirement: `README.md` FR-01
- Related Checklist No.: [`2.7`](./checklist.md), [`4.2`](./checklist.md)
- Endpoint: `POST http://localhost:3000/api/register`

### Steps to Reproduce

1. Register an account with a given email address.
2. Register again with the same email address (different name/password).
3. Observe both responses and whether the UI shows any error on the second attempt.

### Expected Result

The second registration is rejected because the email address is already registered.

### Actual Result

Both attempts complete identically (redirect to Login); no error is ever shown indicating the
email is already registered.

### Evidence

- [Duplicate email request/response log](./evidence/api-register-duplicate-email.txt)

### GitHub Issue

- [Github Issue](https://github.com/KidCute1412/eshop-sut/issues/88)

## BUG-GUI-006: Register Password-Strength Check Rejects a Password That Satisfies Its Own Displayed Rule

- Status: Confirmed
- Severity: Medium
- Feature: Register Screen
- Requirement: `README.md` FR-01
- Related Checklist No.: [`2.8`](./checklist.md)
- URL: `http://localhost:5173/register`

### Steps to Reproduce

1. Open `http://localhost:5173/register`.
2. Enter a password matching the on-screen hint exactly (e.g. `Aa1!aaaa`: uppercase, lowercase,
   digit, special character, no spaces).
3. Click Register.

### Expected Result

The password is accepted, per the hint text and `README.md` FR-01.

### Actual Result

The form still shows "Mật khẩu quá yếu!" (password too weak), rejecting a password that visibly
matches its own stated rule.

### Evidence

- [2.8 screenshot](./evidence/2.8.png)

### GitHub Issue

- [Github Issue](http://github.com/KidCute1412/eshop-sut/issues/89)

## BUG-GUI-007: Navbar Never Highlights the Currently Active Page

- Status: Confirmed
- Severity: Medium
- Feature: Register + Login Screens (shared navbar)
- Requirement: `README.md` FR-23
- Related Checklist No.: Register [`3.1`](./checklist.md), Login [`8.1`](./checklist.md)
- URL: `http://localhost:5173/register`, `http://localhost:5173/login`

### Steps to Reproduce

1. Open either the Register or Login page.
2. Click through Cart / Login / Register / Profile links in the top navbar.
3. Observe whether the currently open page's nav item changes appearance.

### Expected Result

The nav item for the currently open page is visually distinguished (color, underline, bold, etc.).

### Actual Result

No nav item ever changes appearance to indicate the currently open page. This is the same shared
navbar on both screens.

### Evidence

- [Register navbar screenshot](./evidence/3.1.png)
- [Login navbar screenshot](./evidence/8.1.png)

### GitHub Issue

- [Github Issue](https://github.com/KidCute1412/eshop-sut/issues/90)

## BUG-GUI-008: Registration API Accepts a Password That Fails All Strength Rules

- Status: Confirmed
- Severity: High
- Feature: Register Screen
- Requirement: `README.md` FR-01 / SEC-01
- Related Checklist No.: [`4.3`](./checklist.md)
- Endpoint: `POST http://localhost:3000/api/register`

### Steps to Reproduce

1. Bypass the client-side check (e.g. via F12 -> Network, "Copy as fetch", edit the payload to use
   a weak password such as `weakpass`).
2. Send the edited request.
3. Observe the HTTP status and JSON response.

### Expected Result

The server independently re-validates password strength and rejects the request. The exact
failure status and response body are unspecified.

### Actual Result

The server still returns success and creates the account, meaning the password-strength rule is
enforced only client-side and can be bypassed.

### Evidence

- [Weak-password screenshot](./evidence/4.3.png). **Re-confirm via the
  actual F12 Network-tab "Copy as fetch and edit" workflow before final submission.**

### GitHub Issue

- [Github Issue](https://github.com/KidCute1412/eshop-sut/issues/91)

## BUG-GUI-009: Register "Name" Field Is Not Escaped When Later Displayed, Allowing Stored XSS

- Status: Confirmed
- Severity: High (security)
- Feature: Register Screen
- Requirement: `README.md` SEC-04
- Related Checklist No.: [`4.4`](./checklist.md)
- URL: `http://localhost:5173/register`

### Description

User-entered data must be escaped before display (`README.md` SEC-04). The Name field's value is
re-rendered, unescaped, in the site-wide header greeting after login.

### Steps to Reproduce

1. Register a new account with Name = `<img src=x onerror=alert(1)>`, a valid email, and a valid
   password.
2. Log in as that account.
3. Look at the greeting in the top navbar, and open F12 -> Elements to inspect the greeting
   element.

### Expected Result

The name renders as literal text; no embedded tag is interpreted by the browser.

### Actual Result

The greeting element contains an actual `<img>` tag (not literal/escaped text), and the browser
attempts to load/execute it — confirmed stored XSS.

### Evidence

- [4.4 screenshot](./evidence/4.4.png)

### GitHub Issue

- [Github Issue](https://github.com/KidCute1412/eshop-sut/issues/92)

## BUG-GUI-010: Neither Screen Shows a Loading/Disabled State During Submit; Register Also Lacks a Success Confirmation

- Status: Confirmed
- Severity: Low
- Feature: Register + Login Screens
- Requirement: `README.md` FR-24 (feedback/state principle)
- Related Checklist No.: Register [`4.5`](./checklist.md), Login [`9.6`](./checklist.md)
- URL: `http://localhost:5173/register`, `http://localhost:5173/login`

### Steps to Reproduce

1. Click Register (or Sign In) and observe the button state while the request is pending.
2. On successful registration, observe whether any confirmation is shown before navigating away.

### Expected Result

The submit button switches to a loading/disabled state while its request is pending, and a success
confirmation is shown before navigating away from Register.

### Actual Result

Neither button visibly disables or shows a loading indicator while its request is pending. On
successful registration, the page navigates to Login immediately with no confirmation message
shown first.

### Evidence

- [register loading screenshot](./evidence/4.5.png)
- [login loading screenshot](./evidence/9.6.png)

### GitHub Issue

- [Github Issue](https://github.com/KidCute1412/eshop-sut/issues/93)

## BUG-GUI-011: Neither Screen Auto-Focuses the First Field or Refocuses the Field in Error

- Status: Confirmed
- Severity: Low
- Feature: Register + Login Screens
- Requirement: `README.md` FR-24 (feedback/state principle)
- Related Checklist No.: Register [`4.6`](./checklist.md)/[`4.7`](./checklist.md), Login
  [`9.7`](./checklist.md)/[`9.8`](./checklist.md)
- URL: `http://localhost:5173/register`, `http://localhost:5173/login`

### Steps to Reproduce

1. Load the Register page and observe whether any field has focus by default.
2. Submit an invalid Register form (e.g. weak password) and observe whether any field is
   auto-focused afterward.
3. Repeat both checks on the Login page.

### Expected Result

The first input field is focused on page load, and focus moves to the first field in error after a
failed submission.

### Actual Result

On page load, no field shows an active focus ring/cursor by default on either screen. After a
failed submission on either screen, no field is automatically focused or highlighted for
correction.

### Evidence

- [evidence 1](./evidence/2.8.png)
- [evidence 2](./evidence/4.7.png)
- [evidence 3](./evidence/9.7.png)

### GitHub Issue

- [Github Issue](https://github.com/KidCute1412/eshop-sut/issues/94)

## BUG-GUI-012: Neither Screen Associates Form Labels With Their Inputs

- Status: Confirmed
- Severity: Low (accessibility)
- Feature: Register + Login Screens
- Requirement: WCAG 2.1 (not covered by `README.md` — see `ai-gap-analysis.md`)
- Related Checklist No.: Register [`5.1`](./checklist.md), Login [`10.1`](./checklist.md)
- URL: `http://localhost:5173/register`, `http://localhost:5173/login`

### Steps to Reproduce

1. On the Register page, click directly on a label's text (e.g. "Họ Tên", "Email", "Mật khẩu").
2. Observe whether focus moves into the corresponding input.
3. Repeat on the Login page for "Username" and "Mật khẩu".
4. Optionally inspect via F12 -> Elements for a `for`/`id` pairing between label and input.

### Expected Result

Clicking a label moves focus into its corresponding input, and a screen reader announces the
correct field name.

### Actual Result

Clicking a label's text does not move focus into its corresponding input field on either screen;
via F12 -> Elements, no label has a `for`/`id` pairing with its input.

### Evidence

- [evidence screenshot](./evidence/5.1.png)
- [evidence screenshot](./evidence/10.1.png)

### GitHub Issue

- [Github Issue](https://github.com/KidCute1412/eshop-sut/issues/95)

## BUG-GUI-013: Neither Screen Supports Dark Mode

- Status: Confirmed
- Severity: Low (enhancement)
- Feature: Register + Login Screens
- Requirement: WCAG 2.1 / general accessibility (not covered by `README.md`)
- Related Checklist No.: Register [`5.2`](./checklist.md), Login [`10.2`](./checklist.md)
- URL: `http://localhost:5173/register`, `http://localhost:5173/login`

### Steps to Reproduce

1. Switch the OS or browser to dark mode.
2. Open the Register and Login pages and observe their appearance.

### Expected Result

The screen adapts to dark mode via `prefers-color-scheme` or an in-app toggle.

### Actual Result

Switching to dark mode produces no visual change on either screen, and no in-app dark-mode toggle
is visible anywhere.

### Evidence

- [5.2 screenshot](./evidence/5.2.png)
- [10.2 screenshot](./evidence/10.2.png)

### GitHub Issue

- [Github Issue](https://github.com/KidCute1412/eshop-sut/issues/96)

## BUG-GUI-014: Login Submit Button Labeled "Sign In" in English

- Status: Confirmed
- Severity: Low
- Feature: Login Screen
- Requirement: `README.md` FR-21
- Related Checklist No.: [`6.1`](./checklist.md)
- URL: `http://localhost:5173/login`

### Steps to Reproduce

1. Open `http://localhost:5173/login`.
2. Read every visible label/link/button text on the page.

### Expected Result

All visible text uses Vietnamese consistently, except for standard technical terms.

### Actual Result

The submit button reads "Sign In" in English, while every other label/link on the page is in
Vietnamese.

### Evidence

- [6.1 screenshot](./evidence/6.1.png)

### GitHub Issue

- [Github Issue](https://github.com/KidCute1412/eshop-sut/issues/97)

## BUG-GUI-015: Login Page Heading Incorrectly Reads "Đăng Ký" (Register)

- Status: Confirmed
- Severity: Medium
- Feature: Login Screen
- Requirement: `README.md` FR-21
- Related Checklist No.: [`6.2`](./checklist.md)
- URL: `http://localhost:5173/login`

### Steps to Reproduce

1. Open `http://localhost:5173/login`.
2. Read the page heading (or inspect it via F12 -> Elements).

### Expected Result

The heading correctly describes the Login page.

### Actual Result

The heading reads "Đăng Ký" (Register) on the Login screen — an evident copy-paste error.

### Evidence

- [6.2 screenshot](./evidence/6.2.png)

### GitHub Issue

- [Github Issue](https://github.com/KidCute1412/eshop-sut/issues/98)

## BUG-GUI-016: Login Required Field Labels Are Missing Asterisk Markers

- Status: Confirmed
- Severity: Low
- Feature: Login Screen
- Requirement: `README.md` FR-22
- Related Checklist No.: [`7.1`](./checklist.md)
- URL: `http://localhost:5173/login`

### Steps to Reproduce

1. Open `http://localhost:5173/login`.
2. Inspect the Username and Password labels.

### Expected Result

Every required field label displays an adjacent `*` marker.

### Actual Result

Neither the Username nor the Password label shows an asterisk, even though both are required to
submit.

### Evidence

- [7.1 screenshot](./evidence/7.1.png)

### GitHub Issue

- [Github Issue](https://github.com/KidCute1412/eshop-sut/issues/99)

## BUG-GUI-017: Login "Email" Field Is Labeled "Username" and Does Not Use an Email Input Type

- Status: Confirmed
- Severity: Medium
- Feature: Login Screen
- Requirement: `README.md` FR-02
- Related Checklist No.: [`7.2`](./checklist.md)
- URL: `http://localhost:5173/login`

### Steps to Reproduce

1. Open `http://localhost:5173/login`.
2. Read the first field's label.
3. Type a non-email value into it.

### Expected Result

The field is labeled Email and uses `type="email"` with native browser format validation.

### Actual Result

The label reads "Username", and no browser-native email-format warning appears for an invalid
value, even though this value is used as the login email.

### Evidence

- [7.2 screenshot](./evidence/7.2.png)

### GitHub Issue

- [Github Issue](https://github.com/KidCute1412/eshop-sut/issues/100)

## BUG-GUI-018: Login Password Field Renders as Plaintext, Not Masked

- Status: Confirmed
- Severity: High
- Feature: Login Screen
- Requirement: `README.md` FR-22
- Related Checklist No.: [`7.3`](./checklist.md)
- URL: `http://localhost:5173/login`

### Steps to Reproduce

1. Open `http://localhost:5173/login`.
2. Click into the password field and type any characters.

### Expected Result

Characters are masked (shown as dots), per `README.md` FR-22 (the Password field must use
`type="password"` and must not display the value in clear text).

### Actual Result

Every character typed is shown in plain, readable text.

### Evidence

- [7.3 screenshot](./evidence/7.3.png)

### GitHub Issue

- [Github Issue](https://github.com/KidCute1412/eshop-sut/issues/101)

## BUG-GUI-019: Login Error Message Renders Below the Submit Button, Not Above It

- Status: Confirmed
- Severity: Low
- Feature: Login Screen
- Requirement: `README.md` FR-22
- Related Checklist No.: [`7.4`](./checklist.md)
- URL: `http://localhost:5173/login`

### Steps to Reproduce

1. Submit the Login form with wrong credentials.
2. Observe where the error message appears relative to the Sign In button.

### Expected Result

The error message appears above the submit button.

### Actual Result

The red error message appears below the Sign In button, not above it.

### Evidence

- [7.4 screenshot](./evidence/7.4.png)

### GitHub Issue

- [Github Issue](https://github.com/KidCute1412/eshop-sut/issues/102)

## BUG-GUI-020: Login Account Locks After Only 2 Failed Attempts Instead of 3

- Status: Confirmed
- Severity: Medium
- Feature: Login Screen
- Requirement: `README.md` FR-02
- Related Checklist No.: [`9.1`](./checklist.md)
- Endpoint: `POST http://localhost:3000/api/login`

### Steps to Reproduce

1. Enter a wrong password for a real account twice in a row.
2. On the 3rd attempt, enter the correct password.

### Expected Result

The account remains usable through at least 3 wrong attempts before locking; the 3rd attempt with
the correct password succeeds.

### Actual Result

The 3rd attempt is still rejected with an account-locked error, even though the correct password
was used and only 2 wrong attempts had occurred.

### Evidence

- [Lockout request/response log](./evidence/api-login-lockout.txt). **Re-confirm by literally
  attempting login 3 times through the real UI before final submission.**

### GitHub Issue

- [Github Issue](https://github.com/KidCute1412/eshop-sut/issues/103)

## BUG-GUI-021: Login Lockout Lasts Much Longer Than 30 Seconds, and Shows No Distinct "Locked" Message

- Status: Confirmed
- Severity: Low
- Feature: Login Screen
- Requirement: `README.md` FR-02
- Related Checklist No.: [`9.2`](./checklist.md), [`9.5`](./checklist.md)
- URL: `http://localhost:5173/login`

### Steps to Reproduce

1. Trigger an account lockout (3+ wrong login attempts).
2. Retry login well under a minute after being locked out.
3. Observe the error message shown while locked, and compare it with a normal wrong-password error
   message.

### Expected Result

The lockout lasts roughly as long as the documented 30-second demo duration, and a locked account
shows a message distinct from a plain wrong-credentials error.

### Actual Result

A retry attempted well under a minute after lockout still fails, indicating a duration well beyond
the documented 30 seconds (exact figure needs a real timed re-test — see evidence). Separately,
once locked, the user sees the exact same generic "Đăng nhập thất bại..." message as an ordinary
wrong-password error — no distinct "account locked" message is ever shown (this part is directly
UI-observable, no F12 needed).

### GitHub Issue

- [Github Issue](https://github.com/KidCute1412/eshop-sut/issues/104)
