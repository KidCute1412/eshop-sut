# Test Cases - FR-01 Account Registration

## Domain Testing Test Cases

## FR01-DT-001

- Test Case ID: FR01-DT-001
- Feature ID: FR-01
- Test Case Title: Complete valid UI registration
- Technique: Domain Testing
- Objective: Verify the nominal valid UI registration domain and documented Login redirect.
- Requirement or Rule Reference: FR01-R01 through FR01-R14
- Test Basis Reference: `requirement-analysis.md` - FR01-R01 through FR01-R14; `domain-testing.md` - named valid partitions listed below
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: Name `Nguyen Van A`; controlled unused email `new.user@example.com`; password `ValidPass1!`; UI confirmation `ValidPass1!`; guest/unauthenticated state.
- Steps:
  1. Open `/register` as a guest.
  2. Enter Full name `Nguyen Van A`, controlled unused email `new.user@example.com`, Password and Confirm Password `ValidPass1!`.
  3. Activate the registration submit control.
  4. Observe whether registration completes, any displayed validation error, and navigation.
- Expected Result: Registration completes successfully and the UI navigates to the Login page. No exact success text, URL, or timing is asserted.
- Actual Result: The registration page loaded, but no Confirm Password label or input control was present. Execution stopped before form submission.
- Status: Blocked
- Blocking Reason: Step 2 requires a Confirm Password control, but the public registration UI does not provide one.
- Evidence: [FR01-DT-001.png](./evidence/FR01-DT-001.png)

## FR01-DT-002

- Test Case ID: FR01-DT-002
- Feature ID: FR-01
- Test Case Title: Complete valid API registration
- Technique: Domain Testing
- Objective: Verify the documented complete API request and successful response contract.
- Requirement or Rule Reference: FR01-API01 through FR01-API05; FR01-R01 through FR01-R10
- Test Basis Reference: `requirement-analysis.md` - FR01-API01 through FR01-API05; `domain-testing.md` - API-REQUEST-V01, API-SUCCESS-V01
- Preconditions: Public API is available at `http://localhost:3000`; actor is unauthenticated; specified email state is controlled.
- Test Data: `{"name":"Nguyen Van A","email":"new.api.user@example.com","password":"ValidPass1!"}` with email controlled unused
- Steps:
  1. Prepare a JSON request body: `{"name":"Nguyen Van A","email":"new.api.user@example.com","password":"ValidPass1!"}`.
  2. Send `POST http://localhost:3000/api/register`.
  3. Observe the public HTTP status and JSON response.
- Expected Result: The response is `200 OK` JSON containing message `User registered successfully` and an `id` value; the literal ID is not fixed.
- Actual Result: The API returned `200 OK` with the documented success message and id 3.
- Status: Pass
- Evidence: [FR01-DT-002.png](./evidence/FR01-DT-002.png)

## FR01-DT-003

- Test Case ID: FR01-DT-003
- Feature ID: FR-01
- Test Case Title: Missing full name in UI
- Technique: Domain Testing
- Objective: Verify rejection for missing full name in ui while unrelated inputs remain nominal.
- Requirement or Rule Reference: FR01-R01
- Test Basis Reference: `requirement-analysis.md` - FR01-R01; `domain-testing.md` - NAME-PRESENCE-I01
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: Full name empty; Email `fr01.dt003@example.com` controlled unused; Password and Confirm Password `ValidPass1!`.
- Steps:
  1. Open `/register` as a guest.
  2. Leave Full name empty.
  3. Enter Email `fr01.dt003@example.com` and `ValidPass1!` in Password and Confirm Password.
  4. Submit the form and observe completion, errors, and navigation.
- Expected Result: Registration is rejected and does not complete. If an error is displayed, it appears above the submit control; exact text is unspecified.
- Actual Result: The registration page loaded, but no Confirm Password label or input control was present. Execution stopped before form submission.
- Status: Blocked
- Blocking Reason: The test requires a valid Confirm Password value to isolate the missing-name partition, but the UI does not provide this control.
- Evidence: [FR01-DT-003.png](./evidence/FR01-DT-003.png)

## FR01-DT-004

- Test Case ID: FR01-DT-004
- Feature ID: FR-01
- Test Case Title: Missing email in UI
- Technique: Domain Testing
- Objective: Verify rejection for missing email in ui while unrelated inputs remain nominal.
- Requirement or Rule Reference: FR01-R02
- Test Basis Reference: `requirement-analysis.md` - FR01-R02; `domain-testing.md` - EMAIL-PRESENCE-I01
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: Name `Nguyen Van A`; Email empty; Password and Confirm Password `ValidPass1!`.
- Steps:
  1. Open `/register` as a guest.
  2. Enter Name `Nguyen Van A` and leave Email empty.
  3. Enter `ValidPass1!` in Password and Confirm Password.
  4. Submit the form and observe completion, errors, and navigation.
- Expected Result: Registration is rejected and does not complete. If an error is displayed, it appears above the submit control; exact text is unspecified.
- Actual Result: The registration page loaded, but no Confirm Password label or input control was present. Execution stopped before form submission.
- Status: Blocked
- Blocking Reason: The test requires a valid Confirm Password value to isolate the missing-email partition, but the UI does not provide this control.
- Evidence: [FR01-DT-004.png](./evidence/FR01-DT-004.png)

## FR01-DT-005

- Test Case ID: FR01-DT-005
- Feature ID: FR-01
- Test Case Title: Invalid email format in UI
- Technique: Domain Testing
- Objective: Verify rejection for invalid email format in ui while unrelated inputs remain nominal.
- Requirement or Rule Reference: FR01-R04
- Test Basis Reference: `requirement-analysis.md` - FR01-R04; `domain-testing.md` - EMAIL-FORMAT-I01
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: Name `Nguyen Van A`; Email `not-an-email`; Password and Confirm Password `ValidPass1!`.
- Steps:
  1. Open `/register` as a guest.
  2. Enter Name `Nguyen Van A` and Email `not-an-email`.
  3. Enter `ValidPass1!` in Password and Confirm Password.
  4. Submit the form and observe completion, errors, and navigation.
- Expected Result: Registration is rejected and does not complete. If an error is displayed, it appears above the submit control; exact text is unspecified.
- Actual Result: The registration page loaded, but no Confirm Password label or input control was present. Execution stopped before form submission.
- Status: Blocked
- Blocking Reason: The test requires a valid Confirm Password value to isolate the invalid-email partition, but the UI does not provide this control.
- Evidence: [FR01-DT-005.png](./evidence/FR01-DT-005.png)

## FR01-DT-006

- Test Case ID: FR01-DT-006
- Feature ID: FR-01
- Test Case Title: Duplicate email in UI
- Technique: Domain Testing
- Objective: Verify rejection for duplicate email in ui while unrelated inputs remain nominal.
- Requirement or Rule Reference: FR01-R05
- Test Basis Reference: `requirement-analysis.md` - FR01-R05; `domain-testing.md` - EMAIL-UNIQUENESS-I01
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: Name `Nguyen Van A`; Email `registered@example.com` controlled existing; Password and Confirm Password `ValidPass1!`.
- Steps:
  1. Open `/register` as a guest.
  2. Enter Name `Nguyen Van A` and controlled existing Email `registered@example.com`.
  3. Enter `ValidPass1!` in Password and Confirm Password.
  4. Submit the form and observe completion, errors, and navigation.
- Expected Result: Registration is rejected and does not complete. If an error is displayed, it appears above the submit control; exact text is unspecified.
- Actual Result: The registration page loaded, but no Confirm Password label or input control was present. Execution stopped before form submission.
- Status: Blocked
- Blocking Reason: The test requires a valid Confirm Password value to isolate the duplicate-email partition, but the UI does not provide this control.
- Evidence: [FR01-DT-006.png](./evidence/FR01-DT-006.png)

## FR01-DT-007

- Test Case ID: FR01-DT-007
- Feature ID: FR-01
- Test Case Title: Missing password in UI
- Technique: Domain Testing
- Objective: Verify rejection for missing password in ui while unrelated inputs remain nominal.
- Requirement or Rule Reference: FR01-R03
- Test Basis Reference: `requirement-analysis.md` - FR01-R03, FR01-R11; `domain-testing.md` - PASSWORD-PRESENCE-I01, CONFIRM-VALUE-I01
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: Name `Nguyen Van A`; Email `fr01.dt007@example.com` controlled unused; Password empty; Confirm Password empty.
- Steps:
  1. Open `/register` as a guest.
  2. Enter Name `Nguyen Van A` and Email `fr01.dt007@example.com`.
  3. Leave Password and Confirm Password empty.
  4. Submit the form and observe completion, errors, and navigation.
- Expected Result: Registration is rejected and does not complete. If an error is displayed, it appears above the submit control; exact text is unspecified.
- Actual Result: Execution could not continue because The approved steps require a Confirm Password control, but the public registration UI exposes no Confirm Password label or control.
- Status: Blocked
- Blocking Reason: The approved steps require a Confirm Password control, but the public registration UI exposes no Confirm Password label or control.
- Evidence: [FR01-DT-007.png](./evidence/FR01-DT-007.png)

## FR01-DT-008

- Test Case ID: FR01-DT-008
- Feature ID: FR-01
- Test Case Title: Password without uppercase in UI
- Technique: Domain Testing
- Objective: Verify rejection for password without uppercase in ui while unrelated inputs remain nominal.
- Requirement or Rule Reference: FR01-R07
- Test Basis Reference: `requirement-analysis.md` - FR01-R07; `domain-testing.md` - PASSWORD-UPPERCASE-I01
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: Name `Nguyen Van A`; Email `fr01.dt008@example.com` controlled unused; Password and Confirm Password `validpass1!`.
- Steps:
  1. Open `/register` as a guest.
  2. Enter Name `Nguyen Van A` and Email `fr01.dt008@example.com`.
  3. Enter `validpass1!` in Password and Confirm Password.
  4. Submit the form and observe completion, errors, and navigation.
- Expected Result: Registration is rejected and does not complete. If an error is displayed, it appears above the submit control; exact text is unspecified.
- Actual Result: Execution could not continue because The approved steps require a Confirm Password control, but the public registration UI exposes no Confirm Password label or control.
- Status: Blocked
- Blocking Reason: The approved steps require a Confirm Password control, but the public registration UI exposes no Confirm Password label or control.
- Evidence: [FR01-DT-008.png](./evidence/FR01-DT-008.png)

## FR01-DT-009

- Test Case ID: FR01-DT-009
- Feature ID: FR-01
- Test Case Title: Password without lowercase in UI
- Technique: Domain Testing
- Objective: Verify rejection for password without lowercase in ui while unrelated inputs remain nominal.
- Requirement or Rule Reference: FR01-R08
- Test Basis Reference: `requirement-analysis.md` - FR01-R08; `domain-testing.md` - PASSWORD-LOWERCASE-I01
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: Name `Nguyen Van A`; Email `fr01.dt009@example.com` controlled unused; Password and Confirm Password `VALIDPASS1!`.
- Steps:
  1. Open `/register` as a guest.
  2. Enter Name `Nguyen Van A` and Email `fr01.dt009@example.com`.
  3. Enter `VALIDPASS1!` in Password and Confirm Password.
  4. Submit the form and observe completion, errors, and navigation.
- Expected Result: Registration is rejected and does not complete. If an error is displayed, it appears above the submit control; exact text is unspecified.
- Actual Result: The registration page loaded, but no Confirm Password label or input control was present. Execution stopped before form submission.
- Status: Blocked
- Blocking Reason: The test requires a matching Confirm Password value to isolate the missing-lowercase partition, but the UI does not provide this control.
- Evidence: [FR01-DT-009.png](./evidence/FR01-DT-009.png)

## FR01-DT-010

- Test Case ID: FR01-DT-010
- Feature ID: FR-01
- Test Case Title: Password without digit in UI
- Technique: Domain Testing
- Objective: Verify rejection for password without digit in ui while unrelated inputs remain nominal.
- Requirement or Rule Reference: FR01-R09
- Test Basis Reference: `requirement-analysis.md` - FR01-R09; `domain-testing.md` - PASSWORD-DIGIT-I01
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: Name `Nguyen Van A`; Email `fr01.dt010@example.com` controlled unused; Password and Confirm Password `ValidPass!`.
- Steps:
  1. Open `/register` as a guest.
  2. Enter Name `Nguyen Van A` and Email `fr01.dt010@example.com`.
  3. Enter `ValidPass!` in Password and Confirm Password.
  4. Submit the form and observe completion, errors, and navigation.
- Expected Result: Registration is rejected and does not complete. If an error is displayed, it appears above the submit control; exact text is unspecified.
- Actual Result: The registration page loaded, but no Confirm Password label or input control was present. Execution stopped before form submission.
- Status: Blocked
- Blocking Reason: The test requires a matching Confirm Password value to isolate the missing-digit partition, but the UI does not provide this control.
- Evidence: [FR01-DT-010.png](./evidence/FR01-DT-010.png)

## FR01-DT-011

- Test Case ID: FR01-DT-011
- Feature ID: FR-01
- Test Case Title: Password without documented special character in UI
- Technique: Domain Testing
- Objective: Verify rejection for password without documented special character in ui while unrelated inputs remain nominal.
- Requirement or Rule Reference: FR01-R10
- Test Basis Reference: `requirement-analysis.md` - FR01-R10; `domain-testing.md` - PASSWORD-SPECIAL-I01
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: Name `Nguyen Van A`; Email `fr01.dt011@example.com` controlled unused; Password and Confirm Password `ValidPass12`.
- Steps:
  1. Open `/register` as a guest.
  2. Enter Name `Nguyen Van A` and Email `fr01.dt011@example.com`.
  3. Enter `ValidPass12` in Password and Confirm Password.
  4. Submit the form and observe completion, errors, and navigation.
- Expected Result: Registration is rejected and does not complete. If an error is displayed, it appears above the submit control; exact text is unspecified.
- Actual Result: The registration page loaded, but no Confirm Password label or input control was present. Execution stopped before form submission.
- Status: Blocked
- Blocking Reason: The test requires a matching Confirm Password value to isolate the missing-special-character partition, but the UI does not provide this control.
- Evidence: [FR01-DT-011.png](./evidence/FR01-DT-011.png)

## FR01-DT-012

- Test Case ID: FR01-DT-012
- Feature ID: FR-01
- Test Case Title: Confirm Password control conformance
- Technique: Domain Testing
- Objective: Observe that the registration UI supplies the required Confirm Password control.
- Requirement or Rule Reference: FR01-R11
- Test Basis Reference: `requirement-analysis.md` - FR01-R11; `domain-testing.md` - CONFIRM-CONTROL-V01, CONFIRM-CONTROL-I01
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: a visible Confirm Password input control
- Steps:
  1. Open `/register` as a guest.
  2. Inspect the relevant public form control or label.
- Expected Result: The registration form visibly contains a Confirm Password input control. Absence is the observation that would indicate non-conformance.
- Actual Result: No Confirm Password label or control was visible.
- Status: Fail
- Evidence: [FR01-DT-012.png](./evidence/FR01-DT-012.png);

## FR01-DT-013

- Test Case ID: FR01-DT-013
- Feature ID: FR-01
- Test Case Title: Empty Confirm Password value
- Technique: Domain Testing
- Objective: Verify rejection for empty confirm password value while unrelated inputs remain nominal.
- Requirement or Rule Reference: FR01-R11
- Test Basis Reference: `requirement-analysis.md` - FR01-R11; `domain-testing.md` - CONFIRM-VALUE-I01
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: Name `Nguyen Van A`; Email `fr01.dt013@example.com` controlled unused; Password `ValidPass1!`; Confirm Password empty.
- Steps:
  1. Open `/register` as a guest.
  2. Enter Name `Nguyen Van A`, Email `fr01.dt013@example.com`, and Password `ValidPass1!`.
  3. Leave Confirm Password empty.
  4. Submit the form and observe completion, errors, and navigation.
- Expected Result: Registration is rejected and does not complete. If an error is displayed, it appears above the submit control; exact text is unspecified.
- Actual Result: The registration page loaded, but no Confirm Password label or input control was present. Execution stopped before form submission.
- Status: Blocked
- Blocking Reason: The test requires a Confirm Password control whose value can be left empty, but the UI does not provide this control.
- Evidence: [FR01-DT-013.png](./evidence/FR01-DT-013.png)

## FR01-DT-014

- Test Case ID: FR01-DT-014
- Feature ID: FR-01
- Test Case Title: Mismatching password confirmation
- Technique: Domain Testing
- Objective: Verify rejection for mismatching password confirmation while unrelated inputs remain nominal.
- Requirement or Rule Reference: FR01-R12
- Test Basis Reference: `requirement-analysis.md` - FR01-R12; `domain-testing.md` - CONFIRM-MATCH-I01
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: Name `Nguyen Van A`; Email `fr01.dt014@example.com` controlled unused; Password `ValidPass1!`; Confirm Password `ValidPass2!`.
- Steps:
  1. Open `/register` as a guest.
  2. Enter Name `Nguyen Van A` and Email `fr01.dt014@example.com`.
  3. Enter Password `ValidPass1!` and Confirm Password `ValidPass2!`.
  4. Submit the form and observe completion, errors, and navigation.
- Expected Result: Registration is rejected and does not complete. If an error is displayed, it appears above the submit control; exact text is unspecified.
- Actual Result: The registration page loaded, but no Confirm Password label or input control was present. Execution stopped before form submission.
- Status: Blocked
- Blocking Reason: The test requires a Confirm Password control to create the documented password-mismatch condition, but the UI does not provide this control.
- Evidence: [FR01-DT-014.png](./evidence/FR01-DT-014.png)

## FR01-DT-015

- Test Case ID: FR01-DT-015
- Feature ID: FR-01
- Test Case Title: Required-field marker conformance
- Technique: Domain Testing
- Objective: Verify required registration labels show adjacent `*` markers.
- Requirement or Rule Reference: FR01-SF01
- Test Basis Reference: `requirement-analysis.md` - FR01-SF01; `domain-testing.md` - FORM-REQUIRED-MARKER-V01, FORM-REQUIRED-MARKER-I01
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: Full name, Email, and Password labels with adjacent `*`
- Steps:
  1. Open `/register` as a guest.
  2. Inspect the relevant public form control or label.
- Expected Result: Every unequivocally required label displays adjacent `*`; a missing marker is the non-conforming observation.
- Actual Result: Required labels displayed no adjacent `*` markers.
- Status: Fail
- Evidence: [FR01-DT-015.png](./evidence/FR01-DT-015.png)

## FR01-DT-016

- Test Case ID: FR01-DT-016
- Feature ID: FR-01
- Test Case Title: Email control type conformance
- Technique: Domain Testing
- Objective: Verify the Email control exposes `type="email"`.
- Requirement or Rule Reference: FR01-SF02
- Test Basis Reference: `requirement-analysis.md` - FR01-SF02; `domain-testing.md` - FORM-EMAIL-TYPE-V01, FORM-EMAIL-TYPE-I01
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: observable Email control type
- Steps:
  1. Open `/register` as a guest.
  2. Inspect the relevant public form control or label.
- Expected Result: The Email control exposes `type="email"`; another type is the non-conforming observation.
- Actual Result: Email input again exposed `type="text"`; pilot failure reproduced.
- Status: Fail
- Evidence: [FR01-DT-016.png](./evidence/FR01-DT-016.png)

## FR01-DT-017

- Test Case ID: FR01-DT-017
- Feature ID: FR-01
- Test Case Title: Password masking conformance
- Technique: Domain Testing
- Objective: Verify Password uses a password control and masks entered text.
- Requirement or Rule Reference: FR01-SF03
- Test Basis Reference: `requirement-analysis.md` - FR01-SF03; `domain-testing.md` - FORM-PASSWORD-TYPE-V01, FORM-PASSWORD-TYPE-I01
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: Password value `ValidPass1!`
- Steps:
  1. Open `/register` as a guest.
  2. Inspect the relevant public form control or label.
  3. Enter `ValidPass1!` in Password and observe its display.
- Expected Result: The Password control exposes `type="password"` and entered characters are not shown in clear text.
- Actual Result: Password input exposed `type="password"` and masked the entered value.
- Status: Pass
- Evidence: [FR01-DT-017.png](./evidence/FR01-DT-017.png)

## FR01-DT-018

- Test Case ID: FR01-DT-018
- Feature ID: FR-01
- Test Case Title: Error placement conformance
- Technique: Domain Testing
- Objective: Verify a displayed registration error is above the submit control.
- Requirement or Rule Reference: FR01-SF04
- Test Basis Reference: `requirement-analysis.md` - FR01-SF04; `domain-testing.md` - FORM-ERROR-PLACEMENT-V01, FORM-ERROR-PLACEMENT-I01
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: Name `Nguyen Van A`; Email `not-an-email`; Password and Confirm Password `ValidPass1!`.
- Steps:
  1. Open `/register` as a guest.
  2. Enter Name `Nguyen Van A`, Email `not-an-email`, and `ValidPass1!` in Password and Confirm Password.
  3. Submit the form.
  4. Observe the location of any displayed registration error relative to the submit control.
- Expected Result: A validation error is displayed above, not below, the submit control; exact text is unspecified.
- Actual Result: The registration page loaded, but no Confirm Password label or input control was present. Execution stopped before form submission.
- Status: Blocked
- Blocking Reason: The test requires a valid matching Confirm Password value so error placement can be isolated, but the UI does not provide this control.
- Evidence: [FR01-DT-018.png](./evidence/FR01-DT-018.png)

## FR01-DT-019

- Test Case ID: FR01-DT-019
- Feature ID: FR-01
- Test Case Title: API request missing name
- Technique: Domain Testing
- Objective: Verify rejection when the documented required API property `name` is absent.
- Requirement or Rule Reference: FR01-R01; FR01-API02
- Test Basis Reference: requirement-analysis.md required field and API property; domain-testing.md API-REQUEST-I01; NAME-PRESENCE-I01
- Preconditions: Public API is available at `http://localhost:3000`; actor is unauthenticated; specified email state is controlled.
- Test Data: `{"email":"new.missing.name@example.com","password":"ValidPass1!"}`
- Steps:
  1. Prepare a JSON request body: `{"email":"new.missing.name@example.com","password":"ValidPass1!"}`.
  2. Send `POST http://localhost:3000/api/register`.
  3. Observe the public HTTP status and JSON response.
- Expected Result: The response does not satisfy the documented successful-registration contract of HTTP 200 with the success message and an `id`. Exact invalid status and response body are unspecified.
- Actual Result: The API returned `200 OK` with the documented success message and id 4, contradicting the rejection oracle. The pilot failure reproduced.
- Status: Fail
- Evidence: [FR01-DT-019](./evidence/FR01-DT-019.png)

## FR01-DT-020

- Test Case ID: FR01-DT-020
- Feature ID: FR-01
- Test Case Title: API request missing email
- Technique: Domain Testing
- Objective: Verify rejection when the documented required API property `email` is absent.
- Requirement or Rule Reference: FR01-R02; FR01-API03
- Test Basis Reference: requirement-analysis.md required field and API property; domain-testing.md API-REQUEST-I02; EMAIL-PRESENCE-I01
- Preconditions: Public API is available at `http://localhost:3000`; actor is unauthenticated; specified email state is controlled.
- Test Data: `{"name":"Nguyen Van A","password":"ValidPass1!"}`
- Steps:
  1. Prepare a JSON request body: `{"name":"Nguyen Van A","password":"ValidPass1!"}`.
  2. Send `POST http://localhost:3000/api/register`.
  3. Observe the public HTTP status and JSON response.
- Expected Result: The response does not satisfy the documented successful-registration contract of HTTP 200 with the success message and an `id`. Exact invalid status and response body are unspecified.
- Actual Result: The API returned `200 OK` with the documented success message and id 5, contradicting the rejection oracle.
- Status: Fail
- Evidence: [FR01-DT-020](./evidence/FR01-DT-020.png)

## FR01-DT-021

- Test Case ID: FR01-DT-021
- Feature ID: FR-01
- Test Case Title: API request missing password
- Technique: Domain Testing
- Objective: Verify rejection when the documented required API property `password` is absent.
- Requirement or Rule Reference: FR01-R03; FR01-API04
- Test Basis Reference: requirement-analysis.md required field and API property; domain-testing.md API-REQUEST-I03; PASSWORD-PRESENCE-I01
- Preconditions: Public API is available at `http://localhost:3000`; actor is unauthenticated; specified email state is controlled.
- Test Data: `{"name":"Nguyen Van A","email":"new.missing.password@example.com"}`
- Steps:
  1. Prepare a JSON request body: `{"name":"Nguyen Van A","email":"new.missing.password@example.com"}`.
  2. Send `POST http://localhost:3000/api/register`.
  3. Observe the public HTTP status and JSON response.
- Expected Result: The response does not satisfy the documented successful-registration contract of HTTP 200 with the success message and an `id`. Exact invalid status and response body are unspecified.
- Actual Result: The API returned `200 OK` with the documented success message and id 6, contradicting the rejection oracle.
- Status: Fail
- Evidence: [FR01-DT-021](./evidence/FR01-DT-021.png)

## FR01-DT-022

- Test Case ID: FR01-DT-022
- Feature ID: FR-01
- Test Case Title: Password length invalid partition in UI
- Technique: Domain Testing
- Objective: Verify the UI rejects a password clearly inside the fewer-than-8 partition, without using an adjacent boundary value.
- Requirement or Rule Reference: FR01-R06 through FR01-R10
- Test Basis Reference: `requirement-analysis.md` - FR01-R06 through FR01-R10; `domain-testing.md` - PASSWORD-LENGTH-I01
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; the specified email is controlled unused; Confirm Password control is available.
- Test Data: Name `Nguyen Van A`; Email `fr01.dt022@example.com`; Password and Confirm Password `Ab1!` (4 characters).
- Steps:
  1. Open `/register` as a guest.
  2. Enter Name `Nguyen Van A` and Email `fr01.dt022@example.com`.
  3. Enter `Ab1!` in Password and Confirm Password.
  4. Submit the form and observe completion, errors, and navigation.
- Expected Result: Registration is rejected, does not complete, and does not navigate to Login. If a form error is displayed, it appears above the submit control; exact text is unspecified.
- Actual Result: The registration page loaded, but no Confirm Password label or input control was present. Execution stopped before form submission.
- Status: Blocked
- Blocking Reason: The test requires a matching Confirm Password value to isolate the invalid password-length partition, but the UI does not provide this control.
- Evidence: [FR01-DT-022](./evidence/FR01-DT-022.png)

## FR01-DT-023

- Test Case ID: FR01-DT-023
- Feature ID: FR-01
- Test Case Title: Invalid email format in API
- Technique: Domain Testing
- Objective: Verify API rejection for a plainly malformed email while other properties remain valid.
- Requirement or Rule Reference: FR01-R04
- Test Basis Reference: `requirement-analysis.md` - FR01-R04; `domain-testing.md` - EMAIL-FORMAT-I01
- Preconditions: Public API is available at `http://localhost:3000`; actor is unauthenticated; the specified email state is controlled.
- Test Data: `{"name":"Nguyen Van A","email":"fr01-invalid-email","password":"ValidPass1!"}`
- Steps:
  1. Prepare JSON `{"name":"Nguyen Van A","email":"fr01-invalid-email","password":"ValidPass1!"}`.
  2. Send `POST http://localhost:3000/api/register`.
  3. Observe the public HTTP status and JSON response.
- Expected Result: The response does not satisfy the documented successful-registration contract of HTTP 200 with the success message and an `id` = 7. Exact invalid status and response body are unspecified.
- Actual Result: The API returned `200 OK` with the documented success message and id 8, contradicting the rejection oracle.
- Status: Fail
- Evidence: [FR01-DT-023](./evidence/FR01-DT-023.png)

## FR01-DT-024

- Test Case ID: FR01-DT-024
- Feature ID: FR-01
- Test Case Title: Duplicate email in API
- Technique: Domain Testing
- Objective: Verify API rejection for a controlled existing email while other properties remain valid.
- Requirement or Rule Reference: FR01-R05
- Test Basis Reference: `requirement-analysis.md` - FR01-R05; `domain-testing.md` - EMAIL-UNIQUENESS-I01
- Preconditions: Public API is available at `http://localhost:3000`; actor is unauthenticated; the specified email state is controlled.
- Test Data: `{"name":"Nguyen Van A","email":"registered@example.com","password":"ValidPass1!"}`
- Steps:
  1. Prepare JSON `{"name":"Nguyen Van A","email":"registered@example.com","password":"ValidPass1!"}`.
  2. Send `POST http://localhost:3000/api/register`.
  3. Observe the public HTTP status and JSON response.
- Expected Result: The response does not satisfy the documented successful-registration contract of HTTP 200 with the success message and an `id`. Exact invalid status and response body are unspecified.
- Actual Result: The API returned `200 OK` with the documented success message and id 8, contradicting the rejection oracle.
- Status: Fail
- Evidence: [FR01-DT-024](./evidence/FR01-DT-024.png)

## FR01-DT-025

- Test Case ID: FR01-DT-025
- Feature ID: FR-01
- Test Case Title: Password length invalid partition in API
- Technique: Domain Testing
- Objective: Verify API rejection for a password clearly inside the fewer-than-8 partition, not at an adjacent boundary.
- Requirement or Rule Reference: FR01-R06 through FR01-R10
- Test Basis Reference: `requirement-analysis.md` - FR01-R06 through FR01-R10; `domain-testing.md` - PASSWORD-LENGTH-I01
- Preconditions: Public API is available at `http://localhost:3000`; actor is unauthenticated; the specified email state is controlled.
- Test Data: `{"name":"Nguyen Van A","email":"fr01.dt025@example.com","password":"Ab1!"}`
- Steps:
  1. Prepare JSON `{"name":"Nguyen Van A","email":"fr01.dt025@example.com","password":"Ab1!"}`.
  2. Send `POST http://localhost:3000/api/register`.
  3. Observe the public HTTP status and JSON response.
- Expected Result: The response does not satisfy the documented successful-registration contract of HTTP 200 with the success message and an `id`. Exact invalid status and response body are unspecified.
- Actual Result: The API returned `200 OK` with the documented success message and id 9, contradicting the rejection oracle.
- Status: Fail
- Evidence: [FR01-DT-025](./evidence/FR01-DT-025.png)

## FR01-DT-026

- Test Case ID: FR01-DT-026
- Feature ID: FR-01
- Test Case Title: Password without uppercase in API
- Technique: Domain Testing
- Objective: Verify API rejection when uppercase is absent and all other password rules remain valid.
- Requirement or Rule Reference: FR01-R07
- Test Basis Reference: `requirement-analysis.md` - FR01-R07; `domain-testing.md` - PASSWORD-UPPERCASE-I01
- Preconditions: Public API is available at `http://localhost:3000`; actor is unauthenticated; the specified email state is controlled.
- Test Data: `{"name":"Nguyen Van A","email":"fr01.dt026@example.com","password":"validpass1!"}`
- Steps:
  1. Prepare JSON `{"name":"Nguyen Van A","email":"fr01.dt026@example.com","password":"validpass1!"}`.
  2. Send `POST http://localhost:3000/api/register`.
  3. Observe the public HTTP status and JSON response.
- Expected Result: The response does not satisfy the documented successful-registration contract of HTTP 200 with the success message and an `id`. Exact invalid status and response body are unspecified.
- Actual Result: The API returned `200 OK` with the documented success message and id 10, contradicting the rejection oracle.
- Status: Fail
- Evidence: [FR01-DT-026](./evidence/FR01-DT-026.png)

## FR01-DT-027

- Test Case ID: FR01-DT-027
- Feature ID: FR-01
- Test Case Title: Password without lowercase in API
- Technique: Domain Testing
- Objective: Verify API rejection when lowercase is absent and all other password rules remain valid.
- Requirement or Rule Reference: FR01-R08
- Test Basis Reference: `requirement-analysis.md` - FR01-R08; `domain-testing.md` - PASSWORD-LOWERCASE-I01
- Preconditions: Public API is available at `http://localhost:3000`; actor is unauthenticated; the specified email state is controlled.
- Test Data: `{"name":"Nguyen Van A","email":"fr01.dt027@example.com","password":"VALIDPASS1!"}`
- Steps:
  1. Prepare JSON `{"name":"Nguyen Van A","email":"fr01.dt027@example.com","password":"VALIDPASS1!"}`.
  2. Send `POST http://localhost:3000/api/register`.
  3. Observe the public HTTP status and JSON response.
- Expected Result: The response does not satisfy the documented successful-registration contract of HTTP 200 with the success message and an `id`. Exact invalid status and response body are unspecified.
- Actual Result: The API returned `200 OK` with the documented success message and id 11, contradicting the rejection oracle.
- Status: Fail
- Evidence: [FR01-DT-027](./evidence/FR01-DT-027.png)

## FR01-DT-028

- Test Case ID: FR01-DT-028
- Feature ID: FR-01
- Test Case Title: Password without digit in API
- Technique: Domain Testing
- Objective: Verify API rejection when a digit is absent and all other password rules remain valid.
- Requirement or Rule Reference: FR01-R09
- Test Basis Reference: `requirement-analysis.md` - FR01-R09; `domain-testing.md` - PASSWORD-DIGIT-I01
- Preconditions: Public API is available at `http://localhost:3000`; actor is unauthenticated; the specified email state is controlled.
- Test Data: `{"name":"Nguyen Van A","email":"fr01.dt028@example.com","password":"ValidPass!"}`
- Steps:
  1. Prepare JSON `{"name":"Nguyen Van A","email":"fr01.dt028@example.com","password":"ValidPass!"}`.
  2. Send `POST http://localhost:3000/api/register`.
  3. Observe the public HTTP status and JSON response.
- Expected Result: The response does not satisfy the documented successful-registration contract of HTTP 200 with the success message and an `id`. Exact invalid status and response body are unspecified.
- Actual Result: The API returned `200 OK` with the documented success message and id 12, contradicting the rejection oracle.
- Status: Fail
- Evidence: [FR01-DT-028](./evidence/FR01-DT-028.png)

## FR01-DT-029

- Test Case ID: FR01-DT-029
- Feature ID: FR-01
- Test Case Title: Password without special character in API
- Technique: Domain Testing
- Objective: Verify API rejection when a documented special character is absent and all other password rules remain valid.
- Requirement or Rule Reference: FR01-R10
- Test Basis Reference: `requirement-analysis.md` - FR01-R10; `domain-testing.md` - PASSWORD-SPECIAL-I01
- Preconditions: Public API is available at `http://localhost:3000`; actor is unauthenticated; the specified email state is controlled.
- Test Data: `{"name":"Nguyen Van A","email":"fr01.dt029@example.com","password":"ValidPass12"}`
- Steps:
  1. Prepare JSON `{"name":"Nguyen Van A","email":"fr01.dt029@example.com","password":"ValidPass12"}`.
  2. Send `POST http://localhost:3000/api/register`.
  3. Observe the public HTTP status and JSON response.
- Expected Result: The response does not satisfy the documented successful-registration contract of HTTP 200 with the success message and an `id`. Exact invalid status and response body are unspecified.
- Actual Result: The API returned `200 OK` with the documented success message and id 13, contradicting the rejection oracle.
- Status: Fail
- Evidence: [FR01-DT-029](./evidence/FR01-DT-029.png)

## Boundary Value Analysis Test Cases

## FR01-BVA-001

- Test Case ID: FR01-BVA-001
- Feature ID: FR-01
- Test Case Title: UI password length 7 characters
- Technique: Boundary Value Analysis
- Objective: Verify the UI classification at FR01-PASSWORD-LENGTH-B01 using an exactly 7-character password.
- Requirement or Rule Reference: FR01-R06 through FR01-R10
- Test Basis Reference: boundary-value-analysis.md - FR01-PASSWORD-LENGTH-B01
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: Name `Nguyen Van A`; controlled unused email `bva.ui.001@example.com`; Password and Confirm Password `Abcd1!x` (7 characters).
- Steps:
  1. Open `/register` as a guest.
  2. Enter Name `Nguyen Van A`, unused Email `bva.ui.001@example.com`, Password and Confirm Password `Abcd1!x`.
  3. Activate the registration submit control.
  4. Observe whether registration completes, any displayed validation error, and navigation.
- Expected Result: Registration is rejected because the password is shorter than 8 characters; it does not complete. Exact UI error text is unspecified.
- Actual Result: The registration page loaded, but no Confirm Password label or input control was present. Execution stopped before form submission.
- Status: Blocked
- Blocking Reason: The test requires Confirm Password to match the 7-character password so the min-1 boundary is isolated, but the UI does not provide this control.
- Evidence: [FR01-BVA-001.png](./evidence/FR01-BVA-001.png)

## FR01-BVA-002

- Test Case ID: FR01-BVA-002
- Feature ID: FR-01
- Test Case Title: UI password length 8 characters
- Technique: Boundary Value Analysis
- Objective: Verify the UI classification at FR01-PASSWORD-LENGTH-B02 using an exactly 8-character password.
- Requirement or Rule Reference: FR01-R06 through FR01-R10
- Test Basis Reference: boundary-value-analysis.md - FR01-PASSWORD-LENGTH-B02
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: Name `Nguyen Van A`; controlled unused email `bva.ui.002@example.com`; Password and Confirm Password `Abcd1!xy` (8 characters).
- Steps:
  1. Open `/register` as a guest.
  2. Enter Name `Nguyen Van A`, unused Email `bva.ui.002@example.com`, Password and Confirm Password `Abcd1!xy`.
  3. Activate the registration submit control.
  4. Observe whether registration completes, any displayed validation error, and navigation.
- Expected Result: Registration completes successfully and navigates to the Login page; no exact URL, timing, or success text is asserted.
- Actual Result: The registration page loaded, but no Confirm Password label or input control was present. Execution stopped before form submission.
- Status: Blocked
- Blocking Reason: The test requires Confirm Password to match the 8-character password so the minimum boundary is isolated, but the UI does not provide this control.
- Evidence: [FR01-BVA-002.png](./evidence/FR01-BVA-002.png)

## FR01-BVA-003

- Test Case ID: FR01-BVA-003
- Feature ID: FR-01
- Test Case Title: UI password length 9 characters
- Technique: Boundary Value Analysis
- Objective: Verify the UI classification at FR01-PASSWORD-LENGTH-B03 using an exactly 9-character password.
- Requirement or Rule Reference: FR01-R06 through FR01-R10
- Test Basis Reference: boundary-value-analysis.md - FR01-PASSWORD-LENGTH-B03
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: Name `Nguyen Van A`; controlled unused email `bva.ui.003@example.com`; Password and Confirm Password `Abcd1!xyz` (9 characters).
- Steps:
  1. Open `/register` as a guest.
  2. Enter Name `Nguyen Van A`, unused Email `bva.ui.003@example.com`, Password and Confirm Password `Abcd1!xyz`.
  3. Activate the registration submit control.
  4. Observe whether registration completes, any displayed validation error, and navigation.
- Expected Result: Registration completes successfully and navigates to the Login page; no exact URL, timing, or success text is asserted.
- Actual Result: The registration page loaded, but no Confirm Password label or input control was present. Execution stopped before form submission.
- Status: Blocked
- Blocking Reason: The test requires Confirm Password to match the 9-character password so the min+1 boundary is isolated, but the UI does not provide this control.
- Evidence: [FR01-BVA-003.png](./evidence/FR01-BVA-003.png)

## FR01-BVA-004

- Test Case ID: FR01-BVA-004
- Feature ID: FR-01
- Test Case Title: UI password length 11 characters
- Technique: Boundary Value Analysis
- Objective: Verify the UI classification at FR01-PASSWORD-LENGTH-N01 using an exactly 11-character password.
- Requirement or Rule Reference: FR01-R06 through FR01-R10
- Test Basis Reference: boundary-value-analysis.md - FR01-PASSWORD-LENGTH-N01
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: Name `Nguyen Van A`; controlled unused email `bva.ui.004@example.com`; Password and Confirm Password `ValidPass1!` (11 characters).
- Steps:
  1. Open `/register` as a guest.
  2. Enter Name `Nguyen Van A`, unused Email `bva.ui.004@example.com`, Password and Confirm Password `ValidPass1!`.
  3. Activate the registration submit control.
  4. Observe whether registration completes, any displayed validation error, and navigation.
- Expected Result: Registration completes successfully and navigates to the Login page; no exact URL, timing, or success text is asserted.
- Actual Result: The registration page loaded, but no Confirm Password label or input control was present. Execution stopped before form submission.
- Status: Blocked
- Blocking Reason: The test requires Confirm Password to match the 11-character nominal password, but the UI does not provide this control.
- Evidence: [FR01-BVA-004.png](./evidence/FR01-BVA-004.png)

## FR01-BVA-005

- Test Case ID: FR01-BVA-005
- Feature ID: FR-01
- Test Case Title: API password length 7 characters
- Technique: Boundary Value Analysis
- Objective: Verify the API classification at FR01-PASSWORD-LENGTH-B01 using an exactly 7-character password.
- Requirement or Rule Reference: FR01-R06 through FR01-R10
- Test Basis Reference: boundary-value-analysis.md - FR01-PASSWORD-LENGTH-B01
- Preconditions: Public API is available at `http://localhost:3000`; actor is unauthenticated; specified email state is controlled.
- Test Data: `{"name":"Nguyen Van A","email":"bva.api.005@example.com","password":"Abcd1!x"}`; email controlled unused.
- Steps:
  1. Prepare a JSON request body: `{"name":"Nguyen Van A","email":"bva.api.005@example.com","password":"Abcd1!x"}`.
  2. Send `POST http://localhost:3000/api/register`.
  3. Observe the public HTTP status and JSON response.
- Expected Result: The response does not satisfy the documented successful-registration contract because the password is shorter than 8 characters. Exact invalid status and response body are unspecified.
- Actual Result: The API returned `200 OK` with the documented success message and id 14, contradicting the rejection oracle.
- Status: Fail
- Evidence: [FR01-BVA-005](./evidence/FR01-BVA-005.png)

## FR01-BVA-006

- Test Case ID: FR01-BVA-006
- Feature ID: FR-01
- Test Case Title: API password length 8 characters
- Technique: Boundary Value Analysis
- Objective: Verify the API classification at FR01-PASSWORD-LENGTH-B02 using an exactly 8-character password.
- Requirement or Rule Reference: FR01-R06 through FR01-R10
- Test Basis Reference: boundary-value-analysis.md - FR01-PASSWORD-LENGTH-B02
- Preconditions: Public API is available at `http://localhost:3000`; actor is unauthenticated; specified email state is controlled.
- Test Data: `{"name":"Nguyen Van A","email":"bva.api.006@example.com","password":"Abcd1!xy"}`; email controlled unused.
- Steps:
  1. Prepare a JSON request body: `{"name":"Nguyen Van A","email":"bva.api.006@example.com","password":"Abcd1!xy"}`.
  2. Send `POST http://localhost:3000/api/register`.
  3. Observe the public HTTP status and JSON response.
- Expected Result: The response is `200 OK` JSON containing the documented success message and an `id` value.
- Actual Result: The API returned `200 OK` with the documented success message and id 15.
- Status: Pass
- Evidence: [FR01-BVA-006](./evidence/FR01-BVA-006.png)

## FR01-BVA-007

- Test Case ID: FR01-BVA-007
- Feature ID: FR-01
- Test Case Title: API password length 9 characters
- Technique: Boundary Value Analysis
- Objective: Verify the API classification at FR01-PASSWORD-LENGTH-B03 using an exactly 9-character password.
- Requirement or Rule Reference: FR01-R06 through FR01-R10
- Test Basis Reference: boundary-value-analysis.md - FR01-PASSWORD-LENGTH-B03
- Preconditions: Public API is available at `http://localhost:3000`; actor is unauthenticated; specified email state is controlled.
- Test Data: `{"name":"Nguyen Van A","email":"bva.api.007@example.com","password":"Abcd1!xyz"}`; email controlled unused.
- Steps:
  1. Prepare a JSON request body: `{"name":"Nguyen Van A","email":"bva.api.007@example.com","password":"Abcd1!xyz"}`.
  2. Send `POST http://localhost:3000/api/register`.
  3. Observe the public HTTP status and JSON response.
- Expected Result: The response is `200 OK` JSON containing the documented success message and an `id` value.
- Actual Result: The API returned `200 OK` with the documented success message and id 16.
- Status: Pass
- Evidence: [FR01-BVA-007](./evidence/FR01-BVA-007.png)

## FR01-BVA-008

- Test Case ID: FR01-BVA-008
- Feature ID: FR-01
- Test Case Title: API password length 11 characters
- Technique: Boundary Value Analysis
- Objective: Verify the API classification at FR01-PASSWORD-LENGTH-N01 using an exactly 11-character password.
- Requirement or Rule Reference: FR01-R06 through FR01-R10
- Test Basis Reference: boundary-value-analysis.md - FR01-PASSWORD-LENGTH-N01
- Preconditions: Public API is available at `http://localhost:3000`; actor is unauthenticated; specified email state is controlled.
- Test Data: `{"name":"Nguyen Van A","email":"bva.api.008@example.com","password":"ValidPass1!"}`; email controlled unused.
- Steps:
  1. Prepare a JSON request body: `{"name":"Nguyen Van A","email":"bva.api.008@example.com","password":"ValidPass1!"}`.
  2. Send `POST http://localhost:3000/api/register`.
  3. Observe the public HTTP status and JSON response.
- Expected Result: The response is `200 OK` JSON containing the documented success message and an `id` value.
- Actual Result: The API returned `200 OK` with the documented success message and id 18.
- Status: Pass
- Evidence: [FR01-BVA-008](./evidence/FR01-BVA-008.png)

## Exploratory Backlog

| Candidate ID            | Input or Observation             | Missing Oracle                         | Clarification Required                | Reason Excluded from Normative Coverage |
| ----------------------- | -------------------------------- | -------------------------------------- | ------------------------------------- | --------------------------------------- |
| NAME-WHITESPACE-A01     | Full name `"   "`                | Whether whitespace counts as provided  | Trimming/whitespace policy            | FR01-R01 does not define it.            |
| EMAIL-CASE-A01          | Case variants of one email       | Whether variants are the same identity | Case/normalization policy             | FR01-R05 does not define it.            |
| PASSWORD-SPECIAL-A01    | Password containing unlisted `#` | Whether `#` qualifies                  | Whether special list is exhaustive    | FR01-R10 is ambiguous.                  |
| FORM-STEP-INDICATOR-A01 | Observe step count/indicator     | Whether registration is multi-step     | Authoritative registration step model | SF05 is conditional.                    |

## Preliminary Coverage Summary

| Rule ID                       | Partition or Boundary ID                        | Technique      | Covering Test Case ID      | Surface | Coverage Status         | Notes                                                            |
| ----------------------------- | ----------------------------------------------- | -------------- | -------------------------- | ------- | ----------------------- | ---------------------------------------------------------------- |
| FR01-R01                      | NAME-PRESENCE-V01 / I01                         | Domain Testing | FR01-DT-001, 002, 003, 019 | UI/API  | Covered                 | Valid, empty UI, and omitted API representations covered.        |
| FR01-R02                      | EMAIL-PRESENCE-V01 / I01                        | Domain Testing | FR01-DT-001, 002, 004, 020 | UI/API  | Covered                 | Valid, empty UI, and omitted API representations covered.        |
| FR01-R04                      | EMAIL-FORMAT-V01 / I01                          | Domain Testing | FR01-DT-001, 002, 005, 023 | UI/API  | Covered                 | Malformed email covered separately on both surfaces.             |
| FR01-R05                      | EMAIL-UNIQUENESS-V01 / I01                      | Domain Testing | FR01-DT-001, 002, 006, 024 | UI/API  | Covered                 | Controlled unused and existing states covered on both surfaces.  |
| FR01-R03                      | PASSWORD-PRESENCE-V01 / I01                     | Domain Testing | FR01-DT-001, 002, 007, 021 | UI/API  | Covered                 | UI dependency is documented; API omission isolates requiredness. |
| FR01-R06                      | PASSWORD-LENGTH-V01 / I01                       | Domain Testing | FR01-DT-001, 002, 022, 025 | UI/API  | Covered                 | DT uses 4-character non-boundary representative.                 |
| FR01-R07                      | PASSWORD-UPPERCASE-V01 / I01                    | Domain Testing | FR01-DT-001, 002, 008, 026 | UI/API  | Covered                 | Invalid class isolated on both surfaces.                         |
| FR01-R08                      | PASSWORD-LOWERCASE-V01 / I01                    | Domain Testing | FR01-DT-001, 002, 009, 027 | UI/API  | Covered                 | Invalid class isolated on both surfaces.                         |
| FR01-R09                      | PASSWORD-DIGIT-V01 / I01                        | Domain Testing | FR01-DT-001, 002, 010, 028 | UI/API  | Covered                 | Invalid class isolated on both surfaces.                         |
| FR01-R10                      | PASSWORD-SPECIAL-V01 / I01                      | Domain Testing | FR01-DT-001, 002, 011, 029 | UI/API  | Covered                 | Invalid class isolated on both surfaces.                         |
| FR01-R11                      | CONFIRM-CONTROL-V01 / I01                       | Domain Testing | FR01-DT-012                | UI      | Covered                 | Invalid output is a possible non-conforming observation.         |
| FR01-R11                      | CONFIRM-VALUE-V01 / I01                         | Domain Testing | FR01-DT-001, 007, 013      | UI      | Covered                 | Empty confirmation and dependency case covered.                  |
| FR01-R12                      | CONFIRM-MATCH-V01 / I01                         | Domain Testing | FR01-DT-001, 014           | UI      | Covered                 | Match and mismatch covered.                                      |
| FR01-R13, FR01-R14            | REGISTRATION-COMPLETE-V01; REDIRECT-SUCCESS-V01 | Domain Testing | FR01-DT-001                | UI      | Covered                 | Valid completion and Login navigation covered.                   |
| FR01-API01 through FR01-API05 | API-REQUEST-V01/I01/I02/I03; API-SUCCESS-V01    | Domain Testing | FR01-DT-002, 019-021       | API     | Covered                 | Complete and omitted-property request shapes covered.            |
| FR01-SF01                     | FORM-REQUIRED-MARKER-V01/I01                    | Domain Testing | FR01-DT-015                | UI      | Covered                 | Invalid output is a possible non-conforming observation.         |
| FR01-SF02                     | FORM-EMAIL-TYPE-V01/I01                         | Domain Testing | FR01-DT-016                | UI      | Covered                 | Invalid output is a possible non-conforming observation.         |
| FR01-SF03                     | FORM-PASSWORD-TYPE-V01/I01                      | Domain Testing | FR01-DT-017                | UI      | Covered                 | Invalid output is a possible non-conforming observation.         |
| FR01-SF04                     | FORM-ERROR-PLACEMENT-V01/I01                    | Domain Testing | FR01-DT-018                | UI      | Covered                 | Invalid output is a possible non-conforming observation.         |
| FR01-R01 through FR01-R12     | VALIDATION-REJECTION-V01                        | Domain Testing | FR01-DT-003-014, 019-029   | UI/API  | Covered                 | Each invalid rule has an observable rejection oracle.            |
| Feature Intake                | ACTOR-GUEST-V01                                 | Domain Testing | All cases                  | UI/API  | Covered                 | Guest state is an explicit precondition.                         |
| FR01-R06                      | FR01-PASSWORD-LENGTH-B01/B02/B03/N01            | BVA            | FR01-BVA-001-008           | UI/API  | Covered                 | Four approved values covered separately on both surfaces.        |
| FR01 ambiguities              | Four A01 candidates                             | Exploratory    | None                       | UI/API  | Exploratory - No Oracle | Listed in backlog; excluded from normative coverage.             |

## Design Gaps and Assumptions

- Controlled email state must be prepared without treating hidden data as an oracle.
- UI BVA execution depends on the approved Confirm Password control being available.
- The API contract has no Confirm Password property, so none is added.
- Invalid API outcomes use rejection/non-completion only; exact status/body needs clarification.
- No normative tests cover undocumented whitespace, case normalization, unlisted symbols, step count, maximum lengths, Unicode semantics, exact Login URL/timing, or UI message text.
- Each case states its exact rule, test basis, partition or boundary, concrete representative data, dependencies, surface, and observable expected result.

## Human Review - Phase 5

- Reviewer: Nguyen Thanh Tien

- Review Date and Time: 2026-06-24 13:08

- Review Scope: FR-01 Test-Case Design

- Corrections Made:
  - Replaced nominal placeholders with concrete test data.
  - Rewrote unclear and duplicated test steps.
  - Standardized Rule IDs and test-basis references.
  - Added exact partition and boundary IDs.
  - Removed `Source Code Reference` from black-box cases.
  - Added UI and API cases for the invalid password-length partition using `Ab1!`.
  - Added missing API cases for invalid email, duplicate email, and missing password character classes.
  - Kept each invalid case focused on one invalid condition.
  - Avoided undocumented API status codes and error messages.
  - Updated the coverage table for all new cases.
  - Confirmed that all eight BVA cases remain covered.
  - Confirmed that all cases were unexecuted at the time of the Phase 5 design review.

- Missing Cases Added: 8
  - `FR01-DT-022`: Short password through UI.
  - `FR01-DT-023`: Invalid email through API.
  - `FR01-DT-024`: Duplicate email through API.
  - `FR01-DT-025`: Short password through API.
  - `FR01-DT-026`: Missing uppercase through API.
  - `FR01-DT-027`: Missing lowercase through API.
  - `FR01-DT-028`: Missing digit through API.
  - `FR01-DT-029`: Missing special character through API.

- Test Cases Before Review: 21 DT and 8 BVA

- Test Cases After Review: 29 DT and 8 BVA

- Duplicate Cases Removed: None

- Incorrect Cases Removed: None

- Status: Completed

- Approved for Validation: Yes

- Approved for Traceability and Quality Review: Yes

- Approved for Test Execution: Yes
