# Test Cases - FR-01 Account Registration

## Black-box Test Basis and Approval Summary

The approved bases are `requirement-analysis.md`, the completed and BVA-approved `domain-testing.md`, and the completed, test-case-derivation-approved `boundary-value-analysis.md`. Only public UI/API procedures are designed. No implementation source or runtime behaviour is used. All cases remain unexecuted.

## Test Design Strategy

Compatible valid partitions are combined in nominal UI/API flows. Each invalid DT case isolates one condition with unrelated values nominal. UI conformance cases expect compliant public controls and map the corresponding invalid partition as a possible non-conforming observation. BVA uses separate UI and API procedures for every approved value. Repeated boundary cases are intentional because surface and boundary position differ.

## Shared Preconditions and Test Data

- UI: `/register`. API: `POST http://localhost:3000/api/register`.
- Actor: guest/unauthenticated.
- Nominal name: `Nguyen Van A`.
- Controlled unused emails must be confirmed unused before later execution; `registered@example.com` must be controlled as existing.
- Nominal password: `ValidPass1!`; UI confirmation matches unless the case says otherwise.
- Exact invalid API status/body, duplicate error, UI validation text, Login URL, redirect timing, and success text are not oracles.

## Domain Testing Test Cases

## FR01-DT-001

- Test Case ID: FR01-DT-001
- Feature ID: FR-01
- Test Case Title: Complete valid UI registration
- Technique: Domain Testing
- Objective: Verify the nominal valid UI registration domain and documented Login redirect.
- Requirement or Rule Reference: FR01-R01-R14; FR01-SF04
- Test Basis Reference: requirement-analysis.md; domain-testing.md normative valid partitions
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: Name `Nguyen Van A`; controlled unused email `new.user@example.com`; password `ValidPass1!`; UI confirmation `ValidPass1!`; guest/unauthenticated state.
- Steps:
  1. Open `/register` as a guest.
  2. Enter Full name `Nguyen Van A`, controlled unused email `new.user@example.com`, Password and Confirm Password `ValidPass1!`.
  3. Activate the registration submit control.
  4. Observe whether registration completes, any displayed validation error, and navigation.
- Expected Result: Registration completes successfully and the UI navigates to the Login page. No exact success text, URL, or timing is asserted.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: NAME-PRESENCE-V01; EMAIL-PRESENCE-V01; EMAIL-FORMAT-V01; EMAIL-UNIQUENESS-V01; PASSWORD-PRESENCE-V01; PASSWORD-LENGTH-V01; PASSWORD-UPPERCASE-V01; PASSWORD-LOWERCASE-V01; PASSWORD-DIGIT-V01; PASSWORD-SPECIAL-V01; CONFIRM-VALUE-V01; CONFIRM-MATCH-V01; REGISTRATION-COMPLETE-V01; REDIRECT-SUCCESS-V01; ACTOR-GUEST-V01
- Source Code Reference: Not Applicable - Black-box testing
- Notes and Assumptions: Uses a controlled unused email; exact success message is outside the oracle.

## FR01-DT-002

- Test Case ID: FR01-DT-002
- Feature ID: FR-01
- Test Case Title: Complete valid API registration
- Technique: Domain Testing
- Objective: Verify the documented complete API request and successful response contract.
- Requirement or Rule Reference: FR01-API01-API05; FR01-R01-R10
- Test Basis Reference: requirement-analysis.md API rules; domain-testing.md API-REQUEST-V01 and API-SUCCESS-V01
- Preconditions: Public API is available at `http://localhost:3000`; actor is unauthenticated; specified email state is controlled.
- Test Data: `{"name":"Nguyen Van A","email":"new.api.user@example.com","password":"ValidPass1!"}` with email controlled unused
- Steps:
  1. Prepare a JSON request body: `{"name":"Nguyen Van A","email":"new.api.user@example.com","password":"ValidPass1!"}`.
  2. Send `POST http://localhost:3000/api/register`.
  3. Observe the public HTTP status and JSON response.
- Expected Result: The response is `200 OK` JSON containing message `User registered successfully` and an `id` value; the literal ID is not fixed.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: API-REQUEST-V01; API-SUCCESS-V01; ACTOR-GUEST-V01; all compatible valid name/email/password partitions
- Source Code Reference: Not Applicable - Black-box testing
- Notes and Assumptions: Confirm Password is not added because it is absent from the approved API contract.

## FR01-DT-003

- Test Case ID: FR01-DT-003
- Feature ID: FR-01
- Test Case Title: Missing full name in UI
- Technique: Domain Testing
- Objective: Verify rejection for missing full name in ui while unrelated inputs remain nominal.
- Requirement or Rule Reference: FR01-R01
- Test Basis Reference: requirement-analysis.md corresponding rule; domain-testing.md NAME-PRESENCE-I01
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: leave Full name empty; enter nominal email/password/confirmation
- Steps:
  1. Open `/register` as a guest.
  2. Enter leave Full name empty; enter nominal email/password/confirmation.
  3. Activate the registration submit control.
  4. Observe whether registration completes, any displayed validation error, and navigation.
- Expected Result: Registration is rejected and does not complete. If an error is displayed, it appears above the submit control; exact text is unspecified.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: NAME-PRESENCE-I01; VALIDATION-REJECTION-V01
- Source Code Reference: Not Applicable - Black-box testing
- Notes and Assumptions: Isolates one invalid partition; no undocumented message is asserted.

## FR01-DT-004

- Test Case ID: FR01-DT-004
- Feature ID: FR-01
- Test Case Title: Missing email in UI
- Technique: Domain Testing
- Objective: Verify rejection for missing email in ui while unrelated inputs remain nominal.
- Requirement or Rule Reference: FR01-R02
- Test Basis Reference: requirement-analysis.md corresponding rule; domain-testing.md EMAIL-PRESENCE-I01
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: enter nominal name/password/confirmation; leave Email empty
- Steps:
  1. Open `/register` as a guest.
  2. Enter enter nominal name/password/confirmation; leave Email empty.
  3. Activate the registration submit control.
  4. Observe whether registration completes, any displayed validation error, and navigation.
- Expected Result: Registration is rejected and does not complete. If an error is displayed, it appears above the submit control; exact text is unspecified.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: EMAIL-PRESENCE-I01; VALIDATION-REJECTION-V01
- Source Code Reference: Not Applicable - Black-box testing
- Notes and Assumptions: Isolates one invalid partition; no undocumented message is asserted.

## FR01-DT-005

- Test Case ID: FR01-DT-005
- Feature ID: FR-01
- Test Case Title: Invalid email format in UI
- Technique: Domain Testing
- Objective: Verify rejection for invalid email format in ui while unrelated inputs remain nominal.
- Requirement or Rule Reference: FR01-R04
- Test Basis Reference: requirement-analysis.md corresponding rule; domain-testing.md EMAIL-FORMAT-I01
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: enter nominal name/password/confirmation and Email `not-an-email`
- Steps:
  1. Open `/register` as a guest.
  2. Enter enter nominal name/password/confirmation and Email `not-an-email`.
  3. Activate the registration submit control.
  4. Observe whether registration completes, any displayed validation error, and navigation.
- Expected Result: Registration is rejected and does not complete. If an error is displayed, it appears above the submit control; exact text is unspecified.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: EMAIL-FORMAT-I01; VALIDATION-REJECTION-V01
- Source Code Reference: Not Applicable - Black-box testing
- Notes and Assumptions: Isolates one invalid partition; no undocumented message is asserted.

## FR01-DT-006

- Test Case ID: FR01-DT-006
- Feature ID: FR-01
- Test Case Title: Duplicate email in UI
- Technique: Domain Testing
- Objective: Verify rejection for duplicate email in ui while unrelated inputs remain nominal.
- Requirement or Rule Reference: FR01-R05
- Test Basis Reference: requirement-analysis.md corresponding rule; domain-testing.md EMAIL-UNIQUENESS-I01
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: enter nominal name/password/confirmation and controlled existing Email `registered@example.com`
- Steps:
  1. Open `/register` as a guest.
  2. Enter enter nominal name/password/confirmation and controlled existing Email `registered@example.com`.
  3. Activate the registration submit control.
  4. Observe whether registration completes, any displayed validation error, and navigation.
- Expected Result: Registration is rejected and does not complete. If an error is displayed, it appears above the submit control; exact text is unspecified.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: EMAIL-UNIQUENESS-I01; VALIDATION-REJECTION-V01
- Source Code Reference: Not Applicable - Black-box testing
- Notes and Assumptions: Isolates one invalid partition; no undocumented message is asserted.

## FR01-DT-007

- Test Case ID: FR01-DT-007
- Feature ID: FR-01
- Test Case Title: Missing password in UI
- Technique: Domain Testing
- Objective: Verify rejection for missing password in ui while unrelated inputs remain nominal.
- Requirement or Rule Reference: FR01-R03
- Test Basis Reference: requirement-analysis.md corresponding rule; domain-testing.md PASSWORD-PRESENCE-I01
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: enter nominal name and unused email; leave Password empty; leave confirmation empty
- Steps:
  1. Open `/register` as a guest.
  2. Enter enter nominal name and unused email; leave Password empty; leave confirmation empty.
  3. Activate the registration submit control.
  4. Observe whether registration completes, any displayed validation error, and navigation.
- Expected Result: Registration is rejected and does not complete. If an error is displayed, it appears above the submit control; exact text is unspecified.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: PASSWORD-PRESENCE-I01; VALIDATION-REJECTION-V01
- Source Code Reference: Not Applicable - Black-box testing
- Notes and Assumptions: Isolates one invalid partition; no undocumented message is asserted.

## FR01-DT-008

- Test Case ID: FR01-DT-008
- Feature ID: FR-01
- Test Case Title: Password without uppercase in UI
- Technique: Domain Testing
- Objective: Verify rejection for password without uppercase in ui while unrelated inputs remain nominal.
- Requirement or Rule Reference: FR01-R07
- Test Basis Reference: requirement-analysis.md corresponding rule; domain-testing.md PASSWORD-UPPERCASE-I01
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: enter nominal name/unused email and Password/confirmation `validpass1!`
- Steps:
  1. Open `/register` as a guest.
  2. Enter enter nominal name/unused email and Password/confirmation `validpass1!`.
  3. Activate the registration submit control.
  4. Observe whether registration completes, any displayed validation error, and navigation.
- Expected Result: Registration is rejected and does not complete. If an error is displayed, it appears above the submit control; exact text is unspecified.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: PASSWORD-UPPERCASE-I01; VALIDATION-REJECTION-V01
- Source Code Reference: Not Applicable - Black-box testing
- Notes and Assumptions: Isolates one invalid partition; no undocumented message is asserted.

## FR01-DT-009

- Test Case ID: FR01-DT-009
- Feature ID: FR-01
- Test Case Title: Password without lowercase in UI
- Technique: Domain Testing
- Objective: Verify rejection for password without lowercase in ui while unrelated inputs remain nominal.
- Requirement or Rule Reference: FR01-R08
- Test Basis Reference: requirement-analysis.md corresponding rule; domain-testing.md PASSWORD-LOWERCASE-I01
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: enter nominal name/unused email and Password/confirmation `VALIDPASS1!`
- Steps:
  1. Open `/register` as a guest.
  2. Enter enter nominal name/unused email and Password/confirmation `VALIDPASS1!`.
  3. Activate the registration submit control.
  4. Observe whether registration completes, any displayed validation error, and navigation.
- Expected Result: Registration is rejected and does not complete. If an error is displayed, it appears above the submit control; exact text is unspecified.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: PASSWORD-LOWERCASE-I01; VALIDATION-REJECTION-V01
- Source Code Reference: Not Applicable - Black-box testing
- Notes and Assumptions: Isolates one invalid partition; no undocumented message is asserted.

## FR01-DT-010

- Test Case ID: FR01-DT-010
- Feature ID: FR-01
- Test Case Title: Password without digit in UI
- Technique: Domain Testing
- Objective: Verify rejection for password without digit in ui while unrelated inputs remain nominal.
- Requirement or Rule Reference: FR01-R09
- Test Basis Reference: requirement-analysis.md corresponding rule; domain-testing.md PASSWORD-DIGIT-I01
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: enter nominal name/unused email and Password/confirmation `ValidPass!`
- Steps:
  1. Open `/register` as a guest.
  2. Enter enter nominal name/unused email and Password/confirmation `ValidPass!`.
  3. Activate the registration submit control.
  4. Observe whether registration completes, any displayed validation error, and navigation.
- Expected Result: Registration is rejected and does not complete. If an error is displayed, it appears above the submit control; exact text is unspecified.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: PASSWORD-DIGIT-I01; VALIDATION-REJECTION-V01
- Source Code Reference: Not Applicable - Black-box testing
- Notes and Assumptions: Isolates one invalid partition; no undocumented message is asserted.

## FR01-DT-011

- Test Case ID: FR01-DT-011
- Feature ID: FR-01
- Test Case Title: Password without documented special character in UI
- Technique: Domain Testing
- Objective: Verify rejection for password without documented special character in ui while unrelated inputs remain nominal.
- Requirement or Rule Reference: FR01-R10
- Test Basis Reference: requirement-analysis.md corresponding rule; domain-testing.md PASSWORD-SPECIAL-I01
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: enter nominal name/unused email and Password/confirmation `ValidPass12`
- Steps:
  1. Open `/register` as a guest.
  2. Enter enter nominal name/unused email and Password/confirmation `ValidPass12`.
  3. Activate the registration submit control.
  4. Observe whether registration completes, any displayed validation error, and navigation.
- Expected Result: Registration is rejected and does not complete. If an error is displayed, it appears above the submit control; exact text is unspecified.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: PASSWORD-SPECIAL-I01; VALIDATION-REJECTION-V01
- Source Code Reference: Not Applicable - Black-box testing
- Notes and Assumptions: Isolates one invalid partition; no undocumented message is asserted.

## FR01-DT-012

- Test Case ID: FR01-DT-012
- Feature ID: FR-01
- Test Case Title: Confirm Password control conformance
- Technique: Domain Testing
- Objective: Observe that the registration UI supplies the required Confirm Password control.
- Requirement or Rule Reference: FR01-R11
- Test Basis Reference: requirement-analysis.md shared/UI rule; domain-testing.md corresponding FORM/CONFIRM partition
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: a visible Confirm Password input control
- Steps:
  1. Open `/register` as a guest.
  2. Inspect the relevant public form control or label.
- Expected Result: The registration form visibly contains a Confirm Password input control. Absence is the observation that would indicate non-conformance.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: CONFIRM-CONTROL-V01; non-conforming observation CONFIRM-CONTROL-I01
- Source Code Reference: Not Applicable - Black-box testing
- Notes and Assumptions: The invalid partition is an observable non-conformance, not a state forced by the tester.

## FR01-DT-013

- Test Case ID: FR01-DT-013
- Feature ID: FR-01
- Test Case Title: Empty Confirm Password value
- Technique: Domain Testing
- Objective: Verify rejection for empty confirm password value while unrelated inputs remain nominal.
- Requirement or Rule Reference: FR01-R11
- Test Basis Reference: requirement-analysis.md corresponding rule; domain-testing.md CONFIRM-VALUE-I01
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: enter nominal name/unused email/Password and leave Confirm Password empty
- Steps:
  1. Open `/register` as a guest.
  2. Enter enter nominal name/unused email/Password and leave Confirm Password empty.
  3. Activate the registration submit control.
  4. Observe whether registration completes, any displayed validation error, and navigation.
- Expected Result: Registration is rejected and does not complete. If an error is displayed, it appears above the submit control; exact text is unspecified.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: CONFIRM-VALUE-I01; VALIDATION-REJECTION-V01
- Source Code Reference: Not Applicable - Black-box testing
- Notes and Assumptions: Isolates one invalid partition; no undocumented message is asserted.

## FR01-DT-014

- Test Case ID: FR01-DT-014
- Feature ID: FR-01
- Test Case Title: Mismatching password confirmation
- Technique: Domain Testing
- Objective: Verify rejection for mismatching password confirmation while unrelated inputs remain nominal.
- Requirement or Rule Reference: FR01-R12
- Test Basis Reference: requirement-analysis.md corresponding rule; domain-testing.md CONFIRM-MATCH-I01
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: enter nominal name/unused email, Password `ValidPass1!`, Confirm Password `ValidPass2!`
- Steps:
  1. Open `/register` as a guest.
  2. Enter enter nominal name/unused email, Password `ValidPass1!`, Confirm Password `ValidPass2!`.
  3. Activate the registration submit control.
  4. Observe whether registration completes, any displayed validation error, and navigation.
- Expected Result: Registration is rejected and does not complete. If an error is displayed, it appears above the submit control; exact text is unspecified.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: CONFIRM-MATCH-I01; VALIDATION-REJECTION-V01
- Source Code Reference: Not Applicable - Black-box testing
- Notes and Assumptions: Isolates one invalid partition; no undocumented message is asserted.

## FR01-DT-015

- Test Case ID: FR01-DT-015
- Feature ID: FR-01
- Test Case Title: Required-field marker conformance
- Technique: Domain Testing
- Objective: Verify required registration labels show adjacent `*` markers.
- Requirement or Rule Reference: FR01-SF01
- Test Basis Reference: requirement-analysis.md shared/UI rule; domain-testing.md corresponding FORM/CONFIRM partition
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: Full name, Email, and Password labels with adjacent `*`
- Steps:
  1. Open `/register` as a guest.
  2. Inspect the relevant public form control or label.
- Expected Result: Every unequivocally required label displays adjacent `*`; a missing marker is the non-conforming observation.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: FORM-REQUIRED-MARKER-V01; non-conforming observation FORM-REQUIRED-MARKER-I01
- Source Code Reference: Not Applicable - Black-box testing
- Notes and Assumptions: The invalid partition is an observable non-conformance, not a state forced by the tester.

## FR01-DT-016

- Test Case ID: FR01-DT-016
- Feature ID: FR-01
- Test Case Title: Email control type conformance
- Technique: Domain Testing
- Objective: Verify the Email control exposes `type="email"`.
- Requirement or Rule Reference: FR01-SF02
- Test Basis Reference: requirement-analysis.md shared/UI rule; domain-testing.md corresponding FORM/CONFIRM partition
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: observable Email control type
- Steps:
  1. Open `/register` as a guest.
  2. Inspect the relevant public form control or label.
- Expected Result: The Email control exposes `type="email"`; another type is the non-conforming observation.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: FORM-EMAIL-TYPE-V01; non-conforming observation FORM-EMAIL-TYPE-I01
- Source Code Reference: Not Applicable - Black-box testing
- Notes and Assumptions: The invalid partition is an observable non-conformance, not a state forced by the tester.

## FR01-DT-017

- Test Case ID: FR01-DT-017
- Feature ID: FR-01
- Test Case Title: Password masking conformance
- Technique: Domain Testing
- Objective: Verify Password uses a password control and masks entered text.
- Requirement or Rule Reference: FR01-SF03
- Test Basis Reference: requirement-analysis.md shared/UI rule; domain-testing.md corresponding FORM/CONFIRM partition
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: Password value `ValidPass1!`
- Steps:
  1. Open `/register` as a guest.
  2. Inspect the relevant public form control or label.
  3. Enter `ValidPass1!` in Password and observe its display.
- Expected Result: The Password control exposes `type="password"` and entered characters are not shown in clear text.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: FORM-PASSWORD-TYPE-V01; non-conforming observation FORM-PASSWORD-TYPE-I01
- Source Code Reference: Not Applicable - Black-box testing
- Notes and Assumptions: The invalid partition is an observable non-conformance, not a state forced by the tester.

## FR01-DT-018

- Test Case ID: FR01-DT-018
- Feature ID: FR-01
- Test Case Title: Error placement conformance
- Technique: Domain Testing
- Objective: Verify a displayed registration error is above the submit control.
- Requirement or Rule Reference: FR01-SF04
- Test Basis Reference: requirement-analysis.md shared/UI rule; domain-testing.md corresponding FORM/CONFIRM partition
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: Email `not-an-email`; other inputs nominal
- Steps:
  1. Open `/register` as a guest.
  2. Enter nominal values except Email `not-an-email`.
  3. Activate the registration submit control.
  4. Observe whether registration completes, any displayed validation error, and navigation.
- Expected Result: A validation error is displayed above, not below, the submit control; exact text is unspecified.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: FORM-ERROR-PLACEMENT-V01; non-conforming observation FORM-ERROR-PLACEMENT-I01
- Source Code Reference: Not Applicable - Black-box testing
- Notes and Assumptions: The invalid partition is an observable non-conformance, not a state forced by the tester.

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
- Expected Result: The registration request is rejected and does not complete successfully. Exact invalid status and response body require clarification.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: API-REQUEST-I01; NAME-PRESENCE-I01; VALIDATION-REJECTION-V01
- Source Code Reference: Not Applicable - Black-box testing
- Notes and Assumptions: No Confirm Password property is added; invalid response details are undocumented.

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
- Expected Result: The registration request is rejected and does not complete successfully. Exact invalid status and response body require clarification.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: API-REQUEST-I02; EMAIL-PRESENCE-I01; VALIDATION-REJECTION-V01
- Source Code Reference: Not Applicable - Black-box testing
- Notes and Assumptions: No Confirm Password property is added; invalid response details are undocumented.

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
- Expected Result: The registration request is rejected and does not complete successfully. Exact invalid status and response body require clarification.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: API-REQUEST-I03; PASSWORD-PRESENCE-I01; VALIDATION-REJECTION-V01
- Source Code Reference: Not Applicable - Black-box testing
- Notes and Assumptions: No Confirm Password property is added; invalid response details are undocumented.

## Boundary Value Analysis Test Cases

## FR01-BVA-001

- Test Case ID: FR01-BVA-001
- Feature ID: FR-01
- Test Case Title: UI password length 7 characters
- Technique: Boundary Value Analysis
- Objective: Verify the UI classification at FR01-PASSWORD-LENGTH-B01 using an exactly 7-character password.
- Requirement or Rule Reference: FR01-R06; FR01-R07-R10
- Test Basis Reference: boundary-value-analysis.md - FR01-PASSWORD-LENGTH-B01
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: Name `Nguyen Van A`; controlled unused email `bva.ui.001@example.com`; Password and Confirm Password `Abcd1!x` (7 characters).
- Steps:
  1. Open `/register` as a guest.
  2. Enter Name `Nguyen Van A`, unused Email `bva.ui.001@example.com`, Password and Confirm Password `Abcd1!x`.
  3. Activate the registration submit control.
  4. Observe whether registration completes, any displayed validation error, and navigation.
- Expected Result: Registration is rejected because the password is shorter than 8 characters; it does not complete. Exact error text or API failure status/body is unspecified.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: FR01-PASSWORD-LENGTH-B01
- Source Code Reference: Not Applicable - Black-box testing
- Notes and Assumptions: All character-class rules remain valid. Execution depends on Confirm Password control availability. This case is distinct by surface and boundary position.

## FR01-BVA-002

- Test Case ID: FR01-BVA-002
- Feature ID: FR-01
- Test Case Title: UI password length 8 characters
- Technique: Boundary Value Analysis
- Objective: Verify the UI classification at FR01-PASSWORD-LENGTH-B02 using an exactly 8-character password.
- Requirement or Rule Reference: FR01-R06; FR01-R07-R10
- Test Basis Reference: boundary-value-analysis.md - FR01-PASSWORD-LENGTH-B02
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: Name `Nguyen Van A`; controlled unused email `bva.ui.002@example.com`; Password and Confirm Password `Abcd1!xy` (8 characters).
- Steps:
  1. Open `/register` as a guest.
  2. Enter Name `Nguyen Van A`, unused Email `bva.ui.002@example.com`, Password and Confirm Password `Abcd1!xy`.
  3. Activate the registration submit control.
  4. Observe whether registration completes, any displayed validation error, and navigation.
- Expected Result: Registration completes successfully and navigates to the Login page; no exact URL, timing, or success text is asserted.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: FR01-PASSWORD-LENGTH-B02
- Source Code Reference: Not Applicable - Black-box testing
- Notes and Assumptions: All character-class rules remain valid. Execution depends on Confirm Password control availability. This case is distinct by surface and boundary position.

## FR01-BVA-003

- Test Case ID: FR01-BVA-003
- Feature ID: FR-01
- Test Case Title: UI password length 9 characters
- Technique: Boundary Value Analysis
- Objective: Verify the UI classification at FR01-PASSWORD-LENGTH-B03 using an exactly 9-character password.
- Requirement or Rule Reference: FR01-R06; FR01-R07-R10
- Test Basis Reference: boundary-value-analysis.md - FR01-PASSWORD-LENGTH-B03
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: Name `Nguyen Van A`; controlled unused email `bva.ui.003@example.com`; Password and Confirm Password `Abcd1!xyz` (9 characters).
- Steps:
  1. Open `/register` as a guest.
  2. Enter Name `Nguyen Van A`, unused Email `bva.ui.003@example.com`, Password and Confirm Password `Abcd1!xyz`.
  3. Activate the registration submit control.
  4. Observe whether registration completes, any displayed validation error, and navigation.
- Expected Result: Registration completes successfully and navigates to the Login page; no exact URL, timing, or success text is asserted.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: FR01-PASSWORD-LENGTH-B03
- Source Code Reference: Not Applicable - Black-box testing
- Notes and Assumptions: All character-class rules remain valid. Execution depends on Confirm Password control availability. This case is distinct by surface and boundary position.

## FR01-BVA-004

- Test Case ID: FR01-BVA-004
- Feature ID: FR-01
- Test Case Title: UI password length 11 characters
- Technique: Boundary Value Analysis
- Objective: Verify the UI classification at FR01-PASSWORD-LENGTH-N01 using an exactly 11-character password.
- Requirement or Rule Reference: FR01-R06; FR01-R07-R10
- Test Basis Reference: boundary-value-analysis.md - FR01-PASSWORD-LENGTH-N01
- Preconditions: Application is available at `/register`; actor is guest/unauthenticated; specified email state is controlled; Confirm Password control availability is required except in the control-conformance case.
- Test Data: Name `Nguyen Van A`; controlled unused email `bva.ui.004@example.com`; Password and Confirm Password `ValidPass1!` (11 characters).
- Steps:
  1. Open `/register` as a guest.
  2. Enter Name `Nguyen Van A`, unused Email `bva.ui.004@example.com`, Password and Confirm Password `ValidPass1!`.
  3. Activate the registration submit control.
  4. Observe whether registration completes, any displayed validation error, and navigation.
- Expected Result: Registration completes successfully and navigates to the Login page; no exact URL, timing, or success text is asserted.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: FR01-PASSWORD-LENGTH-N01
- Source Code Reference: Not Applicable - Black-box testing
- Notes and Assumptions: All character-class rules remain valid. Execution depends on Confirm Password control availability. This case is distinct by surface and boundary position.

## FR01-BVA-005

- Test Case ID: FR01-BVA-005
- Feature ID: FR-01
- Test Case Title: API password length 7 characters
- Technique: Boundary Value Analysis
- Objective: Verify the API classification at FR01-PASSWORD-LENGTH-B01 using an exactly 7-character password.
- Requirement or Rule Reference: FR01-R06; FR01-R07-R10
- Test Basis Reference: boundary-value-analysis.md - FR01-PASSWORD-LENGTH-B01
- Preconditions: Public API is available at `http://localhost:3000`; actor is unauthenticated; specified email state is controlled.
- Test Data: `{"name":"Nguyen Van A","email":"bva.api.005@example.com","password":"Abcd1!x"}`; email controlled unused.
- Steps:
  1. Prepare a JSON request body: `{"name":"Nguyen Van A","email":"bva.api.005@example.com","password":"Abcd1!x"}`.
  2. Send `POST http://localhost:3000/api/register`.
  3. Observe the public HTTP status and JSON response.
- Expected Result: Registration is rejected because the password is shorter than 8 characters; it does not complete. Exact error text or API failure status/body is unspecified.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: FR01-PASSWORD-LENGTH-B01
- Source Code Reference: Not Applicable - Black-box testing
- Notes and Assumptions: All character-class rules remain valid. Confirm Password is omitted from the API body per contract. This case is distinct by surface and boundary position.

## FR01-BVA-006

- Test Case ID: FR01-BVA-006
- Feature ID: FR-01
- Test Case Title: API password length 8 characters
- Technique: Boundary Value Analysis
- Objective: Verify the API classification at FR01-PASSWORD-LENGTH-B02 using an exactly 8-character password.
- Requirement or Rule Reference: FR01-R06; FR01-R07-R10
- Test Basis Reference: boundary-value-analysis.md - FR01-PASSWORD-LENGTH-B02
- Preconditions: Public API is available at `http://localhost:3000`; actor is unauthenticated; specified email state is controlled.
- Test Data: `{"name":"Nguyen Van A","email":"bva.api.006@example.com","password":"Abcd1!xy"}`; email controlled unused.
- Steps:
  1. Prepare a JSON request body: `{"name":"Nguyen Van A","email":"bva.api.006@example.com","password":"Abcd1!xy"}`.
  2. Send `POST http://localhost:3000/api/register`.
  3. Observe the public HTTP status and JSON response.
- Expected Result: The response is `200 OK` JSON containing the documented success message and an `id` value.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: FR01-PASSWORD-LENGTH-B02
- Source Code Reference: Not Applicable - Black-box testing
- Notes and Assumptions: All character-class rules remain valid. Confirm Password is omitted from the API body per contract. This case is distinct by surface and boundary position.

## FR01-BVA-007

- Test Case ID: FR01-BVA-007
- Feature ID: FR-01
- Test Case Title: API password length 9 characters
- Technique: Boundary Value Analysis
- Objective: Verify the API classification at FR01-PASSWORD-LENGTH-B03 using an exactly 9-character password.
- Requirement or Rule Reference: FR01-R06; FR01-R07-R10
- Test Basis Reference: boundary-value-analysis.md - FR01-PASSWORD-LENGTH-B03
- Preconditions: Public API is available at `http://localhost:3000`; actor is unauthenticated; specified email state is controlled.
- Test Data: `{"name":"Nguyen Van A","email":"bva.api.007@example.com","password":"Abcd1!xyz"}`; email controlled unused.
- Steps:
  1. Prepare a JSON request body: `{"name":"Nguyen Van A","email":"bva.api.007@example.com","password":"Abcd1!xyz"}`.
  2. Send `POST http://localhost:3000/api/register`.
  3. Observe the public HTTP status and JSON response.
- Expected Result: The response is `200 OK` JSON containing the documented success message and an `id` value.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: FR01-PASSWORD-LENGTH-B03
- Source Code Reference: Not Applicable - Black-box testing
- Notes and Assumptions: All character-class rules remain valid. Confirm Password is omitted from the API body per contract. This case is distinct by surface and boundary position.

## FR01-BVA-008

- Test Case ID: FR01-BVA-008
- Feature ID: FR-01
- Test Case Title: API password length 11 characters
- Technique: Boundary Value Analysis
- Objective: Verify the API classification at FR01-PASSWORD-LENGTH-N01 using an exactly 11-character password.
- Requirement or Rule Reference: FR01-R06; FR01-R07-R10
- Test Basis Reference: boundary-value-analysis.md - FR01-PASSWORD-LENGTH-N01
- Preconditions: Public API is available at `http://localhost:3000`; actor is unauthenticated; specified email state is controlled.
- Test Data: `{"name":"Nguyen Van A","email":"bva.api.008@example.com","password":"ValidPass1!"}`; email controlled unused.
- Steps:
  1. Prepare a JSON request body: `{"name":"Nguyen Van A","email":"bva.api.008@example.com","password":"ValidPass1!"}`.
  2. Send `POST http://localhost:3000/api/register`.
  3. Observe the public HTTP status and JSON response.
- Expected Result: The response is `200 OK` JSON containing the documented success message and an `id` value.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: FR01-PASSWORD-LENGTH-N01
- Source Code Reference: Not Applicable - Black-box testing
- Notes and Assumptions: All character-class rules remain valid. Confirm Password is omitted from the API body per contract. This case is distinct by surface and boundary position.

## Exploratory Backlog

| Candidate ID | Input or Observation | Missing Oracle | Clarification Required | Reason Excluded from Normative Coverage |
| --- | --- | --- | --- | --- |
| NAME-WHITESPACE-A01 | Full name `"   "` | Whether whitespace counts as provided | Trimming/whitespace policy | FR01-R01 does not define it. |
| EMAIL-CASE-A01 | Case variants of one email | Whether variants are the same identity | Case/normalization policy | FR01-R05 does not define it. |
| PASSWORD-SPECIAL-A01 | Password containing unlisted `#` | Whether `#` qualifies | Whether special list is exhaustive | FR01-R10 is ambiguous. |
| FORM-STEP-INDICATOR-A01 | Observe step count/indicator | Whether registration is multi-step | Authoritative registration step model | SF05 is conditional. |

## Preliminary Coverage Summary

| Rule ID | Partition or Boundary ID | Technique | Covering Test Case ID | Surface | Coverage Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| FR01-R01 | NAME-PRESENCE-V01 / I01 | Domain Testing | FR01-DT-001, 003, 019 | UI/API | Covered | Approved normative partition/boundary. |
| FR01-R02 | EMAIL-PRESENCE-V01 / I01 | Domain Testing | FR01-DT-001, 004, 020 | UI/API | Covered | Approved normative partition/boundary. |
| FR01-R04 | EMAIL-FORMAT-V01 / I01 | Domain Testing | FR01-DT-001, 005 | UI | Covered | Approved normative partition/boundary. |
| FR01-R05 | EMAIL-UNIQUENESS-V01 / I01 | Domain Testing | FR01-DT-001, 006 | UI | Covered | Approved normative partition/boundary. |
| FR01-R03 | PASSWORD-PRESENCE-V01 / I01 | Domain Testing | FR01-DT-001, 007, 021 | UI/API | Covered | Approved normative partition/boundary. |
| FR01-R06 | PASSWORD-LENGTH-V01 / PASSWORD-LENGTH-I01 | DT + BVA | FR01-DT-001; FR01-BVA-001-008 | UI/API | Covered | Approved normative partition/boundary. |
| FR01-R07 | PASSWORD-UPPERCASE-V01 / I01 | Domain Testing | FR01-DT-001, 008 | UI | Covered | Approved normative partition/boundary. |
| FR01-R08 | PASSWORD-LOWERCASE-V01 / I01 | Domain Testing | FR01-DT-001, 009 | UI | Covered | Approved normative partition/boundary. |
| FR01-R09 | PASSWORD-DIGIT-V01 / I01 | Domain Testing | FR01-DT-001, 010 | UI | Covered | Approved normative partition/boundary. |
| FR01-R10 | PASSWORD-SPECIAL-V01 / I01 | Domain Testing | FR01-DT-001, 011 | UI | Covered | Approved normative partition/boundary. |
| FR01-R11 | CONFIRM-CONTROL-V01 / I01 | Domain Testing | FR01-DT-012 | UI | Covered | Approved normative partition/boundary. |
| FR01-R11 | CONFIRM-VALUE-V01 / I01 | Domain Testing | FR01-DT-001, 013 | UI | Covered | Approved normative partition/boundary. |
| FR01-R12 | CONFIRM-MATCH-V01 / I01 | Domain Testing | FR01-DT-001, 014 | UI | Covered | Approved normative partition/boundary. |
| FR01-R13/R14 | REGISTRATION-COMPLETE-V01; REDIRECT-SUCCESS-V01 | Domain Testing | FR01-DT-001 | UI | Covered | Approved normative partition/boundary. |
| API01-API05 | API-REQUEST-V01/I01/I02/I03; API-SUCCESS-V01 | Domain Testing | FR01-DT-002, 019-021 | API | Covered | Approved normative partition/boundary. |
| SF01 | FORM-REQUIRED-MARKER-V01/I01 | Domain Testing | FR01-DT-015 | UI | Covered | Approved normative partition/boundary. |
| SF02 | FORM-EMAIL-TYPE-V01/I01 | Domain Testing | FR01-DT-016 | UI | Covered | Approved normative partition/boundary. |
| SF03 | FORM-PASSWORD-TYPE-V01/I01 | Domain Testing | FR01-DT-017 | UI | Covered | Approved normative partition/boundary. |
| SF04 | FORM-ERROR-PLACEMENT-V01/I01 | Domain Testing | FR01-DT-018 | UI | Covered | Approved normative partition/boundary. |
| R01-R12 | VALIDATION-REJECTION-V01 | Domain Testing | FR01-DT-003-014, 019-021 | UI/API | Covered | Approved normative partition/boundary. |
| Feature Intake | ACTOR-GUEST-V01 | Domain Testing | All cases | UI/API | Covered | Approved normative partition/boundary. |
| FR01-R06 | FR01-PASSWORD-LENGTH-B01/B02/B03/N01 | BVA | FR01-BVA-001-008 | UI/API | Covered | Approved normative partition/boundary. |
| FR01 ambiguities | Four A01 candidates | Exploratory | None | UI/API | Exploratory - No Oracle | Listed in backlog; excluded from normative coverage. |

## Design Gaps and Assumptions

- Controlled email state must be prepared without treating hidden data as an oracle.
- UI BVA execution depends on the approved Confirm Password control being available.
- The API contract has no Confirm Password property, so none is added.
- Invalid API outcomes use rejection/non-completion only; exact status/body needs clarification.
- No normative tests cover undocumented whitespace, case normalization, unlisted symbols, step count, maximum lengths, Unicode semantics, exact Login URL/timing, or UI message text.
- Each case’s derivation is stated by its exact rule, test-basis, partition/boundary, representative data, nominal dependencies, surface, and expected observable outcome.

## Human Review - Phase 5

- Reviewer:
- Review Date and Time:
- Corrections Made:
- Missing Cases Added:
- Duplicate Cases Removed:
- Incorrect Cases Removed:
- Status: Pending
- Approved for Validation: No
- Approved for Traceability and Quality Review: No
- Approved for Test Execution: No
