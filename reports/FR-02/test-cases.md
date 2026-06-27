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
- Actual Result: After submitting valid credentials, the system navigated to the product list page. The navbar displayed `Chào, Test User` and a `Thoát` button, indicating an authenticated UI state. A JWT token was observed in browser localStorage.
- Status: Pass
- Evidence: [FR02-DT-001](./evidence/FR02-DT-001.png)
- Test Basis Reference: `requirement-analysis.md` - FR02-R04, FR02-R10, FR02-R11; `domain-testing.md` - LOGIN-CREDENTIALS-V01, UI-SUCCESS-V01, TOKEN-STORAGE-V01

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
- Actual Result: The API request `POST /api/login` with valid credentials returned `200 OK`. The response body contained a JWT `token` and `user` information.
- Status: Pass
- Evidence: [FR02-DT-002](./evidence/FR02-DT-002.png)
- Test Basis Reference: `requirement-analysis.md` - FR02-API01 through FR02-API04; `domain-testing.md` - API-REQUEST-V01, API-SUCCESS-V01

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
- Actual Result: After submitting the login form with the Email/Username field empty and Password filled, the browser displayed a required-field validation message on the empty field: `Vui lòng điền vào trường này.` The user remained on the login page and did not reach an authenticated state.
- Status: Pass
- Evidence: [FR02-DT-003](./evidence/FR02-DT-003.png)
- Test Basis Reference: `requirement-analysis.md` - FR02-R02; `domain-testing.md` - LOGIN-EMAIL-PRESENCE-I01

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
- Actual Result: After submitting the login form with Email/Username `test@eshop.com` and the Password field empty, the browser displayed a required-field validation message on the empty Password field: `Vui lòng điền vào trường này.` The user remained on the login page and did not reach an authenticated state.
- Status: Pass
- Evidence: [FR02-DT-004](./evidence/FR02-DT-004.png)
- Test Basis Reference: `requirement-analysis.md` - FR02-R03; `domain-testing.md` - LOGIN-PASSWORD-PRESENCE-I01

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
- Actual Result: Submitted malformed Email 'not-an-email'. Input states: [{"type":"text","value":"not-an-email","validationMessage":""},{"type":"text","value":"Test1234!","validationMessage":""}]. Token present: false.
- Status: Fail
- Evidence: [FR02-DT-005](./evidence/FR02-DT-005.png)
- Test Basis Reference: `requirement-analysis.md` - FR02-R13, FR02-SF02; `domain-testing.md` - LOGIN-EMAIL-FORMAT-I01

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
- Actual Result: UI wrong password. Isolated account: fr02.fr02-dt-006.1782442149992@example.com. Token present: false. Visible text: EShop Giỏ hàng Đăng nhập Đăng ký Đăng Ký Username Mật khẩu Quên mật khẩu? Sign In Chưa có tài khoản? Đăng ký ngay Đăng nhập thất bại. Vui lòng kiểm tra lại. © 2026 EShop SUT. Dành cho mục đích kiểm thử..
- Status: Pass
- Evidence: [FR02-DT-006](./evidence/FR02-DT-006.png)
- Test Basis Reference: `requirement-analysis.md` - FR02-R05, FR02-R09; `domain-testing.md` - LOGIN-CREDENTIALS-I01

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
- Actual Result: UI attempt completed. URL: http://localhost:5173/login. Token present: false. Validation messages: ["",""]. Visible text: EShop Giỏ hàng Đăng nhập Đăng ký Đăng Ký Username Mật khẩu Quên mật khẩu? Sign In Chưa có tài khoản? Đăng ký ngay Đăng nhập thất bại. Vui lòng kiểm tra lại. © 2026 EShop SUT. Dành cho mục đích kiểm thử..
- Status: Pass
- Evidence: [FR02-DT-007](./evidence/FR02-DT-007.png)
- Test Basis Reference: `requirement-analysis.md` - FR02-R09; `domain-testing.md` - LOGIN-ACCOUNT-EXISTS-I01

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
- Actual Result: API login request was rejected or did not return a token. HTTP status: 401. Token present: false. Response: {"error":"Invalid email or password"}
- Status: Pass
- Evidence: [FR02-DT-008](./evidence/FR02-DT-008.png)
- Test Basis Reference: `requirement-analysis.md` - FR02-R02, FR02-API02; `domain-testing.md` - API-REQUEST-I01

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
- Actual Result: API login request was rejected or did not return a token. HTTP status: 401. Token present: false. Response: {"error":"Invalid email or password"}
- Status: Pass
- Evidence: [FR02-DT-009](./evidence/FR02-DT-009.png)
- Test Basis Reference: `requirement-analysis.md` - FR02-R03, FR02-API03; `domain-testing.md` - API-REQUEST-I02

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
- Actual Result: Wrong password API login. Isolated account: fr02.fr02-dt-010.1782442153381@example.com. HTTP status: 401. Token present: false. Response: {"error":"Invalid email or password"}
- Status: Pass
- Evidence: [FR02-DT-010](./evidence/FR02-DT-010.png)
- Test Basis Reference: `requirement-analysis.md` - FR02-R05, FR02-R09; `domain-testing.md` - LOGIN-CREDENTIALS-I01

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
- Actual Result: API login request was rejected or did not return a token. HTTP status: 401. Token present: false. Response: {"error":"Invalid email or password"}
- Status: Pass
- Evidence: [FR02-DT-011](./evidence/FR02-DT-011.png)
- Test Basis Reference: `requirement-analysis.md` - FR02-R09; `domain-testing.md` - LOGIN-ACCOUNT-EXISTS-I01

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
- Actual Result: Login form text inspected for required-field '\*' markers. Asterisk present: false. Visible text: EShop Giỏ hàng Đăng nhập Đăng ký Đăng Ký Username Mật khẩu Quên mật khẩu? Sign In Chưa có tài khoản? Đăng ký ngay © 2026 EShop SUT. Dành cho mục đích kiểm thử..
- Status: Fail
- Evidence: [FR02-DT-014](./evidence/FR02-DT-014.png)
- Test Basis Reference: `requirement-analysis.md` - FR02-SF01; `domain-testing.md` - FORM-REQUIRED-MARKER-V01/I01

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
- Actual Result: Email/first login input type observed as 'text'. Full input list: [{"type":"text","required":true,"value":""},{"type":"text","required":true,"value":""}].
- Status: Fail
- Evidence: [FR02-DT-015](./evidence/FR02-DT-015.png)
- Test Basis Reference: `requirement-analysis.md` - FR02-R13, FR02-SF02; `domain-testing.md` - FORM-EMAIL-TYPE-V01/I01

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
- Actual Result: Password/second login input type observed as 'text' with value visible to DOM as entered. Full input list: [{"type":"text","value":""},{"type":"text","value":"Test1234!"}].
- Status: Fail
- Evidence: [FR02-DT-016](./evidence/FR02-DT-016.png)
- Test Basis Reference: `requirement-analysis.md` - FR02-SF03; `domain-testing.md` - FORM-PASSWORD-TYPE-V01/I01

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
- Actual Result: After submitting a wrong-password login attempt, the login form displayed the error message `Đăng nhập thất bại. Vui lòng kiểm tra lại.` However, the error message appeared below the `Sign In` submit button instead of above it.
- Status: Fail
- Evidence: [FR02-DT-017](./evidence/FR02-DT-017.png)
- Test Basis Reference: `requirement-analysis.md` - FR02-SF04; `domain-testing.md` - FORM-ERROR-PLACEMENT-V01/I01

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
- Actual Result: Obtained login token: true. Sent GET /api/users/me with Authorization: Bearer <token>. Response status: 200.
- Status: Pass
- Evidence: [FR02-DT-018](./evidence/FR02-DT-018.png)
- Test Basis Reference: `requirement-analysis.md` - FR02-R12; `api_specification.md` - authenticated API note; `domain-testing.md` - AUTHORIZATION-HEADER-V01

## FR02-DT-020

- Test Case ID: FR02-DT-020
- Technique: Domain Testing
- Objective: Verify active API lockout rejects correct credentials.
- Requirement or Rule Reference: FR02-R07, FR02-R08
- Preconditions: Public API is available; account `test@eshop.com` is already locked through public failed login attempts.
- Test Data: `{"email":"test@eshop.com","password":"Test1234!"}`.
- Steps:
  1. During active lockout, send correct-password `POST /api/login`.
  2. Observe the HTTP status and response body.

- Expected Result: The correct login request is rejected during active lockout. Exact status and body are unspecified.
- Actual Result: During active lockout, a correct-password `POST /api/login` request was sent for `test@eshop.com` with body `{"email":"test@eshop.com","password":"Test1234!"}`. The API returned `403 Forbidden`, no token was returned, and the response body was `{"error":"Tài khoản đã bị khóa. Vui lòng thử lại sau."}`.
- Status: Pass
- Evidence: [FR02-DT-020](./evidence/FR02-DT-020.png)
- Test Basis Reference: `requirement-analysis.md` - FR02-R07/R08; `domain-testing.md` - LOGIN-LOCKOUT-ACTIVE-V01

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
- Actual Result: After the account was locked through public failed login attempts, the tester waited until the documented 30-second lockout duration had elapsed. A correct-password UI login attempt was then submitted. The login succeeded and the user reached the authenticated product list page. The navbar displayed `Chào, Test User` and the `Thoát` button, showing that the account was no longer rejected due to lockout.
- Status: Pass
- Evidence: [FR02-DT-021](./evidence/FR02-DT-021.png)
- Test Basis Reference: `requirement-analysis.md` - FR02-R07; `domain-testing.md` - LOGIN-LOCKOUT-EXPIRED-V01

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
- Actual Result: After the account was locked through public failed API attempts and the documented lockout duration had elapsed, a correct-password `POST /api/login` request was sent with body `{"email":"test@eshop.com","password":"Test1234!"}`. The API returned `200 OK`, the response body contained `message: Login successful`, a JWT `token`, and `user` information. Therefore, the request was no longer rejected due to lockout.
- Status: Pass
- Evidence: [FR02-DT-022](./evidence/FR02-DT-022.png)
- Test Basis Reference: `requirement-analysis.md` - FR02-R07; `domain-testing.md` - LOGIN-LOCKOUT-EXPIRED-V01

## Boundary Value Analysis Test Cases

## FR02-BVA-001

- Test Case ID: FR02-BVA-001
- Technique: Boundary Value Analysis
- Objective: Verify UI lockout classification at 2 consecutive failed attempts.
- Requirement or Rule Reference: FR02-R05, FR02-R06
- Preconditions: `/login` is available; account `test@eshop.com` starts unlocked with zero consecutive failed attempts.
- Test Data: Email `test@eshop.com`; wrong password `WrongPass123!`; correct password `Test1234!`; count = 2 failures.
- Steps:
  1. Submit two consecutive wrong-password UI login attempts.
  2. Immediately attempt UI login with correct password.
  3. Observe whether account is locked or rejected.
- Expected Result: The account has not reached the 3-attempt lockout threshold; correct login is not rejected solely due lockout.
- Actual Result: After two consecutive wrong-password UI login attempts for `test@eshop.com`, a correct-password login attempt using `Test1234!` was submitted immediately. The user did not reach an authenticated state, no token was observed, and the login page displayed the error message `Đăng nhập thất bại. Vui lòng kiểm tra lại.`
- Status: Fail
- Evidence: [FR02-BVA-001](./evidence/FR02-BVA-001.png)
- Test Basis Reference: `boundary-value-analysis.md` - FR02-FAILED-ATTEMPTS-B01

## FR02-BVA-002

- Test Case ID: FR02-BVA-002
- Technique: Boundary Value Analysis
- Objective: Verify UI lockout classification at 3 consecutive failed attempts.
- Requirement or Rule Reference: FR02-R05, FR02-R06
- Preconditions: `/login` is available; account `test@eshop.com` starts unlocked with zero consecutive failed attempts.
- Test Data: Email `test@eshop.com`; wrong password `WrongPass123!`; correct password `Test1234!`; count = 3 failures.
- Steps:
  1. Submit three consecutive wrong-password UI login attempts.
  2. Immediately attempt UI login with correct password.
  3. Observe whether account is locked.

- Expected Result: The account is locked at the third consecutive failed attempt; correct credentials are rejected during active lockout.
- Actual Result: After three consecutive wrong-password UI login attempts for `test@eshop.com`, a correct-password login attempt using `Test1234!` was submitted immediately. The user did not reach an authenticated state, no token was observed, and the login page displayed the error message `Đăng nhập thất bại. Vui lòng kiểm tra lại.`
- Status: Pass
- Evidence: [FR02-BVA-002](./evidence/FR02-BVA-002.png)
- Test Basis Reference: `boundary-value-analysis.md` - FR02-FAILED-ATTEMPTS-B02

## FR02-BVA-003

- Test Case ID: FR02-BVA-003
- Technique: Boundary Value Analysis
- Objective: Verify UI lockout classification at 4 consecutive failed attempts.
- Requirement or Rule Reference: FR02-R05, FR02-R06
- Preconditions: `/login` is available; account `test@eshop.com` starts unlocked with zero consecutive failed attempts.
- Test Data: Email `test@eshop.com`; wrong password `WrongPass123!`; correct password `Test1234!`; count = 4 failures.
- Steps:
  1. Submit four consecutive wrong-password UI login attempts.
  2. Immediately attempt UI login with correct password.
  3. Observe whether account is locked.

- Expected Result: Four consecutive failed attempts are inside the locked domain after the documented 3-attempt threshold; the correct-password login remains rejected due active lockout.
- Actual Result: After four consecutive wrong-password UI login attempts for `test@eshop.com`, a correct-password login attempt using `Test1234!` was submitted immediately. The user did not reach an authenticated state, no token was observed, and the login page displayed the error message `Đăng nhập thất bại. Vui lòng kiểm tra lại.`
- Status: Pass
- Evidence: [FR02-BVA-003](./evidence/FR02-BVA-003.png)
- Test Basis Reference: `boundary-value-analysis.md` - FR02-FAILED-ATTEMPTS-B03

## FR02-BVA-004

- Test Case ID: FR02-BVA-004
- Technique: Boundary Value Analysis
- Objective: Verify UI nominal below-threshold classification at 1 failed attempt.
- Requirement or Rule Reference: FR02-R05, FR02-R06
- Preconditions: `/login` is available; account `test@eshop.com` starts unlocked.
- Test Data: Email `test@eshop.com`; wrong password `WrongPass123!`; correct password `Test1234!`; count = 1 failure.
- Steps:
  1. Submit one wrong-password UI login attempt.
  2. Attempt UI login with correct password.
  3. Observe whether lockout blocks login.

- Expected Result: One failed attempt is below threshold; correct login is not rejected solely due lockout.
- Actual Result: After one wrong-password UI login attempt for `test@eshop.com`, a correct-password login attempt using `Test1234!` was submitted. The login succeeded, the user reached the authenticated product list page, and the navbar displayed `Chào, Test User` and the `Thoát` button.
- Status: Pass
- Evidence: [FR02-BVA-004](./evidence/FR02-BVA-004.png)
- Test Basis Reference: `boundary-value-analysis.md` - FR02-FAILED-ATTEMPTS-N01

## FR02-BVA-005

- Test Case ID: FR02-BVA-005
- Technique: Boundary Value Analysis
- Objective: Verify API lockout classification at 2 consecutive failed attempts.
- Requirement or Rule Reference: FR02-R05, FR02-R06
- Preconditions: Public API is available; account `test@eshop.com` starts unlocked with zero consecutive failed attempts.
- Test Data: Wrong body `{"email":"test@eshop.com","password":"WrongPass123!"}`; correct body `{"email":"test@eshop.com","password":"Test1234!"}`.
- Steps:
  1. Send two consecutive wrong-password `POST /api/login` requests.
  2. Send a correct-password `POST /api/login` request.
  3. Observe whether lockout blocks the correct request.

- Expected Result: Two failures do not reach the 3-attempt lockout threshold; the correct request is not rejected solely due lockout.
- Actual Result: After two consecutive wrong-password API login attempts for `test@eshop.com`, the observed wrong-password response statuses were `401` and `401`. A correct-password `POST /api/login` request was then sent immediately with body `{"email":"test@eshop.com","password":"Test1234!"}`. The API returned `403 Forbidden`, no token was returned, and the response body was `{"error":"Tài khoản đã bị khóa. Vui lòng thử lại sau."}`.
- Status: Fail
- Evidence: [FR02-BVA-005](./evidence/FR02-BVA-005.png)
- Test Basis Reference: `boundary-value-analysis.md` - FR02-FAILED-ATTEMPTS-B01

## FR02-BVA-006

- Test Case ID: FR02-BVA-006
- Technique: Boundary Value Analysis
- Objective: Verify API lockout classification at 3 consecutive failed attempts.
- Requirement or Rule Reference: FR02-R05, FR02-R06
- Preconditions: Public API is available; account `test@eshop.com` starts unlocked with zero consecutive failed attempts.
- Test Data: Wrong body `{"email":"test@eshop.com","password":"WrongPass123!"}`; correct body `{"email":"test@eshop.com","password":"Test1234!"}`.
- Steps:
  1. Send three consecutive wrong-password `POST /api/login` requests.
  2. Send a correct-password `POST /api/login` request.
  3. Observe whether lockout blocks the correct request.

- Expected Result: Three failures reach the 3-attempt lockout threshold; the correct request is rejected due to lockout.
- Actual Result: After three consecutive wrong-password API login attempts for `test@eshop.com`, the observed wrong-password response statuses were `401`, `401`, and `403`. A correct-password `POST /api/login` request was then sent immediately with body `{"email":"test@eshop.com","password":"Test1234!"}`. The API returned `403 Forbidden`, no token was returned, and the response body was `{"error":"Tài khoản đã bị khóa. Vui lòng thử lại sau."}`.
- Status: Pass
- Evidence: [FR02-BVA-006](./evidence/FR02-BVA-006.png)
- Test Basis Reference: `boundary-value-analysis.md` - FR02-FAILED-ATTEMPTS-B02

## FR02-BVA-007

- Test Case ID: FR02-BVA-007
- Technique: Boundary Value Analysis
- Objective: Verify API lockout classification at 4 consecutive failed attempts.
- Requirement or Rule Reference: FR02-R05, FR02-R06
- Preconditions: Public API is available; account `test@eshop.com` starts unlocked with zero consecutive failed attempts.
- Test Data: Wrong body `{"email":"test@eshop.com","password":"WrongPass123!"}`; correct body `{"email":"test@eshop.com","password":"Test1234!"}`.
- Steps:
  1. Send four consecutive wrong-password `POST /api/login` requests.
  2. Send a correct-password `POST /api/login` request.
  3. Observe whether lockout blocks the correct request.

- Expected Result: Four consecutive failed attempts are inside the locked domain after the documented 3-attempt threshold; the correct request is rejected due active lockout.
- Actual Result: After four consecutive wrong-password API login attempts for `test@eshop.com`, the observed wrong-password response statuses were `401`, `401`, `403`, and `403`. A correct-password `POST /api/login` request was then sent immediately with body `{"email":"test@eshop.com","password":"Test1234!"}`. The API returned `403 Forbidden`, no token was returned, and the response body was `{"error":"Tài khoản đã bị khóa. Vui lòng thử lại sau."}`.
- Status: Pass
- Evidence: [FR02-BVA-007](./evidence/FR02-BVA-007.png)
- Test Basis Reference: `boundary-value-analysis.md` - FR02-FAILED-ATTEMPTS-B03

## FR02-BVA-008

- Test Case ID: FR02-BVA-008
- Technique: Boundary Value Analysis
- Objective: Verify API nominal below-threshold classification at 1 failed attempt.
- Requirement or Rule Reference: FR02-R05, FR02-R06
- Preconditions: Public API is available; account `test@eshop.com` starts unlocked.
- Test Data: Wrong body `{"email":"test@eshop.com","password":"WrongPass123!"}`; correct body `{"email":"test@eshop.com","password":"Test1234!"}`.
- Steps:
  1. Send one wrong-password `POST /api/login` request.
  2. Send a correct-password `POST /api/login` request.
  3. Observe whether lockout blocks the correct request.

- Expected Result: One failure is below threshold; correct login is not rejected solely due lockout.
- Actual Result: After one wrong-password API login attempt for `test@eshop.com`, a correct-password `POST /api/login` request was sent immediately with body `{"email":"test@eshop.com","password":"Test1234!"}`. The API returned `200 OK`, the response body contained `message: Login successful`, a JWT `token`, and `user` information. Therefore, the correct request was not blocked by lockout after only one failed attempt.
- Status: Pass
- Evidence: [FR02-BVA-008](./evidence/FR02-BVA-008.png)
- Test Basis Reference: `boundary-value-analysis.md` - FR02-FAILED-ATTEMPTS-N01

## FR02-BVA-009

- Test Case ID: FR02-BVA-009
- Technique: Boundary Value Analysis
- Objective: Verify UI lockout remains active at 29 seconds after lockout.
- Requirement or Rule Reference: FR02-R07, FR02-R08
- Preconditions: `/login` is available; account `test@eshop.com` has been locked through public failed login attempts.
- Test Data: Correct credentials `test@eshop.com` / `Test1234!`; elapsed time = approximately 29 seconds.
- Steps:
  1. Lock the account through three consecutive failed attempts.
  2. Wait approximately 29 seconds from lockout.
  3. Attempt UI login with correct credentials.
  4. Observe whether lockout still blocks login.

- Expected Result: At 29 seconds, the account is still within the documented 30-second lockout and login is rejected due active lockout.
- Actual Result: After the account `test@eshop.com` was locked through three consecutive failed UI login attempts, the tester waited approximately 29 seconds. A correct-password login attempt using `Test1234!` was then submitted. The login was rejected, no token was observed, the user remained unauthenticated, and the login page displayed the error message `Đăng nhập thất bại. Vui lòng kiểm tra lại.`
- Status: Pass
- Evidence: [FR02-BVA-009](./evidence/FR02-BVA-009.png)
- Test Basis Reference: `boundary-value-analysis.md` - FR02-LOCKOUT-DURATION-B01

## FR02-BVA-010

- Test Case ID: FR02-BVA-010
- Technique: Boundary Value Analysis
- Objective: Verify UI lockout expiry at 30 seconds after lockout.
- Requirement or Rule Reference: FR02-R07
- Preconditions: `/login` is available; account `test@eshop.com` has been locked through public failed login attempts.
- Test Data: Correct credentials `test@eshop.com` / `Test1234!`; elapsed time = approximately 30 seconds.
- Steps:
  1. Lock the account through three consecutive failed attempts.
  2. Wait approximately 30 seconds from lockout.
  3. Attempt UI login with correct credentials.
  4. Observe whether lockout still blocks login.

- Expected Result: At the documented 30-second duration, the account is no longer rejected solely due lockout. Exact timing precision is unspecified.
- Actual Result: After the account `test@eshop.com` was locked through three consecutive failed UI login attempts, the tester waited approximately 30 seconds. A correct-password login attempt using `Test1234!` was then submitted. No token was observed, the user remained unauthenticated, and the login page displayed the error message `Đăng nhập thất bại. Vui lòng kiểm tra lại.`
- Status: Fail
- Evidence: [FR02-BVA-010](./evidence/FR02-BVA-010.png)
- Test Basis Reference: `boundary-value-analysis.md` - FR02-LOCKOUT-DURATION-B02

## FR02-BVA-011

- Test Case ID: FR02-BVA-011
- Technique: Boundary Value Analysis
- Objective: Verify UI lockout expiry after 31 seconds.
- Requirement or Rule Reference: FR02-R07
- Preconditions: `/login` is available; account `test@eshop.com` has been locked through public failed login attempts.
- Test Data: Correct credentials `test@eshop.com` / `Test1234!`; elapsed time = approximately 31 seconds.
- Steps:
  1. Lock the account through three consecutive failed attempts.
  2. Wait approximately 31 seconds from lockout.
  3. Attempt UI login with correct credentials.
  4. Observe whether lockout still blocks login.

- Expected Result: At 31 seconds, the account is beyond the documented duration and is not rejected solely due lockout.
- Actual Result: After the account `test@eshop.com` was locked through three consecutive failed UI login attempts, the tester waited approximately 31 seconds. A correct-password login attempt using `Test1234!` was then submitted. No token was observed, the user remained unauthenticated, and the login page displayed the error message `Đăng nhập thất bại. Vui lòng kiểm tra lại.`
- Status: Fail
- Evidence: [FR02-BVA-011](./evidence/FR02-BVA-011.png)
- Test Basis Reference: `boundary-value-analysis.md` - FR02-LOCKOUT-DURATION-B03

## FR02-BVA-012

- Test Case ID: FR02-BVA-012
- Technique: Boundary Value Analysis
- Objective: Verify UI nominal active-lockout state at 10 seconds.
- Requirement or Rule Reference: FR02-R07, FR02-R08
- Preconditions: `/login` is available; account `test@eshop.com` has been locked through public failed login attempts.
- Test Data: Correct credentials `test@eshop.com` / `Test1234!`; elapsed time = approximately 10 seconds.
- Steps:
  1. Lock the account through three consecutive failed attempts.
  2. Wait approximately 10 seconds.
  3. Attempt UI login with correct credentials.
  4. Observe whether lockout blocks login.

- Expected Result: At 10 seconds, the account remains inside the active lockout period and login is rejected due lockout.
- Actual Result: After the account `test@eshop.com` was locked through three consecutive failed UI login attempts, the tester waited approximately 10 seconds. A correct-password login attempt using `Test1234!` was then submitted. No token was observed, the user remained unauthenticated, and the login page displayed the error message `Đăng nhập thất bại. Vui lòng kiểm tra lại.`
- Status: Pass
- Evidence: [FR02-BVA-012](./evidence/FR02-BVA-012.png)
- Test Basis Reference: `boundary-value-analysis.md` - FR02-LOCKOUT-DURATION-N01

## Exploratory Backlog

| Candidate ID               | Input or Observation                              | Missing Oracle                                 | Clarification Required         | Reason Excluded from Normative Coverage   |
| -------------------------- | ------------------------------------------------- | ---------------------------------------------- | ------------------------------ | ----------------------------------------- |
| LOGIN-EMAIL-WHITESPACE-A01 | Email with leading/trailing spaces or spaces only | Whether trimming/whitespace counts as provided | Whitespace and trimming policy | FR-02 does not define it.                 |
| LOGIN-EMAIL-CASE-A01       | Case variant such as `TEST@ESHOP.COM`             | Whether Email matching is case-sensitive       | Email normalization policy     | FR-02 does not define it.                 |
| LOGIN-COUNTER-RESET-A01    | Failure count before/after a successful login     | Whether success resets failed-attempt count    | Failed-attempt reset rule      | FR-02 does not define it.                 |
| FORM-STEP-INDICATOR-A01    | Login step count and Step Indicator               | Whether Login is multi-step                    | Authoritative login step model | FR-02 does not state login is multi-step. |

## Preliminary Coverage Summary

| Rule ID              | Partition or Boundary ID                                                            | Technique            | Covering Test Case ID               | Surface | Coverage Status                                                   | Notes                                                                                                                         |
| -------------------- | ----------------------------------------------------------------------------------- | -------------------- | ----------------------------------- | ------- | ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| FR02-R01, R02        | LOGIN-EMAIL-PRESENCE-V01/I01                                                        | Domain Testing       | FR02-DT-001, 002, 003, 008          | UI/API  | Covered                                                           | Provided and missing Email covered on both surfaces.                                                                          |
| FR02-R01, R03        | LOGIN-PASSWORD-PRESENCE-V01/I01                                                     | Domain Testing       | FR02-DT-001, 002, 004, 009          | UI/API  | Covered                                                           | Provided and missing Password covered on both surfaces.                                                                       |
| FR02-R13, SF02       | LOGIN-EMAIL-FORMAT-V01/I01; FORM-EMAIL-TYPE-V01/I01                                 | Domain Testing       | FR02-DT-005, 015                    | UI      | Covered                                                           | API email-format rejection excluded because no API oracle is specified.                                                       |
| FR02-R04, R10, API04 | LOGIN-CREDENTIALS-V01; API-SUCCESS-V01; UI-SUCCESS-V01                              | Domain Testing       | FR02-DT-001, 002                    | UI/API  | Covered                                                           | Successful login covered on both surfaces.                                                                                    |
| FR02-R05, R09        | LOGIN-CREDENTIALS-I01; LOGIN-ERROR-NONLEAKY-V01                                     | Domain Testing       | FR02-DT-006, 010                    | UI/API  | Covered                                                           | Wrong password covered on both surfaces.                                                                                      |
| FR02-R09             | LOGIN-ACCOUNT-EXISTS-I01; LOGIN-ERROR-NONLEAKY-V01                                  | Domain Testing       | FR02-DT-007, 011                    | UI/API  | Covered                                                           | Non-existing account covered without exact message oracle.                                                                    |
| FR02-R05, R06, R08   | LOGIN-LOCKOUT-THRESHOLD-V01; LOGIN-LOCKOUT-ACTIVE-V01                               | BVA / Domain Testing | FR02-BVA-002, 006, 012; FR02-DT-020 | UI/API  | Covered                                                           | Duplicate DT threshold/active-lockout cases were merged into BVA where the exact boundary or active-lockout timing is tested. |
| FR02-R07             | LOGIN-LOCKOUT-EXPIRED-V01                                                           | Domain Testing / BVA | FR02-DT-021, 022; FR02-BVA-010, 011 | UI/API  | Covered                                                           | Expired-lockout state covered; exact 30s and 31s UI boundary observations are retained as BVA evidence.                       |
| FR02-SF01            | FORM-REQUIRED-MARKER-V01/I01                                                        | Domain Testing       | FR02-DT-014                         | UI      | Covered                                                           | Required marker conformance case.                                                                                             |
| FR02-SF03            | FORM-PASSWORD-TYPE-V01/I01                                                          | Domain Testing       | FR02-DT-016                         | UI      | Covered                                                           | Password masking conformance case.                                                                                            |
| FR02-SF04            | FORM-ERROR-PLACEMENT-V01/I01                                                        | Domain Testing       | FR02-DT-017                         | UI      | Covered                                                           | Error placement conformance case.                                                                                             |
| FR02-R11             | TOKEN-STORAGE-V01                                                                   | Domain Testing       | FR02-DT-001                         | UI      | Covered                                                           | Storage key unspecified.                                                                                                      |
| FR02-R12             | AUTHORIZATION-HEADER-V01                                                            | Domain Testing       | FR02-DT-018                         | UI/API  | Covered                                                           | Uses documented authenticated request header.                                                                                 |
| FR02-R05, R06        | FR02-FAILED-ATTEMPTS-B01/B02/B03/N01                                                | BVA                  | FR02-BVA-001 through FR02-BVA-008   | UI/API  | Covered                                                           | Attempt-count boundary values covered on both surfaces.                                                                       |
| FR02-R07             | FR02-LOCKOUT-DURATION-B01/B02/B03/N01                                               | BVA                  | FR02-BVA-009 through FR02-BVA-012   | UI      | Covered for UI; API duration BVA not included in this merged file | UI duration values covered. API active/expired lockout behaviour remains covered by FR02-DT-020 and FR02-DT-022.              |
| FR02 ambiguities     | LOGIN-EMAIL-WHITESPACE-A01; LOGIN-EMAIL-CASE-A01; LOGIN-COUNTER-RESET-A01; STEP-A01 | Exploratory          | None                                | UI/API  | Exploratory - No Oracle                                           | Listed in backlog; excluded from normative coverage.                                                                          |

## Design Gaps and Assumptions

- Controlled account state must be prepared through public setup or documented accounts without inspecting database records.
- BVA sequences can change account lockout state; execution must isolate or reset state through public means.
- Exact invalid API statuses, response bodies, UI messages, token claims, token storage key, and redirect target are unspecified.
- Timing BVA depends on whole-second observation; exact millisecond behaviour is not asserted.
- No normative tests cover whitespace handling, Email case normalization, counter reset on success, or step indicator because no oracle exists.
- Execution results and evidence are recorded only for the included reviewed cases. Bug reporting and GitHub Issue links are handled separately in the bug report phase.

## Human Review - Phase 5

- Reviewer: Nguyen Thanh Tien
- Review Date and Time: 2026-06-26 11:15
- Review Scope: FR-02 Test-Case Design after duplicate merge
- Corrections Made:
  - Merged duplicate DT lockout cases into existing BVA cases where the same UI/API threshold or active-lockout timing was already covered.
  - Corrected the BVA 4-attempt expected result so it is treated as `threshold + 1` inside the locked domain, not as a separate 4-attempt threshold.
  - Corrected duplicated or wrong evidence references for BVA cases.
  - Updated the coverage summary to match the retained test cases.
- Missing Cases Added: None
- Test Cases Before Review: 22 DT and 12 BVA
- Test Cases After Review: 19 DT and 12 BVA
- Duplicate Cases Removed: FR02-DT-012 merged into FR02-BVA-002; FR02-DT-013 merged into FR02-BVA-006; FR02-DT-019 merged into FR02-BVA-012
- Incorrect Cases Removed: None
- Status: Completed
- Approved for Validation: Yes
- Approved for Test-Case Quality Review: Yes
- Approved for Test Execution: Yes
