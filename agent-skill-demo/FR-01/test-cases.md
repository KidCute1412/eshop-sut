# Test Cases - FR-01 Account registration

## FR01-DT-001

- Test Case ID: FR01-DT-001
- Technique: Domain Testing
- Objective: Verify that a guest can register with valid name, unique valid email, strong password, and matching confirmation.
- Requirement or Rule Reference: R-FR01-01, R-FR01-02, R-FR01-03, R-FR01-04, R-FR01-05
- Preconditions: User is logged out; email `valid.fr01@example.com` does not already exist.
- Test Data: Name `Nguyen Van A`; Email `valid.fr01@example.com`; Password `Password1!`; Confirm Password `Password1!`.
- Steps: Open registration page; enter all test data; submit the form.
- Expected Result: The account is created, the user is redirected to the login page, and no validation error is shown.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: Valid partitions for required name, unique email, strong password, matching confirmation, successful outcome.
- Source Code Reference: `README.md` FR-01; `api_specification.md` 1.1; `frontend-web/src/pages/Register.jsx`; `backend/server.js` `/api/register`.
- Notes and Assumptions: Source inspection suggests the web regex may reject this valid password because it lacks whitespace; this test must be executed before reporting a bug.

## FR01-DT-002

- Test Case ID: FR01-DT-002
- Technique: Domain Testing
- Objective: Verify rejection of malformed email format.
- Requirement or Rule Reference: R-FR01-02
- Preconditions: User is logged out.
- Test Data: Name `Nguyen Van A`; Email `not-an-email`; Password `Password1!`; Confirm Password `Password1!`.
- Steps: Open registration page; enter test data; submit the form.
- Expected Result: Registration is rejected with an email-format validation message and no account is created.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: Invalid email-format partition.
- Source Code Reference: `README.md` FR-01; `frontend-web/src/pages/Register.jsx` email input; `backend/server.js` `/api/register`.
- Notes and Assumptions: Web input is `type="text"` and backend has no email validation by source inspection.

## FR01-DT-003

- Test Case ID: FR01-DT-003
- Technique: Domain Testing
- Objective: Verify rejection of duplicate email.
- Requirement or Rule Reference: R-FR01-02
- Preconditions: User is logged out; seed data contains `test@eshop.com`.
- Test Data: Name `Another User`; Email `test@eshop.com`; Password `Password1!`; Confirm Password `Password1!`.
- Steps: Open registration page; enter test data; submit the form.
- Expected Result: Registration is rejected with a duplicate-email message and no second account is created for the same email.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: Invalid duplicate-email partition.
- Source Code Reference: `README.md` FR-01; `backend/database.js` seed users and `CREATE TABLE users`; `backend/server.js` `/api/register`.
- Notes and Assumptions: Database source shows no unique constraint for `users.email`.

## FR01-DT-004

- Test Case ID: FR01-DT-004
- Technique: Domain Testing
- Objective: Verify rejection when confirm password does not match password.
- Requirement or Rule Reference: R-FR01-04
- Preconditions: User is logged out.
- Test Data: Name `Nguyen Van A`; Email `mismatch.fr01@example.com`; Password `Password1!`; Confirm Password `Password2!`.
- Steps: Open registration page; enter test data; submit the form.
- Expected Result: Registration is rejected with a password-confirmation mismatch message and no account is created.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: Invalid password-confirmation mismatch partition.
- Source Code Reference: `README.md` FR-01; `frontend-web/src/pages/Register.jsx`; `api_specification.md` 1.1.
- Notes and Assumptions: Source inspection shows the web form has no confirm-password field.

## FR01-DT-005

- Test Case ID: FR01-DT-005
- Technique: Domain Testing
- Objective: Verify rejection of a password missing an allowed special character.
- Requirement or Rule Reference: R-FR01-03
- Preconditions: User is logged out.
- Test Data: Name `Nguyen Van A`; Email `nospecial.fr01@example.com`; Password `Password12`; Confirm Password `Password12`.
- Steps: Open registration page; enter test data; submit the form.
- Expected Result: Registration is rejected with a password-complexity message and no account is created.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: Invalid partition missing allowed special character.
- Source Code Reference: `README.md` FR-01; `frontend-web/src/pages/Register.jsx`.
- Notes and Assumptions: Other password rules are satisfied so the missing special character is isolated.

## FR01-BVA-001

- Test Case ID: FR01-BVA-001
- Technique: Boundary Value Analysis
- Objective: Verify password length just below the minimum is rejected.
- Requirement or Rule Reference: R-FR01-03
- Preconditions: User is logged out.
- Test Data: Name `Nguyen Van A`; Email `pw7.fr01@example.com`; Password `Aa1!xyz` with length 7; Confirm Password `Aa1!xyz`.
- Steps: Open registration page; enter test data; submit the form.
- Expected Result: Registration is rejected because password length is below the 8-character minimum.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: Password length boundary min-1.
- Source Code Reference: `README.md` FR-01; `frontend-web/src/pages/Register.jsx`; `backend/server.js` `/api/register`.
- Notes and Assumptions: Test isolates length while satisfying uppercase/lowercase/digit/special composition.

## FR01-BVA-002

- Test Case ID: FR01-BVA-002
- Technique: Boundary Value Analysis
- Objective: Verify password length at the minimum is accepted when all complexity rules are satisfied.
- Requirement or Rule Reference: R-FR01-03
- Preconditions: User is logged out; email `pw8.fr01@example.com` does not already exist.
- Test Data: Name `Nguyen Van A`; Email `pw8.fr01@example.com`; Password `Aa1!xyzz` with length 8; Confirm Password `Aa1!xyzz`.
- Steps: Open registration page; enter test data; submit the form.
- Expected Result: Password length is accepted as valid, and registration proceeds if all other inputs are valid.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: Password length boundary min.
- Source Code Reference: `README.md` FR-01; `frontend-web/src/pages/Register.jsx`; `backend/server.js` `/api/register`.
- Notes and Assumptions: Source inspection suggests the current frontend regex may reject this valid value because it expects whitespace.

## FR01-BVA-003

- Test Case ID: FR01-BVA-003
- Technique: Boundary Value Analysis
- Objective: Verify password length just above the minimum is accepted when all complexity rules are satisfied.
- Requirement or Rule Reference: R-FR01-03
- Preconditions: User is logged out; email `pw9.fr01@example.com` does not already exist.
- Test Data: Name `Nguyen Van A`; Email `pw9.fr01@example.com`; Password `Aa1!xyzzy` with length 9; Confirm Password `Aa1!xyzzy`.
- Steps: Open registration page; enter test data; submit the form.
- Expected Result: Password length is accepted as valid, and registration proceeds if all other inputs are valid.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: Password length boundary min+1.
- Source Code Reference: `README.md` FR-01; `frontend-web/src/pages/Register.jsx`; `backend/server.js` `/api/register`.
- Notes and Assumptions: This is adjacent to the lower-bound password length.

## FR01-BVA-004

- Test Case ID: FR01-BVA-004
- Technique: Boundary Value Analysis
- Objective: Verify duplicate-email boundary when one existing matching row already exists.
- Requirement or Rule Reference: R-FR01-02
- Preconditions: User is logged out; seed data contains exactly one `test@eshop.com` account before this test.
- Test Data: Name `Duplicate User`; Email `test@eshop.com`; Password `Password1!`; Confirm Password `Password1!`.
- Steps: Open registration page; enter test data; submit the form.
- Expected Result: Registration is rejected because the number of existing accounts with that email is at the invalid boundary of 1.
- Actual Result: Not Executed
- Status: Not Executed
- Evidence: None
- Partition or Boundary Covered: Duplicate email count boundary max valid 0, max+1 invalid 1.
- Source Code Reference: `README.md` FR-01; `backend/database.js`; `backend/server.js` `/api/register`.
- Notes and Assumptions: If case-insensitive uniqueness is required, repeat with case variation after human review.
