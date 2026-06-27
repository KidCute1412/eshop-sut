# Domain Testing - FR-17 Coupon Management CRUD

## Step 1. Identify Input & Output Variables

| Type              | Variable or Output            | Description                                                          | Related Rule IDs     | Applies To |
| ----------------- | ----------------------------- | -------------------------------------------------------------------- | -------------------- | ---------- |
| State / Condition | Admin authenticated state     | Valid JWT for account with admin role.                               | FR17-R11, FR17-API04 | API/UI     |
| State / Condition | Non-admin authenticated state | Valid JWT for ordinary user.                                         | FR17-R11, FR17-API04 | API        |
| State / Condition | Unauthenticated state         | No bearer token.                                                     | FR17-R11, FR17-API04 | API/UI     |
| Input             | Coupon code                   | Unique required coupon identifier.                                   | FR17-R04, FR17-R05   | API/UI     |
| Input             | Coupon type                   | Required `percent` or `fixed`.                                       | FR17-R06             | API/UI     |
| Input             | Discount value                | Required positive number.                                            | FR17-R07             | API/UI     |
| Input             | Expiration date               | Required `expired_at` value.                                         | FR17-R08             | API/UI     |
| Input             | Minimum order amount          | Required amount `>= 0`.                                              | FR17-R09             | API/UI     |
| Input             | Max uses per user             | Required integer count `>= 1`.                                       | FR17-R10             | API/UI     |
| Input             | Coupon id                     | Existing coupon id for deletion.                                     | FR17-R03, FR17-API03 | API/UI     |
| API Contract      | Coupon list response          | `GET /api/coupons`.                                                  | FR17-R02, FR17-API01 | API        |
| API Contract      | Coupon create response        | `POST /api/admin/coupons`.                                           | FR17-R01, FR17-API02 | API        |
| API Contract      | Coupon delete response        | `DELETE /api/admin/coupons/:id`.                                     | FR17-R03, FR17-API03 | API        |
| Output            | Access-control rejection      | Missing/non-admin token is rejected and does not mutate coupon data. | FR17-R11, FR17-API04 | API/UI     |

## Step 2. Identify Equivalence Classes

| Partition ID     | Type              | Variable or Condition | Equivalence Class Description                  | Validity | Representative Value                     | Dependencies                     | Rule IDs             | Test Basis Reference                                         | Assumptions                         |
| ---------------- | ----------------- | --------------------- | ---------------------------------------------- | -------- | ---------------------------------------- | -------------------------------- | -------------------- | ------------------------------------------------------------ | ----------------------------------- |
| AUTH-ADMIN-V01   | State / Condition | Admin auth            | Valid admin token.                             | Valid    | Admin token from successful public login | Admin login available.           | FR17-R11, FR17-API04 | `README.md` - FR-12; `api_specification.md` - Admin API rule | Blocked if credential unavailable.  |
| AUTH-USER-I01    | State / Condition | Non-admin auth        | Ordinary user token attempts admin mutation.   | Invalid  | `test@eshop.com` token                   | User login available.            | FR17-R11, FR17-API04 | `README.md` - FR-12                                          | Must be rejected.                   |
| AUTH-MISSING-I01 | State / Condition | Missing token         | No Authorization header.                       | Invalid  | Omit token                               | API reachable.                   | FR17-R11, FR17-API04 | `api_specification.md` Admin API rule                        | Exact status/body unspecified.      |
| CODE-V01         | Input             | Code                  | Provided unique code.                          | Valid    | `FR17_OK_<timestamp>`                    | Admin token.                     | FR17-R04, FR17-R05   | `README.md` - FR-17                                          | Prefix avoids collision.            |
| CODE-I01         | Input             | Code                  | Missing code.                                  | Invalid  | Body without `code`                      | Admin token, other fields valid. | FR17-R04             | `README.md` - FR-17                                          | Exact error unspecified.            |
| CODE-I02         | Input             | Code                  | Duplicate code.                                | Invalid  | Create same code twice                   | Admin token and first create.    | FR17-R05             | `README.md` - FR-17                                          | Exact duplicate code is invalid.    |
| TYPE-PERCENT-V01 | Input             | Type                  | Type is `percent`.                             | Valid    | `percent`                                | Other fields valid.              | FR17-R06             | `README.md` - FR-17; `api_specification.md` - 6.4            | Lowercase documented value.         |
| TYPE-FIXED-V01   | Input             | Type                  | Type is `fixed`.                               | Valid    | `fixed`                                  | Other fields valid.              | FR17-R06             | `README.md` - FR-17; `api_specification.md` - 6.4            | Lowercase documented value.         |
| TYPE-I01         | Input             | Type                  | Unsupported type.                              | Invalid  | `bogus`                                  | Other fields valid.              | FR17-R06             | `README.md` - FR-17                                          | Exact error unspecified.            |
| DISCOUNT-V01     | Input             | Discount value        | Positive discount value.                       | Valid    | `10`                                     | Other fields valid.              | FR17-R07             | `README.md` - FR-17                                          | No upper bound.                     |
| DISCOUNT-I01     | Input             | Discount value        | Zero discount value.                           | Invalid  | `0`                                      | Other fields valid.              | FR17-R07             | `README.md` - FR-17                                          | Positive excludes zero.             |
| DISCOUNT-I02     | Input             | Discount value        | Negative discount value.                       | Invalid  | `-1`                                     | Other fields valid.              | FR17-R07             | `README.md` - FR-17                                          | Exact error unspecified.            |
| EXPIRED-V01      | Input             | Expired at            | Expiration date provided.                      | Valid    | `2027-12-31`                             | Other fields valid.              | FR17-R08             | `README.md` - FR-17; API body sample                         | Format from API sample.             |
| EXPIRED-I01      | Input             | Expired at            | Missing expiration date.                       | Invalid  | Body without `expired_at`                | Other fields valid.              | FR17-R08             | `README.md` - FR-17                                          | Exact error unspecified.            |
| MIN-ORDER-V01    | Input             | Minimum order amount  | Minimum order is zero or positive.             | Valid    | `0`                                      | Other fields valid.              | FR17-R09             | `README.md` - FR-17                                          | Integer VND amount.                 |
| MIN-ORDER-I01    | Input             | Minimum order amount  | Minimum order is negative.                     | Invalid  | `-1`                                     | Other fields valid.              | FR17-R09             | `README.md` - FR-17                                          | Exact error unspecified.            |
| MAX-USES-V01     | Input             | Max uses per user     | Max uses is at least 1.                        | Valid    | `1`                                      | Other fields valid.              | FR17-R10             | `README.md` - FR-17                                          | Integer count.                      |
| MAX-USES-I01     | Input             | Max uses per user     | Max uses is below 1.                           | Invalid  | `0`                                      | Other fields valid.              | FR17-R10             | `README.md` - FR-17                                          | Exact error unspecified.            |
| CREATE-V01       | API Contract      | Coupon create         | Admin creates coupon with complete valid body. | Valid    | Valid `POST /api/admin/coupons` body     | Admin token.                     | FR17-R01, FR17-API02 | `README.md` - FR-17; `api_specification.md` - 6.4            | Later visibility confirms creation. |
| LIST-V01         | API Contract      | Coupon list           | Admin list request returns coupon list.        | Valid    | `GET /api/coupons`                       | Admin token.                     | FR17-R02, FR17-API01 | `api_specification.md` - 5.2                                 | Response schema not fixed.          |
| DELETE-V01       | Input             | Coupon id             | Existing coupon id is deleted by admin.        | Valid    | Test-created coupon id                   | Admin token and created coupon.  | FR17-R03, FR17-API03 | `api_specification.md` - 6.4                                 | Test data cleanup required.         |

## Step 3. Best Representatives

| Partition ID     | Representative Value                      | Why This Representative Was Chosen                                                     | Required Nominal Values for Other Variables | Applies To |
| ---------------- | ----------------------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------- | ---------- |
| AUTH-ADMIN-V01   | Admin token from successful public login  | Uses documented setup access without treating credentials as a functional requirement. | API available.                              | API/UI     |
| AUTH-USER-I01    | `test@eshop.com` token                    | Known ordinary user token for access-control rejection.                                | Valid user login.                           | API        |
| AUTH-MISSING-I01 | No Authorization header                   | Isolates missing token.                                                                | Valid endpoint.                             | API        |
| CODE-V01         | `FR17_OK_<timestamp>`                     | Unique disposable code.                                                                | Other fields valid.                         | API/UI     |
| CODE-I01         | Body without `code`                       | Isolates required field.                                                               | Other fields valid.                         | API/UI     |
| CODE-I02         | Same code twice                           | Direct duplicate representative.                                                       | First create succeeds.                      | API/UI     |
| TYPE-PERCENT-V01 | `percent`                                 | Documented valid type.                                                                 | Other fields valid.                         | API/UI     |
| TYPE-FIXED-V01   | `fixed`                                   | Documented valid type.                                                                 | Other fields valid.                         | API/UI     |
| TYPE-I01         | `bogus`                                   | Clearly outside enum.                                                                  | Other fields valid.                         | API/UI     |
| DISCOUNT-V01     | `10`                                      | Simple positive value.                                                                 | Other fields valid.                         | API/UI     |
| DISCOUNT-I01     | `0`                                       | Boundary-adjacent invalid for positive.                                                | Other fields valid.                         | API/UI     |
| DISCOUNT-I02     | `-1`                                      | Invalid negative representative.                                                       | Other fields valid.                         | API/UI     |
| EXPIRED-V01      | `2027-12-31`                              | Sample-compatible future date.                                                         | Other fields valid.                         | API/UI     |
| EXPIRED-I01      | Missing `expired_at`                      | Isolates required field.                                                               | Other fields valid.                         | API/UI     |
| MIN-ORDER-V01    | `0`                                       | Inclusive minimum.                                                                     | Other fields valid.                         | API/UI     |
| MIN-ORDER-I01    | `-1`                                      | Immediately below minimum.                                                             | Other fields valid.                         | API/UI     |
| MAX-USES-V01     | `1`                                       | Inclusive minimum.                                                                     | Other fields valid.                         | API/UI     |
| MAX-USES-I01     | `0`                                       | Immediately below minimum.                                                             | Other fields valid.                         | API/UI     |
| CREATE-V01       | Complete coupon body with disposable code | Covers nominal add operation.                                                          | Admin token.                                | API/UI     |
| LIST-V01         | Admin `GET /api/coupons`                  | Nominal read operation.                                                                | Admin token.                                | API        |
| DELETE-V01       | Disposable created id                     | Avoids deleting seeded coupons.                                                        | Admin token.                                | API/UI     |

## Partition Derivation

Partitions come directly from FR-17 required fields, uniqueness, enum type, positive and `>=` constraints, add/view/delete permissions, and FR-12 admin access-control requirements. Valid partitions represent the documented nominal classes. Invalid partitions represent missing required fields, duplicate code, unsupported type, non-positive or below-minimum numeric inputs, missing token, or non-admin access.

Unsupported behaviours such as code length, code character set, trimming policy, date validity beyond required presence, upper numeric limits, and exact error bodies are excluded from normative coverage.

## Coverage Decisions

- Normative API coverage includes access control, list, add, delete, required fields, enum validation, uniqueness, and lower-bound numeric constraints.
- UI admin coverage is excluded from execution if Web Admin is unavailable; this should be recorded as a blocked UI condition during execution, not as an implementation inference.
- BVA is limited to lower-bound numeric constraints: `discount_value > 0`, `min_order_amount >= 0`, and `max_uses_per_user >= 1`.
- Positive and validation CRUD tests are designed but execution is blocked when no valid admin token exists.
- Setup credentials are not modeled as a domain partition because they are environment setup data, not a FR-17 functional rule.

## Human Review - Phase 3

- Reviewer: Nguyen Thanh Tien
- Review Date and Time: 2026-06-26 11:12
- Review Scope: FR-17 Domain Modeling
- Human Review Status: Completed
- Approved for BVA: Yes
- Approved for Test-Case Derivation: Yes
- Approved for Test Execution: Yes

## Human Corrections

- Removed `FR17-R12` references because setup credentials are not a normative FR-17 requirement.
- Updated `AUTH-ADMIN-V01` to depend on a successful admin login rather than a hard-coded credential rule.
- Added separate invalid partitions for zero and negative `discount_value`.
- Added `CREATE-V01` as the nominal coupon creation API contract partition.
- Kept UI applicability where relevant but clarified that unavailable Web Admin UI should be handled as a blocked execution condition.
- Confirmed that update/edit coupon is excluded because README and API specification only define add, view, and delete.
