# Bug Report - FR-20 Login and Account Lockout (Mobile)

## Confirmed Bugs

## BUG-FR20-001: Mobile Login Required Fields Are Missing Required Markers

- Status: Confirmed
- Severity: Low
- Feature: FR-20 Login and Account Lockout (Mobile)
- Requirement: FR20-FORM01
- Related Test Case: [FR20-DT-008](./test-cases.md#fr20-dt-008)
- Surface: Mobile login screen

### Description

The mobile login screen displays required login fields, but the visible labels do not show `*` markers or an equivalent required-field indicator.

### Preconditions

The mobile app is running in an observable mobile session, and the login screen is open.

### Steps to Reproduce

1. Launch the EShop Mobile app.
2. Open the mobile login screen.
3. Inspect the visible login field labels for Email/Username and Password.
4. Check whether required-field markers are displayed beside the required fields.

### Expected Result

Required fields show `*` or an equivalent visible required-field marker beside the labels.

### Actual Result

The mobile login screen displayed labels for `Username` and `Mật khẩu`, but no visible `*` marker or equivalent required-field indicator was shown beside either required field.

### Evidence

- [FR20-DT-008 screenshot](./evidence/FR20-DT-007.png)

### GitHub Issue

- [GitHub Issue link](https://github.com/KidCute1412/eshop-sut/issues/47#issue-4761342837)

## BUG-FR20-002: Mobile Login Error Message Appears Below the Submit Button

- Status: Confirmed
- Severity: Low
- Feature: FR-20 Login and Account Lockout (Mobile)
- Requirement: FR20-FORM04
- Related Test Case: [FR20-DT-010](./test-cases.md#fr20-dt-010)
- Surface: Mobile login screen

### Description

The mobile login form displays the login failure message below the `Sign In` submit button. The shared form rule requires error messages to appear above the submit button.

### Preconditions

The mobile app is running in an observable mobile session, and the login screen is open.

### Steps to Reproduce

1. Open the mobile login screen.
2. Enter `test@eshop.com` in the email/username field.
3. Leave the password field empty or submit invalid credentials.
4. Tap `Sign In`.
5. Observe the displayed error message position relative to the submit button.

### Expected Result

The login error message appears above the submit button.

### Actual Result

After tapping `Sign In`, the mobile login screen displayed the error message `Đăng nhập thất bại. Vui lòng kiểm tra lại.` below the `Sign In` submit button, not above it.

### Evidence

- [FR20-DT-010 screenshot](./evidence/FR20-DT-010.png)

### GitHub Issue

- [GitHub Issue link](https://github.com/KidCute1412/eshop-sut/issues/48#issue-4761345590)

## BUG-FR20-003: Mobile App Does Not Reach Authenticated State After Valid Login

- Status: Confirmed
- Severity: High
- Feature: FR-20 Login and Account Lockout (Mobile)
- Requirements: FR20-R01, FR20-R08
- Related Test Case: [FR20-DT-012](./test-cases.md#fr20-dt-012)
- Surface: Mobile login screen

### Description

The public login API accepts the same valid credentials and returns a JWT token, but the mobile app does not reach an authenticated state after those valid credentials are submitted through the mobile login screen.

### Preconditions

- The mobile app is running in an observable mobile session.
- Backend API is available.
- User `test@eshop.com` exists and is not locked.
- The same credentials were confirmed through the public login API in `FR20-DT-001`.

### Steps to Reproduce

1. Open the mobile login screen.
2. Enter `test@eshop.com` in the email/username field.
3. Enter correct password `Test1234!`.
4. Tap `Sign In`.
5. Observe whether the mobile app reaches an authenticated state or authenticated screen.

### Expected Result

The mobile app logs in successfully and reaches an authenticated state.

### Actual Result

After entering valid credentials `test@eshop.com` / `Test1234!` and tapping `Sign In`, the mobile app remained on the login screen and displayed the error message `Đăng nhập thất bại. Vui lòng kiểm tra lại.` No authenticated mobile state was reached.

### Evidence

- [FR20-DT-012 screenshot](./evidence/FR20-DT-012.png)

### GitHub Issue

- [GitHub Issue link](https://github.com/KidCute1412/eshop-sut/issues/49#issue-4761347115)
