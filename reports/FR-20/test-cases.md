# Test Cases - FR-20 Login and Account Lockout (Mobile)

## Domain Testing Test Cases

## FR20-DT-001

- Test Case ID: FR20-DT-001
- Technique: Domain Testing
- Objective: Verify valid registered credentials log in successfully through the public login API used by mobile.
- Requirement or Rule Reference: FR20-R07, FR20-API01, FR20-API02
- Preconditions: Backend API is available; user `test@eshop.com` exists and is not locked.
- Test Data: `{"email":"test@eshop.com","password":"Test1234!"}`.
- Steps:
  1. Send `POST /api/login` with registered email and correct password.
  2. Observe HTTP status and response body.
- Expected Result: Login succeeds and response includes a JWT `token` and `user`.
- Actual Result: `POST /api/login` with `test@eshop.com` / `Test1234!` returned HTTP `200 OK`. The response body contained `message: "Login successful"`, a JWT `token`, and a `user` object for `test@eshop.com`.
- Status: Pass
- Evidence: [FR20-DT-001](./evidence/FR20-DT-001.png)
- Test Basis Reference: `requirement-analysis.md` - FR20-R07, FR20-API01, FR20-API02; `domain-testing.md` - CREDENTIALS-MATCH-V01, API-SUCCESS-V01

## FR20-DT-002

- Test Case ID: FR20-DT-002
- Technique: Domain Testing
- Objective: Verify missing email is rejected.
- Requirement or Rule Reference: FR20-R02, FR20-API01, FR20-API03
- Preconditions: Backend API is available.
- Test Data: `{"password":"Test1234!"}`.
- Steps:
  1. Send `POST /api/login` without `email`.
  2. Observe status/body and token absence.
- Expected Result: Request is rejected and no token is returned.
- Actual Result: `POST /api/login` without `email` returned HTTP `401 Unauthorized` with body `{"error":"Invalid email or password"}`. No JWT `token` was returned.
- Status: Pass
- Evidence: [FR20-DT-002](./evidence/FR20-DT-002.png)
- Test Basis Reference: `requirement-analysis.md` - FR20-R02, FR20-API01, FR20-API03; `domain-testing.md` - EMAIL-MISSING-I01, API-REJECTION-I01

## FR20-DT-003

- Test Case ID: FR20-DT-003
- Technique: Domain Testing
- Objective: Verify missing password is rejected.
- Requirement or Rule Reference: FR20-R02, FR20-API01, FR20-API03
- Preconditions: Backend API is available; user `test@eshop.com` exists.
- Test Data: `{"email":"test@eshop.com"}`.
- Steps:
  1. Send `POST /api/login` without `password`.
  2. Observe status/body and token absence.
- Expected Result: Request is rejected and no token is returned.
- Actual Result: `POST /api/login` without `password` returned HTTP `401 Unauthorized` with body `{"error":"Invalid email or password"}`. No JWT `token` was returned.
- Status: Pass
- Evidence: [FR20-DT-003](./evidence/FR20-DT-003.png)
- Test Basis Reference: `requirement-analysis.md` - FR20-R02, FR20-API01, FR20-API03; `domain-testing.md` - PASSWORD-MISSING-I01, API-REJECTION-I01

## FR20-DT-004

- Test Case ID: FR20-DT-004
- Technique: Domain Testing
- Objective: Verify invalid email format does not authenticate.
- Requirement or Rule Reference: FR20-R09, FR20-API03
- Preconditions: Backend API is available.
- Test Data: `{"email":"not-an-email","password":"Test1234!"}`.
- Steps:
  1. Send `POST /api/login` with invalid email format.
  2. Observe status/body and token absence.
- Expected Result: Request is rejected and no token is returned.
- Actual Result: `POST /api/login` with malformed email `not-an-email` returned HTTP `401 Unauthorized` with body `{"error":"Invalid email or password"}`. No JWT `token` was returned.
- Status: Pass
- Evidence: [FR20-DT-004](./evidence/FR20-DT-004.png)
- Test Basis Reference: `requirement-analysis.md` - FR20-R09, FR20-API03; `domain-testing.md` - EMAIL-FORMAT-I01, API-REJECTION-I01

## FR20-DT-005

- Test Case ID: FR20-DT-005
- Technique: Domain Testing
- Objective: Verify a wrong password is rejected before lockout.
- Requirement or Rule Reference: FR20-R03, FR20-API03
- Preconditions: Backend API is available; user `test@eshop.com` exists and is not locked.
- Test Data: `{"email":"test@eshop.com","password":"Wrong123!"}`.
- Steps:
  1. Send `POST /api/login` with registered email and wrong password.
  2. Observe status/body and token absence.
- Expected Result: Request is rejected and no token is returned.
- Actual Result: `POST /api/login` with `test@eshop.com` and wrong password `Wrong123!` returned HTTP `401 Unauthorized` with body `{"error":"Invalid email or password"}`. No JWT `token` was returned.
- Status: Pass
- Evidence: [FR20-DT-005](./evidence/FR20-DT-005.png)
- Test Basis Reference: `requirement-analysis.md` - FR20-R03, FR20-API03; `domain-testing.md` - CREDENTIALS-MISMATCH-I01, API-REJECTION-I01

## FR20-DT-006

- Test Case ID: FR20-DT-006
- Technique: Domain Testing
- Objective: Verify correct password is rejected while account is locked.
- Requirement or Rule Reference: FR20-R04, FR20-R05
- Preconditions: Backend API is available; account `test@eshop.com` has just reached lockout threshold.
- Test Data: `{"email":"test@eshop.com","password":"Test1234!"}` after lockout is triggered.
- Steps:
  1. Trigger lockout with three consecutive wrong passwords for `test@eshop.com`.
  2. Immediately send `POST /api/login` with correct password `Test1234!`.
  3. Observe status/body and token absence.
- Expected Result: Request is rejected while lockout is active.
- Actual Result: After lockout was triggered, `POST /api/login` with correct password `Test1234!` returned HTTP `403 Forbidden` with body `{"error":"Tài khoản đã bị khóa. Vui lòng thử lại sau."}`. No JWT `token` was returned.
- Status: Pass
- Evidence: [FR20-DT-006](./evidence/FR20-DT-006.png)
- Test Basis Reference: `requirement-analysis.md` - FR20-R04, FR20-R05; `domain-testing.md` - LOCKED-CORRECT-I01

## FR20-DT-007

- Test Case ID: FR20-DT-007
- Technique: Domain Testing
- Objective: Verify the mobile login screen is accessible.
- Requirement or Rule Reference: FR20-R01
- Preconditions: Expo mobile runtime, Expo Go device, Android emulator, iOS simulator, or equivalent observable session is available.
- Test Data: Open mobile app.
- Steps:
  1. Launch the mobile app through Expo.
  2. Navigate to or observe login screen.
  3. Confirm email/password login controls are visible and usable.
- Expected Result: Login screen is visible and usable.
- Actual Result: The mobile app displayed the login screen titled `Đăng Nhập`. The screen showed an email/username input, a password input, a `Sign In` submit button, and related login navigation controls.
- Status: Pass
- Evidence: [FR20-DT-007](./evidence/FR20-DT-007.png)
- Test Basis Reference: `requirement-analysis.md` - FR20-R01; `domain-testing.md` - MOBILE-SCREEN-V01; `setup_guide.md` - Frontend Mobile

## FR20-DT-008

- Test Case ID: FR20-DT-008
- Technique: Domain Testing
- Objective: Verify mobile login required fields display required markers.
- Requirement or Rule Reference: FR20-FORM01
- Preconditions: Mobile login screen is observable.
- Test Data: Login screen labels for email and password.
- Steps:
  1. Open mobile login screen.
  2. Inspect email/password labels or required-field indicators.
- Expected Result: Required fields show `*` or equivalent visible required markers beside labels.
- Actual Result: The mobile login screen displayed labels for `Username` and `Mật khẩu`, but no visible `*` marker or equivalent required-field indicator was shown beside either required field.
- Status: Fail
- Evidence: [FR20-DT-008](./evidence/FR20-DT-007.png)
- Test Basis Reference: `requirement-analysis.md` - FR20-FORM01; `domain-testing.md` - FORM-REQUIRED-MARKER-I01

## FR20-DT-009

- Test Case ID: FR20-DT-009
- Technique: Domain Testing
- Objective: Verify mobile password input masks entered password.
- Requirement or Rule Reference: FR20-FORM03
- Preconditions: Mobile login screen is observable.
- Test Data: Type `Test1234!` into password field.
- Steps:
  1. Open mobile login screen.
  2. Enter password text.
  3. Observe whether characters are masked.
- Expected Result: Password value is not displayed in clear text.
- Actual Result: After entering `Test1234!` into the mobile password field, the tester directly observed that the value was displayed as masked dots instead of clear text.
- Status: Pass
- Evidence: [FR20-DT-009](./evidence/FR20-DT-009.png)
- Test Basis Reference: `requirement-analysis.md` - FR20-FORM03; `domain-testing.md` - FORM-PASSWORD-MASK-V01

## FR20-DT-010

- Test Case ID: FR20-DT-010
- Technique: Domain Testing
- Objective: Verify mobile login error appears above the submit button.
- Requirement or Rule Reference: FR20-FORM04
- Preconditions: Mobile login screen is observable.
- Test Data: Email `test@eshop.com` with missing/invalid password.
- Steps:
  1. Open mobile login screen.
  2. Enter `test@eshop.com` in the email/username field.
  3. Leave the password field empty or submit invalid credentials.
  4. Tap `Sign In`.
  5. Observe error placement relative to submit button.
- Expected Result: Error message appears above the submit button.
- Actual Result: After tapping `Sign In`, the mobile login screen displayed the error message `Đăng nhập thất bại. Vui lòng kiểm tra lại.` below the `Sign In` submit button, not above it.
- Status: Fail
- Evidence: [FR20-DT-010](./evidence/FR20-DT-010.png)
- Test Basis Reference: `requirement-analysis.md` - FR20-FORM04; `domain-testing.md` - FORM-ERROR-PLACEMENT-I01

## FR20-DT-011

- Test Case ID: FR20-DT-011
- Technique: Domain Testing
- Objective: Verify mobile email input uses email keyboard/content-type semantics or equivalent validation.
- Requirement or Rule Reference: FR20-R09, FR20-FORM02
- Preconditions: Mobile login screen is observable.
- Test Data: Email input value `not-an-email`; nominal password value.
- Steps:
  1. Open mobile login screen.
  2. Focus the email/username field.
  3. Enter malformed email `not-an-email`.
  4. Enter a nominal password value.
  5. Tap `Sign In`.
  6. Observe whether malformed email authenticates.
- Expected Result: Mobile email input uses email-oriented semantics or rejects malformed email without authentication.
- Actual Result: After entering malformed email `not-an-email` and submitting the login form, the mobile app displayed the error message `Đăng nhập thất bại. Vui lòng kiểm tra lại.` and did not enter an authenticated state.
- Status: Pass
- Evidence: [FR20-DT-011](./evidence/FR20-DT-011.png)
- Test Basis Reference: `requirement-analysis.md` - FR20-R09, FR20-FORM02; `domain-testing.md` - FORM-EMAIL-SEMANTICS-V01, EMAIL-FORMAT-I01

## FR20-DT-012

- Test Case ID: FR20-DT-012
- Technique: Domain Testing
- Objective: Verify mobile app reaches authenticated state after valid login.
- Requirement or Rule Reference: FR20-R01, FR20-R08
- Preconditions: Mobile login screen is observable; backend API is available; registered user `test@eshop.com` exists and is not locked.
- Test Data: `test@eshop.com` / `Test1234!`.
- Steps:
  1. Open mobile login screen.
  2. Enter `test@eshop.com` in the email/username field.
  3. Enter correct password `Test1234!`.
  4. Tap `Sign In`.
  5. Observe whether the mobile app reaches an authenticated state or authenticated screen.
- Expected Result: Mobile app logs in successfully and reaches an authenticated state.
- Actual Result: After entering valid credentials `test@eshop.com` / `Test1234!` and tapping `Sign In`, the mobile app remained on the login screen and displayed the error message `Đăng nhập thất bại. Vui lòng kiểm tra lại.` No authenticated mobile state was reached.
- Status: Fail
- Evidence: [FR20-DT-012](./evidence/FR20-DT-012.png)
- Test Basis Reference: `requirement-analysis.md` - FR20-R01, FR20-R08; `domain-testing.md` - MOBILE-POSTLOGIN-I01

## Boundary Value Analysis Test Cases

## FR20-BVA-001

- Test Case ID: FR20-BVA-001
- Technique: Boundary Value Analysis
- Objective: Verify the second consecutive wrong login remains below the lockout threshold.
- Requirement or Rule Reference: FR20-R03, FR20-R04
- Preconditions: Backend API is available; test account is registered, unlocked, and starts with zero consecutive failed-login attempts.
- Test Data: Same registered email with `Wrong123!`; attempt count = 2.
- Steps:
  1. Send a first wrong-password login.
  2. Send a second consecutive wrong-password login.
  3. Observe status/body.
  4. Optionally send a correct-password login to confirm the account is not locked.
- Expected Result: Second wrong attempt is rejected as invalid credentials but does not yet lock the account.
- Actual Result: Execution could not be completed because no verified clean/unlocked account with zero consecutive failed-login attempts was available. The previously used account state was affected by earlier login and lockout tests.
- Status: Blocked
- Blocking Reason: Clean account state was unavailable, so the second-attempt boundary could not be evaluated reliably.
- Evidence: None
- Test Basis Reference: `boundary-value-analysis.md` - FR20-ATTEMPT-LOCK-B01; `requirement-analysis.md` - FR20-R03, FR20-R04

## FR20-BVA-002

- Test Case ID: FR20-BVA-002
- Technique: Boundary Value Analysis
- Objective: Verify the third consecutive wrong login triggers account lockout.
- Requirement or Rule Reference: FR20-R04
- Preconditions: Backend API is available; same account has two immediately prior wrong logins.
- Test Data: Same registered email with `Wrong123!`; attempt count = 3.
- Steps:
  1. Send first and second consecutive wrong-password logins.
  2. Send third consecutive wrong-password login.
  3. Observe status/body and token absence.
- Expected Result: Third wrong attempt locks the account and returns a locked/rejected response without token.
- Actual Result: Execution could not be completed because no verified clean/unlocked account with controlled consecutive failed-login state was available. The previously used account state was affected by earlier login and lockout tests, so the third-attempt lockout boundary could not be evaluated reliably.
- Status: Blocked
- Blocking Reason: Clean account state with exactly two immediately prior wrong logins was unavailable.
- Evidence: None
- Test Basis Reference: `boundary-value-analysis.md` - FR20-ATTEMPT-LOCK-B02; `requirement-analysis.md` - FR20-R04

## FR20-BVA-003

- Test Case ID: FR20-BVA-003
- Technique: Boundary Value Analysis
- Objective: Verify a fourth consecutive wrong login remains in locked classification.
- Requirement or Rule Reference: FR20-R04
- Preconditions: Backend API is available; same account has reached lockout through three consecutive wrong logins.
- Test Data: Same registered email with `Wrong123!`; attempt count = 4.
- Steps:
  1. Send three consecutive wrong-password logins to reach lockout.
  2. Send a fourth wrong-password login.
  3. Observe status/body and token absence.
- Expected Result: Fourth wrong attempt is still rejected as locked or otherwise not authenticated.
- Actual Result: Execution could not be completed because no verified account with a controlled three-attempt lockout setup was available. The previously used account state was affected by earlier login and lockout tests, so the fourth-attempt above-threshold boundary could not be evaluated reliably.
- Status: Blocked
- Blocking Reason: Controlled locked account state after exactly three consecutive wrong logins was unavailable.
- Evidence: None
- Test Basis Reference: `boundary-value-analysis.md` - FR20-ATTEMPT-LOCK-B03; `requirement-analysis.md` - FR20-R04

## FR20-BVA-004

- Test Case ID: FR20-BVA-004
- Technique: Boundary Value Analysis
- Objective: Verify lockout remains active at 29 seconds after lockout.
- Requirement or Rule Reference: FR20-R05
- Preconditions: Backend API is available; disposable account is locked by three wrong attempts.
- Test Data: Same locked email with correct password `Test1234!`; wait approximately 29 seconds.
- Steps:
  1. Trigger lockout with three consecutive wrong-password logins.
  2. Wait approximately 29 seconds from lockout.
  3. Send `POST /api/login` with correct password.
  4. Observe status/body and token absence.
- Expected Result: At 29 seconds, the account is still within the documented 30-second lockout and login is rejected due active lockout.
- Actual Result: Execution could not be completed because no verified controlled lockout start time was available. The previously used account state was affected by earlier login and lockout tests, so the 29-second active-lockout boundary could not be evaluated reliably.
- Status: Blocked
- Blocking Reason: Controlled lockout start time was unavailable for measuring the 29-second boundary.
- Evidence: None
- Test Basis Reference: `boundary-value-analysis.md` - FR20-LOCK-DURATION-B01; `requirement-analysis.md` - FR20-R05

## FR20-BVA-005

- Test Case ID: FR20-BVA-005
- Technique: Boundary Value Analysis
- Objective: Verify lockout expiry at the documented 30-second boundary.
- Requirement or Rule Reference: FR20-R05
- Preconditions: Backend API is available; disposable account is locked by three wrong attempts.
- Test Data: Same locked email with correct password `Test1234!`; wait approximately 30 seconds.
- Steps:
  1. Trigger lockout with three consecutive wrong-password logins.
  2. Wait approximately 30 seconds from lockout.
  3. Send `POST /api/login` with correct password.
  4. Observe whether lockout still blocks the request.
- Expected Result: At the documented 30-second duration, the account is no longer rejected solely due to lockout. Exact timing precision is unspecified.
- Actual Result: Execution could not be completed because no verified controlled lockout start time was available. The previously used account state was affected by earlier login and lockout tests, so the 30-second expiry boundary could not be evaluated reliably.
- Status: Blocked
- Blocking Reason: Controlled lockout start time was unavailable for measuring the 30-second boundary.
- Evidence: None
- Test Basis Reference: `boundary-value-analysis.md` - FR20-LOCK-DURATION-B02; `requirement-analysis.md` - FR20-R05

## FR20-BVA-006

- Test Case ID: FR20-BVA-006
- Technique: Boundary Value Analysis
- Objective: Verify correct login succeeds after the 30-second lockout duration expires.
- Requirement or Rule Reference: FR20-R05
- Preconditions: Backend API is available; disposable account is locked by three wrong attempts.
- Test Data: Same locked email with correct password `Test1234!`; wait approximately 31 seconds.
- Steps:
  1. Trigger lockout with three consecutive wrong-password logins.
  2. Wait approximately 31 seconds from lockout.
  3. Send `POST /api/login` with correct password.
  4. Observe status/body and token presence.
- Expected Result: Because lockout duration is 30 seconds in demo, correct login after more than 30 seconds succeeds and returns token.
- Actual Result: Execution could not be completed because no verified controlled lockout start time was available. The previously used account state was affected by earlier login and lockout tests, so the 31-second post-expiry boundary could not be evaluated reliably.
- Status: Blocked
- Blocking Reason: Controlled lockout start time was unavailable for measuring the 31-second boundary.
- Evidence: None
- Test Basis Reference: `boundary-value-analysis.md` - FR20-LOCK-DURATION-B03; `requirement-analysis.md` - FR20-R05

## FR20-BVA-007

- Test Case ID: FR20-BVA-007
- Technique: Boundary Value Analysis
- Objective: Verify nominal active-lockout state at 10 seconds.
- Requirement or Rule Reference: FR20-R05
- Preconditions: Backend API is available; disposable account is locked by three wrong attempts.
- Test Data: Same locked email with correct password `Test1234!`; wait approximately 10 seconds.
- Steps:
  1. Trigger lockout with three consecutive wrong-password logins.
  2. Wait approximately 10 seconds from lockout.
  3. Send `POST /api/login` with correct password.
  4. Observe status/body and token absence.
- Expected Result: At 10 seconds, the account remains inside the active lockout period and login is rejected due lockout.
- Actual Result: Execution could not be completed because no verified controlled lockout start time was available. The previously used account state was affected by earlier login and lockout tests, so the 10-second nominal active-lockout case could not be evaluated reliably.
- Status: Blocked
- Blocking Reason: Controlled lockout start time was unavailable for measuring the 10-second active-lockout state.
- Evidence: None
- Test Basis Reference: `boundary-value-analysis.md` - FR20-LOCK-DURATION-N01; `requirement-analysis.md` - FR20-R05

## Human Review - Phase 5

- Reviewer: Nguyen Thanh Tien
- Review Date and Time: 2026-06-27 19:46
- Review Scope: FR-20 test-case design and execution-result wording
- Human Review Status: Completed
- Approved for Test Execution: Yes

## Human Corrections

- Kept API login cases separate from mobile UI cases because API execution cannot prove mobile keyboard semantics, visual required markers, error placement, navigation, or client-side token storage.
- Added missing mobile email semantics case `FR20-DT-011`.
- Added missing mobile post-login/authenticated-state case `FR20-DT-012`.
- Expanded BVA coverage from only 2/3/31-second checks to include attempt-count `4`, lockout duration `29s`, `30s`, `31s`, and nominal active `10s`.
- Updated BVA references to specific boundary IDs instead of broad combined IDs.
- Updated executed cases with real Actual Result, Status, and Evidence references after manual API/mobile execution.
- Recorded BVA cases as Blocked because clean account state and controlled lockout timing were unavailable.
