# Requirement Analysis - FR-20 Login and Account Lockout (Mobile)

## Feature Intake

| Field               | Value                                                        |
| ------------------- | ------------------------------------------------------------ |
| Feature ID          | FR-20                                                        |
| Feature name        | Login and Account Lockout (Mobile)                           |
| Pool                | D - Mobile                                                   |
| Actor               | Guest / unauthenticated mobile user; registered user         |
| Application surface | React Native / Expo mobile app and public authentication API |
| UI location         | Mobile login screen in `frontend-mobile` runtime             |
| API endpoint        | `POST /api/login`                                            |
| Output root         | `reports/FR-20`                                              |

Note: the workspace script warned that `FR-20` may look inconsistent with Pool D naming, but `README.md` lists FR-20 under the Mobile subsystem. The supplied feature selection is therefore preserved.

## Approved Black-box Test Bases

- `README.md` - system overview and default backend/mobile setup information.
- `README.md` - FR-02 Login and Account Lockout, reused as the functional login-lockout requirement for the mobile implementation.
- `README.md` - FR-20 Mobile feature, requiring mobile app coverage for Login.
- `README.md` - FR-22 shared form requirements relevant to login forms.
- `api_specification.md` - 1.2 `POST /api/login`.
- `setup_guide.md` - public startup guidance for backend and Expo mobile, used only as execution setup basis.

No frontend/mobile implementation source, backend implementation source, database schema, controllers, services, routes, middleware, models, or internal tests were inspected.

## Requirement Rules

| Rule ID  | Rule                                                                                                | Test Basis Type      | Test Basis Reference                              | Observable Expected Behaviour                                                                      | Ambiguity                                                                                                     | Assumption                                                                                                             |
| -------- | --------------------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| FR20-R01 | The mobile app must provide Login functionality.                                                    | Official requirement | `README.md` - FR-20                               | Mobile users can access a login surface.                                                           | Exact screen route, labels, and navigation target are unspecified.                                            | A mobile login screen is the public UI surface for this feature.                                                       |
| FR20-R02 | User enters Email and Password to log in.                                                           | Official requirement | `README.md` - FR-02                               | Login request/form accepts email and password inputs.                                              | Exact empty-field message is unspecified.                                                                     | Missing email or missing password is invalid.                                                                          |
| FR20-R03 | Each failed login increments the failed-attempt counter by exactly one.                             | Official requirement | `README.md` - FR-02                               | One wrong-password attempt is rejected but does not lock before the threshold.                     | Counter value is not directly exposed.                                                                        | Public lockout transition is the observable proxy for counter increments.                                              |
| FR20-R04 | Three or more consecutive failed logins temporarily lock the account.                               | Official requirement | `README.md` - FR-02                               | On or after the third consecutive wrong password, later login attempts are rejected as locked.     | Exact status code and message are unspecified.                                                                | A 4xx/no-token lockout response is acceptable rejection.                                                               |
| FR20-R05 | Lockout duration is 30 seconds in demo environment.                                                 | Official requirement | `README.md` - FR-02                               | Correct login after the lockout duration should no longer be rejected solely due to lockout.       | Exact behaviour at precisely 30.000 seconds is unspecified.                                                   | `29`, `30`, and `31` seconds are useful boundary values.                                                               |
| FR20-R06 | Lockout error must not expose internal or sensitive cause details.                                  | Official requirement | `README.md` - FR-02                               | Lockout error is user-safe and does not expose implementation details.                             | Exact wording is unspecified.                                                                                 | Saying the account is locked is acceptable; exposing internal counters, database errors, or security internals is not. |
| FR20-R07 | Successful login returns a JWT token.                                                               | Official requirement | `README.md` - FR-02; `api_specification.md` - 1.2 | Successful login returns HTTP success with `token`.                                                | Exact token format and user fields are unspecified.                                                           | Token presence in public API response is sufficient for API success.                                                   |
| FR20-R08 | Token is stored client-side and sent in `Authorization: Bearer <token>` for authenticated requests. | Official requirement | `README.md` - FR-02                               | Authenticated mobile flows can later use bearer token.                                             | Client storage is not directly observable without mobile runtime/tool support.                                | Covered as a mobile UI/runtime dependency; API token presence is tested separately.                                    |
| FR20-R09 | Login email field must use email input semantics with format validation.                            | Official requirement | `README.md` - FR-02; `README.md` - FR-22          | Mobile login should provide email-oriented input behaviour; invalid email should not authenticate. | React Native does not expose HTML `type="email"`; equivalent keyboard/content-type semantics are unspecified. | API invalid-email tests assert no token; mobile UI semantics require mobile runtime evidence.                          |

## API Specification Rules

| Rule ID    | Rule                                                             | Test Basis Type                            | Test Basis Reference                                    | Observable Expected Behaviour                                                               | Ambiguity                                     | Assumption                                         |
| ---------- | ---------------------------------------------------------------- | ------------------------------------------ | ------------------------------------------------------- | ------------------------------------------------------------------------------------------- | --------------------------------------------- | -------------------------------------------------- |
| FR20-API01 | `POST /api/login` accepts JSON body with `email` and `password`. | API specification                          | `api_specification.md` - 1.2 Login                      | Request with valid registered credentials succeeds.                                         | Missing-property status/body are unspecified. | Missing required properties are invalid.           |
| FR20-API02 | Successful login returns JWT `token` and `user` information.     | API specification                          | `api_specification.md` - 1.2 Login                      | Response includes a token and user object.                                                  | Exact user fields are unspecified.            | Token is the primary success oracle.               |
| FR20-API03 | Invalid credentials are rejected.                                | Official requirement / API behaviour basis | `README.md` - FR-02; `api_specification.md` - 1.2 Login | Wrong password, missing required properties, or invalid email format do not return a token. | Exact status/body are unspecified.            | Any 4xx/no-token response is acceptable rejection. |

## Shared Form Rules

| Rule ID     | Rule                                                    | Test Basis Type      | Test Basis Reference | Observable Expected Behaviour                                                        | Ambiguity                                         | Assumption                                                             |
| ----------- | ------------------------------------------------------- | -------------------- | -------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------------- | ---------------------------------------------------------------------- |
| FR20-FORM01 | Required fields have visible `*` beside labels.         | Official requirement | `README.md` - FR-22  | Mobile login required fields show required markers or equivalent visible indication. | Mobile label style is unspecified.                | Applies if labels are used in mobile UI.                               |
| FR20-FORM02 | Email field uses email input type or mobile equivalent. | Official requirement | `README.md` - FR-22  | Mobile email input uses equivalent email keyboard/content-type semantics.            | HTML `type="email"` is web-specific.              | Mobile equivalent is treated as email keyboard/content-type semantics. |
| FR20-FORM03 | Password field masks input.                             | Official requirement | `README.md` - FR-22  | Mobile password input does not display clear text.                                   | Exact masking character is unspecified.           | Password should not be visibly clear.                                  |
| FR20-FORM04 | Error messages appear above the submit button.          | Official requirement | `README.md` - FR-22  | Mobile login validation/login errors appear above the login submit control.          | Exact message and layout spacing are unspecified. | Applies to login form errors.                                          |

## Requirement Ambiguities

- FR-20 broadly lists mobile coverage; this report scopes FR-20 to Login and Account Lockout (Mobile).
- Exact mobile login route, screen title, button text, and post-login navigation are not specified.
- React Native equivalent for HTML `type="email"` is ambiguous.
- Exact invalid-login, lockout, missing-field, and expired-lockout status codes/messages are unspecified.
- Failed-attempt counter value is not exposed by API; lockout transition is used as public evidence.
- Exact behaviour at precisely 30.000 seconds is unspecified.
- Client-side token storage cannot be verified through API-only execution.

## Assumptions

- Public API login behaviour is a valid black-box test surface for the mobile login feature because the mobile app uses the same documented backend API.
- Disposable registered users created through `POST /api/register` may be used as setup data for login-lockout tests.
- Any 4xx response without token is an acceptable rejection for invalid credentials unless a rule specifies an exact status/body.
- Mobile UI-only checks require an observable Expo Go/device/emulator session; without it, those cases are recorded as Blocked rather than Pass or Fail.
- Source code inspection is not used to infer expected or actual behaviour.

## Coverage Gaps

- Mobile UI login screen, email keyboard semantics, password masking, required markers, and error placement require Expo/device/emulator evidence.
- Client-side token storage and mobile bearer-token reuse are not directly verified by API-only execution.
- Exact status/body for invalid input and lockout are not specified, so tests avoid over-asserting exact messages.
- No implementation source or database state was used to verify failed-attempt counter increments.

## Human Review

- Reviewer: Nguyen Thanh Tien
- Review Date and Time: 2026-06-27 16:09
- Review Scope: FR-20 requirement analysis and black-box test basis
- Human Review Status: Completed
- Approved for Domain Modeling: Yes
- Approved for BVA: Yes
- Approved for Test-Case Derivation: Yes
- Approved for Test Execution: Yes

## Human Corrections

- Clarified that FR-20 is scoped to mobile Login and Account Lockout.
- Kept API login as a valid black-box surface because the mobile app uses the documented backend API.
- Clarified that mobile email input semantics are not identical to HTML `type="email"`.
- Treated mobile UI-only checks as blocked unless Expo/device evidence is available.
- Removed the contradiction between pending human review and approved execution.
