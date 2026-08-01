# AI Audit — Task 1 GUI Checklist (Prompt + Raw AI Output Only)

- AI Tool: Claude (Sonnet 5)
- Date: 2026-07-27

## Prompt

```text
You have access to the "gui-usability" Agent Skill I designed for this course (see
.agents/skills/gui-usability/SKILL.md, and its references/ and assets/ subfolders). Use it to
execute Task 1 (GUI Checklist) of HW03 for the EShop SUT, scoped to exactly two screens: the
Register screen (frontend-web/src/pages/Register.jsx, requirement FR-01) and the Login screen
(frontend-web/src/pages/Login.jsx, requirement FR-02).

Follow these constraints exactly:

1. Do NOT start from the professor's generic Web GUI checklist Template.xlsx taxonomy (Links,
   Colors, Images, Compatibility, etc.) — most of it does not apply to a 2-3-field auth form.
   Instead, ground every checklist item directly in a specific rule you find in README.md:
   FR-01 (Registration), FR-02 (Login), FR-21 (General UI), FR-22 (Forms), FR-23 (Navigation),
   FR-24 (Feedback/State), and SEC-04 (output escaping). Quote or closely paraphrase the rule
   each item comes from in the "Requirement / Heuristic Reference" column.
2. Cover all four interface aspects required by the assignment: IA-01 General UI, IA-02 Forms,
   IA-03 Navigation, IA-04 Feedback/State. Organize items under numbered sections per screen
   (Sections 1-4 or similar for Register, continuing the numbering for Login so item numbers
   never collide within the same file).
3. Add one additional small section per screen for Accessibility / Dark Mode / RTL readiness,
   even though README does not mention these at all — the assignment explicitly calls this out
   as a category generic checklists (including AI-generated ones) commonly miss.
4. The combined item count across both screens must exceed 40 — this is a total across the
   checklist you design, not a per-screen minimum, so do not pad either screen with items that
   do not meaningfully apply to it.
5. Phrase every item as a black-box question that is verifiable purely through UI interaction
   and the browser's F12 DevTools (Elements / Console / Network / Application tabs). Do not
   phrase an item in a way that requires opening the application's source code to answer it.
6. Output the result as a Markdown table using the full checklist schema — every column: No.
   (dotted-decimal, e.g. 1, 1.1, 1.1.1), Type (Section or Item), Checkpoint (the question or
   section title), IA (IA-01..IA-04), Requirement / Heuristic Reference, Platform, Source,
   AI-Miss Reason, Yes, No, Remarks, Evidence, Bug ID. Set Platform to "Baseline" (or "N/A" for
   Section rows), Source to "AI-Generated" for every row, and AI-Miss Reason to "N/A" for every
   row. Leave Yes, No, Remarks, Evidence, and Bug ID completely BLANK — you do not execute tests
   or fabricate results; that happens later, by a human, against the real running application.

Keep the prompt's own scope tight to these two screens; do not generate items for other screens.
```

## AI Output

| No. | Type | Checkpoint | IA | Requirement / Heuristic Reference | Platform | Source | AI-Miss Reason | Yes | No | Remarks | Evidence | Bug ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Section | GENERAL UI (REGISTER) | IA-01 | N/A | N/A | AI-Generated | N/A |  |  |  |  |  |
| 1.1 | Item | Does the page use Vietnamese consistently, except for standard technical terms? | IA-01 | README.md FR-21 | Baseline | AI-Generated | N/A |  |  |  |  |  |
| 1.2 | Item | Does the page have exactly one `<h1>` heading describing the page content? | IA-01 | README.md FR-21 | Baseline | AI-Generated | N/A |  |  |  |  |  |
| 1.3 | Item | Does the Tab focus order go top-to-bottom, left-to-right? | IA-01 | README.md FR-21 | Baseline | AI-Generated | N/A |  |  |  |  |  |
| 2 | Section | FORMS (REGISTER) | IA-02 | N/A | N/A | AI-Generated | N/A |  |  |  |  |  |
| 2.1 | Item | Does every required field show a * next to its label? | IA-02 | README.md FR-22 | Baseline | AI-Generated | N/A |  |  |  |  |  |
| 2.2 | Item | Does the Email field use type="email" (native browser format validation)? | IA-02 | README.md FR-22 | Baseline | AI-Generated | N/A |  |  |  |  |  |
| 2.3 | Item | Does the Password field use type="password"? | IA-02 | README.md FR-22 | Baseline | AI-Generated | N/A |  |  |  |  |  |
| 2.4 | Item | Does the error message appear above the submit button, not below it? | IA-02 | README.md FR-22 | Baseline | AI-Generated | N/A |  |  |  |  |  |
| 2.5 | Item | Does the form provide a separate "Confirm Password" field, and does the system reject mismatched passwords? | IA-02 | README.md FR-01 | Baseline | AI-Generated | N/A |  |  |  |  |  |
| 2.6 | Item | Is the entered email validated for correct format before the form is submitted? | IA-02 | README.md FR-01 | Baseline | AI-Generated | N/A |  |  |  |  |  |
| 2.7 | Item | Is the email required to be unique -- is registering with an already-used email rejected? | IA-02 | README.md FR-01 | Baseline | AI-Generated | N/A |  |  |  |  |  |
| 2.8 | Item | Does the password field accept a password that satisfies its own displayed requirement hint (uppercase, lowercase, digit, special character)? | IA-02 | README.md FR-01 | Baseline | AI-Generated | N/A |  |  |  |  |  |
| 3 | Section | NAVIGATION (REGISTER) | IA-03 | N/A | N/A | AI-Generated | N/A |  |  |  |  |  |
| 3.1 | Item | Does the navbar highlight the currently active/selected page? | IA-03 | README.md FR-23 | Baseline | AI-Generated | N/A |  |  |  |  |  |
| 3.2 | Item | Is there a link back to the home page from this screen? | IA-03 | README.md FR-23 | Baseline | AI-Generated | N/A |  |  |  |  |  |
| 4 | Section | FEEDBACK / STATE (REGISTER) | IA-04 | N/A | N/A | AI-Generated | N/A |  |  |  |  |  |
| 4.1 | Item | After a successful registration, is the user redirected to the Login page? | IA-04 | README.md FR-01 | Baseline | AI-Generated | N/A |  |  |  |  |  |
| 4.2 | Item | When registering with a duplicate email, is a clear error message shown to the user (not just silent success)? | IA-04 | README.md FR-01 (feedback aspect of the uniqueness rule) | Baseline | AI-Generated | N/A |  |  |  |  |  |
| 4.5 | Item | While the registration request is in flight, does the submit button switch to a loading/disabled state (and is a success confirmation shown before navigating away)? | IA-04 | README.md FR-24 (feedback/state principle) | Baseline | AI-Generated | N/A |  |  |  |  |  |
| 4.6 | Item | When a submission error occurs, does focus move to the first field in error? | IA-04 | README.md FR-24 (feedback/state principle) | Baseline | AI-Generated | N/A |  |  |  |  |  |
| 4.7 | Item | Is the first input field automatically focused when the form loads? | IA-04 | README.md FR-24 (feedback/state principle) | Baseline | AI-Generated | N/A |  |  |  |  |  |
| 5 | Section | ACCESSIBILITY & ADVANCED UI (REGISTER) -- not covered by README, added because HW03 explicitly names these as commonly AI-missed categories | IA-01 | N/A | N/A | AI-Generated | N/A |  |  |  |  |  |
| 5.1 | Item | Are form labels programmatically associated with their inputs, so clicking a label focuses its input (and a screen reader announces the correct field name)? | IA-01 | WCAG 2.1 (accessibility) | Baseline | AI-Generated | N/A |  |  |  |  |  |
| 5.2 | Item | Does the screen support dark mode (via prefers-color-scheme or a manual toggle)? | IA-01 | WCAG 2.1 / general accessibility | Baseline | AI-Generated | N/A |  |  |  |  |  |
| 6 | Section | GENERAL UI (LOGIN) | IA-01 | N/A | N/A | AI-Generated | N/A |  |  |  |  |  |
| 6.1 | Item | Does the page use Vietnamese consistently, except for standard technical terms? | IA-01 | README.md FR-21 | Baseline | AI-Generated | N/A |  |  |  |  |  |
| 6.2 | Item | Does the page have exactly one `<h1>` heading that correctly describes the page content? | IA-01 | README.md FR-21 | Baseline | AI-Generated | N/A |  |  |  |  |  |
| 6.3 | Item | Does the Tab focus order go top-to-bottom, left-to-right? | IA-01 | README.md FR-21 | Baseline | AI-Generated | N/A |  |  |  |  |  |
| 7 | Section | FORMS (LOGIN) | IA-02 | N/A | N/A | AI-Generated | N/A |  |  |  |  |  |
| 7.1 | Item | Does every required field show a * next to its label? | IA-02 | README.md FR-22 | Baseline | AI-Generated | N/A |  |  |  |  |  |
| 7.2 | Item | Does the email field use type="email" with native browser format validation, as required for the login form specifically? | IA-02 | README.md FR-02 | Baseline | AI-Generated | N/A |  |  |  |  |  |
| 7.3 | Item | Does the Password field use type="password"? | IA-02 | README.md FR-22 | Baseline | AI-Generated | N/A |  |  |  |  |  |
| 7.4 | Item | Does the error message appear above the submit button, not below it? | IA-02 | README.md FR-22 | Baseline | AI-Generated | N/A |  |  |  |  |  |
| 8 | Section | NAVIGATION (LOGIN) | IA-03 | N/A | N/A | AI-Generated | N/A |  |  |  |  |  |
| 8.1 | Item | Does the navbar highlight the currently active/selected page? | IA-03 | README.md FR-23 | Baseline | AI-Generated | N/A |  |  |  |  |  |
| 8.2 | Item | Is there a link back to the home page from this screen? | IA-03 | README.md FR-23 | Baseline | AI-Generated | N/A |  |  |  |  |  |
| 9 | Section | FEEDBACK / STATE (LOGIN) | IA-04 | N/A | N/A | AI-Generated | N/A |  |  |  |  |  |
| 9.1 | Item | After each wrong login attempt, does the account remain usable for at least 3 attempts before locking? | IA-04 | README.md FR-02 | Baseline | AI-Generated | N/A |  |  |  |  |  |
| 9.2 | Item | Does the account lock only after 3 or more consecutive wrong attempts (not fewer)? | IA-04 | README.md FR-02 | Baseline | AI-Generated | N/A |  |  |  |  |  |
| 9.3 | Item | Is the account lockout roughly as short as the documented 30-second demo duration (not dramatically longer)? | IA-04 | README.md FR-02 | Baseline | AI-Generated | N/A |  |  |  |  |  |
| 9.4 | Item | On successful login, does the session persist (e.g. survive a page reload) as expected of a stored auth token? | IA-04 | README.md FR-02 | Baseline | AI-Generated | N/A |  |  |  |  |  |
| 9.5 | Item | Does the login-failure message avoid leaking which specific detail (email vs. password) was wrong? | IA-04 | README.md FR-02 | Baseline | AI-Generated | N/A |  |  |  |  |  |
| 9.7 | Item | While the login request is in flight, does the submit button switch to a loading/disabled state? | IA-04 | README.md FR-24 (feedback/state principle) | Baseline | AI-Generated | N/A |  |  |  |  |  |
| 9.8 | Item | When a login error occurs, does focus move to the first field in error? | IA-04 | README.md FR-24 (feedback/state principle) | Baseline | AI-Generated | N/A |  |  |  |  |  |
| 9.9 | Item | Is the first input field automatically focused when the form loads? | IA-04 | README.md FR-24 (feedback/state principle) | Baseline | AI-Generated | N/A |  |  |  |  |  |
| 10 | Section | ACCESSIBILITY & ADVANCED UI (LOGIN) -- not covered by README, added because HW03 explicitly names these as commonly AI-missed categories | IA-01 | N/A | N/A | AI-Generated | N/A |  |  |  |  |  |
| 10.1 | Item | Are form labels programmatically associated with their inputs? | IA-01 | WCAG 2.1 (accessibility) | Baseline | AI-Generated | N/A |  |  |  |  |  |
| 10.2 | Item | Does the screen support dark mode? | IA-01 | WCAG 2.1 / general accessibility | Baseline | AI-Generated | N/A |  |  |  |  |  |

