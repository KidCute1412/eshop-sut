# Test Design Report - Mini API Testing

- Student: Trương Lý Khải
- Class: 23KTPM3
- API tested: POST /api/login

## 1. Prompt dùng để sinh test case bằng AI

Prompt:

Generate a structured test case table for the API POST /api/login of the EShop backend. The API accepts JSON body with fields email and password and returns 200 with a token and user for valid credentials, 401 for invalid credentials, and 403 for account lockout. Create at least 12 test cases covering valid, invalid, missing, boundary, security, and schema-validation scenarios. Return a table with columns: tc_id, input, expected status, expected fields, rationale.

## 2. AI output rút gọn

| tc_id | input | expected status | expected fields | rationale |
|---|---|---:|---|---|
| TC01 | Valid existing email and correct password | 200 | token, user | Successful login should return JWT and user profile. |
| TC02 | Correct email, wrong password | 401 | error | Wrong password must be rejected. |
| TC03 | Unknown email, valid password | 401 | error | Unknown email should fail auth. |
| TC04 | Missing email field | 401 | error | Missing required input should be rejected. |
| TC05 | Missing password field | 401 | error | Missing required input should be rejected. |
| TC06 | Empty email string | 401 | error | Empty string is invalid input. |
| TC07 | Empty password string | 401 | error | Empty password should not authenticate. |
| TC08 | Malformed email | 401 | error | Invalid format should be handled. |
| TC09 | SQL injection in email | 401 | error | Prevent injection via parameterized query. |
| TC10 | SQL injection in password | 401 | error | Prevent injection via parameterized query. |
| TC11 | Repeated invalid attempts | 403 | error | Account should be locked after repeated failures. |
| TC12 | Response header content-type | 200/401/403 | Content-Type includes application/json | API should respond with JSON according to contract. |

## 3. Bảng audit

| TC | Nhãn | Nhận xét / chỉnh sửa |
|---|---|---|
| TC01 | VALID | Positive case is valid because seeded user exists. |
| TC02 | VALID | Wrong password path is implemented and returns 401. |
| TC03 | VALID | Unknown email returns 401. |
| TC04 | VALID | Missing email is properly rejected. |
| TC05 | VALID | Missing password is properly rejected. |
| TC06 | VALID | Empty email is a useful edge case. |
| TC07 | VALID | Empty password is a useful edge case. |
| TC08 | VALID | Malformed email is a valid negative input. |
| TC09 | VALID | SQL injection attempt is relevant for security. |
| TC10 | VALID | SQL injection attempt is relevant for security. |
| TC11 | INCOMPLETE | This requires repeated attempts to verify lockout state. |
| TC12 | VALID | Response header check is useful and was included in assertions. |

## 4. Test case tự bổ sung (extend)

### Extend 1: repeated invalid login leading to lockout
- Input: valid email with wrong password repeated multiple times.
- Expected status: 401 first, then 403 after lockout.
- Why added: AI did not explicitly capture the multi-step lockout flow.

### Extend 2: header presence check
- Input: valid credentials plus X-Student-Id header.
- Expected status: 200.
- Why added: The exercise specifically requires the student header in requests.

## 5. Bảng Postman features đã dùng

| Feature | Có / Không | Ghi chú |
|---|---|---|
| Collections | Có | Dùng collection để lưu request POST /api/login. |
| Environment variables | Có | Dùng baseUrl và studentId. |
| Collection variables | Không | Không cần cho bài tập này. |
| Pre-request scripts | Có | Thêm X-Student-Id vào header trước khi gửi request. |
| Test scripts (assertions) | Có | Kiểm tra status code, Content-Type và cấu trúc response. |
| Data-driven runs | Có | Dùng iteration data file cho 5 lần chạy. |
| Newman CLI | Có | Chạy collection bằng Newman để tạo report JSON. |
| Monitors | Không | Không dùng trong bài này. |
| Mock servers | Không | Không dùng trong bài này. |
| Workspaces | Không | Không dùng trong bài này. |
