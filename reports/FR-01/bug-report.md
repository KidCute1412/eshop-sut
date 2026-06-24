# Bug Report - FR-01 Account Registration

## Summary

| Bug ID       | Title                                                               | Severity | Related Test Cases                            | GitHub Issue |
| ------------ | ------------------------------------------------------------------- | -------- | --------------------------------------------- | ------------ |
| BUG-FR01-001 | Registration UI is missing Confirm Password                         | Medium   | FR01-DT-012                                   | Pending      |
| BUG-FR01-002 | Required registration labels are missing `*` markers                | Low      | FR01-DT-015                                   | Pending      |
| BUG-FR01-003 | Email input uses `type="text"` instead of `type="email"`            | Low      | FR01-DT-016                                   | Pending      |
| BUG-FR01-004 | Registration API accepts requests with missing required properties  | High     | FR01-DT-019, FR01-DT-020, FR01-DT-021         | Pending      |
| BUG-FR01-005 | Registration API accepts malformed email addresses                  | Medium   | FR01-DT-023                                   | Pending      |
| BUG-FR01-006 | Registration API accepts duplicate email addresses                  | High     | FR01-DT-024                                   | Pending      |
| BUG-FR01-007 | Registration API accepts passwords that violate the strength policy | High     | FR01-DT-025 through FR01-DT-029; FR01-BVA-005 | Pending      |

## BUG-FR01-001: Registration UI Is Missing Confirm Password

- Status: Confirmed
- Severity: Medium
- Feature: FR-01 Account Registration
- Requirement: FR01-R11
- Related Test Case: [FR01-DT-012](./test-cases.md#fr01-dt-012)

- URL: `http://localhost:5173/register`

### Description

The registration form does not provide the required Confirm Password label or input control. This also blocks UI test cases that require a matching confirmation value.

### Steps to Reproduce

1. Open `http://localhost:5173/register` as a guest.
2. Inspect the registration form fields.

### Expected Result

The form displays a Confirm Password input and rejects submission when Password and Confirm Password do not match.

### Actual Result

No Confirm Password label or input control is displayed.

### Evidence

- [FR01-DT-012 screenshot](./evidence/FR01-DT-012.png)

### GitHub Issue

- Pending - attach the screenshot above when creating the issue.

## BUG-FR01-002: Required Registration Labels Are Missing Asterisk Markers

- Status: Confirmed
- Severity: Low
- Feature: FR-01 Account Registration
- Requirement: FR01-SF01
- Related Test Case: [FR01-DT-015](./test-cases.md#fr01-dt-015)
- URL: `http://localhost:5173/register`

### Description

The Full name, Email, and Password fields are required, but their labels do not display adjacent `*` markers.

### Steps to Reproduce

1. Open `http://localhost:5173/register` as a guest.
2. Inspect the Full name, Email, and Password labels.

### Expected Result

Every required field label displays an adjacent `*` marker.

### Actual Result

The required labels are displayed without adjacent `*` markers.

### Evidence

- [FR01-DT-015 screenshot](./evidence/FR01-DT-015.png)

### GitHub Issue

- Pending - attach the screenshot above when creating the issue.

## BUG-FR01-003: Email Input Uses the Wrong HTML Type

- Status: Confirmed
- Severity: Low
- Feature: FR-01 Account Registration
- Requirement: FR01-SF02
- Related Test Case: [FR01-DT-016](./test-cases.md#fr01-dt-016)
- URL: `http://localhost:5173/register`

### Description

The Email input exposes `type="text"` instead of the required `type="email"`.

### Steps to Reproduce

1. Open `http://localhost:5173/register` as a guest.
2. Inspect the Email input using browser developer tools or Playwright.
3. Read its `type` attribute.

### Expected Result

The Email input exposes `type="email"`.

### Actual Result

The Email input exposes `type="text"`.

### Evidence

- [FR01-DT-016 screenshot](./evidence/FR01-DT-016.png)

### GitHub Issue

- Pending - attach evidence that visibly shows the input attribute.

## BUG-FR01-004: Registration API Accepts Missing Required Properties

- Status: Confirmed
- Severity: High
- Feature: FR-01 Account Registration
- Requirements: FR01-R01, FR01-R02, FR01-R03, FR01-API02, FR01-API03, FR01-API04
- Related Test Cases: [FR01-DT-019](./test-cases.md#fr01-dt-019), [FR01-DT-020](./test-cases.md#fr01-dt-020), [FR01-DT-021](./test-cases.md#fr01-dt-021)
- Endpoint: `POST http://localhost:3000/api/register`

### Description

The API reports successful registration when `name`, `email`, or `password` is omitted from the request body.

### Steps to Reproduce

1. Send `POST http://localhost:3000/api/register` with one of the following bodies:

```json
{ "email": "fr01.missing.name@example.com", "password": "ValidPass1!" }
```

```json
{ "name": "Nguyen Van A", "password": "ValidPass1!" }
```

```json
{ "name": "Nguyen Van A", "email": "fr01.missing.password@example.com" }
```

2. Observe the HTTP status and JSON response.

### Expected Result

Each request is rejected because a documented required property is missing. The exact failure status and response body are unspecified.

### Actual Result

Each request returned `200 OK` with the documented success message and an `id` value.

### Evidence

- [Missing name](./evidence/FR01-DT-019.png)
- [Missing email](./evidence/FR01-DT-020.png)
- [Missing password](./evidence/FR01-DT-021.png)

### GitHub Issue

- Pending - attach all three API screenshots to the issue.

## BUG-FR01-005: Registration API Accepts Malformed Email Addresses

- Status: Confirmed
- Severity: Medium
- Feature: FR-01 Account Registration
- Requirement: FR01-R04
- Related Test Case: [FR01-DT-023](./test-cases.md#fr01-dt-023)
- Endpoint: `POST http://localhost:3000/api/register`

### Steps to Reproduce

1. Send the following request:

```json
{
  "name": "Nguyen Van A",
  "email": "fr01-invalid-email",
  "password": "ValidPass1!"
}
```

2. Observe the HTTP status and JSON response.

### Expected Result

The API rejects the malformed email address. The exact failure status and response body are unspecified.

### Actual Result

The API returned `200 OK` with the documented success message and an `id` value.

### Evidence

- [FR01-DT-023 screenshot](./evidence/FR01-DT-023.png)

### GitHub Issue

- Pending - attach the screenshot above when creating the issue.

## BUG-FR01-006: Registration API Accepts Duplicate Email Addresses

- Status: Confirmed
- Severity: High
- Feature: FR-01 Account Registration
- Requirement: FR01-R05
- Related Test Case: [FR01-DT-024](./test-cases.md#fr01-dt-024)
- Endpoint: `POST http://localhost:3000/api/register`

### Preconditions

`registered@example.com` already exists in the controlled test environment.

### Steps to Reproduce

1. Send the following request:

```json
{
  "name": "Nguyen Van A",
  "email": "registered@example.com",
  "password": "ValidPass1!"
}
```

2. Observe the HTTP status and JSON response.

### Expected Result

The API rejects the duplicate email address. The exact failure status and response body are unspecified.

### Actual Result

The API returned `200 OK` with the documented success message and an `id` value.

### Evidence

- [FR01-DT-024 screenshot](./evidence/FR01-DT-024.png)

### GitHub Issue

- Pending - attach the screenshot above and evidence that the email existed before execution.

## BUG-FR01-007: Registration API Accepts Weak Passwords

- Status: Confirmed
- Severity: High
- Feature: FR-01 Account Registration
- Requirements: FR01-R06, FR01-R07, FR01-R08, FR01-R09, FR01-R10
- Related Test Cases: [FR01-DT-025](./test-cases.md#fr01-dt-025) through [FR01-DT-029](./test-cases.md#fr01-dt-029), [FR01-BVA-005](./test-cases.md#fr01-bva-005)
- Endpoint: `POST http://localhost:3000/api/register`

### Description

The API accepts passwords that violate the documented minimum length and required character classes.

### Tested Variants

| Test Case    | Invalid Password | Violated Rule                    | Actual Result                  |
| ------------ | ---------------- | -------------------------------- | ------------------------------ |
| FR01-DT-025  | `Ab1!`           | Fewer than 8 characters          | `200 OK` with success response |
| FR01-DT-026  | `validpass1!`    | Missing uppercase                | `200 OK` with success response |
| FR01-DT-027  | `VALIDPASS1!`    | Missing lowercase                | `200 OK` with success response |
| FR01-DT-028  | `ValidPass!`     | Missing digit                    | `200 OK` with success response |
| FR01-DT-029  | `ValidPass12`    | Missing special character        | `200 OK` with success response |
| FR01-BVA-005 | `Abcd1!x`        | Seven-character `min-1` boundary | `200 OK` with success response |

### Steps to Reproduce

1. Prepare a complete registration request with a fresh controlled email.
2. Use one invalid password from the table above.
3. Send `POST http://localhost:3000/api/register`.
4. Observe the HTTP status and JSON response.

### Expected Result

The API rejects every password that violates the documented password policy. Exact failure statuses and response bodies are unspecified.

### Actual Result

Every tested password was accepted with `200 OK`, the documented success message, and an `id` value.

### Evidence

- [Short password](./evidence/FR01-DT-025.png)
- [Missing uppercase](./evidence/FR01-DT-026.png)
- [Missing lowercase](./evidence/FR01-DT-027.png)
- [Missing digit](./evidence/FR01-DT-028.png)
- [Missing special character](./evidence/FR01-DT-029.png)
- [Seven-character boundary](./evidence/FR01-BVA-005.png)

### GitHub Issue

- Pending - attach all relevant API screenshots to the issue.
