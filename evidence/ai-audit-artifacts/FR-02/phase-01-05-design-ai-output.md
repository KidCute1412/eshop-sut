# AI Audit - FR-02 Login and Account Lockout

| Field             | Value                                                        |
| ----------------- | ------------------------------------------------------------ |
| Feature ID        | FR-02                                                        |
| Feature Name      | Login and Account Lockout                                    |
| Generated At      | 2026-06-26 08:37:48 +07:00                                   |
| AI Tool           | ChatGPT 5.5                                                  |
| Skill             | domain-testing-bva                                           |
| Scope             | Preserve FR-02 AI/report outputs in a phase-separated audit. |
| Human Review      | Pending                                                      |
| Human Corrections | None yet                                                     |

## Phase 1-2: Feature Intake and Black-box Test Basis Collection

Output file: `reports/FR-02/requirement-analysis.md`

```markdown
# Requirement Analysis - FR-02 Login and Account Lockout

## Feature Intake

| Field                 | Value                                                                                                                                                   |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Feature ID            | FR-02                                                                                                                                                   |
| Feature Name          | Login and Account Lockout                                                                                                                               |
| Pool                  | A                                                                                                                                                       |
| Actor                 | Guest, unauthenticated user, or user attempting to authenticate                                                                                         |
| Application Surface   | EShop User Web login form and public login API                                                                                                          |
| Requirement Source    | `README.md` - FR-02 and Shared Form Requirements; `api_specification.md` - `POST /api/login`; `2026.HW02.Domain Testing_En.pdf`                         |
| Public API Endpoint   | `POST /api/login`                                                                                                                                       |
| API Base URL          | `http://localhost:3000`                                                                                                                                 |
| UI Location           | `/login`                                                                                                                                                |
| Output Directory      | `reports/FR-02/`                                                                                                                                        |
| Execution Environment | Not started or inspected; Phase 1-5 design only                                                                                                         |
| Pool Rule Review      | FR-02 is listed under Pool A in the official assignment PDF. The supplied Pool A classification is consistent. No other feature allocation was assumed. |

## Approved Black-box Test Bases

| Test Basis                                     | Type                    | Use in This Analysis                                                                                                                                     |
| ---------------------------------------------- | ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `2026.HW02.Domain Testing_En.pdf`              | Official requirement    | Identifies FR-02 Login and account lockout as a Pool A feature and establishes the individual, AI-audited assignment context.                            |
| `README.md` - FR-02                            | Official requirement    | Defines login inputs, failed-attempt incrementing, account lockout threshold and duration, login success token behaviour, and Email control type.        |
| `README.md` - Shared Form Requirements (FR-22) | Official requirement    | Defines required-field markers, Email and Password control types, error placement, and the conditional multi-step indicator rule.                        |
| `api_specification.md` - `POST /api/login`     | API specification       | Defines the public method, endpoint, JSON request example, and documented successful response containing JWT `token` and `user` information.             |
| Public UI observations                         | Observable UI behaviour | Not used. The application was not started, and no previously recorded public UI observation was supplied as a test basis for FR-02 in this design phase. |

No implementation source, internal test, database record/schema, controller, route, service, middleware, model, or inferred implementation behaviour was used.

## Requirement Rules

| Rule ID  | Rule                                                                              | Test Basis Type      | Test Basis Reference | Observable Expected Behaviour                                                                                                                       | Ambiguity                                                                                                                           | Assumption                                                                                                 |
| -------- | --------------------------------------------------------------------------------- | -------------------- | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| FR02-R01 | The user enters Email and Password to log in.                                     | Official requirement | `README.md` - FR-02  | A login attempt uses both an Email value and a Password value.                                                                                      | The exact UI labels, placeholder text, and whether the login identifier can be username instead of email are not specified.         | The login identifier is Email because FR-02 and the API contract name `email`.                             |
| FR02-R02 | Email is required for login.                                                      | Official requirement | `README.md` - FR-02  | A login attempt without Email is not accepted as a valid login.                                                                                     | Missing, empty, whitespace-only, and null Email handling are not distinguished.                                                     | Requiredness follows from the statement that the user enters Email and from the documented API body.       |
| FR02-R03 | Password is required for login.                                                   | Official requirement | `README.md` - FR-02  | A login attempt without Password is not accepted as a valid login.                                                                                  | Missing, empty, whitespace-only, and null Password handling are not distinguished.                                                  | Requiredness follows from the statement that the user enters Password and from the documented API body.    |
| FR02-R04 | A correct Email and Password combination logs the user in successfully.           | Official requirement | `README.md` - FR-02  | A valid login reaches an authenticated outcome and obtains the documented token behaviour.                                                          | The exact UI success message, route after login, and visible authenticated indicator are not specified.                             | Existing account with matching password is the nominal valid-credentials state.                            |
| FR02-R05 | A failed login attempt increments the failed-attempt counter by exactly one unit. | Official requirement | `README.md` - FR-02  | After each failed login, the public behaviour reflects one additional consecutive failed attempt for that account.                                  | The counter is not directly exposed; reset timing, per-account versus per-email scope, and persistence across sessions are unclear. | Counter effects may be inferred only through public lockout behaviour, not hidden storage.                 |
| FR02-R06 | Three or more consecutive failed login attempts temporarily lock the account.     | Official requirement | `README.md` - FR-02  | At the third consecutive failed attempt and beyond, the account enters a locked state.                                                              | Whether different invalid credential types count equally is not explicitly enumerated.                                              | Wrong password for an existing account is the cleanest representative of a failed login.                   |
| FR02-R07 | The lockout duration is 30 seconds in the demo environment.                       | Official requirement | `README.md` - FR-02  | A locked account remains temporarily locked for the documented 30-second duration and should no longer be rejected solely for lockout after expiry. | Exact timing precision, start time, clock source, and behaviour exactly at 30.000 seconds are unspecified.                          | Use whole-second observations for BVA and record timing precision as a test assumption.                    |
| FR02-R08 | During lockout, the system returns an appropriate error message.                  | Official requirement | `README.md` - FR-02  | Login while locked produces an observable error rather than successful authentication.                                                              | The exact text, status code, response body, and UI placement for the lockout error are unspecified.                                 | The error must be visible through the public UI/API surface used for the login attempt.                    |
| FR02-R09 | Lockout and failed-login errors must not reveal detailed cause information.       | Official requirement | `README.md` - FR-02  | Invalid or locked login responses avoid exposing sensitive account-existence or internal cause details.                                             | The allowed and prohibited wording is not defined; the exact non-leaky message cannot be asserted.                                  | Treat obvious disclosure of account existence or internal lockout cause details as non-conforming.         |
| FR02-R10 | Successful login returns a JWT token.                                             | Official requirement | `README.md` - FR-02  | Successful login produces a JWT token through the public response or observable client state.                                                       | The JWT claims, expiry, signing details, and exact token format beyond being a token are unspecified.                               | Token structure is not decoded or validated beyond observable presence unless a public contract states it. |
| FR02-R11 | The token is stored on the client side.                                           | Official requirement | `README.md` - FR-02  | After successful UI login, the token is observable in client-side storage available to the web application.                                         | Storage location, key name, persistence lifetime, and security attributes are unspecified.                                          | Only public browser-observable storage is in scope; no implementation source is inspected.                 |
| FR02-R12 | Authenticated requests send the token using `Authorization: Bearer <token>`.      | Official requirement | `README.md` - FR-02  | A request requiring authentication includes the documented Authorization header shape.                                                              | Which post-login request must be inspected is not specified by FR-02; header timing and target endpoint are unspecified.            | Use a documented authenticated API such as `GET /api/users/me` only after a successful login.              |
| FR02-R13 | The login Email field must use `type="email"` and HTML5 email validation.         | Official requirement | `README.md` - FR-02  | The public login Email control exposes standard email-input behaviour.                                                                              | Browser-specific validation text and full accepted email grammar are unspecified.                                                   | This rule applies to the EShop User Web login form, not to the API request body unless separately stated.  |

## API Specification Rules

| Rule ID    | Rule                                                                                    | Test Basis Type   | Test Basis Reference                                        | Observable Expected Behaviour                                                                    | Ambiguity                                                                                                                 | Assumption                                                                                     |
| ---------- | --------------------------------------------------------------------------------------- | ----------------- | ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| FR02-API01 | Public login uses HTTP `POST /api/login`.                                               | API specification | `api_specification.md` - `POST /api/login`                  | A login request is submitted to the documented method and endpoint.                              | Authentication headers and content-type requirements are not fully specified.                                             | The endpoint is public because it is the supplied authentication contract.                     |
| FR02-API02 | The documented JSON login request contains `email`.                                     | API specification | `api_specification.md` - `POST /api/login` request body     | The documented API request body contains an `email` property. such as `test@domain.com`.         | Requiredness, type enforcement, format-error response, normalization, and case handling are unspecified.                  | API `email` corresponds to the FR-02 Email login field.                                        |
| FR02-API03 | The documented JSON login request contains `password`.                                  | API specification | `api_specification.md` - `POST /api/login` request body     | The documented API request body contains a `password` property. such as `Password123!`.          | Requiredness, empty handling, invalid-input status, and message are unspecified.                                          | API `password` corresponds to the FR-02 Password login field.                                  |
| FR02-API04 | A documented successful login returns `200 OK` with JWT `token` and `user` information. | API specification | `api_specification.md` - `POST /api/login` success response | A successful request returns HTTP 200 and a response body containing token and user information. | The exact `user` schema, token claims, additional fields, headers, and whether the example is exhaustive are unspecified. | Treat presence of `token` and `user` as the success contract; do not assume exact user fields. |
| FR02-API05 | Authenticated user APIs require `Authorization: Bearer <token>`.                        | API specification | `api_specification.md` - Users section                      | Authenticated API requests use the documented Bearer token header shape.                         | Exact unauthorized status, response body, and token validation errors are unspecified.                                    | This supports FR02-R12 without inspecting implementation source.                               |
| FR02-API06 | `GET /api/users/me` is a documented authenticated endpoint.                             | API specification | `api_specification.md` - `GET /api/users/me`                | After a successful login, this endpoint can be used as a public authenticated request surface.   | Exact success response schema is not specified.                                                                           | Use it only to observe authenticated request behaviour after obtaining a token.                |

## Shared Form Rules

| Rule ID   | Rule                                                                                    | Test Basis Type      | Test Basis Reference                           | Observable Expected Behaviour                                           | Ambiguity                                                                                   | Assumption                                                                                          |
| --------- | --------------------------------------------------------------------------------------- | -------------------- | ---------------------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| FR02-SF01 | Every required field has a `*` beside its label.                                        | Official requirement | `README.md` - Shared Form Requirements (FR-22) | Required login controls visibly show `*` adjacent to their labels.      | FR-22 does not define exact label text or styling.                                          | Email and Password are required for login.                                                          |
| FR02-SF02 | The Email field uses `type="email"`.                                                    | Official requirement | `README.md` - Shared Form Requirements (FR-22) | The login Email control exposes `type="email"`.                         | This duplicates FR02-R13 but FR-22 applies the rule broadly to forms.                       | Keep it as shared-form traceability; do not create a separate API format oracle from it.            |
| FR02-SF03 | The Password field uses `type="password"` and does not display its value in clear text. | Official requirement | `README.md` - Shared Form Requirements (FR-22) | Entered password characters are masked in the public login form.        | Browser-specific masking display is not specified.                                          | This governs the UI Password control only.                                                          |
| FR02-SF04 | Form error messages appear above the submit button, not below it.                       | Official requirement | `README.md` - Shared Form Requirements (FR-22) | Any displayed login validation or authentication error is above Submit. | Exact text, styling, multiple-error order, inline field errors, and timing are unspecified. | Applies to UI errors that the login form displays.                                                  |
| FR02-SF05 | Forms with two or more steps display a clear Step Indicator.                            | Official requirement | `README.md` - Shared Form Requirements (FR-22) | If login is a multi-step form, a visible step indicator is shown.       | Neither FR-02 nor the API specification states that login has two or more steps.            | Do not require a Step Indicator unless an approved test basis establishes that login is multi-step. |

## Shared Form Rules Relevant to FR-02

| Rule ID   | Rule                                                 | Test Basis Type      | Test Basis Reference | Observable Expected Behaviour                                                          | Ambiguity                                                      | Assumption                                                 |
| --------- | ---------------------------------------------------- | -------------------- | -------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------- | ---------------------------------------------------------- |
| FR02-SF01 | Required login fields display adjacent `*` markers.  | Official requirement | `README.md` - FR-22  | Email and Password labels show required-field markers.                                 | Exact visual spacing and styling are unspecified.              | Email and Password are required login fields.              |
| FR02-SF02 | The login Password field uses `type="password"`.     | Official requirement | `README.md` - FR-22  | Password input masks entered characters.                                               | Whether visibility-toggle controls are allowed is unspecified. | Masking is required unless explicitly toggled by the user. |
| FR02-SF03 | Login error messages appear above the submit button. | Official requirement | `README.md` - FR-22  | A displayed login validation or authentication error appears above the submit control. | Exact message text is unspecified.                             | This applies when the login form displays an error.        |
| FR02-SF04 | Step Indicator is not applicable to the login form.  | Official requirement | `README.md` - FR-22  | No step indicator is required for a one-step login form.                               | If the login flow becomes multi-step, this must be reassessed. | FR-02 login is treated as a one-step form.                 |

## Requirement Ambiguities

- The exact login UI path is not specified in the approved requirement text; `/login` is used as the conventional public UI location for this feature.
- Exact invalid-credential, missing-field, and lockout API status codes and response bodies are unspecified.
- Exact UI error message text, styling, and timing are unspecified.
- The non-leakage rule says not to expose detailed cause information, but does not define the allowed wording.
- Failed-attempt counter visibility, storage, reset conditions, and scope are unspecified.
- Whether failed attempts for non-existing accounts count toward lockout is unspecified.
- Whether successful login resets the failed-attempt counter is unspecified.
- Email case sensitivity, normalization, whitespace trimming, and Unicode handling are unspecified.
- The exact meaning of "30 seconds" at the instant of expiry and the tolerated timing precision are unspecified.
- The exact post-login redirect target, authenticated UI state, token storage key, token storage mechanism, and token lifetime are unspecified.
- The API success response does not define the `user` object schema.
- It is not established whether login is single-step or multi-step, so the Step Indicator rule cannot yet be classified as applicable.

## Assumptions

- FR-02 covers the public user-facing login form and public login API, not admin-only authentication.
- The documented default user account `test@eshop.com` / `Test1234!` may be used later as a controlled existing account during execution, but this design phase does not inspect database records.
- Wrong password for an existing controlled account is the primary representative for invalid credentials and failed attempts.
- Public lockout behaviour is the only approved way to infer failed-attempt counter changes; hidden counter storage is not inspected.
- No undocumented validation rule, status code, message, token claim, storage key, redirect URL, or implementation behaviour is assumed.

## Coverage Gaps

## Coverage Gaps

- An authoritative clarification is needed for all ambiguities listed above before they can become exact expected results.
- No approved public UI observation was available in this design phase, so actual controls, labels, navigation target, token storage location, and messages have not been corroborated observationally.
- The API specification documents the successful `POST /api/login` response and authenticated Bearer-token usage, but it does not define exact invalid-login, missing-field, malformed-email, wrong-password, or lockout response status/body contracts.
- `GET /api/users/me` is documented as an authenticated endpoint and may be used as a public surface to observe Bearer-token usage, but its exact response schema is not specified.
- Reset/unlock semantics beyond the documented 30-second lockout duration are not fully specified.
- This Phase 1-2 analysis records test bases and rules only. Partitions, boundaries, and test cases are created separately in later sections and remain unexecuted pending human review.

## Human Review - Phase 1 and Phase 2

- Reviewer: Nguyen Thanh Tien
- Review Date and Time: 2026-06-26 08:30 GMT+7
- Review Scope: Feature Intake and Black-box Test Basis Collection for FR-02
- Corrections Made:
  - Refined API login request rules to avoid overclaiming undocumented validation behaviour.
  - Added Bearer-token and `GET /api/users/me` API basis for authenticated request checking.
  - Added relevant shared-form rules for required markers, email/password controls, error placement, and step-indicator applicability.
  - Updated coverage gaps to reflect missing invalid-login, missing-field, lockout, and exact response contracts.
  - Confirmed that no implementation source, database, internal route, service, or hidden state was used as a test basis.

- Missing Rules or Test Bases: None after review.
- Status: Completed
- Approved for Domain Modeling: Yes
- Approved for Test Execution: No
```

## Phase 3: Domain Modeling

Output file: `reports/FR-02/domain-testing.md`

```markdown
# Domain Testing - FR-02 Login and Account Lockout

## Black-box Test Basis Summary

- This model is based on `reports/FR-02/requirement-analysis.md`, which uses only approved black-box test bases.
- No implementation source, database, internal tests, or execution behaviour was used.
- No test execution, screenshots, Pass/Fail results, or bugs are created in this phase.
- BVA is handled separately in `boundary-value-analysis.md`; test cases are handled separately in `test-cases.md`.

## Step 1. Identify Input & Output Variables

| Type              | Variable or Output                      | Description                                                                                       | Related Rule IDs                       | Applies To |
| ----------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------- | -------------------------------------- | ---------- |
| Input             | Email                                   | Login identifier supplied by the user or API request body.                                        | FR02-R01, FR02-R02, FR02-API02         | UI and API |
| Input             | Password                                | Credential secret supplied by the user or API request body.                                       | FR02-R01, FR02-R03, FR02-API03         | UI and API |
| State / Condition | Account identity state                  | Whether the supplied Email corresponds to a controlled existing account.                          | FR02-R04, FR02-R09                     | UI and API |
| State / Condition | Credential match relation               | Whether supplied Email and Password match a valid account.                                        | FR02-R04, FR02-R05                     | UI and API |
| State / Condition | Consecutive failed-attempt count        | Publicly inferred count of consecutive failed logins for an account.                              | FR02-R05, FR02-R06                     | UI and API |
| State / Condition | Account lockout state                   | Whether account is unlocked, newly locked, or locked due to too many consecutive failed attempts. | FR02-R06, FR02-R07, FR02-R08           | UI and API |
| State / Condition | Lockout elapsed time                    | Time elapsed after lockout begins relative to the documented 30-second duration.                  | FR02-R07                               | UI and API |
| Input             | API request body                        | JSON representation containing `email` and `password`.                                            | FR02-API02, FR02-API03                 | API        |
| State / Condition | Guest or unauthenticated actor state    | Actor attempting to authenticate before login succeeds.                                           | Feature Intake, FR02-API01             | UI and API |
| Output            | API success response                    | Successful login returns `200 OK` with JWT `token` and `user` information.                        | FR02-API04, FR02-R10                   | API        |
| Output            | UI successful login outcome             | Successful UI login reaches an authenticated state; exact redirect is unspecified.                | FR02-R04, FR02-R10, FR02-R11           | UI         |
| Output            | JWT token availability                  | Token is present after successful login.                                                          | FR02-R10                               | UI and API |
| Output            | Client-side token storage               | Token is stored on the client side after successful UI login.                                     | FR02-R11                               | UI         |
| Output            | Authorization header usage              | Authenticated requests use `Authorization: Bearer <token>`.                                       | FR02-R12                               | UI/API     |
| Output            | Validation or authentication rejection  | Invalid, missing, or locked login attempts are rejected.                                          | FR02-R02, FR02-R03, FR02-R08, FR02-R09 | UI and API |
| Output            | UI required-field markers               | `*` appears beside required Email and Password labels.                                            | FR02-SF01                              | UI         |
| Output            | Email input control type                | Email control exposes `type="email"` and HTML5 email validation.                                  | FR02-R13, FR02-SF02                    | UI         |
| Output            | Password input control type and masking | Password control uses `type="password"` and does not show clear text.                             | FR02-SF03                              | UI         |
| Output            | Error-message placement                 | Displayed form errors appear above the submit button.                                             | FR02-SF04                              | UI         |

## Step 2. Identify Equivalence Classes

### Normative partitions

| Partition ID                  | Type              | Variable or Condition               | Equivalence Class Description                                                                  | Validity | Representative Value                                                        | Dependencies                                                    | Rule IDs             | Test Basis Reference                         | Assumptions                                                 |
| ----------------------------- | ----------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------- | -------- | --------------------------------------------------------------------------- | --------------------------------------------------------------- | -------------------- | -------------------------------------------- | ----------------------------------------------------------- |
| LOGIN-EMAIL-PRESENCE-V01      | Input             | Email                               | Email is provided.                                                                             | Valid    | `test@eshop.com`                                                            | Password nominal.                                               | FR02-R01, FR02-R02   | `requirement-analysis.md` - FR02-R01/R02     | Existing account state controlled at execution.             |
| LOGIN-EMAIL-PRESENCE-I01      | Input             | Email                               | Email is missing or empty.                                                                     | Invalid  | empty Email field / JSON without `email`                                    | Password nominal.                                               | FR02-R02             | `requirement-analysis.md` - FR02-R02         | Missing and empty share the "not provided" outcome.         |
| LOGIN-EMAIL-FORMAT-V01        | Input             | Email                               | UI Email value satisfies HTML5 email validation.                                               | Valid    | `test@eshop.com`                                                            | Email control uses `type="email"`.                              | FR02-R13, FR02-SF02  | `requirement-analysis.md` - FR02-R13/SF02    | UI-only normative format behaviour from HTML5 type rule.    |
| LOGIN-EMAIL-FORMAT-I01        | Input             | Email                               | UI Email value does not satisfy HTML5 email validation.                                        | Invalid  | `not-an-email`                                                              | Email control uses `type="email"`; Password nominal.            | FR02-R13, FR02-SF02  | `requirement-analysis.md` - FR02-R13/SF02    | Browser-specific message is not asserted.                   |
| LOGIN-PASSWORD-PRESENCE-V01   | Input             | Password                            | Password is provided.                                                                          | Valid    | `Test1234!`                                                                 | Email nominal.                                                  | FR02-R01, FR02-R03   | `requirement-analysis.md` - FR02-R01/R03     | Uses documented default user credential as controlled data. |
| LOGIN-PASSWORD-PRESENCE-I01   | Input             | Password                            | Password is missing or empty.                                                                  | Invalid  | empty Password field / JSON without `password`                              | Email nominal.                                                  | FR02-R03             | `requirement-analysis.md` - FR02-R03         | No null semantics inferred.                                 |
| LOGIN-CREDENTIALS-V01         | State / Condition | Credential match relation           | Email and Password match an existing account.                                                  | Valid    | `test@eshop.com` / `Test1234!`                                              | Account not locked.                                             | FR02-R04, FR02-R10   | `requirement-analysis.md` - FR02-R04/R10     | Account exists as controlled public test data.              |
| LOGIN-CREDENTIALS-I01         | State / Condition | Credential match relation           | Email exists but Password is incorrect.                                                        | Invalid  | `test@eshop.com` / `WrongPass123!`                                          | Account not locked before attempt.                              | FR02-R05, FR02-R09   | `requirement-analysis.md` - FR02-R05/R09     | Wrong password is a failed login.                           |
| LOGIN-ACCOUNT-EXISTS-V01      | State / Condition | Account identity state              | Login identity corresponds to an existing account.                                             | Valid    | `test@eshop.com`                                                            | Matching password for success, wrong password for failure.      | FR02-R04             | `requirement-analysis.md` - FR02-R04         | Existing state is a precondition, not database inspection.  |
| LOGIN-ACCOUNT-EXISTS-I01      | State / Condition | Account identity state              | Login identity does not correspond to an existing account.                                     | Invalid  | `no.such.user@example.com`                                                  | Password otherwise nominal.                                     | FR02-R09             | `requirement-analysis.md` - FR02-R09         | Expected rejection must avoid account-enumeration detail.   |
| LOGIN-FAILED-INCREMENT-V01    | State / Condition | Failed-attempt count                | Each failed login increases the consecutive failed-attempt count by exactly 1.                 | Valid    | first wrong-password attempt changes count from 0 to 1                      | Counter observed only through later public lockout behaviour.   | FR02-R05             | `requirement-analysis.md` - FR02-R05         | Hidden count is not inspected.                              |
| LOGIN-FAILED-INCREMENT-I01    | State / Condition | Failed-attempt count                | Failed login does not increase by exactly 1.                                                   | Invalid  | counter skips, does not change, or increments more than one                 | Observable only through lockout timing/threshold contradiction. | FR02-R05             | `requirement-analysis.md` - FR02-R05         | Exact hidden value is not asserted.                         |
| LOGIN-LOCKOUT-BELOW-V01       | State / Condition | Failed-attempt threshold            | Fewer than 3 consecutive failed attempts has not yet reached the documented lockout threshold. | Valid    | 2 consecutive wrong-password attempts                                       | Same existing account; no previous lockout.                     | FR02-R06             | `requirement-analysis.md` - FR02-R06         | Below-threshold behaviour inferred from "3 or more".        |
| LOGIN-LOCKOUT-THRESHOLD-V01   | State / Condition | Failed-attempt threshold            | 3 or more consecutive failed attempts locks the account.                                       | Valid    | 3 consecutive wrong-password attempts                                       | Same existing account.                                          | FR02-R06             | `requirement-analysis.md` - FR02-R06         | Threshold is inclusive.                                     |
| LOGIN-LOCKOUT-NOT-APPLIED-I01 | Output            | Account lockout state               | Account is not locked after 3 or more consecutive failed attempts.                             | Invalid  | valid password accepted immediately after three consecutive failures        | Same existing account.                                          | FR02-R06             | `requirement-analysis.md` - FR02-R06         | Non-conforming observable outcome.                          |
| LOGIN-LOCKOUT-ACTIVE-V01      | State / Condition | Account lockout state               | Locked account rejects login during active 30-second lockout.                                  | Valid    | correct password attempted shortly after third failure                      | Account locked first.                                           | FR02-R07, FR02-R08   | `requirement-analysis.md` - FR02-R07/R08     | Exact message is unspecified.                               |
| LOGIN-LOCKOUT-EXPIRED-V01     | State / Condition | Lockout elapsed time                | After the documented 30-second duration, account is no longer rejected solely due lockout.     | Valid    | correct password after lockout duration expires                             | Account was locked; credentials correct.                        | FR02-R07             | `requirement-analysis.md` - FR02-R07         | Whole-second timing tolerance needed.                       |
| LOGIN-ERROR-NONLEAKY-V01      | Output            | Error information disclosure        | Invalid or locked login error avoids detailed cause disclosure.                                | Valid    | generic invalid/locked error                                                | Invalid or locked attempt.                                      | FR02-R09             | `requirement-analysis.md` - FR02-R09         | Exact allowed text is unknown.                              |
| LOGIN-ERROR-LEAKY-I01         | Output            | Error information disclosure        | Error reveals sensitive cause details such as account existence or internal counter details.   | Invalid  | message explicitly says account exists/non-exists or exposes internal count | Invalid or locked attempt.                                      | FR02-R09             | `requirement-analysis.md` - FR02-R09         | Clear disclosure is non-conforming.                         |
| API-REQUEST-V01               | API Contract      | Request body                        | JSON contains both `email` and `password`.                                                     | Valid    | `{"email":"test@eshop.com","password":"Test1234!"}`                         | Account not locked.                                             | FR02-API02, API03    | `requirement-analysis.md` - FR02-API02/API03 | Complete documented shape.                                  |
| API-REQUEST-I01               | API Contract      | Request body                        | Required `email` property is missing.                                                          | Invalid  | `{"password":"Test1234!"}`                                                  | Password nominal.                                               | FR02-R02, FR02-API02 | `requirement-analysis.md` - FR02-R02/API02   | No status/body inferred.                                    |
| API-REQUEST-I02               | API Contract      | Request body                        | Required `password` property is missing.                                                       | Invalid  | `{"email":"test@eshop.com"}`                                                | Email nominal.                                                  | FR02-R03, FR02-API03 | `requirement-analysis.md` - FR02-R03/API03   | No status/body inferred.                                    |
| API-SUCCESS-V01               | API Contract      | API success response                | Successful login returns HTTP 200 with JWT `token` and `user` information.                     | Valid    | `200 OK` body containing `token` and `user`                                 | Complete valid API request.                                     | FR02-API04, FR02-R10 | `requirement-analysis.md` - FR02-API04/R10   | Do not assume exact user schema.                            |
| UI-SUCCESS-V01                | Output            | UI successful login outcome         | Successful UI login reaches an authenticated client state.                                     | Valid    | valid login shows logged-in/user state or authenticated navigation          | Valid credentials; account unlocked.                            | FR02-R04, FR02-R10   | `requirement-analysis.md` - FR02-R04/R10     | Exact redirect is unspecified.                              |
| TOKEN-STORAGE-V01             | Output            | Client-side token storage           | Token is stored client-side after successful UI login.                                         | Valid    | token present in public browser-observable storage                          | Successful UI login.                                            | FR02-R11             | `requirement-analysis.md` - FR02-R11         | Storage key/location not fixed.                             |
| AUTHORIZATION-HEADER-V01      | Output            | Authenticated request header        | A post-login authenticated request uses `Authorization: Bearer <token>`.                       | Valid    | `GET /api/users/me` with Bearer token                                       | Successful login produces token.                                | FR02-R12             | `requirement-analysis.md` - FR02-R12         | Uses documented authenticated endpoint.                     |
| VALIDATION-REJECTION-V01      | Output            | Validation or authentication result | Missing, invalid, wrong, or locked login attempt is rejected.                                  | Valid    | rejection for wrong password or missing input                               | Invalid condition selected; other values nominal.               | FR02-R02/R03/R08/R09 | `requirement-analysis.md` - relevant rules   | Exact text/status unspecified.                              |
| FORM-REQUIRED-MARKER-V01      | UI Form Rule      | Required-field markers              | Required Email and Password labels display adjacent `*`.                                       | Valid    | Email and Password labels with `*`                                          | Login form visible.                                             | FR02-SF01            | `requirement-analysis.md` - FR02-SF01        | Required fields are Email and Password.                     |
| FORM-REQUIRED-MARKER-I01      | UI Form Rule      | Required-field markers              | Required Email or Password label lacks adjacent `*`.                                           | Invalid  | Email label without `*`                                                     | Login form visible.                                             | FR02-SF01            | `requirement-analysis.md` - FR02-SF01        | Clear UI conformance violation.                             |
| FORM-EMAIL-TYPE-V01           | UI Form Rule      | Email input control type            | Email control uses `type="email"`.                                                             | Valid    | observable `type="email"`                                                   | Login form visible.                                             | FR02-R13, FR02-SF02  | `requirement-analysis.md` - FR02-R13/SF02    | UI only.                                                    |
| FORM-EMAIL-TYPE-I01           | UI Form Rule      | Email input control type            | Email control does not use `type="email"`.                                                     | Invalid  | observable `type="text"`                                                    | Login form visible.                                             | FR02-R13, FR02-SF02  | `requirement-analysis.md` - FR02-R13/SF02    | UI only.                                                    |
| FORM-PASSWORD-TYPE-V01        | UI Form Rule      | Password input control type/masking | Password control uses `type="password"` and masks input.                                       | Valid    | masked password field                                                       | Login form visible.                                             | FR02-SF03            | `requirement-analysis.md` - FR02-SF03        | UI only.                                                    |
| FORM-PASSWORD-TYPE-I01        | UI Form Rule      | Password input control type/masking | Password control exposes input in clear text or uses a non-password type.                      | Invalid  | visible clear text password field                                           | Login form visible.                                             | FR02-SF03            | `requirement-analysis.md` - FR02-SF03        | UI only.                                                    |
| FORM-ERROR-PLACEMENT-V01      | UI Form Rule      | Error-message placement             | Login error appears above the submit button.                                                   | Valid    | error above Submit                                                          | An invalid UI login triggers a displayed error.                 | FR02-SF04            | `requirement-analysis.md` - FR02-SF04        | Exact text not asserted.                                    |
| FORM-ERROR-PLACEMENT-I01      | UI Form Rule      | Error-message placement             | Login error appears below the submit button.                                                   | Invalid  | error below Submit                                                          | An invalid UI login triggers a displayed error.                 | FR02-SF04            | `requirement-analysis.md` - FR02-SF04        | Clear placement violation.                                  |
| ACTOR-UNAUTHENTICATED-V01     | State / Condition | Actor state                         | User begins login while unauthenticated.                                                       | Valid    | no authenticated session                                                    | Public login available.                                         | Feature Intake       | `requirement-analysis.md` - Feature Intake   | No prior token/session.                                     |

### Ambiguous or exploratory candidates

| Partition ID               | Type              | Variable or Condition        | Equivalence Class Description                                    | Validity | Representative Value                 | Dependencies                     | Rule IDs  | Test Basis Reference                    | Assumptions                                       |
| -------------------------- | ----------------- | ---------------------------- | ---------------------------------------------------------------- | -------- | ------------------------------------ | -------------------------------- | --------- | --------------------------------------- | ------------------------------------------------- |
| LOGIN-EMAIL-WHITESPACE-A01 | Input             | Email                        | Email contains leading/trailing spaces or whitespace-only input. | Invalid  | `" test@eshop.com "` / `"   "`       | Other values nominal.            | FR02-R02  | `requirement-analysis.md` - ambiguities | Classification is ambiguous; no normative oracle. |
| LOGIN-EMAIL-CASE-A01       | State / Condition | Email normalization          | Case variant of the same Email identity is used.                 | Invalid  | `TEST@ESHOP.COM`                     | Controlled account exists.       | FR02-R04  | `requirement-analysis.md` - ambiguities | Case sensitivity is unspecified.                  |
| LOGIN-COUNTER-RESET-A01    | State / Condition | Failed-attempt counter reset | Successful login resets the failed-attempt counter.              | Invalid  | two failures, one success, then fail | Requires controllable account.   | FR02-R05  | `requirement-analysis.md` - ambiguities | Reset semantics are unspecified.                  |
| FORM-STEP-INDICATOR-A01    | UI Form Rule      | Step indicator               | Login form has a clear step indicator if it is multi-step.       | Invalid  | observe login step count/indicator   | Login must be proven multi-step. | FR02-SF05 | `requirement-analysis.md` - FR02-SF05   | Login is not documented as multi-step.            |

## Step 3. Best Representatives

| Partition ID                | Representative Value                                       | Why This Representative Was Chosen                                                | Required Nominal Values for Other Variables                 | Applies To |
| --------------------------- | ---------------------------------------------------------- | --------------------------------------------------------------------------------- | ----------------------------------------------------------- | ---------- |
| LOGIN-EMAIL-PRESENCE-V01    | `test@eshop.com`                                           | Documented default user Email; clearly present.                                   | Password `Test1234!`; account unlocked.                     | UI/API     |
| LOGIN-EMAIL-PRESENCE-I01    | empty Email / omitted `email`                              | Directly isolates missing required Email.                                         | Password nominal.                                           | UI/API     |
| LOGIN-EMAIL-FORMAT-V01      | `test@eshop.com`                                           | Clearly satisfies normal HTML5 email syntax.                                      | Password nominal; Email control type compliant.             | UI         |
| LOGIN-EMAIL-FORMAT-I01      | `not-an-email`                                             | Plainly fails HTML5 email syntax without edge-grammar debate.                     | Password nominal; Email control type compliant.             | UI         |
| LOGIN-PASSWORD-PRESENCE-V01 | `Test1234!`                                                | Documented default user password; clearly present.                                | Email `test@eshop.com`; account unlocked.                   | UI/API     |
| LOGIN-PASSWORD-PRESENCE-I01 | empty Password / omitted `password`                        | Directly isolates missing required Password.                                      | Email nominal.                                              | UI/API     |
| LOGIN-CREDENTIALS-V01       | `test@eshop.com` / `Test1234!`                             | Clearly represents matching controlled credentials.                               | Account unlocked; no prior failed attempts.                 | UI/API     |
| LOGIN-CREDENTIALS-I01       | `test@eshop.com` / `WrongPass123!`                         | Same account, wrong secret isolates invalid credentials.                          | Account unlocked before the attempt.                        | UI/API     |
| LOGIN-ACCOUNT-EXISTS-I01    | `no.such.user@example.com` / `Test1234!`                   | Plainly represents non-existing login identity without needing source inspection. | Password present; account state controlled by public setup. | UI/API     |
| LOGIN-LOCKOUT-BELOW-V01     | 2 consecutive wrong-password attempts                      | Immediately below the documented threshold.                                       | Same existing account; no previous lockout.                 | UI/API     |
| LOGIN-LOCKOUT-THRESHOLD-V01 | 3 consecutive wrong-password attempts                      | Exactly reaches the inclusive lockout threshold.                                  | Same existing account.                                      | UI/API     |
| LOGIN-LOCKOUT-ACTIVE-V01    | correct password attempted during lockout                  | Shows lockout state independent of credential correctness.                        | Account first locked by 3 failed attempts.                  | UI/API     |
| LOGIN-LOCKOUT-EXPIRED-V01   | correct password after lockout expires                     | Represents documented temporary duration.                                         | Account locked first; wait duration elapsed.                | UI/API     |
| API-REQUEST-V01             | `{"email":"test@eshop.com","password":"Test1234!"}`        | Exactly matches documented request shape with nominal values.                     | Account unlocked.                                           | API        |
| API-REQUEST-I01             | `{"password":"Test1234!"}`                                 | Isolates missing `email`.                                                         | Password nominal.                                           | API        |
| API-REQUEST-I02             | `{"email":"test@eshop.com"}`                               | Isolates missing `password`.                                                      | Email nominal.                                              | API        |
| API-SUCCESS-V01             | `200 OK` with `token` and `user`                           | Captures every documented success element without inventing user schema.          | Complete valid API request.                                 | API        |
| UI-SUCCESS-V01              | authenticated UI state after valid login                   | Observable success without fixing redirect URL.                                   | Valid credentials; account unlocked.                        | UI         |
| TOKEN-STORAGE-V01           | token present in browser-observable client storage         | Directly represents client-side token storage.                                    | Successful UI login.                                        | UI         |
| AUTHORIZATION-HEADER-V01    | authenticated request with `Authorization: Bearer <token>` | Matches documented header shape.                                                  | Token available after login.                                | UI/API     |
| FORM-REQUIRED-MARKER-I01    | Email label lacks `*`                                      | Email requiredness is explicit.                                                   | Login form visible.                                         | UI         |
| FORM-EMAIL-TYPE-I01         | Email control exposes `type="text"`                        | Clear non-compliant alternative to required type.                                 | Login form visible.                                         | UI         |
| FORM-PASSWORD-TYPE-I01      | Password visible in clear text                             | Clear violation of password masking.                                              | Login form visible.                                         | UI         |
| FORM-ERROR-PLACEMENT-I01    | error below Submit                                         | Exact prohibited placement.                                                       | Invalid login triggers UI error.                            | UI         |
| ACTOR-UNAUTHENTICATED-V01   | no authenticated session                                   | Directly represents public login actor state.                                     | Login page/API available.                                   | UI/API     |

## Partition Derivation

- `LOGIN-EMAIL-PRESENCE-V01/I01` and `LOGIN-PASSWORD-PRESENCE-V01/I01` follow from FR02-R01 through FR02-R03 and the API request body. Present values are valid; omitted/empty values are invalid. Other variables remain nominal.
- `LOGIN-EMAIL-FORMAT-V01/I01` follows from FR02-R13 and FR02-SF02 for the UI Email field. A normal address is valid and `not-an-email` is invalid under the HTML5 email-input rule; exact browser message is not asserted.
- `LOGIN-CREDENTIALS-V01/I01` follows from successful login and failed-login rules. Matching credentials are valid; wrong password for an existing account is invalid and increments failed attempts.
- `LOGIN-ACCOUNT-EXISTS-V01/I01` separates existing and non-existing identity states because successful login requires an account while non-existing identity must not disclose detailed cause information.
- `LOGIN-FAILED-INCREMENT-V01/I01`, `LOGIN-LOCKOUT-BELOW-V01`, `LOGIN-LOCKOUT-THRESHOLD-V01`, and `LOGIN-LOCKOUT-NOT-APPLIED-I01` follow from the exact one-unit increment rule and inclusive threshold of 3 failed attempts.
- `LOGIN-LOCKOUT-ACTIVE-V01` and `LOGIN-LOCKOUT-EXPIRED-V01` follow from the documented 30-second temporary lockout. They depend on first reaching lockout through public failed attempts.
- `LOGIN-ERROR-NONLEAKY-V01/I01` follows from the requirement not to expose detailed cause information. Exact text is ambiguous, so only clearly leaky details are treated as invalid.
- `API-REQUEST-V01/I01/I02` and `API-SUCCESS-V01` follow from the documented `POST /api/login` request and success contract.
- `UI-SUCCESS-V01`, `TOKEN-STORAGE-V01`, and `AUTHORIZATION-HEADER-V01` follow from successful login token requirements. Exact redirect, storage key, and post-login request target remain assumptions/gaps.
- `FORM-REQUIRED-MARKER`, `FORM-EMAIL-TYPE`, `FORM-PASSWORD-TYPE`, and `FORM-ERROR-PLACEMENT` partitions follow from shared form requirements and apply only to UI.
- `ACTOR-UNAUTHENTICATED-V01` follows from the public login feature: the user begins unauthenticated and becomes authenticated only after success.
- The four `A01` candidates are not normative expected behaviour because whitespace, case normalization, counter reset, and step count are not specified.

## Coverage Decisions

- Normative coverage includes required Email/Password presence, UI Email format validation, valid credentials, invalid credentials, existing/non-existing identity, failed-attempt increment, lockout threshold, active/expired lockout, non-leaky errors, API request/response, UI token/client state, Authorization header, shared form rules, and unauthenticated actor state.
- Ambiguous/exploratory candidates are excluded from normative coverage: Email whitespace, Email case normalization, failed-attempt reset semantics, and Step Indicator applicability.
- BVA is reserved for the ordered failed-attempt threshold and 30-second lockout duration.
- Test-case derivation must cover applicable partitions on both UI and API surfaces unless a rule is UI-only or API-only.
- Exact invalid API status codes, exact UI/API error text, exact redirect URL, token claims, token storage key, and hidden counter values are intentionally not asserted.

## Human Review - Phase 3

- Reviewer:
- Review Date and Time:
- Review Scope: Domain Modeling for FR-02 Login and Account Lockout
- Corrections Made:
- Missing Partitions Added:
- Duplicate Partitions Removed:
- Status: Pending
- Approved for BVA: No
- Approved for Test-Case Derivation: No
- Approved for Test Execution: No
```

## Phase 4: Boundary Value Analysis

Output file: `reports/FR-02/boundary-value-analysis.md`

```markdown
# Boundary Value Analysis - FR-02 Login and Account Lockout

## Step 1: Candidate Domain Assessment

| Domain or Variable              | Rule ID             | Domain Type                     | Documented Constraint                                         | BVA Applicability                        | Reason                                                                                                | Test Basis Reference                                                              |
| ------------------------------- | ------------------- | ------------------------------- | ------------------------------------------------------------- | ---------------------------------------- | ----------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Email presence                  | FR02-R02            | Categorical presence            | Email must be provided.                                       | Not applicable                           | Present/absent is categorical.                                                                        | `domain-testing.md` - LOGIN-EMAIL-PRESENCE                                        |
| Password presence               | FR02-R03            | Categorical presence            | Password must be provided.                                    | Not applicable                           | Present/absent is categorical.                                                                        | `domain-testing.md` - LOGIN-PASSWORD-PRESENCE                                     |
| Credential match                | FR02-R04, FR02-R05  | Relational category             | Credentials match or do not match.                            | Not applicable                           | Match/mismatch is not ordered.                                                                        | `domain-testing.md` - LOGIN-CREDENTIALS                                           |
| Account existence               | FR02-R04, FR02-R09  | State category                  | Existing or non-existing identity.                            | Not applicable                           | Identity state is unordered.                                                                          | `domain-testing.md` - LOGIN-ACCOUNT-EXISTS                                        |
| Failed-attempt count            | FR02-R05, FR02-R06  | Inclusive lower threshold count | Account locks at 3 or more consecutive failed login attempts. | Applicable                               | Explicit ordered integer threshold supports count BVA.                                                | `requirement-analysis.md` - FR02-R05/R06; `domain-testing.md` - LOGIN-LOCKOUT     |
| Failed-attempt increment amount | FR02-R05            | Count delta                     | Failed login increments counter by exactly 1.                 | Applicable through threshold observation | The hidden delta is not directly observable, but threshold BVA can expose incorrect public behaviour. | `requirement-analysis.md` - FR02-R05                                              |
| Lockout duration                | FR02-R07            | Time duration                   | Temporary lockout lasts 30 seconds in demo environment.       | Applicable                               | Explicit time boundary supports duration BVA using whole seconds.                                     | `requirement-analysis.md` - FR02-R07; `domain-testing.md` - LOGIN-LOCKOUT-EXPIRED |
| Error non-disclosure            | FR02-R09            | Message-content category        | Do not reveal detailed cause.                                 | Not applicable                           | Disclosure categories are semantic, not numeric.                                                      | `domain-testing.md` - LOGIN-ERROR-NONLEAKY                                        |
| API request properties          | FR02-API02, API03   | Contract structure              | Request contains `email` and `password`.                      | Not applicable                           | Named-property presence is categorical.                                                               | `domain-testing.md` - API-REQUEST                                                 |
| Email control type              | FR02-R13, FR02-SF02 | UI property                     | Email control uses `type="email"`.                            | Not applicable                           | Control type is categorical.                                                                          | `domain-testing.md` - FORM-EMAIL-TYPE                                             |
| Password control type/masking   | FR02-SF03           | UI property                     | Password uses `type="password"` and is masked.                | Not applicable                           | Type and visibility are categorical.                                                                  | `domain-testing.md` - FORM-PASSWORD-TYPE                                          |
| Error placement                 | FR02-SF04           | UI spatial category             | Error appears above Submit.                                   | Not applicable                           | Placement categories are not numeric boundaries.                                                      | `domain-testing.md` - FORM-ERROR-PLACEMENT                                        |

## Step 2: Applicable Boundary Models

| Boundary Model ID         | Variable                          | Rule               | Test Basis                                        | Boundary Type             | Off Point          | On Point           | In Point           | Nominal Internal Value | Expected Classification                                           | Justification                                                                                                 |
| ------------------------- | --------------------------------- | ------------------ | ------------------------------------------------- | ------------------------- | ------------------ | ------------------ | ------------------ | ---------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| FR02-FAILED-ATTEMPTS-M01  | Consecutive failed login attempts | Lockout threshold  | FR02-R05, FR02-R06; LOGIN-LOCKOUT-BELOW/THRESHOLD | Inclusive lower-only      | 2 failed attempts  | 3 failed attempts  | 4 failed attempts  | 1 failed attempt       | 2 and 1: not locked; 3 and 4: locked                              | Integer attempts immediately below, at, and above the inclusive threshold isolate the lockout count boundary. |
| FR02-LOCKOUT-DURATION-M01 | Lockout elapsed time              | 30-second duration | FR02-R07; LOGIN-LOCKOUT-ACTIVE/EXPIRED            | Inclusive duration expiry | 29 seconds elapsed | 30 seconds elapsed | 31 seconds elapsed | 10 seconds elapsed     | 10/29: still locked; 30/31: no longer rejected solely due lockout | Whole-second values around the documented duration isolate temporary-lock expiry.                             |

## Step 3: Concrete Boundary Values

| Boundary ID               | Variable                    | Rule ID  | Boundary Position         | Concrete Value                        | Expected Classification  | Dependencies and Nominal Values                                                                                    | Applicable Surface | Test Basis Reference                                                                        | Justification                                                 | Assumptions                                                                  |
| ------------------------- | --------------------------- | -------- | ------------------------- | ------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------ | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| FR02-FAILED-ATTEMPTS-B01  | Consecutive failed attempts | FR02-R06 | `threshold-1` / off point | 2 consecutive wrong-password attempts | Valid not-locked state   | Existing account `test@eshop.com`; wrong password for failures; account starts unlocked.                           | UI and API         | `requirement-analysis.md` - FR02-R05/R06; `domain-testing.md` - LOGIN-LOCKOUT-BELOW-V01     | Immediately below inclusive lockout threshold.                | Same controlled account; no prior failures.                                  |
| FR02-FAILED-ATTEMPTS-B02  | Consecutive failed attempts | FR02-R06 | threshold / on point      | 3 consecutive wrong-password attempts | Valid locked state       | Existing account; wrong password repeated; then observe locked response or correct-password rejection due lockout. | UI and API         | `requirement-analysis.md` - FR02-R05/R06; `domain-testing.md` - LOGIN-LOCKOUT-THRESHOLD-V01 | Exactly reaches inclusive threshold.                          | Failed attempts are consecutive.                                             |
| FR02-FAILED-ATTEMPTS-B03  | Consecutive failed attempts | FR02-R06 | `threshold+1` / in point  | 4 consecutive wrong-password attempts | Valid locked state       | Existing account; wrong password repeated; account remains in or reaches locked state.                             | UI and API         | `requirement-analysis.md` - FR02-R05/R06; `domain-testing.md` - LOGIN-LOCKOUT-THRESHOLD-V01 | Immediately inside locked domain.                             | Later attempts during lockout may be rejected without changing hidden count. |
| FR02-FAILED-ATTEMPTS-N01  | Consecutive failed attempts | FR02-R06 | Nominal below-threshold   | 1 wrong-password attempt              | Valid not-locked state   | Existing account; wrong password once; correct password should not be rejected solely due lockout.                 | UI and API         | `requirement-analysis.md` - FR02-R05/R06; `domain-testing.md` - LOGIN-LOCKOUT-BELOW-V01     | Nominal safe value below threshold.                           | Hidden count not directly inspected.                                         |
| FR02-LOCKOUT-DURATION-B01 | Lockout elapsed time        | FR02-R07 | `duration-1` / off point  | 29 seconds after lockout              | Valid still-locked state | Account locked by 3 failed attempts; attempt correct credentials at approximately 29 seconds.                      | UI and API         | `requirement-analysis.md` - FR02-R07; `domain-testing.md` - LOGIN-LOCKOUT-ACTIVE-V01        | Immediately before documented 30-second expiry.               | Whole-second timing; small scheduling variance noted during execution.       |
| FR02-LOCKOUT-DURATION-B02 | Lockout elapsed time        | FR02-R07 | duration / on point       | 30 seconds after lockout              | Valid expired state      | Account locked first; attempt correct credentials at approximately 30 seconds.                                     | UI and API         | `requirement-analysis.md` - FR02-R07; `domain-testing.md` - LOGIN-LOCKOUT-EXPIRED-V01       | At documented duration completion.                            | Exact millisecond precision unspecified.                                     |
| FR02-LOCKOUT-DURATION-B03 | Lockout elapsed time        | FR02-R07 | `duration+1` / in point   | 31 seconds after lockout              | Valid expired state      | Account locked first; attempt correct credentials after approximately 31 seconds.                                  | UI and API         | `requirement-analysis.md` - FR02-R07; `domain-testing.md` - LOGIN-LOCKOUT-EXPIRED-V01       | Immediately after documented duration.                        | Whole-second timing.                                                         |
| FR02-LOCKOUT-DURATION-N01 | Lockout elapsed time        | FR02-R07 | Nominal active-lock value | 10 seconds after lockout              | Valid still-locked state | Account locked first; attempt correct credentials while clearly inside the 30-second lockout period.               | UI and API         | `requirement-analysis.md` - FR02-R07; `domain-testing.md` - LOGIN-LOCKOUT-ACTIVE-V01        | Internal active-lockout sample distinct from boundary points. | Whole-second timing.                                                         |

## Boundary Derivation

FR02-R06 states that login failures from 3 consecutive failed attempts upward lock the account. This creates an inclusive lower threshold over integer attempt counts. Therefore, 3 failed attempts is the on point, 2 is the adjacent off point, 4 is the adjacent in point, and 1 is a nominal below-threshold value.

FR02-R07 states that lockout lasts 30 seconds in the demo environment. This creates a time-duration boundary. The design uses whole-second representatives: 29 seconds immediately before expiry, 30 seconds at documented expiry, 31 seconds after expiry, and 10 seconds as a nominal active-lockout point. Exact millisecond behaviour remains an ambiguity and must be handled carefully during execution.

The failed-attempt boundary also indirectly checks the "increment by exactly 1" rule because public lockout should occur only when the correct number of consecutive failed attempts has accumulated. Hidden counter values are not inspected.

For both UI and API surfaces, boundary execution requires a controlled existing account, a wrong password representative, a correct password representative, and a way to begin from an unlocked state. Those setup conditions must be achieved through public actions or documented test accounts only.

No Actual Result, Pass/Fail status, screenshot, evidence, bug report, or GitHub Issue is created in this Phase 4 analysis.

## Coverage Decisions and Exclusions

- BVA is included for failed-attempt threshold and lockout duration because both are ordered and explicitly documented.
- Email and Password presence, credential matching, account existence, message disclosure, request shape, control types, error placement, token presence, and client storage remain Domain Testing domains.
- No BVA is created for token length, token expiry, user ID, Email length, Password length, or message length because FR-02 provides no approved numeric limits for those domains.
- Timing BVA is retained despite execution complexity because the 30-second duration is explicit; execution must record timing assumptions and evidence honestly.
- Test cases providing BVA coverage are generated in Phase 5 and remain unexecuted until human approval.

## Assumptions and Gaps

- Boundary attempt counts are consecutive failed attempts against the same controlled existing account.
- Whole-second timing is used because no smaller precision is specified.
- A correct-password attempt during lockout is expected to remain rejected solely because the account is locked; after expiry, it should not be rejected solely due lockout.
- Counter reset and unlock setup mechanics are not specified; test execution may need public setup or waiting, but no database modification or source inspection is allowed.

## Human Review - Phase 4

- Reviewer:
- Review Date and Time:
- Review Scope: Boundary Value Analysis for FR-02 Login and Account Lockout
- Corrections Made:
- Missing Boundaries Added:
- Incorrect Boundaries Removed:
- Status: Pending
- Approved for Test-Case Derivation: No
- Approved for Test Execution: No
```

## Phase 5: AI Test-Case Generation

Output file: `reports/FR-02/test-cases.md`

```markdown
# Test Cases - FR-02 Login and Account Lockout

## Domain Testing Test Cases

## FR02-DT-001

- Test Case ID: FR02-DT-001
- Technique: Domain Testing
- Objective: Verify nominal valid UI login for an unlocked existing account.
- Requirement or Rule Reference: FR02-R01, FR02-R04, FR02-R10, FR02-R11
- Preconditions: EShop User Web is available at `/login`; actor is unauthenticated; account `test@eshop.com` is controlled, existing, unlocked, and has password `Test1234!`.
- Test Data: Email `test@eshop.com`; Password `Test1234!`.
- Steps:
  1. Open `/login` as an unauthenticated user.
  2. Enter Email `test@eshop.com` and Password `Test1234!`.
  3. Submit the login form.
  4. Observe authenticated UI state and client-side token availability.
- Expected Result: Login succeeds, the user reaches an authenticated UI state, and a JWT token is available in client-side storage. No exact redirect URL, success text, storage key, or token claims are asserted.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: Partition LOGIN-CREDENTIALS-V01; UI-SUCCESS-V01; TOKEN-STORAGE-V01
- Test Basis Reference: `requirement-analysis.md` - FR02-R04, FR02-R10, FR02-R11; `domain-testing.md` - LOGIN-CREDENTIALS-V01, UI-SUCCESS-V01, TOKEN-STORAGE-V01
- Notes and Assumptions: Uses documented default account as controlled public test data; no database inspection.

### Derivation

FR02-R04 and FR02-R10 define successful login with a token. The chosen Email and Password represent the matching-credential partition. The observable oracle is authenticated UI/token state, not implementation internals.

## FR02-DT-002

- Test Case ID: FR02-DT-002
- Technique: Domain Testing
- Objective: Verify nominal valid API login success contract.
- Requirement or Rule Reference: FR02-API01 through FR02-API04; FR02-R10
- Preconditions: Public API is available at `http://localhost:3000`; account `test@eshop.com` is controlled, existing, unlocked, and has password `Test1234!`.
- Test Data: `{"email":"test@eshop.com","password":"Test1234!"}`.
- Steps:
  1. Send `POST http://localhost:3000/api/login` with the JSON body.
  2. Observe the public HTTP status and JSON response body.
- Expected Result: The response is `200 OK` and contains a JWT `token` and `user` information. The exact token value and user schema are not fixed.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: Partition API-REQUEST-V01; API-SUCCESS-V01; LOGIN-CREDENTIALS-V01
- Test Basis Reference: `requirement-analysis.md` - FR02-API01 through FR02-API04; `domain-testing.md` - API-REQUEST-V01, API-SUCCESS-V01
- Notes and Assumptions: No authenticated header is required before login.

### Derivation

The API specification defines `POST /api/login` and the success response. The complete JSON body represents the valid API request and matching credentials.

## FR02-DT-003

- Test Case ID: FR02-DT-003
- Technique: Domain Testing
- Objective: Verify UI rejection when Email is missing.
- Requirement or Rule Reference: FR02-R02
- Preconditions: `/login` is available; actor is unauthenticated.
- Test Data: Email empty; Password `Test1234!`.
- Steps:
  1. Open `/login`.
  2. Leave Email empty and enter Password `Test1234!`.
  3. Submit the form.
  4. Observe whether login completes or validation is shown.
- Expected Result: Login is rejected and does not reach authenticated state. If an error is displayed, exact text is unspecified.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: Partition LOGIN-EMAIL-PRESENCE-I01; VALIDATION-REJECTION-V01
- Test Basis Reference: `requirement-analysis.md` - FR02-R02; `domain-testing.md` - LOGIN-EMAIL-PRESENCE-I01
- Notes and Assumptions: Password remains nominal to isolate missing Email.

### Derivation

FR02-R02 makes Email required. Empty Email is the invalid representative; unrelated inputs remain valid.

## FR02-DT-004

- Test Case ID: FR02-DT-004
- Technique: Domain Testing
- Objective: Verify UI rejection when Password is missing.
- Requirement or Rule Reference: FR02-R03
- Preconditions: `/login` is available; actor is unauthenticated.
- Test Data: Email `test@eshop.com`; Password empty.
- Steps:
  1. Open `/login`.
  2. Enter Email `test@eshop.com` and leave Password empty.
  3. Submit the form.
  4. Observe whether login completes or validation is shown.
- Expected Result: Login is rejected and does not reach authenticated state. If an error is displayed, exact text is unspecified.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: Partition LOGIN-PASSWORD-PRESENCE-I01; VALIDATION-REJECTION-V01
- Test Basis Reference: `requirement-analysis.md` - FR02-R03; `domain-testing.md` - LOGIN-PASSWORD-PRESENCE-I01
- Notes and Assumptions: Email remains nominal to isolate missing Password.

### Derivation

FR02-R03 makes Password required. Empty Password is the invalid representative; unrelated inputs remain valid.

## FR02-DT-005

- Test Case ID: FR02-DT-005
- Technique: Domain Testing
- Objective: Verify UI HTML5 email-format rejection for a plainly malformed Email.
- Requirement or Rule Reference: FR02-R13, FR02-SF02
- Preconditions: `/login` is available; Email control is present.
- Test Data: Email `not-an-email`; Password `Test1234!`.
- Steps:
  1. Open `/login`.
  2. Enter Email `not-an-email` and Password `Test1234!`.
  3. Submit the form.
  4. Observe whether browser/form validation prevents successful login.
- Expected Result: Login is rejected because the Email value does not satisfy HTML5 email validation. Exact browser validation text is unspecified.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: Partition LOGIN-EMAIL-FORMAT-I01; VALIDATION-REJECTION-V01
- Test Basis Reference: `requirement-analysis.md` - FR02-R13, FR02-SF02; `domain-testing.md` - LOGIN-EMAIL-FORMAT-I01
- Notes and Assumptions: This is UI-only; API email-format rejection is not asserted by the approved API contract.

### Derivation

The `type="email"` rule supplies a UI email-format oracle. `not-an-email` is a clear invalid representative that avoids edge grammar disputes.

## FR02-DT-006

- Test Case ID: FR02-DT-006
- Technique: Domain Testing
- Objective: Verify UI rejection for wrong password on an existing account.
- Requirement or Rule Reference: FR02-R05, FR02-R09
- Preconditions: `/login` is available; account `test@eshop.com` exists and is not locked.
- Test Data: Email `test@eshop.com`; Password `WrongPass123!`.
- Steps:
  1. Open `/login`.
  2. Enter Email `test@eshop.com` and Password `WrongPass123!`.
  3. Submit the form.
  4. Observe rejection and any error message.
- Expected Result: Login is rejected and does not reveal detailed cause information. Exact error text is unspecified.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: Partition LOGIN-CREDENTIALS-I01; LOGIN-ERROR-NONLEAKY-V01
- Test Basis Reference: `requirement-analysis.md` - FR02-R05, FR02-R09; `domain-testing.md` - LOGIN-CREDENTIALS-I01
- Notes and Assumptions: This single failed attempt may affect later lockout state; execution should use isolated setup.

### Derivation

Wrong password for a controlled existing account is the representative invalid credential. FR02-R09 supplies the non-disclosure oracle.

## FR02-DT-007

- Test Case ID: FR02-DT-007
- Technique: Domain Testing
- Objective: Verify UI rejection for a non-existing account without detailed cause disclosure.
- Requirement or Rule Reference: FR02-R09
- Preconditions: `/login` is available; Email `no.such.user@example.com` is controlled as non-existing through public setup, not database inspection.
- Test Data: Email `no.such.user@example.com`; Password `Test1234!`.
- Steps:
  1. Open `/login`.
  2. Enter the non-existing Email and nominal Password.
  3. Submit the form.
  4. Observe rejection and disclosure level.
- Expected Result: Login is rejected without revealing detailed account-existence cause information. Exact message is unspecified.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: Partition LOGIN-ACCOUNT-EXISTS-I01; LOGIN-ERROR-NONLEAKY-V01
- Test Basis Reference: `requirement-analysis.md` - FR02-R09; `domain-testing.md` - LOGIN-ACCOUNT-EXISTS-I01
- Notes and Assumptions: Non-existing state must be controlled without inspecting database records.

### Derivation

A non-existing identity is an invalid login identity. The expected result is rejection plus non-disclosure, not a specific message.

## FR02-DT-008

- Test Case ID: FR02-DT-008
- Technique: Domain Testing
- Objective: Verify API rejection when `email` is missing.
- Requirement or Rule Reference: FR02-R02, FR02-API02
- Preconditions: Public API is available at `http://localhost:3000`.
- Test Data: `{"password":"Test1234!"}`.
- Steps:
  1. Send `POST http://localhost:3000/api/login` without the `email` property.
  2. Observe the HTTP status and response body.
- Expected Result: Login is rejected because Email is required. Exact invalid status and body are unspecified.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: Partition API-REQUEST-I01; LOGIN-EMAIL-PRESENCE-I01
- Test Basis Reference: `requirement-analysis.md` - FR02-R02, FR02-API02; `domain-testing.md` - API-REQUEST-I01
- Notes and Assumptions: Password remains nominal.

### Derivation

The documented API request contains `email`, and FR02-R02 requires Email. Omitting it isolates the missing Email partition.

## FR02-DT-009

- Test Case ID: FR02-DT-009
- Technique: Domain Testing
- Objective: Verify API rejection when `password` is missing.
- Requirement or Rule Reference: FR02-R03, FR02-API03
- Preconditions: Public API is available at `http://localhost:3000`.
- Test Data: `{"email":"test@eshop.com"}`.
- Steps:
  1. Send `POST http://localhost:3000/api/login` without the `password` property.
  2. Observe the HTTP status and response body.
- Expected Result: Login is rejected because Password is required. Exact invalid status and body are unspecified.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: Partition API-REQUEST-I02; LOGIN-PASSWORD-PRESENCE-I01
- Test Basis Reference: `requirement-analysis.md` - FR02-R03, FR02-API03; `domain-testing.md` - API-REQUEST-I02
- Notes and Assumptions: Email remains nominal.

### Derivation

The documented API request contains `password`, and FR02-R03 requires Password. Omitting it isolates the missing Password partition.

## FR02-DT-010

- Test Case ID: FR02-DT-010
- Technique: Domain Testing
- Objective: Verify API rejection for wrong password on an existing account.
- Requirement or Rule Reference: FR02-R05, FR02-R09
- Preconditions: Public API is available; account `test@eshop.com` exists and is not locked.
- Test Data: `{"email":"test@eshop.com","password":"WrongPass123!"}`.
- Steps:
  1. Send `POST http://localhost:3000/api/login` with wrong password.
  2. Observe the HTTP status and response body.
- Expected Result: Login is rejected and the response does not reveal detailed cause information. Exact status and body are unspecified.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: Partition LOGIN-CREDENTIALS-I01; LOGIN-ERROR-NONLEAKY-V01
- Test Basis Reference: `requirement-analysis.md` - FR02-R05, FR02-R09; `domain-testing.md` - LOGIN-CREDENTIALS-I01
- Notes and Assumptions: Execution should isolate this attempt from BVA lockout sequences.

### Derivation

Wrong password is a failed login that should be rejected and counted. Exact failure response is not invented.

## FR02-DT-011

- Test Case ID: FR02-DT-011
- Technique: Domain Testing
- Objective: Verify API rejection for a non-existing account without detailed cause disclosure.
- Requirement or Rule Reference: FR02-R09
- Preconditions: Public API is available; Email `no.such.user@example.com` is controlled as non-existing through public setup.
- Test Data: `{"email":"no.such.user@example.com","password":"Test1234!"}`.
- Steps:
  1. Send `POST http://localhost:3000/api/login` with the non-existing Email.
  2. Observe the HTTP status and response body.
- Expected Result: Login is rejected without revealing detailed account-existence cause information. Exact status and body are unspecified.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: Partition LOGIN-ACCOUNT-EXISTS-I01; LOGIN-ERROR-NONLEAKY-V01
- Test Basis Reference: `requirement-analysis.md` - FR02-R09; `domain-testing.md` - LOGIN-ACCOUNT-EXISTS-I01
- Notes and Assumptions: No database inspection is used to prove non-existence.

### Derivation

The invalid account identity should not authenticate. FR02-R09 provides the public non-disclosure oracle.

## FR02-DT-012

- Test Case ID: FR02-DT-012
- Technique: Domain Testing
- Objective: Verify UI lockout after three consecutive failed login attempts.
- Requirement or Rule Reference: FR02-R05, FR02-R06, FR02-R08
- Preconditions: `/login` is available; account `test@eshop.com` exists, starts unlocked, and failed-attempt state is controlled through public setup.
- Test Data: Email `test@eshop.com`; wrong password `WrongPass123!`; correct password `Test1234!`.
- Steps:
  1. Open `/login`.
  2. Submit three consecutive wrong-password login attempts for `test@eshop.com`.
  3. Attempt login with correct password immediately after the third failure.
  4. Observe whether the account is locked and an error is shown.
- Expected Result: The account is locked after the third consecutive failed attempt, and the correct-password attempt during lockout is rejected with an appropriate error. Exact message is unspecified.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: Partition LOGIN-LOCKOUT-THRESHOLD-V01; LOGIN-LOCKOUT-ACTIVE-V01
- Test Basis Reference: `requirement-analysis.md` - FR02-R05, FR02-R06, FR02-R08; `domain-testing.md` - LOGIN-LOCKOUT-THRESHOLD-V01
- Notes and Assumptions: This case overlaps the threshold boundary concept but is classified as DT because it verifies the general lockout rule.

### Derivation

FR02-R06 says three or more consecutive failures lock the account. Correct credentials during lockout isolate lockout state from credential validity.

## FR02-DT-013

- Test Case ID: FR02-DT-013
- Technique: Domain Testing
- Objective: Verify API lockout after three consecutive failed login attempts.
- Requirement or Rule Reference: FR02-R05, FR02-R06, FR02-R08
- Preconditions: Public API is available; account `test@eshop.com` exists, starts unlocked, and failed-attempt state is controlled.
- Test Data: Wrong request `{"email":"test@eshop.com","password":"WrongPass123!"}`; correct request `{"email":"test@eshop.com","password":"Test1234!"}`.
- Steps:
  1. Send three consecutive wrong-password `POST /api/login` requests.
  2. Send a correct-password `POST /api/login` request immediately after the third failure.
  3. Observe whether the correct request is rejected due to lockout.
- Expected Result: The account is locked after the third consecutive failure; the correct-password request during lockout is rejected. Exact status and response body are unspecified.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: Partition LOGIN-LOCKOUT-THRESHOLD-V01; LOGIN-LOCKOUT-ACTIVE-V01
- Test Basis Reference: `requirement-analysis.md` - FR02-R05, FR02-R06, FR02-R08; `domain-testing.md` - LOGIN-LOCKOUT-THRESHOLD-V01
- Notes and Assumptions: Hidden counter values are not inspected.

### Derivation

The API case projects the same lockout partition onto the public API surface.

## FR02-DT-014

- Test Case ID: FR02-DT-014
- Technique: Domain Testing
- Objective: Verify UI required-field markers for Email and Password.
- Requirement or Rule Reference: FR02-SF01
- Preconditions: `/login` is available.
- Test Data: Login form labels for Email and Password.
- Steps:
  1. Open `/login`.
  2. Inspect Email and Password labels.
- Expected Result: Required Email and Password labels display adjacent `*` markers.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: Partition FORM-REQUIRED-MARKER-V01; FORM-REQUIRED-MARKER-I01
- Test Basis Reference: `requirement-analysis.md` - FR02-SF01; `domain-testing.md` - FORM-REQUIRED-MARKER-V01/I01
- Notes and Assumptions: Absence of marker is a UI conformance failure.

### Derivation

FR02-SF01 applies to all required login fields. Email and Password are required by FR02-R02/R03.

## FR02-DT-015

- Test Case ID: FR02-DT-015
- Technique: Domain Testing
- Objective: Verify login Email control uses `type="email"`.
- Requirement or Rule Reference: FR02-R13, FR02-SF02
- Preconditions: `/login` is available.
- Test Data: Email input control.
- Steps:
  1. Open `/login`.
  2. Inspect the public Email input control or browser-exposed attribute.
- Expected Result: The Email input exposes `type="email"`.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: Partition FORM-EMAIL-TYPE-V01; FORM-EMAIL-TYPE-I01
- Test Basis Reference: `requirement-analysis.md` - FR02-R13, FR02-SF02; `domain-testing.md` - FORM-EMAIL-TYPE-V01/I01
- Notes and Assumptions: Browser devtools or public DOM observation is permitted as public UI observation; source code is not inspected.

### Derivation

The requirement explicitly names `type="email"`. A non-email type is the invalid conformance class.

## FR02-DT-016

- Test Case ID: FR02-DT-016
- Technique: Domain Testing
- Objective: Verify login Password control masks input using `type="password"`.
- Requirement or Rule Reference: FR02-SF03
- Preconditions: `/login` is available.
- Test Data: Password input control; value `Test1234!`.
- Steps:
  1. Open `/login`.
  2. Enter `Test1234!` in the Password field.
  3. Inspect whether the control uses password masking and does not display clear text.
- Expected Result: The Password control uses `type="password"` and does not show the value in clear text.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: Partition FORM-PASSWORD-TYPE-V01; FORM-PASSWORD-TYPE-I01
- Test Basis Reference: `requirement-analysis.md` - FR02-SF03; `domain-testing.md` - FORM-PASSWORD-TYPE-V01/I01
- Notes and Assumptions: UI observation only; no source inspection.

### Derivation

FR02-SF03 creates masked versus clear-text classes. The selected value makes visibility observable.

## FR02-DT-017

- Test Case ID: FR02-DT-017
- Technique: Domain Testing
- Objective: Verify UI error placement above the submit button.
- Requirement or Rule Reference: FR02-SF04
- Preconditions: `/login` is available; an invalid login attempt can produce a visible error.
- Test Data: Email `test@eshop.com`; Password `WrongPass123!`.
- Steps:
  1. Open `/login`.
  2. Submit the wrong-password login attempt.
  3. Observe the location of the displayed error relative to the submit button.
- Expected Result: Any displayed login error appears above the submit button, not below it. Exact text is unspecified.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: Partition FORM-ERROR-PLACEMENT-V01; FORM-ERROR-PLACEMENT-I01
- Test Basis Reference: `requirement-analysis.md` - FR02-SF04; `domain-testing.md` - FORM-ERROR-PLACEMENT-V01/I01
- Notes and Assumptions: If no error is displayed, execution must record actual observation honestly.

### Derivation

FR02-SF04 gives an observable placement oracle independent of the exact error text.

## FR02-DT-018

- Test Case ID: FR02-DT-018
- Technique: Domain Testing
- Objective: Verify Authorization header usage after successful login.
- Requirement or Rule Reference: FR02-R12
- Preconditions: Public API is available; valid login can return a token.
- Test Data: Login body `{"email":"test@eshop.com","password":"Test1234!"}`; authenticated endpoint `GET /api/users/me`.
- Steps:
  1. Obtain a token through successful public login.
  2. Send `GET http://localhost:3000/api/users/me` using `Authorization: Bearer <token>`.
  3. Observe that the request uses the documented header shape.
- Expected Result: The authenticated request includes `Authorization: Bearer <token>`. The exact response body from `/api/users/me` is outside this case unless separately specified.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: Partition AUTHORIZATION-HEADER-V01
- Test Basis Reference: `requirement-analysis.md` - FR02-R12; `api_specification.md` - authenticated API note; `domain-testing.md` - AUTHORIZATION-HEADER-V01
- Notes and Assumptions: Uses public API traffic only; does not inspect implementation source.

### Derivation

FR02-R12 defines the header shape. Successful login supplies the token dependency.

## FR02-DT-019

- Test Case ID: FR02-DT-019
- Technique: Domain Testing
- Objective: Verify active UI lockout rejects correct credentials.
- Requirement or Rule Reference: FR02-R07, FR02-R08
- Preconditions: `/login` is available; account is already locked through public failed attempts.
- Test Data: Email `test@eshop.com`; Password `Test1234!`.
- Steps:
  1. While the account is in active lockout, open `/login`.
  2. Enter correct credentials.
  3. Submit the form.
  4. Observe whether login is rejected because lockout is active.
- Expected Result: Correct credentials are rejected during active lockout with an appropriate error. Exact message is unspecified.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: Partition LOGIN-LOCKOUT-ACTIVE-V01; VALIDATION-REJECTION-V01
- Test Basis Reference: `requirement-analysis.md` - FR02-R07/R08; `domain-testing.md` - LOGIN-LOCKOUT-ACTIVE-V01
- Notes and Assumptions: Lockout setup must be achieved through public UI/API actions.

### Derivation

Active lockout is a state partition separate from credential validity. Correct credentials isolate the lockout state.

## FR02-DT-020

- Test Case ID: FR02-DT-020
- Technique: Domain Testing
- Objective: Verify active API lockout rejects correct credentials.
- Requirement or Rule Reference: FR02-R07, FR02-R08
- Preconditions: Public API is available; account is already locked through public failed attempts.
- Test Data: `{"email":"test@eshop.com","password":"Test1234!"}`.
- Steps:
  1. During active lockout, send correct-password `POST /api/login`.
  2. Observe the HTTP status and response body.
- Expected Result: The correct login request is rejected during active lockout. Exact status and body are unspecified.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: Partition LOGIN-LOCKOUT-ACTIVE-V01; VALIDATION-REJECTION-V01
- Test Basis Reference: `requirement-analysis.md` - FR02-R07/R08; `domain-testing.md` - LOGIN-LOCKOUT-ACTIVE-V01
- Notes and Assumptions: No hidden lockout state is inspected.

### Derivation

The API surface must respect the same lockout state because FR-02 defines system behaviour, not UI-only behaviour.

## FR02-DT-021

- Test Case ID: FR02-DT-021
- Technique: Domain Testing
- Objective: Verify UI login after documented lockout expiry is not rejected solely due lockout.
- Requirement or Rule Reference: FR02-R07
- Preconditions: `/login` is available; account was locked through public failed attempts and at least the documented lockout duration has elapsed.
- Test Data: Email `test@eshop.com`; Password `Test1234!`.
- Steps:
  1. Lock the account through public failed attempts.
  2. Wait until the documented 30-second lockout duration has elapsed.
  3. Attempt login with correct credentials.
  4. Observe whether lockout still blocks authentication.
- Expected Result: The account is no longer rejected solely due lockout after the documented duration has elapsed. If credentials are otherwise valid, login can succeed.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: Partition LOGIN-LOCKOUT-EXPIRED-V01
- Test Basis Reference: `requirement-analysis.md` - FR02-R07; `domain-testing.md` - LOGIN-LOCKOUT-EXPIRED-V01
- Notes and Assumptions: Exact millisecond precision is not asserted.

### Derivation

The 30-second temporary lockout creates an expired-lockout state. This DT case samples that state outside strict boundary timing.

## FR02-DT-022

- Test Case ID: FR02-DT-022
- Technique: Domain Testing
- Objective: Verify API login after documented lockout expiry is not rejected solely due lockout.
- Requirement or Rule Reference: FR02-R07
- Preconditions: Public API is available; account was locked through public failed attempts and at least the documented lockout duration has elapsed.
- Test Data: `{"email":"test@eshop.com","password":"Test1234!"}`.
- Steps:
  1. Lock the account through public failed API attempts.
  2. Wait until the documented 30-second duration has elapsed.
  3. Send a correct-password `POST /api/login`.
  4. Observe whether lockout still blocks authentication.
- Expected Result: The request is not rejected solely due lockout after the documented duration has elapsed; if credentials are valid and account is otherwise usable, success contract can apply.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: Partition LOGIN-LOCKOUT-EXPIRED-V01
- Test Basis Reference: `requirement-analysis.md` - FR02-R07; `domain-testing.md` - LOGIN-LOCKOUT-EXPIRED-V01
- Notes and Assumptions: Timing tolerance must be recorded during execution.

### Derivation

This is the API counterpart of the expired-lockout partition.

## Boundary Value Analysis Test Cases

## FR02-BVA-001

- Test Case ID: FR02-BVA-001
- Technique: Boundary Value Analysis
- Objective: Verify UI lockout classification at 2 consecutive failed attempts.
- Requirement or Rule Reference: FR02-R05, FR02-R06
- Preconditions: `/login` is available; account starts unlocked with zero consecutive failed attempts.
- Test Data: Email `test@eshop.com`; wrong password `WrongPass123!`; correct password `Test1234!`; count = 2 failures.
- Steps:
  1. Submit two consecutive wrong-password UI login attempts.
  2. Immediately attempt UI login with correct password.
  3. Observe whether account is locked.
- Expected Result: The account has not reached the 3-attempt lockout threshold; correct login is not rejected solely due lockout.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: FR02-FAILED-ATTEMPTS-B01
- Test Basis Reference: `boundary-value-analysis.md` - FR02-FAILED-ATTEMPTS-B01
- Notes and Assumptions: Other authentication failures unrelated to lockout should be recorded separately.

### Derivation

Two attempts is the adjacent off point below the inclusive threshold of three.

## FR02-BVA-002

- Test Case ID: FR02-BVA-002
- Technique: Boundary Value Analysis
- Objective: Verify UI lockout classification at 3 consecutive failed attempts.
- Requirement or Rule Reference: FR02-R05, FR02-R06
- Preconditions: `/login` is available; account starts unlocked with zero consecutive failed attempts.
- Test Data: Email `test@eshop.com`; wrong password `WrongPass123!`; correct password `Test1234!`; count = 3 failures.
- Steps:
  1. Submit three consecutive wrong-password UI login attempts.
  2. Immediately attempt UI login with correct password.
  3. Observe whether account is locked.
- Expected Result: The account is locked at the third consecutive failed attempt; correct credentials are rejected during active lockout.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: FR02-FAILED-ATTEMPTS-B02
- Test Basis Reference: `boundary-value-analysis.md` - FR02-FAILED-ATTEMPTS-B02
- Notes and Assumptions: Threshold is inclusive.

### Derivation

Three attempts is the on point for "3 or more" lockout.

## FR02-BVA-003

- Test Case ID: FR02-BVA-003
- Technique: Boundary Value Analysis
- Objective: Verify UI lockout classification at 4 consecutive failed attempts.
- Requirement or Rule Reference: FR02-R05, FR02-R06
- Preconditions: `/login` is available; account starts unlocked.
- Test Data: Email `test@eshop.com`; wrong password `WrongPass123!`; count = 4 failures.
- Steps:
  1. Submit wrong-password UI login attempts up to the fourth attempt.
  2. Observe whether the account is or remains locked.
- Expected Result: Four consecutive failed attempts is inside the locked domain; login remains rejected due active lockout.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: FR02-FAILED-ATTEMPTS-B03
- Test Basis Reference: `boundary-value-analysis.md` - FR02-FAILED-ATTEMPTS-B03
- Notes and Assumptions: Later attempts during lockout may be rejected before incrementing; record observed sequence honestly.

### Derivation

Four attempts is the adjacent in point above the inclusive threshold.

## FR02-BVA-004

- Test Case ID: FR02-BVA-004
- Technique: Boundary Value Analysis
- Objective: Verify UI nominal below-threshold classification at 1 failed attempt.
- Requirement or Rule Reference: FR02-R05, FR02-R06
- Preconditions: `/login` is available; account starts unlocked.
- Test Data: Email `test@eshop.com`; wrong password `WrongPass123!`; correct password `Test1234!`; count = 1 failure.
- Steps:
  1. Submit one wrong-password UI login attempt.
  2. Attempt UI login with correct password.
  3. Observe whether lockout blocks login.
- Expected Result: One failed attempt is below threshold; correct login is not rejected solely due lockout.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: FR02-FAILED-ATTEMPTS-N01
- Test Basis Reference: `boundary-value-analysis.md` - FR02-FAILED-ATTEMPTS-N01
- Notes and Assumptions: Nominal below-threshold sample.

### Derivation

One failure is a nominal internal value in the not-locked side of the attempt-count domain.

## FR02-BVA-005

- Test Case ID: FR02-BVA-005
- Technique: Boundary Value Analysis
- Objective: Verify API lockout classification at 2 consecutive failed attempts.
- Requirement or Rule Reference: FR02-R05, FR02-R06
- Preconditions: Public API is available; account starts unlocked with zero consecutive failed attempts.
- Test Data: Wrong body `{"email":"test@eshop.com","password":"WrongPass123!"}`; correct body `{"email":"test@eshop.com","password":"Test1234!"}`.
- Steps:
  1. Send two consecutive wrong-password `POST /api/login` requests.
  2. Send a correct-password `POST /api/login` request.
  3. Observe whether lockout blocks the correct request.
- Expected Result: Two failures do not reach lockout; the correct request is not rejected solely due lockout.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: FR02-FAILED-ATTEMPTS-B01
- Test Basis Reference: `boundary-value-analysis.md` - FR02-FAILED-ATTEMPTS-B01
- Notes and Assumptions: Same account and consecutive failures.

### Derivation

This is the API surface coverage for the threshold off point.

## FR02-BVA-006

- Test Case ID: FR02-BVA-006
- Technique: Boundary Value Analysis
- Objective: Verify API lockout classification at 3 consecutive failed attempts.
- Requirement or Rule Reference: FR02-R05, FR02-R06
- Preconditions: Public API is available; account starts unlocked.
- Test Data: Wrong body `{"email":"test@eshop.com","password":"WrongPass123!"}`; correct body `{"email":"test@eshop.com","password":"Test1234!"}`.
- Steps:
  1. Send three consecutive wrong-password `POST /api/login` requests.
  2. Send a correct-password `POST /api/login` request.
  3. Observe whether the account is locked.
- Expected Result: The account is locked at the third consecutive failed attempt; the correct request during active lockout is rejected.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: FR02-FAILED-ATTEMPTS-B02
- Test Basis Reference: `boundary-value-analysis.md` - FR02-FAILED-ATTEMPTS-B02
- Notes and Assumptions: Exact failure status/body unspecified.

### Derivation

This is the API surface coverage for the threshold on point.

## FR02-BVA-007

- Test Case ID: FR02-BVA-007
- Technique: Boundary Value Analysis
- Objective: Verify API lockout classification at 4 consecutive failed attempts.
- Requirement or Rule Reference: FR02-R05, FR02-R06
- Preconditions: Public API is available; account starts unlocked.
- Test Data: Wrong body `{"email":"test@eshop.com","password":"WrongPass123!"}`; count = 4 failures.
- Steps:
  1. Send wrong-password API login attempts up to the fourth attempt.
  2. Observe whether the account is or remains locked.
- Expected Result: Four consecutive failed attempts is inside the locked domain; login remains rejected due active lockout.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: FR02-FAILED-ATTEMPTS-B03
- Test Basis Reference: `boundary-value-analysis.md` - FR02-FAILED-ATTEMPTS-B03
- Notes and Assumptions: If the fourth attempt is blocked due existing lockout, record the observable locked state.

### Derivation

This is the API surface coverage for the threshold in point.

## FR02-BVA-008

- Test Case ID: FR02-BVA-008
- Technique: Boundary Value Analysis
- Objective: Verify API nominal below-threshold classification at 1 failed attempt.
- Requirement or Rule Reference: FR02-R05, FR02-R06
- Preconditions: Public API is available; account starts unlocked.
- Test Data: Wrong body `{"email":"test@eshop.com","password":"WrongPass123!"}`; correct body `{"email":"test@eshop.com","password":"Test1234!"}`.
- Steps:
  1. Send one wrong-password `POST /api/login` request.
  2. Send a correct-password `POST /api/login` request.
  3. Observe whether lockout blocks the correct request.
- Expected Result: One failure is below threshold; correct login is not rejected solely due lockout.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: FR02-FAILED-ATTEMPTS-N01
- Test Basis Reference: `boundary-value-analysis.md` - FR02-FAILED-ATTEMPTS-N01
- Notes and Assumptions: Nominal below-threshold sample.

### Derivation

This is the API surface coverage for the nominal below-threshold value.

## FR02-BVA-009

- Test Case ID: FR02-BVA-009
- Technique: Boundary Value Analysis
- Objective: Verify UI lockout remains active at 29 seconds after lockout.
- Requirement or Rule Reference: FR02-R07, FR02-R08
- Preconditions: `/login` is available; account has been locked through public failed attempts.
- Test Data: Correct credentials `test@eshop.com` / `Test1234!`; elapsed time = approximately 29 seconds.
- Steps:
  1. Lock the account through three consecutive failed attempts.
  2. Wait approximately 29 seconds from lockout.
  3. Attempt UI login with correct credentials.
  4. Observe whether lockout still blocks login.
- Expected Result: At 29 seconds, the account is still within the documented 30-second lockout and login is rejected due active lockout.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: FR02-LOCKOUT-DURATION-B01
- Test Basis Reference: `boundary-value-analysis.md` - FR02-LOCKOUT-DURATION-B01
- Notes and Assumptions: Whole-second timing; record actual measured timing during execution.

### Derivation

Twenty-nine seconds is immediately before the documented 30-second duration expires.

## FR02-BVA-010

- Test Case ID: FR02-BVA-010
- Technique: Boundary Value Analysis
- Objective: Verify UI lockout expiry at 30 seconds after lockout.
- Requirement or Rule Reference: FR02-R07
- Preconditions: `/login` is available; account has been locked through public failed attempts.
- Test Data: Correct credentials `test@eshop.com` / `Test1234!`; elapsed time = approximately 30 seconds.
- Steps:
  1. Lock the account through three consecutive failed attempts.
  2. Wait approximately 30 seconds from lockout.
  3. Attempt UI login with correct credentials.
  4. Observe whether lockout still blocks login.
- Expected Result: At the documented 30-second duration, the account is no longer rejected solely due lockout. Exact timing precision is unspecified.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: FR02-LOCKOUT-DURATION-B02
- Test Basis Reference: `boundary-value-analysis.md` - FR02-LOCKOUT-DURATION-B02
- Notes and Assumptions: If timing precision makes the exact on point unstable, record the observation and timing.

### Derivation

Thirty seconds is the documented duration boundary.

## FR02-BVA-011

- Test Case ID: FR02-BVA-011
- Technique: Boundary Value Analysis
- Objective: Verify UI lockout expiry after 31 seconds.
- Requirement or Rule Reference: FR02-R07
- Preconditions: `/login` is available; account has been locked through public failed attempts.
- Test Data: Correct credentials `test@eshop.com` / `Test1234!`; elapsed time = approximately 31 seconds.
- Steps:
  1. Lock the account through three consecutive failed attempts.
  2. Wait approximately 31 seconds from lockout.
  3. Attempt UI login with correct credentials.
  4. Observe whether lockout still blocks login.
- Expected Result: At 31 seconds, the account is beyond the documented duration and is not rejected solely due lockout.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: FR02-LOCKOUT-DURATION-B03
- Test Basis Reference: `boundary-value-analysis.md` - FR02-LOCKOUT-DURATION-B03
- Notes and Assumptions: Correct credentials isolate lockout expiry from credential validity.

### Derivation

Thirty-one seconds is immediately after the documented duration boundary.

## FR02-BVA-012

- Test Case ID: FR02-BVA-012
- Technique: Boundary Value Analysis
- Objective: Verify UI nominal active-lockout state at 10 seconds.
- Requirement or Rule Reference: FR02-R07, FR02-R08
- Preconditions: `/login` is available; account has been locked through public failed attempts.
- Test Data: Correct credentials `test@eshop.com` / `Test1234!`; elapsed time = approximately 10 seconds.
- Steps:
  1. Lock the account through three consecutive failed attempts.
  2. Wait approximately 10 seconds.
  3. Attempt UI login with correct credentials.
  4. Observe whether lockout blocks login.
- Expected Result: At 10 seconds, the account remains inside the active lockout period and login is rejected due lockout.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: FR02-LOCKOUT-DURATION-N01
- Test Basis Reference: `boundary-value-analysis.md` - FR02-LOCKOUT-DURATION-N01
- Notes and Assumptions: Nominal active-lockout sample.

### Derivation

Ten seconds is a nominal value clearly inside the documented 30-second lockout.

## FR02-BVA-013

- Test Case ID: FR02-BVA-013
- Technique: Boundary Value Analysis
- Objective: Verify API lockout remains active at 29 seconds after lockout.
- Requirement or Rule Reference: FR02-R07, FR02-R08
- Preconditions: Public API is available; account has been locked through public failed attempts.
- Test Data: Correct body `{"email":"test@eshop.com","password":"Test1234!"}`; elapsed time = approximately 29 seconds.
- Steps:
  1. Lock the account through three consecutive failed API attempts.
  2. Wait approximately 29 seconds.
  3. Send correct-password `POST /api/login`.
  4. Observe whether lockout still blocks the request.
- Expected Result: At 29 seconds, the request is rejected due active lockout. Exact status/body is unspecified.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: FR02-LOCKOUT-DURATION-B01
- Test Basis Reference: `boundary-value-analysis.md` - FR02-LOCKOUT-DURATION-B01
- Notes and Assumptions: Whole-second timing.

### Derivation

This is the API surface coverage for the duration off point.

## FR02-BVA-014

- Test Case ID: FR02-BVA-014
- Technique: Boundary Value Analysis
- Objective: Verify API lockout expiry at 30 seconds.
- Requirement or Rule Reference: FR02-R07
- Preconditions: Public API is available; account has been locked through public failed attempts.
- Test Data: Correct body `{"email":"test@eshop.com","password":"Test1234!"}`; elapsed time = approximately 30 seconds.
- Steps:
  1. Lock the account through three consecutive failed API attempts.
  2. Wait approximately 30 seconds.
  3. Send correct-password `POST /api/login`.
  4. Observe whether lockout still blocks the request.
- Expected Result: At the documented 30-second duration, the request is not rejected solely due lockout. Exact timing precision is unspecified.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: FR02-LOCKOUT-DURATION-B02
- Test Basis Reference: `boundary-value-analysis.md` - FR02-LOCKOUT-DURATION-B02
- Notes and Assumptions: Record actual timing during execution.

### Derivation

This is the API surface coverage for the duration on point.

## FR02-BVA-015

- Test Case ID: FR02-BVA-015
- Technique: Boundary Value Analysis
- Objective: Verify API lockout expiry after 31 seconds.
- Requirement or Rule Reference: FR02-R07
- Preconditions: Public API is available; account has been locked through public failed attempts.
- Test Data: Correct body `{"email":"test@eshop.com","password":"Test1234!"}`; elapsed time = approximately 31 seconds.
- Steps:
  1. Lock the account through three consecutive failed API attempts.
  2. Wait approximately 31 seconds.
  3. Send correct-password `POST /api/login`.
  4. Observe whether lockout still blocks the request.
- Expected Result: At 31 seconds, the request is beyond the documented duration and is not rejected solely due lockout.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: FR02-LOCKOUT-DURATION-B03
- Test Basis Reference: `boundary-value-analysis.md` - FR02-LOCKOUT-DURATION-B03
- Notes and Assumptions: Correct credentials isolate lockout expiry.

### Derivation

This is the API surface coverage for the duration in point.

## FR02-BVA-016

- Test Case ID: FR02-BVA-016
- Technique: Boundary Value Analysis
- Objective: Verify API nominal active-lockout state at 10 seconds.
- Requirement or Rule Reference: FR02-R07, FR02-R08
- Preconditions: Public API is available; account has been locked through public failed attempts.
- Test Data: Correct body `{"email":"test@eshop.com","password":"Test1234!"}`; elapsed time = approximately 10 seconds.
- Steps:
  1. Lock the account through three consecutive failed API attempts.
  2. Wait approximately 10 seconds.
  3. Send correct-password `POST /api/login`.
  4. Observe whether lockout blocks the request.
- Expected Result: At 10 seconds, the request remains inside the active lockout period and is rejected due lockout.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: FR02-LOCKOUT-DURATION-N01
- Test Basis Reference: `boundary-value-analysis.md` - FR02-LOCKOUT-DURATION-N01
- Notes and Assumptions: Nominal active-lockout sample.

### Derivation

This is the API surface coverage for a nominal active-lockout duration value.

## Exploratory Backlog

| Candidate ID               | Input or Observation                              | Missing Oracle                                 | Clarification Required         | Reason Excluded from Normative Coverage   |
| -------------------------- | ------------------------------------------------- | ---------------------------------------------- | ------------------------------ | ----------------------------------------- |
| LOGIN-EMAIL-WHITESPACE-A01 | Email with leading/trailing spaces or spaces only | Whether trimming/whitespace counts as provided | Whitespace and trimming policy | FR-02 does not define it.                 |
| LOGIN-EMAIL-CASE-A01       | Case variant such as `TEST@ESHOP.COM`             | Whether Email matching is case-sensitive       | Email normalization policy     | FR-02 does not define it.                 |
| LOGIN-COUNTER-RESET-A01    | Failure count before/after a successful login     | Whether success resets failed-attempt count    | Failed-attempt reset rule      | FR-02 does not define it.                 |
| FORM-STEP-INDICATOR-A01    | Login step count and Step Indicator               | Whether Login is multi-step                    | Authoritative login step model | FR-02 does not state login is multi-step. |

## Preliminary Coverage Summary

| Rule ID              | Partition or Boundary ID                                                            | Technique      | Covering Test Case ID             | Surface | Coverage Status         | Notes                                                      |
| -------------------- | ----------------------------------------------------------------------------------- | -------------- | --------------------------------- | ------- | ----------------------- | ---------------------------------------------------------- |
| FR02-R01, R02        | LOGIN-EMAIL-PRESENCE-V01/I01                                                        | Domain Testing | FR02-DT-001, 002, 003, 008        | UI/API  | Covered                 | Provided and missing Email covered on both surfaces.       |
| FR02-R01, R03        | LOGIN-PASSWORD-PRESENCE-V01/I01                                                     | Domain Testing | FR02-DT-001, 002, 004, 009        | UI/API  | Covered                 | Provided and missing Password covered on both surfaces.    |
| FR02-R13, SF02       | LOGIN-EMAIL-FORMAT-V01/I01; FORM-EMAIL-TYPE-V01/I01                                 | Domain Testing | FR02-DT-005, 015                  | UI      | Covered                 | API email-format rejection excluded; not specified.        |
| FR02-R04, R10, API04 | LOGIN-CREDENTIALS-V01; API-SUCCESS-V01; UI-SUCCESS-V01                              | Domain Testing | FR02-DT-001, 002                  | UI/API  | Covered                 | Successful login covered on both surfaces.                 |
| FR02-R05, R09        | LOGIN-CREDENTIALS-I01; LOGIN-ERROR-NONLEAKY-V01                                     | Domain Testing | FR02-DT-006, 010                  | UI/API  | Covered                 | Wrong password covered on both surfaces.                   |
| FR02-R09             | LOGIN-ACCOUNT-EXISTS-I01; LOGIN-ERROR-NONLEAKY-V01                                  | Domain Testing | FR02-DT-007, 011                  | UI/API  | Covered                 | Non-existing account covered without exact message oracle. |
| FR02-R05, R06, R08   | LOGIN-LOCKOUT-THRESHOLD-V01; LOGIN-LOCKOUT-ACTIVE-V01                               | Domain Testing | FR02-DT-012, 013, 019, 020        | UI/API  | Covered                 | General lockout covered separately from BVA.               |
| FR02-R07             | LOGIN-LOCKOUT-EXPIRED-V01                                                           | Domain Testing | FR02-DT-021, 022                  | UI/API  | Covered                 | Expired-lockout state covered on both surfaces.            |
| FR02-SF01            | FORM-REQUIRED-MARKER-V01/I01                                                        | Domain Testing | FR02-DT-014                       | UI      | Covered                 | Required marker conformance case.                          |
| FR02-SF03            | FORM-PASSWORD-TYPE-V01/I01                                                          | Domain Testing | FR02-DT-016                       | UI      | Covered                 | Password masking conformance case.                         |
| FR02-SF04            | FORM-ERROR-PLACEMENT-V01/I01                                                        | Domain Testing | FR02-DT-017                       | UI      | Covered                 | Error placement conformance case.                          |
| FR02-R11             | TOKEN-STORAGE-V01                                                                   | Domain Testing | FR02-DT-001                       | UI      | Covered                 | Storage key unspecified.                                   |
| FR02-R12             | AUTHORIZATION-HEADER-V01                                                            | Domain Testing | FR02-DT-018                       | UI/API  | Covered                 | Uses documented authenticated request header.              |
| FR02-R05, R06        | FR02-FAILED-ATTEMPTS-B01/B02/B03/N01                                                | BVA            | FR02-BVA-001 through FR02-BVA-008 | UI/API  | Covered                 | Threshold values covered on both surfaces.                 |
| FR02-R07             | FR02-LOCKOUT-DURATION-B01/B02/B03/N01                                               | BVA            | FR02-BVA-009 through FR02-BVA-016 | UI/API  | Covered                 | Duration values covered on both surfaces.                  |
| FR02 ambiguities     | LOGIN-EMAIL-WHITESPACE-A01; LOGIN-EMAIL-CASE-A01; LOGIN-COUNTER-RESET-A01; STEP-A01 | Exploratory    | None                              | UI/API  | Exploratory - No Oracle | Listed in backlog; excluded from normative coverage.       |

## Design Gaps and Assumptions

- Controlled account state must be prepared through public setup or documented accounts without inspecting database records.
- BVA sequences can change account lockout state; execution must isolate or reset state through public means.
- Exact invalid API statuses, response bodies, UI messages, token claims, token storage key, and redirect target are unspecified.
- Timing BVA depends on whole-second observation; exact millisecond behaviour is not asserted.
- No normative tests cover whitespace handling, Email case normalization, counter reset on success, or step indicator because no oracle exists.
- All cases are design-time only. No execution, evidence, Pass/Fail/Blocked result, bug report, or GitHub Issue is created in Phase 5.

## Human Review - Phase 5

- Reviewer:
- Review Date and Time:
- Review Scope: FR-02 Test-Case Design
- Corrections Made:
- Missing Cases Added:
- Test Cases Before Review: 22 DT and 16 BVA
- Test Cases After Review: Pending
- Duplicate Cases Removed:
- Incorrect Cases Removed:
- Status: Pending
- Approved for Validation: No
- Approved for Traceability and Quality Review: No
- Approved for Test Execution: No
```

## Phase 7 Placeholder: Bug Report

Output file: `reports/FR-02/bug-report.md`

```markdown
# Bug Report - FR-02 Login and Account Lockout

## Status

No confirmed bugs are recorded for FR-02 yet.

Phase 6 execution and Phase 7 human-verified evidence have not been performed. Per the `domain-testing-bva` skill, bug records may be created only after:

1. A test has a documented expected result.
2. Observable public UI/API behaviour contradicts that expected result.
3. The failure has been reproduced.
4. Human-verified evidence exists.

## Pending Execution

- Test cases remain `Not Executed`.
- Evidence files have not been captured.
- GitHub Issues have not been created.
- GitHub Issue links remain not applicable until confirmed bugs exist.

## Human Review

- Reviewer:
- Review Date and Time:
- Human Review Status: Pending
- Human Corrections:
```

## Phase 8 Placeholder: AI Gap Analysis

Output file: `reports/FR-02/ai-gap-analysis.md`

```markdown
# AI Gap Analysis - FR-02 Login and Account Lockout

## Scope and Sources

FR-02 AI Gap Analysis is not yet final because FR-02 has not passed the human review gate, execution has not occurred, and no human-reviewed corrections or runtime findings are available.

This placeholder preserves the required workspace structure without inventing gaps, evidence, bugs, or execution results.

## Current Baseline

| Artifact                | Current State                                    |
| ----------------------- | ------------------------------------------------ |
| Requirement analysis    | Created from approved black-box test bases only. |
| Domain model            | Created by AI; human review pending.             |
| Boundary value analysis | Created by AI; human review pending.             |
| Test cases              | Created by AI; all cases are `Not Executed`.     |
| Execution results       | None.                                            |
| Evidence                | None.                                            |
| Confirmed bugs          | None.                                            |
| GitHub Issue links      | None.                                            |

## Gap Register

No AI gaps are recorded yet. Gap analysis must compare preserved initial AI outputs with later human-reviewed reports, human corrections, execution evidence, and bug records. Those inputs do not exist yet for FR-02.

## AI Gap Summary

- Human review is pending.
- Test execution is not approved.
- No runtime behaviour has been observed.
- No bug report has been confirmed.

## Lessons Learned

Lessons learned will be added after human review and execution reveal actual AI omissions, human improvements, or runtime findings.

## Human Review

- Reviewer: Pending
- Review Date and Time: Pending
- Human Review Status: Pending
- Human Corrections: Pending
```

## AI Prompt Artifact

Output file: `evidence/agent-skill/FR-02/phase-01-05-design-prompt.md`

````markdown
Use the `domain-testing-bva` Agent Skill to complete FR-02 using the same report style, formatting, naming conventions, and quality level as the completed FR-01 artifacts.

Project root: current repository
Feature ID: FR-02
Feature name: Login and account lockout
Pool: A
Output directory: `reports/FR-02/`
AI evidence directory: `evidence/agent-skill/FR-02/`
AI audit file: `ai-audit/ai-audit.md`

Follow the current skill exactly:

`.agents/skills/domain-testing-bva/SKILL.md`

Do not redesign the workflow, do not add extra phases, and do not create Phase 9. Execute only the phases currently defined in the skill, from Feature Intake through AI Gap Analysis, while respecting all human review and execution gates.

Use FR-01 as the formatting and quality model. Study these completed FR-01 artifacts before creating FR-02:

- `reports/FR-01/requirement-analysis.md`
- `reports/FR-01/domain-testing.md`
- `reports/FR-01/boundary-value-analysis.md`
- `reports/FR-01/test-cases.md`
- `reports/FR-01/bug-report.md`
- `reports/FR-01/ai-gap-analysis.md`
- `ai-audit/ai-audit.md`
- `evidence/agent-skill/FR-01/`

Use FR-01 only as a template for:

- File structure.
- Heading structure.
- Table format.
- Rule ID naming style.
- Partition ID naming style.
- Test case format.
- Coverage summary format.
- Human review block format.
- Bug report format.
- AI gap analysis format.
- AI audit style.
- Evidence naming style.

Do not copy FR-01 requirements, partitions, test data, bugs, execution results, or conclusions into FR-02 unless they are explicitly supported by the FR-02 approved test basis.

Read all required skill references before working:

- `.agents/skills/domain-testing-bva/references/instructor-clarifications.md`
- `.agents/skills/domain-testing-bva/references/assignment-requirements.md`
- `.agents/skills/domain-testing-bva/references/eshop-analysis-guide.md`
- `.agents/skills/domain-testing-bva/references/domain-testing-method.md`
- `.agents/skills/domain-testing-bva/references/bva-method.md`
- `.agents/skills/domain-testing-bva/references/test-case-schema.md`
- `.agents/skills/domain-testing-bva/references/human-review-checklist.md`

Strict rules:

1. This is black-box functional testing.
2. Do not inspect implementation source code.
3. Do not inspect frontend source, backend source, database schema, database records, controllers, services, routes, middleware, models, or internal tests.
4. Do not modify application source code.
5. Do not use implementation behaviour as the oracle.
6. Expected results must come only from approved requirements, API specification, observable public UI/API behaviour, explicit assumptions, ambiguities, or real execution evidence.
7. Do not fabricate requirements, test results, screenshots, evidence, bugs, or GitHub Issue links.
8. Leave GitHub Issue links as `Pending` unless real GitHub Issues already exist.
9. Preserve every prompt and AI output under `evidence/agent-skill/FR-02/`.
10. Append every AI interaction to `ai-audit/ai-audit.md`.
11. Do not commit or stage database files, build artifacts, `node_modules`, logs, or unrelated files.

Create the FR-02 workspace with this final structure:

```text
reports/FR-02/
|-- requirement-analysis.md
|-- domain-testing.md
|-- boundary-value-analysis.md
|-- test-cases.md
|-- bug-report.md
|-- ai-gap-analysis.md
`-- evidence/
    |-- <TEST-CASE-ID>.png
    `-- <other-real-evidence-files>
```
````

Do not create or require:

- `traceability-matrix.md`
- `execution-summary.md`
- `evidence-index.md`

The final execution summary will be written in the assignment-level `README.md` later.

For FR-02, extract the official login and account lockout requirements from approved black-box bases only. Pay attention to any documented rules about:

- Login identifier, such as email or username.
- Password.
- Required login fields.
- Successful login.
- Failed login.
- Invalid credentials.
- Existing and non-existing accounts.
- Account lockout.
- Failed-attempt threshold.
- Lockout duration.
- Unlock or reset conditions.
- Error message or error placement.
- Post-login redirect or user state.
- Shared form requirements relevant to the login form.
- Public login API contract, if documented.

For `reports/FR-02/requirement-analysis.md`, follow the same structure and level of detail as `reports/FR-01/requirement-analysis.md`. Create FR-02-specific rule IDs and test basis references. Record ambiguities, assumptions, observable behaviours, and exclusions clearly.

For `reports/FR-02/domain-testing.md`, follow the same structure and level of detail as `reports/FR-01/domain-testing.md`. Identify FR-02-specific variables, states, outputs, dependencies, valid partitions, invalid partitions, representatives, and assumptions. Use stable FR-02 partition IDs such as `LOGIN-EMAIL-PRESENCE-V01`, but only create IDs that are actually supported by the test basis.

For `reports/FR-02/boundary-value-analysis.md`, follow the same structure and level of detail as `reports/FR-01/boundary-value-analysis.md`. Apply BVA only to documented ordered or bounded domains. For FR-02, likely candidates may include failed-attempt count, lockout threshold, lockout duration, or time window, but use them only if they are explicitly documented in an approved test basis. Do not invent thresholds, limits, or durations.

For `reports/FR-02/test-cases.md`, follow the same format as `reports/FR-01/test-cases.md`. Generate both Domain Testing and BVA cases according to the current skill schema. Use IDs such as:

- `FR02-DT-001`
- `FR02-DT-002`
- `FR02-BVA-001`
- `FR02-BVA-002`

Before execution, every test case must contain exactly:

```text
Actual Result: Not Executed
Status: Not Executed
Evidence: None
```

The AI must not execute tests during test-case generation.

Inside `reports/FR-02/test-cases.md`, include a coverage summary in the same style as FR-01. The coverage summary must map:

- Each normative FR-02 partition to at least one DT case on each applicable public surface.
- Each selected FR-02 boundary value to at least one BVA case on each applicable public surface.
- Each omitted surface, partition, or boundary to a documented exclusion reason.
- Each dependency or blocking-prone conformance condition to a dedicated case when it can affect many later cases.

Run the validator after test-case generation only if the validator exists and matches the current skill schema:

```bash
python .agents/skills/domain-testing-bva/scripts/validate_test_cases.py reports/FR-02/test-cases.md
```

Fix only safe schema, formatting, reference, or validation errors. Do not invent execution results.

When the skill reaches a human review gate, stop and request human confirmation. The AI must not approve its own test cases.

After human review, record in `reports/FR-02/test-cases.md` or `ai-audit/ai-audit.md`:

- Reviewer.
- Review date and time.
- Review scope.
- Human corrections.
- Human-added, removed, or reclassified cases.
- Duplicate-case decisions.
- `Approved for Test Execution: Yes/No`.

Do not execute tests while approval is `No` or missing.

After human approval, execute only through public UI or public API. Do not inspect implementation code or database contents. For each attempted case, record:

- Execution date and time.
- Environment.
- Actual Result.
- Status: `Pass`, `Fail`, or `Blocked`.
- Blocking Reason when status is `Blocked`.
- Real evidence reference.

Save evidence under:

```text
reports/FR-02/evidence/<TEST-CASE-ID>.png
```

Evidence must match the exact test case and execution result. Do not leave a `Pass`, `Fail`, or `Blocked` case with `Evidence: None`.

After execution evidence is available, create or update:

- `reports/FR-02/bug-report.md`
- `reports/FR-02/ai-gap-analysis.md`

For `reports/FR-02/bug-report.md`, follow the same format as `reports/FR-01/bug-report.md`. Create bug records only when:

1. The test has a documented expected result.
2. The observable actual result contradicts it.
3. The failure has been reproduced.
4. Human-verified evidence exists.

For every confirmed bug, record:

- Bug ID.
- Title.
- Severity.
- Status.
- Related test case.
- Related requirement.
- Preconditions.
- Reproduction steps.
- Expected result.
- Actual result.
- Evidence links.
- GitHub Issue link.

Leave GitHub Issue links as `Pending` until real GitHub Issues are created.

For `reports/FR-02/ai-gap-analysis.md`, follow the same format as `reports/FR-01/ai-gap-analysis.md`. Compare preserved initial AI outputs with the current human-reviewed and executed artifacts. Separate:

- AI-missed test cases.
- Human improvements to existing tests.
- Runtime bugs exposed by AI-generated tests.
- Runtime bugs exposed by human-added tests.
- Runtime-only findings.
- Prompt-quality or reasoning gaps.

Do not claim runtime bugs were missed by AI if the AI generated the tests that exposed them.

At the end, report:

- Created and modified files.
- DT case count.
- BVA case count.
- Total test case count.
- Execution status counts.
- Evidence count.
- Confirmed bug count.
- Pending GitHub Issue count.
- Validator result, if the validator was run.
- Remaining blockers.
- Suggested git commits.

Suggested commit:

```bash
git add reports/FR-02 evidence/agent-skill/FR-02 ai-audit/ai-audit.md
git commit -m "test(fr02): complete black-box DT and BVA workflow"
```

````

## AI Output Summary Artifact

Output file: `evidence/agent-skill/FR-02/phase-01-05-design-ai-output.md`

```markdown
# FR-02 Phase 1-5 AI Output Summary

Created FR-02 black-box design artifacts using the `domain-testing-bva` skill and the completed FR-01 artifacts as formatting/quality references only.

## Created or Updated

- `reports/FR-02/requirement-analysis.md`
- `reports/FR-02/domain-testing.md`
- `reports/FR-02/boundary-value-analysis.md`
- `reports/FR-02/test-cases.md`
- `reports/FR-02/bug-report.md`
- `reports/FR-02/ai-gap-analysis.md`
- `reports/FR-02/evidence/`
- `evidence/agent-skill/FR-02/phase-01-05-design-prompt.md`
- `evidence/agent-skill/FR-02/phase-01-05-design-ai-output.md`

## Phase Result

- Completed Phase 1: Feature Intake.
- Completed Phase 2: Black-box Test Basis Collection.
- Completed Phase 3: Domain Modeling.
- Completed Phase 4: Boundary Value Analysis.
- Completed Phase 5: AI Test-Case Generation.
- Stopped at the human review gate before execution.

## Counts

- Domain Testing cases: 22
- Boundary Value Analysis cases: 16
- Total test cases: 38
- Execution status counts: 38 `Not Executed`, 0 `Pass`, 0 `Fail`, 0 `Blocked`
- Evidence count: 0
- Confirmed bug count: 0
- Pending GitHub Issue count: 0

## Validator

`python .agents/skills/domain-testing-bva/scripts/validate_test_cases.py reports/FR-02/test-cases.md`

Result: `Validation passed: 38 test case(s) in 1 file(s).`

## Integrity Notes

- No implementation source code was inspected.
- No frontend or backend source, database schema/records, controllers, services, routes, middleware, models, or internal tests were inspected.
- No application was started.
- No test was executed.
- No screenshots or execution evidence were captured.
- No Pass/Fail/Blocked result was fabricated.
- No bug or GitHub Issue was created.
- Human review remains pending and test execution is not approved.

````

## Audit Integrity Notes

- This audit captures report/design outputs only.
- Human review remains pending.
- Test execution is not approved.
- No execution evidence, Pass/Fail/Blocked result, confirmed bug, or GitHub Issue link is created by this audit update.
