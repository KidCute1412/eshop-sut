# Requirement Analysis - FR-17 Coupon Management CRUD

## Feature Intake

| Field               | Value                                                                                               |
| ------------------- | --------------------------------------------------------------------------------------------------- |
| Feature ID          | FR-17                                                                                               |
| Feature name        | Coupon Management CRUD / Quản lý Mã Giảm Giá                                                        |
| Pool                | C - Web Admin                                                                                       |
| Actor               | Admin user                                                                                          |
| Application surface | Web Admin and public/admin coupon API                                                               |
| UI location         | Web Admin coupon management area; admin web expected at `http://localhost:5174` from setup guidance |
| API endpoints       | `GET /api/coupons`, `POST /api/admin/coupons`, `DELETE /api/admin/coupons/:id`                      |
| Output root         | `reports/FR-17`                                                                                     |

## Approved Black-box Test Bases

- `2026.HW02.Domain Testing_En.pdf` - Pool C includes FR-17 Coupon management CRUD.
- `README.md` - FR-12 Access Control.
- `README.md` - FR-17 Coupon CRUD.
- `api_specification.md` - 5.2 `GET /api/coupons`.
- `api_specification.md` - 6 Admin API access rule.
- `api_specification.md` - 6.4 Coupon Management.
- `setup_guide.md` - public startup guidance and default credentials, used only as test setup data.

## Requirement Rules

| Rule ID  | Rule                                                                          | Test Basis Type      | Test Basis Reference                                         | Observable Expected Behaviour                                              | Ambiguity                                                                                                                                   | Assumption                                                             |
| -------- | ----------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------ | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| FR17-R01 | Admin can add coupon codes.                                                   | Official requirement | `README.md` - FR-17                                          | Admin can create a coupon through public admin surface/API.                | Exact UI labels and success message are unspecified.                                                                                        | API success plus later visibility is acceptable.                       |
| FR17-R02 | Admin can view coupon codes.                                                  | Official requirement | `README.md` - FR-17; `api_specification.md` - 5.2            | Authorized admin can retrieve coupon list.                                 | Whether non-admin authenticated users may use `GET /api/coupons` is ambiguous because endpoint is labeled admin but outside `/api/admin/*`. | Admin access is the intended surface.                                  |
| FR17-R03 | Admin can delete coupon codes.                                                | Official requirement | `README.md` - FR-17; `api_specification.md` - 6.4            | Admin can delete an existing coupon by id.                                 | Exact delete response status/body is unspecified.                                                                                           | Deletion is observable by success response or later absence.           |
| FR17-R04 | `code` is required.                                                           | Official requirement | `README.md` - FR-17                                          | Create request missing/empty code is rejected.                             | Whitespace handling and maximum length are unspecified.                                                                                     | Missing code is invalid.                                               |
| FR17-R05 | `code` must be unique.                                                        | Official requirement | `README.md` - FR-17                                          | Creating a duplicate code is rejected.                                     | Case sensitivity is unspecified.                                                                                                            | Duplicate exact code is invalid.                                       |
| FR17-R06 | `type` is required and must be `percent` or `fixed`.                          | Official requirement | `README.md` - FR-17; `api_specification.md` - 6.4            | `percent` and `fixed` are valid; other types are rejected.                 | Case sensitivity is unspecified.                                                                                                            | Exact lowercase documented values are valid.                           |
| FR17-R07 | `discount_value` is required and positive.                                    | Official requirement | `README.md` - FR-17                                          | Positive numeric discount value is accepted; zero or negative is rejected. | No upper bound and no percent maximum are specified.                                                                                        | BVA uses the documented lower boundary around positive numeric values. |
| FR17-R08 | `expired_at` is required.                                                     | Official requirement | `README.md` - FR-17; `api_specification.md` - 6.4            | Missing expiration date is rejected.                                       | Date format validation is not explicit beyond sample `YYYY-MM-DD`.                                                                          | `YYYY-MM-DD` sample format is nominal.                                 |
| FR17-R09 | `min_order_amount` is required and must be `>= 0`.                            | Official requirement | `README.md` - FR-17                                          | Zero and positive min order are valid; negative value is rejected.         | Numeric precision is unspecified.                                                                                                           | Integer VND amounts are used.                                          |
| FR17-R10 | `max_uses_per_user` is required and must be `>= 1`.                           | Official requirement | `README.md` - FR-17                                          | One or more uses are valid; zero is rejected.                              | Upper bound is unspecified.                                                                                                                 | Integer counts are used.                                               |
| FR17-R11 | Admin APIs and data-affecting coupon APIs require a valid JWT and admin role. | Official requirement | `README.md` - FR-12; `api_specification.md` - Admin API rule | Missing token and non-admin token requests are rejected.                   | Exact status/body are unspecified.                                                                                                          | Any 4xx/no mutation is acceptable rejection.                           |

## API Specification Rules

| Rule ID    | Rule                                                                           | Test Basis Type   | Test Basis Reference         | Observable Expected Behaviour                                                    | Ambiguity                                                                      | Assumption                                                            |
| ---------- | ------------------------------------------------------------------------------ | ----------------- | ---------------------------- | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | --------------------------------------------------------------------- |
| FR17-API01 | `GET /api/coupons` lists coupons and requires `Authorization: Bearer <token>`. | API specification | `api_specification.md` - 5.2 | Request without token is rejected; authorized admin request returns coupon list. | Admin-role enforcement for this endpoint is less explicit than `/api/admin/*`. | Treat as admin list endpoint because spec labels it `Dành cho Admin`. |
| FR17-API02 | `POST /api/admin/coupons` adds a coupon.                                       | API specification | `api_specification.md` - 6.4 | Admin POST with documented body creates coupon.                                  | Exact response shape is unspecified.                                           | Coupon should be visible after creation.                              |
| FR17-API03 | `DELETE /api/admin/coupons/:id` deletes a coupon.                              | API specification | `api_specification.md` - 6.4 | Admin DELETE removes coupon by id.                                               | Exact not-found status is unspecified.                                         | Test-created coupon is used for delete tests.                         |
| FR17-API04 | All `/api/admin/*` endpoints require bearer token and Admin account.           | API specification | `api_specification.md` - 6   | Unauthenticated and non-admin requests are rejected.                             | Exact status/body are unspecified.                                             | Non-admin token must not mutate coupon data.                          |

## Requirement Ambiguities

- Coupon `code` maximum length, allowed characters, trimming, and case sensitivity are unspecified.
- `discount_value` has no upper bound and no special percent maximum rule.
- Numeric precision for money and discount fields is unspecified.
- Date format and whether `expired_at` may be in the past are unspecified for management CRUD.
- Exact API success/error status codes and response bodies are unspecified.
- Whether `GET /api/coupons` must reject non-admin authenticated users is less explicit than `/api/admin/*`, but it is labeled for admin.
- Update/edit coupon is not specified, so CRUD here covers add/view/delete only.

## Assumptions

- FR-17 may be tested through the public API when the Web Admin UI is unavailable; UI unavailability is recorded as a blocking condition during execution.
- A valid admin token can be obtained through documented public login if the environment is seeded correctly.
- Admin authorization is required for data-affecting coupon APIs.
- For blocked admin-dependent tests, failure to obtain an admin token is recorded as a real blocking condition.
- Numeric BVA is applicable to `discount_value`, `min_order_amount`, and `max_uses_per_user` because their lower bounds are documented.

## Coverage Gaps

- UI admin coupon tests are blocked unless Web Admin is running and reachable.
- Positive admin CRUD and validation tests cannot be executed without a valid admin token.
- No update/edit test is derived because FR-17 and API spec only state add/view/delete.
- No upper-bound BVA for `discount_value`, `min_order_amount`, or `max_uses_per_user` is derived because no upper bound is documented.
- No code length or character-set BVA is derived because no maximum length or allowed-character rule is documented.

## Human Review

- Reviewer: Nguyen Thanh Tien
- Review Date and Time: 2026-06-27 11:08
- Review Scope: FR-17 Requirement Analysis and Black-box Test Basis
- Human Review Status: Completed
- Approved for Domain Modeling: Yes
- Approved for BVA: Yes
- Approved for Test-Case Derivation: Yes
- Approved for Test Execution: Yes

## Human Corrections

- Removed setup credential information from the normative requirement-rule table.
- Moved admin credentials to `Test Setup Inputs` because credentials are setup data, not FR-17 functional requirements.
- Clarified that API testing is acceptable when Web Admin UI is unavailable, and UI unavailability should be recorded as an execution blocker.
- Added explicit BVA applicability for `discount_value`, `min_order_amount`, and `max_uses_per_user`.
- Confirmed that coupon update/edit is excluded because README and API specification only define add, view, and delete for FR-17.
