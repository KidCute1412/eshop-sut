# GUI Checklist - Register (Đăng Ký) + Login (Đăng Nhập)

## Screens Covered

| GUI ID | GUI Name | GUI Detail |
| --- | --- | --- |
| 01 | Register (Đăng Ký) | frontend-web/src/pages/Register.jsx, FR-01, Sections 1-5 below |
| 02 | Login (Đăng Nhập) | frontend-web/src/pages/Login.jsx, FR-02, Sections 6-10 below |


See `references/checklist-item-schema.md` for column definitions (the `Screen` column here
replaces the per-file `GUI ID`/`GUI Name` header used when screens have separate files).

Re-executed on platform: Safari (BrowserStack). Seeded from `e:\HCMUS\HK3_2025\SoftwareTesting\HW\HW3\reports\HW3\gui-checklist\checklist.md`.

| No. | Type | Checkpoint | IA | Requirement / Heuristic Reference | Platform | Source | AI-Miss Reason | Yes | No | Remarks | Evidence | Bug ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Section | GENERAL UI (REGISTER) | IA-01 | N/A | N/A | AI-Generated | N/A |  |  |  |  |  |
| 1.1 | Item | Does the page use Vietnamese consistently, except for standard technical terms? | IA-01 | README.md FR-21 | Safari (BrowserStack) | AI-Generated | N/A |  |  |  |  |  |
| 1.2 | Item | Does the page have exactly one `<h1>` heading describing the page content? | IA-01 | README.md FR-21 | Safari (BrowserStack) | AI-Generated | N/A |  |  |  |  |  |
| 1.3 | Item | Does the Tab focus order go top-to-bottom, left-to-right? | IA-01 | README.md FR-21 | Safari (BrowserStack) | AI-Generated | N/A |  |  |  |  |  |
| 2 | Section | FORMS (REGISTER) | IA-02 | N/A | N/A | AI-Generated | N/A |  |  |  |  |  |
| 2.1 | Item | Does every required field show a * next to its label? | IA-02 | README.md FR-22 | Safari (BrowserStack) | AI-Generated | N/A |  |  |  |  |  |
| 2.2 | Item | Does the Email field use type="email" (native browser format validation)? | IA-02 | README.md FR-22 | Safari (BrowserStack) | AI-Generated | N/A |  |  |  |  |  |
| 2.3 | Item | Does the Password field use type="password"? | IA-02 | README.md FR-22 | Safari (BrowserStack) | AI-Generated | N/A |  |  |  |  |  |
| 2.4 | Item | Does the error message appear above the submit button, not below it? | IA-02 | README.md FR-22 | Safari (BrowserStack) | AI-Generated | N/A |  |  |  |  |  |
| 2.5 | Item | Does the form provide a separate "Confirm Password" field, and does the system reject mismatched passwords? | IA-02 | README.md FR-01 | Safari (BrowserStack) | AI-Generated | N/A |  |  |  |  |  |
| 2.6 | Item | Is the entered email validated for correct format before the form is submitted? | IA-02 | README.md FR-01 | Safari (BrowserStack) | AI-Generated | N/A |  |  |  |  |  |
| 2.7 | Item | Is the email required to be unique -- is registering with an already-used email rejected? | IA-02 | README.md FR-01 | Safari (BrowserStack) | AI-Generated | N/A |  |  |  |  |  |
| 2.8 | Item | Does the password field accept a password that satisfies its own displayed requirement hint (uppercase, lowercase, digit, special character)? | IA-02 | README.md FR-01 | Safari (BrowserStack) | AI-Generated | N/A |  |  |  |  |  |
| 3 | Section | NAVIGATION (REGISTER) | IA-03 | N/A | N/A | AI-Generated | N/A |  |  |  |  |  |
| 3.1 | Item | Does the navbar highlight the currently active/selected page? | IA-03 | README.md FR-23 | Safari (BrowserStack) | AI-Generated | N/A |  |  |  |  |  |
| 3.2 | Item | Is there a link back to the home page from this screen? | IA-03 | README.md FR-23 | Safari (BrowserStack) | AI-Generated | N/A |  |  |  |  |  |
| 4 | Section | FEEDBACK / STATE (REGISTER) | IA-04 | N/A | N/A | AI-Generated | N/A |  |  |  |  |  |
| 4.1 | Item | After a successful registration, is the user redirected to the Login page? | IA-04 | README.md FR-01 | Safari (BrowserStack) | AI-Generated | N/A |  |  |  |  |  |
| 4.2 | Item | When registering with a duplicate email, is a clear error message shown to the user (not just silent success)? | IA-04 | README.md FR-01 (feedback aspect of the uniqueness rule) | Safari (BrowserStack) | AI-Generated | N/A |  |  |  |  |  |
| 4.3 | Item | Does the server independently re-validate password strength, in case the client-side check is bypassed? | IA-04 | README.md FR-01 / SEC-01 | Safari (BrowserStack) | Human-Added | Interface characteristic: only discoverable by bypassing the client check (e.g. via F12 -> Network, replaying the registration request with a weak password) and observing whether the server still accepts it -- invisible from using the form normally. |  |  |  |  |  |
| 4.4 | Item | Is user-entered data (e.g. the Name field) safely escaped everywhere it is later displayed, instead of being rendered as raw HTML? | IA-04 | README.md SEC-04 | Safari (BrowserStack) | Human-Added | Cross-screen blind spot: the place this data is later displayed (the site-wide header, after logging in) is a completely different screen from Register; a checklist scoped to 'this screen' does not naturally prompt checking where else this value re-appears. |  |  |  |  |  |
| 4.5 | Item | While the registration request is in flight, does the submit button switch to a loading/disabled state (and is a success confirmation shown before navigating away)? | IA-04 | README.md FR-24 (feedback/state principle) | Safari (BrowserStack) | AI-Generated | N/A |  |  |  |  |  |
| 4.6 | Item | When a submission error occurs, does focus move to the first field in error? | IA-04 | README.md FR-24 (feedback/state principle) | Safari (BrowserStack) | AI-Generated | N/A |  |  |  |  |  |
| 4.7 | Item | Is the first input field automatically focused when the form loads? | IA-04 | README.md FR-24 (feedback/state principle) | Safari (BrowserStack) | AI-Generated | N/A |  |  |  |  |  |
| 5 | Section | ACCESSIBILITY & ADVANCED UI (REGISTER) -- not covered by README, added because HW03 explicitly names these as commonly AI-missed categories | IA-01 | N/A | N/A | AI-Generated | N/A |  |  |  |  |  |
| 5.1 | Item | Are form labels programmatically associated with their inputs, so clicking a label focuses its input (and a screen reader announces the correct field name)? | IA-01 | WCAG 2.1 (accessibility) | Safari (BrowserStack) | AI-Generated | N/A |  |  |  |  |  |
| 5.2 | Item | Does the screen support dark mode (via prefers-color-scheme or a manual toggle)? | IA-01 | WCAG 2.1 / general accessibility | Safari (BrowserStack) | AI-Generated | N/A |  |  |  |  |  |
| 6 | Section | GENERAL UI (LOGIN) | IA-01 | N/A | N/A | AI-Generated | N/A |  |  |  |  |  |
| 6.1 | Item | Does the page use Vietnamese consistently, except for standard technical terms? | IA-01 | README.md FR-21 | Safari (BrowserStack) | AI-Generated | N/A |  |  |  |  |  |
| 6.2 | Item | Does the page have exactly one `<h1>` heading that correctly describes the page content? | IA-01 | README.md FR-21 | Safari (BrowserStack) | AI-Generated | N/A |  |  |  |  |  |
| 6.3 | Item | Does the Tab focus order go top-to-bottom, left-to-right? | IA-01 | README.md FR-21 | Safari (BrowserStack) | AI-Generated | N/A |  |  |  |  |  |
| 7 | Section | FORMS (LOGIN) | IA-02 | N/A | N/A | AI-Generated | N/A |  |  |  |  |  |
| 7.1 | Item | Does every required field show a * next to its label? | IA-02 | README.md FR-22 | Safari (BrowserStack) | AI-Generated | N/A |  |  |  |  |  |
| 7.2 | Item | Does the email field use type="email" with native browser format validation, as required for the login form specifically? | IA-02 | README.md FR-02 | Safari (BrowserStack) | AI-Generated | N/A |  |  |  |  |  |
| 7.3 | Item | Does the Password field use type="password"? | IA-02 | README.md FR-22 | Safari (BrowserStack) | AI-Generated | N/A |  |  |  |  |  |
| 7.4 | Item | Does the error message appear above the submit button, not below it? | IA-02 | README.md FR-22 | Safari (BrowserStack) | AI-Generated | N/A |  |  |  |  |  |
| 8 | Section | NAVIGATION (LOGIN) | IA-03 | N/A | N/A | AI-Generated | N/A |  |  |  |  |  |
| 8.1 | Item | Does the navbar highlight the currently active/selected page? | IA-03 | README.md FR-23 | Safari (BrowserStack) | AI-Generated | N/A |  |  |  |  |  |
| 8.2 | Item | Is there a link back to the home page from this screen? | IA-03 | README.md FR-23 | Safari (BrowserStack) | AI-Generated | N/A |  |  |  |  |  |
| 9 | Section | FEEDBACK / STATE (LOGIN) | IA-04 | N/A | N/A | AI-Generated | N/A |  |  |  |  |  |
| 9.1 | Item | After each wrong login attempt, does the account remain usable for at least 3 attempts before locking? | IA-04 | README.md FR-02 | Safari (BrowserStack) | AI-Generated | N/A |  |  |  |  |  |
| 9.2 | Item | Does the account lock only after 3 or more consecutive wrong attempts (not fewer)? | IA-04 | README.md FR-02 | Safari (BrowserStack) | AI-Generated | N/A |  |  |  |  |  |
| 9.3 | Item | Is the account lockout roughly as short as the documented 30-second demo duration (not dramatically longer)? | IA-04 | README.md FR-02 | Safari (BrowserStack) | AI-Generated | N/A |  |  |  |  |  |
| 9.4 | Item | On successful login, does the session persist (e.g. survive a page reload) as expected of a stored auth token? | IA-04 | README.md FR-02 | Safari (BrowserStack) | AI-Generated | N/A |  |  |  |  |  |
| 9.5 | Item | Does the login-failure message avoid leaking which specific detail (email vs. password) was wrong? | IA-04 | README.md FR-02 | Safari (BrowserStack) | AI-Generated | N/A |  |  |  |  |  |
| 9.6 | Item | When the account is locked, is the user shown a message distinct from a plain wrong-credentials message? | IA-04 | README.md FR-02 (tension with the 'do not leak detail' rule above -- a locked-account state is arguably different enough from a wrong password to deserve distinct feedback) | Safari (BrowserStack) | Human-Added | Model limitation: a straightforward reading of FR-02 only prompts checking the lockout counter/duration numbers; noticing that the SAME generic message is reused even for the locked-account case requires a human judgment call about UX quality, not just literal compliance. |  |  |  |  |  |
| 9.7 | Item | While the login request is in flight, does the submit button switch to a loading/disabled state? | IA-04 | README.md FR-24 (feedback/state principle) | Safari (BrowserStack) | AI-Generated | N/A |  |  |  |  |  |
| 9.8 | Item | When a login error occurs, does focus move to the first field in error? | IA-04 | README.md FR-24 (feedback/state principle) | Safari (BrowserStack) | AI-Generated | N/A |  |  |  |  |  |
| 9.9 | Item | Is the first input field automatically focused when the form loads? | IA-04 | README.md FR-24 (feedback/state principle) | Safari (BrowserStack) | AI-Generated | N/A |  |  |  |  |  |
| 10 | Section | ACCESSIBILITY & ADVANCED UI (LOGIN) -- not covered by README, added because HW03 explicitly names these as commonly AI-missed categories | IA-01 | N/A | N/A | AI-Generated | N/A |  |  |  |  |  |
| 10.1 | Item | Are form labels programmatically associated with their inputs? | IA-01 | WCAG 2.1 (accessibility) | Safari (BrowserStack) | AI-Generated | N/A |  |  |  |  |  |
| 10.2 | Item | Does the screen support dark mode? | IA-01 | WCAG 2.1 / general accessibility | Safari (BrowserStack) | AI-Generated | N/A |  |  |  |  |  |

## Human Review

- Reviewer: TODO
- Review Date and Time: TODO
- Review Scope: Cross-Platform Execution on Safari (BrowserStack)
- Status: Pending
- Approved for Test Execution: No
