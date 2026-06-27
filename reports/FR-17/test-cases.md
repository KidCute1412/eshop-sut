# Test Cases - FR-17 Coupon Management CRUD

## Domain Testing Test Cases

## FR17-DT-001

- Test Case ID: FR17-DT-001
- Technique: Domain Testing
- Objective: Verify unauthenticated coupon-list request is rejected.
- Requirement or Rule Reference: FR17-R11, FR17-API01
- Preconditions: Backend API is available at `http://localhost:3000`.
- Test Data: No Authorization header.
- Steps:
  1. Send `GET /api/coupons` without bearer token.
  2. Observe the public HTTP status and response body.
- Expected Result: The request is rejected or does not expose coupon list data.
- Actual Result: `GET /api/coupons` without Authorization returned HTTP `401` with body `{"error":"Unauthorized"}`.
- Status: Pass
- Evidence: [FR17-DT-001](./evidence/FR17-DT-001.png)
- Test Basis Reference: `requirement-analysis.md` - FR17-R11, FR17-API01; `domain-testing.md` - AUTH-MISSING-I01

## FR17-DT-002

- Test Case ID: FR17-DT-002
- Technique: Domain Testing
- Objective: Verify unauthenticated admin coupon-create request is rejected.
- Requirement or Rule Reference: FR17-R11, FR17-API04
- Preconditions: Backend API is available at `http://localhost:3000`.
- Test Data: Valid coupon body without Authorization header:
  `{"code":"FR17_NOAUTH_001","type":"percent","discount_value":15,"min_order_amount":200000,"expired_at":"2027-12-31","max_uses_per_user":1}`
- Steps:
  1. Send `POST /api/admin/coupons` without bearer token.
  2. Observe the public HTTP status and response body.
- Expected Result: The request is rejected and no coupon is created.
- Actual Result: `POST /api/admin/coupons` without Authorization returned HTTP `401` with body `{"error":"Unauthorized"}`.
- Status: Pass
- Evidence: [FR17-DT-002](./evidence/FR17-DT-002.png)
- Test Basis Reference: `requirement-analysis.md` - FR17-R11, FR17-API04; `domain-testing.md` - AUTH-MISSING-I01

## FR17-DT-003

- Test Case ID: FR17-DT-003
- Technique: Domain Testing
- Objective: Verify non-admin user token cannot create coupons through admin API.
- Requirement or Rule Reference: FR17-R11, FR17-API04
- Preconditions: Backend API is available; ordinary user token is available.
- Test Data: Non-admin bearer token; valid coupon body `{"code":"FR17_003","type":"percent","discount_value":15,"min_order_amount":200000,"expired_at":"2027-12-31","max_uses_per_user":1}`.
- Steps:
  1. Log in as an ordinary user through the public login API.
  2. Send `POST /api/admin/coupons` with the ordinary user token and the valid coupon body.
  3. Observe the public HTTP status and response body.
  4. If mutation unexpectedly occurs, clean up the disposable coupon.
- Expected Result: The request is rejected and no coupon is created because the caller is not an admin.
- Actual Result: `POST /api/admin/coupons` with a non-admin user token returned HTTP `200 OK` with body `{"message":"Coupon created","id":6}`. The coupon was created even though the caller was not an admin.
- Status: Fail
- Evidence: [FR17-DT-003](./evidence/FR17-DT-003.png)
- Test Basis Reference: `requirement-analysis.md` - FR17-R11, FR17-API04; `domain-testing.md` - AUTH-USER-I01

## FR17-DT-004

- Test Case ID: FR17-DT-004
- Technique: Domain Testing
- Objective: Verify non-admin user token cannot delete coupons through admin API.
- Requirement or Rule Reference: FR17-R11, FR17-API03, FR17-API04
- Preconditions: Backend API is available; ordinary user token is available; disposable coupon setup is available.
- Test Data: Non-admin bearer token; disposable coupon id `6`.
- Steps:
  1. Create a disposable coupon for delete setup.
  2. Send `DELETE /api/admin/coupons/6` using the ordinary user token.
  3. Observe the public HTTP status and response body.
- Expected Result: The delete request is rejected because the caller is not an admin.
- Actual Result: `DELETE /api/admin/coupons/6` with a non-admin user token returned HTTP `200 OK` with body `{"message":"Coupon deleted"}`. The coupon was deleted even though the caller was not an admin.
- Status: Fail
- Evidence: [FR17-DT-004](./evidence/FR17-DT-004.png)
- Test Basis Reference: `requirement-analysis.md` - FR17-R11, FR17-API03, FR17-API04; `domain-testing.md` - AUTH-USER-I01, DELETE-V01

## FR17-DT-005

- Test Case ID: FR17-DT-005
- Technique: Domain Testing
- Objective: Verify admin can retrieve coupon list.
- Requirement or Rule Reference: FR17-R02, FR17-API01
- Preconditions: Backend API is available; valid admin bearer token is available.
- Test Data: Admin bearer token.
- Steps:
  1. Send `GET /api/coupons` with admin bearer token.
  2. Observe coupon list response.
- Expected Result: The request succeeds and returns coupon list data.
- Actual Result: `GET /api/coupons` with bearer token returned HTTP `200 OK` and a JSON array of coupon records, including fields such as `id`, `code`, `type`, `discount_value`, `min_order_amount`, `expired_at`, `is_active`, and `max_uses_per_user`.
- Status: Pass
- Evidence: [FR17-DT-005](./evidence/FR17-DT-005.png)
- Test Basis Reference: `requirement-analysis.md` - FR17-R02, FR17-API01; `domain-testing.md` - LIST-V01, AUTH-ADMIN-V01

## FR17-DT-006

- Test Case ID: FR17-DT-006
- Technique: Domain Testing
- Objective: Verify admin can create a valid percent coupon.
- Requirement or Rule Reference: FR17-R01, FR17-R04, FR17-R05, FR17-R06, FR17-R07, FR17-R08, FR17-R09, FR17-R10, FR17-API02
- Preconditions: Backend API is available; valid admin bearer token is available.
- Test Data: Unique code `FR17_006`; type `percent`; `discount_value: 15`; `expired_at: 2027-12-31`; `min_order_amount: 200000`; `max_uses_per_user: 1`.
- Steps:
  1. Send `POST /api/admin/coupons` with a complete valid percent coupon body.
  2. Observe the public HTTP status and response body.
  3. Verify later visibility through coupon list if available.
- Expected Result: The coupon is created successfully.
- Actual Result: `POST /api/admin/coupons` with valid percent coupon body returned HTTP `200 OK` with body `{"message":"Coupon created","id":7}`.
- Status: Pass
- Evidence: [FR17-DT-006](./evidence/FR17-DT-006.png)
- Test Basis Reference: `requirement-analysis.md` - FR17-R01, FR17-R04 through FR17-R10, FR17-API02; `domain-testing.md` - listed partitions

## FR17-DT-007

- Test Case ID: FR17-DT-007
- Technique: Domain Testing
- Objective: Verify admin can create a valid fixed-amount coupon.
- Requirement or Rule Reference: FR17-R01, FR17-R06, FR17-API02
- Preconditions: Backend API is available; valid admin bearer token is available.
- Test Data: Unique code `FR17_FIXED_001`; type `fixed`; `discount_value: 50000`; `expired_at: 2027-12-31`; `min_order_amount: 0`; `max_uses_per_user: 1`.
- Steps:
  1. Send `POST /api/admin/coupons` with a complete valid fixed coupon body.
  2. Observe the public HTTP status and response body.
- Expected Result: The coupon is created successfully.
- Actual Result: `POST /api/admin/coupons` with valid fixed coupon body returned HTTP `200 OK` with body `{"message":"Coupon created","id":8}`.
- Status: Pass
- Evidence: [FR17-DT-007](./evidence/FR17-DT-007.png)
- Test Basis Reference: `requirement-analysis.md` - FR17-R01, FR17-R06, FR17-API02; `domain-testing.md` - TYPE-FIXED-V01, CREATE-V01

## FR17-DT-008

- Test Case ID: FR17-DT-008
- Technique: Domain Testing
- Objective: Verify admin can delete an existing test-created coupon.
- Requirement or Rule Reference: FR17-R03, FR17-API03
- Preconditions: Backend API is available; valid admin bearer token is available; disposable coupon exists.
- Test Data: Test-created coupon id `8`.
- Steps:
  1. Create a disposable coupon as admin.
  2. Send `DELETE /api/admin/coupons/8` with admin bearer token.
  3. Observe success response or later absence from the coupon list.
- Expected Result: Existing coupon is deleted successfully.
- Actual Result: `DELETE /api/admin/coupons/8` with bearer token returned HTTP `200 OK` with body `{"message":"Coupon deleted"}`.
- Status: Pass
- Evidence: [FR17-DT-008](./evidence/FR17-DT-008.png)
- Test Basis Reference: `requirement-analysis.md` - FR17-R03, FR17-API03; `domain-testing.md` - DELETE-V01

## FR17-DT-009

- Test Case ID: FR17-DT-009
- Technique: Domain Testing
- Objective: Verify duplicate coupon code is rejected.
- Requirement or Rule Reference: FR17-R05
- Preconditions: Backend API is available; valid admin bearer token is available; first coupon with the target code exists.
- Test Data: Duplicate coupon code `FR17_DUPLICATE_001`.
- Steps:
  1. Create a coupon with code `FR17_DUPLICATE_001`.
  2. Attempt to create a second coupon with the same exact code.
  3. Observe rejection.
- Expected Result: Duplicate exact coupon code is rejected.
- Actual Result: Creating a second coupon with duplicate code `FR17_DUPLICATE_001` returned HTTP `500 Internal Server Error` with body `{"error":"SQLITE_CONSTRAINT: UNIQUE constraint failed: coupons.code"}`. The duplicate coupon was rejected.
- Status: Pass
- Evidence: [FR17-DT-009](./evidence/FR17-DT-009.png)
- Test Basis Reference: `requirement-analysis.md` - FR17-R05; `domain-testing.md` - CODE-I02

## FR17-DT-010

- Test Case ID: FR17-DT-010
- Technique: Domain Testing
- Objective: Verify missing coupon code is rejected.
- Requirement or Rule Reference: FR17-R04
- Preconditions: Backend API is available; valid admin bearer token is available.
- Test Data: Coupon create body without `code`; all other fields valid:
  `{"type":"fixed","discount_value":50000,"expired_at":"2027-12-31","min_order_amount":0,"max_uses_per_user":1}`
- Steps:
  1. Send `POST /api/admin/coupons` with `code` omitted.
  2. Observe rejection.
- Expected Result: The request is rejected because `code` is required.
- Actual Result: `POST /api/admin/coupons` with `code` omitted returned HTTP `200 OK` with body `{"message":"Coupon created","id":10}`. The coupon was created even though the required `code` field was missing.
- Status: Fail
- Evidence: [FR17-DT-010](./evidence/FR17-DT-010.png)
- Test Basis Reference: `requirement-analysis.md` - FR17-R04; `domain-testing.md` - CODE-I01

## FR17-DT-011

- Test Case ID: FR17-DT-011
- Technique: Domain Testing
- Objective: Verify unsupported coupon type is rejected.
- Requirement or Rule Reference: FR17-R06
- Preconditions: Backend API is available; valid admin bearer token is available.
- Test Data: Type `bogus`; all other fields valid:
  `{"code":"FR17_BOGUS_001","type":"bogus","discount_value":15,"expired_at":"2027-12-31","min_order_amount":200000,"max_uses_per_user":1}`
- Steps:
  1. Send `POST /api/admin/coupons` with `type: "bogus"`.
  2. Observe rejection.
- Expected Result: The request is rejected because type is not `percent` or `fixed`.
- Actual Result: `POST /api/admin/coupons` with unsupported type `bogus` returned HTTP `200 OK` with body `{"message":"Coupon created","id":11}`. The coupon was created even though `type` was not `percent` or `fixed`.
- Status: Fail
- Evidence: [FR17-DT-011](./evidence/FR17-DT-011.png)
- Test Basis Reference: `requirement-analysis.md` - FR17-R06; `domain-testing.md` - TYPE-I01

## FR17-DT-012

- Test Case ID: FR17-DT-012
- Technique: Domain Testing
- Objective: Verify missing expiration date is rejected.
- Requirement or Rule Reference: FR17-R08
- Preconditions: Backend API is available; valid admin bearer token is available.
- Test Data: Coupon create body without `expired_at`; all other fields valid:
  `{"code":"FR17_NOEXPIRED_001","type":"percent","discount_value":15,"min_order_amount":200000,"max_uses_per_user":1}`
- Steps:
  1. Send `POST /api/admin/coupons` with `expired_at` omitted.
  2. Observe rejection.
- Expected Result: The request is rejected because expiration date is required.
- Actual Result: `POST /api/admin/coupons` with `expired_at` omitted returned HTTP `200 OK` with body `{"message":"Coupon created","id":12}`. The coupon was created even though the required expiration date was missing.
- Status: Fail
- Evidence: [FR17-DT-012](./evidence/FR17-DT-012.png)
- Test Basis Reference: `requirement-analysis.md` - FR17-R08; `domain-testing.md` - EXPIRED-I01

## FR17-DT-013

- Test Case ID: FR17-DT-013
- Technique: Domain Testing
- Objective: Verify negative discount value is rejected as an invalid discount partition.
- Requirement or Rule Reference: FR17-R07
- Preconditions: Backend API is available; valid admin bearer token is available.
- Test Data: `discount_value: -1`; all other fields valid:
  `{"code":"FR17_NEGDISCOUNT_002","type":"fixed","discount_value":-1,"expired_at":"2027-12-31","min_order_amount":0,"max_uses_per_user":1}`
- Steps:
  1. Send `POST /api/admin/coupons` with `discount_value: -1`.
  2. Observe rejection.
- Expected Result: The request is rejected because discount value must be positive.
- Actual Result: `POST /api/admin/coupons` with `discount_value: -1` returned HTTP `200 OK` with body `{"message":"Coupon created","id":14}`. The coupon was created even though discount value was negative.
- Status: Fail
- Evidence: [FR17-DT-013](./evidence/FR17-DT-013.png)
- Test Basis Reference: `requirement-analysis.md` - FR17-R07; `domain-testing.md` - DISCOUNT-I02

## Boundary Value Analysis Test Cases

## FR17-BVA-001

- Test Case ID: FR17-BVA-001
- Technique: Boundary Value Analysis
- Objective: Verify `discount_value` zero is rejected.
- Requirement or Rule Reference: FR17-R07
- Preconditions: Backend API is available; valid admin bearer token is available.
- Test Data: `discount_value: 0`; all other fields valid:
  `{"code":"FR17_ZERO_DISCOUNT_001","type":"fixed","discount_value":0,"expired_at":"2027-12-31","min_order_amount":0,"max_uses_per_user":1}`
- Steps:
  1. Send `POST /api/admin/coupons` with `discount_value: 0`.
  2. Observe rejection.
- Expected Result: The request is rejected because discount value must be positive.
- Actual Result: `POST /api/admin/coupons` with `discount_value: 0` returned HTTP `200 OK` with body `{"message":"Coupon created","id":15}`. The coupon was created even though discount value was not positive.
- Status: Fail
- Evidence: [FR17-BVA-001](./evidence/FR17-BVA-001.png)
- Test Basis Reference: `boundary-value-analysis.md` - FR17-DISCOUNT-POS-B01

## FR17-BVA-002

- Test Case ID: FR17-BVA-002
- Technique: Boundary Value Analysis
- Objective: Verify `discount_value` one is accepted.
- Requirement or Rule Reference: FR17-R07
- Preconditions: Backend API is available; valid admin bearer token is available.
- Test Data: `discount_value: 1`; all other fields valid:
  `{"code":"FR17_DISCOUNT_ONE_001","type":"fixed","discount_value":1,"expired_at":"2027-12-31","min_order_amount":0,"max_uses_per_user":1}`
- Steps:
  1. Send `POST /api/admin/coupons` with `discount_value: 1`.
  2. Observe success.
- Expected Result: The request succeeds because `1` is positive.
- Actual Result: `POST /api/admin/coupons` with `discount_value: 1` returned HTTP `200 OK` with body `{"message":"Coupon created","id":16}`.
- Status: Pass
- Evidence: [FR17-BVA-002](./evidence/FR17-BVA-002.png)
- Test Basis Reference: `boundary-value-analysis.md` - FR17-DISCOUNT-POS-B02

## FR17-BVA-003

- Test Case ID: FR17-BVA-003
- Technique: Boundary Value Analysis
- Objective: Verify `discount_value` two is accepted as the adjacent in-point above the minimum.
- Requirement or Rule Reference: FR17-R07
- Preconditions: Backend API is available; valid admin bearer token is available.
- Test Data: `discount_value: 2`; all other fields valid:
  `{"code":"FR17_DISCOUNT_TWO_001","type":"fixed","discount_value":2,"expired_at":"2027-12-31","min_order_amount":0,"max_uses_per_user":1}`
- Steps:
  1. Send `POST /api/admin/coupons` with `discount_value: 2`.
  2. Observe success.
- Expected Result: The request succeeds because `2` is a positive value above the minimum.
- Actual Result: `POST /api/admin/coupons` with `discount_value: 2` returned HTTP `200 OK` with body `{"message":"Coupon created","id":17}`.
- Status: Pass
- Evidence: [FR17-BVA-003](./evidence/FR17-BVA-003.png)
- Test Basis Reference: `boundary-value-analysis.md` - FR17-DISCOUNT-POS-B03

## FR17-BVA-004

- Test Case ID: FR17-BVA-004
- Technique: Boundary Value Analysis
- Objective: Verify `min_order_amount` `-1` is rejected.
- Requirement or Rule Reference: FR17-R09
- Preconditions: Backend API is available; valid admin bearer token is available.
- Test Data: `min_order_amount: -1`; all other fields valid:
  `{"code":"FR17_MINORDER_NEG_001","type":"fixed","discount_value":50000,"expired_at":"2027-12-31","min_order_amount":-1,"max_uses_per_user":1}`
- Steps:
  1. Send `POST /api/admin/coupons` with `min_order_amount: -1`.
  2. Observe rejection.
- Expected Result: The request is rejected because minimum order amount must be `>= 0`.
- Actual Result: `POST /api/admin/coupons` with `min_order_amount: -1` returned HTTP `200 OK` with body `{"message":"Coupon created","id":18}`. The coupon was created even though minimum order amount was below `0`.
- Status: Fail
- Evidence: [FR17-BVA-004](./evidence/FR17-BVA-004.png)
- Test Basis Reference: `boundary-value-analysis.md` - FR17-MINORDER-B01

## FR17-BVA-005

- Test Case ID: FR17-BVA-005
- Technique: Boundary Value Analysis
- Objective: Verify `min_order_amount` zero is accepted.
- Requirement or Rule Reference: FR17-R09
- Preconditions: Backend API is available; valid admin bearer token is available.
- Test Data: `min_order_amount: 0`; all other fields valid:
  `{"code":"FR17_MINORDER_ZERO_001","type":"fixed","discount_value":50000,"expired_at":"2027-12-31","min_order_amount":0,"max_uses_per_user":1}`
- Steps:
  1. Send `POST /api/admin/coupons` with `min_order_amount: 0`.
  2. Observe success.
- Expected Result: The request succeeds because `0` satisfies `>= 0`.
- Actual Result: `POST /api/admin/coupons` with `min_order_amount: 0` returned HTTP `200 OK` with body `{"message":"Coupon created","id":19}`.
- Status: Pass
- Evidence: [FR17-BVA-005](./evidence/FR17-BVA-005.png)
- Test Basis Reference: `boundary-value-analysis.md` - FR17-MINORDER-B02

## FR17-BVA-006

- Test Case ID: FR17-BVA-006
- Technique: Boundary Value Analysis
- Objective: Verify `min_order_amount` one is accepted as the adjacent in-point above the minimum.
- Requirement or Rule Reference: FR17-R09
- Preconditions: Backend API is available; valid admin bearer token is available.
- Test Data: `min_order_amount: 1`; all other fields valid:
  `{"code":"FR17_MINORDER_ONE_001","type":"fixed","discount_value":50000,"expired_at":"2027-12-31","min_order_amount":1,"max_uses_per_user":1}`
- Steps:
  1. Send `POST /api/admin/coupons` with `min_order_amount: 1`.
  2. Observe success.
- Expected Result: The request succeeds because `1` is above the inclusive minimum `0`.
- Actual Result: `POST /api/admin/coupons` with `min_order_amount: 1` returned HTTP `200 OK` with body `{"message":"Coupon created","id":20}`.
- Status: Pass
- Evidence: [FR17-BVA-006](./evidence/FR17-BVA-006.png)
- Test Basis Reference: `boundary-value-analysis.md` - FR17-MINORDER-B03

## FR17-BVA-007

- Test Case ID: FR17-BVA-007
- Technique: Boundary Value Analysis
- Objective: Verify `max_uses_per_user` zero is rejected.
- Requirement or Rule Reference: FR17-R10
- Preconditions: Backend API is available; valid admin bearer token is available.
- Test Data: `max_uses_per_user: 0`; all other fields valid:
  `{"code":"FR17_MAXUSES_ZERO_001","type":"fixed","discount_value":50000,"expired_at":"2027-12-31","min_order_amount":0,"max_uses_per_user":0}`
- Steps:
  1. Send `POST /api/admin/coupons` with `max_uses_per_user: 0`.
  2. Observe rejection.
- Expected Result: The request is rejected because max uses per user must be at least `1`.
- Actual Result: `POST /api/admin/coupons` with `max_uses_per_user: 0` returned HTTP `200 OK` with body `{"message":"Coupon created","id":21}`. The coupon was created even though max uses per user was below `1`.
- Status: Fail
- Evidence: [FR17-BVA-007](./evidence/FR17-BVA-007.png)
- Test Basis Reference: `boundary-value-analysis.md` - FR17-MAXUSES-B01

## FR17-BVA-008

- Test Case ID: FR17-BVA-008
- Technique: Boundary Value Analysis
- Objective: Verify `max_uses_per_user` one is accepted.
- Requirement or Rule Reference: FR17-R10
- Preconditions: Backend API is available; valid admin bearer token is available.
- Test Data: `max_uses_per_user: 1`; all other fields valid:
  `{"code":"FR17_MAXUSES_ONE_001","type":"fixed","discount_value":50000,"expired_at":"2027-12-31","min_order_amount":0,"max_uses_per_user":1}`
- Steps:
  1. Send `POST /api/admin/coupons` with `max_uses_per_user: 1`.
  2. Observe success.
- Expected Result: The request succeeds because `1` satisfies `>= 1`.
- Actual Result: `POST /api/admin/coupons` with `max_uses_per_user: 1` returned HTTP `200 OK` with body `{"message":"Coupon created","id":22}`.
- Status: Pass
- Evidence: [FR17-BVA-008](./evidence/FR17-BVA-008.png)
- Test Basis Reference: `boundary-value-analysis.md` - FR17-MAXUSES-B02

## FR17-BVA-009

- Test Case ID: FR17-BVA-009
- Technique: Boundary Value Analysis
- Objective: Verify `max_uses_per_user` two is accepted as the adjacent in-point above the minimum.
- Requirement or Rule Reference: FR17-R10
- Preconditions: Backend API is available; valid admin bearer token is available.
- Test Data: `max_uses_per_user: 2`; all other fields valid:
  `{"code":"FR17_MAXUSES_TWO_001","type":"fixed","discount_value":50000,"expired_at":"2027-12-31","min_order_amount":0,"max_uses_per_user":2}`
- Steps:
  1. Send `POST /api/admin/coupons` with `max_uses_per_user: 2`.
  2. Observe success.
- Expected Result: The request succeeds because `2` is above the inclusive minimum `1`.
- Actual Result: `POST /api/admin/coupons` with `max_uses_per_user: 2` returned HTTP `200 OK` with body `{"message":"Coupon created","id":23}`.
- Status: Pass
- Evidence: [FR17-BVA-009](./evidence/FR17-BVA-009.png)
- Test Basis Reference: `boundary-value-analysis.md` - FR17-MAXUSES-B03

## Human Review - Phase 5 / Execution

- Reviewer: Nguyen Thanh Tien
- Review Date and Time: 2026-06-27 15:19
- Review Scope: FR-17 test-case design, execution results, and evidence wording
- Human Review Status: Completed
- Approved for Test Execution: Yes

## Human Corrections

- Removed the standalone admin-login test case because admin authentication is setup, not a FR-17 coupon-management requirement.
- Removed obsolete setup-credential rule references from test cases.
- Reframed admin token availability as a test precondition instead of a separate FR-17 test case.
- Updated executed cases from `Blocked` to actual `Pass` or `Fail` results after API evidence was collected.
- Added BVA `min+1` in-point cases for `discount_value: 2`, `min_order_amount: 1`, and `max_uses_per_user: 2`.
- Split missing `code` and missing `expired_at` into separate test cases for clearer traceability.
- Confirmed final execution status counts: 22 total cases, 13 Pass, 9 Fail, 0 Blocked.
