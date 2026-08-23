# FR17 - AI Audit

## AI Prompt

```text
You are an AI-assisted API test designer for HW6 EShop API Testing.
Use only the assignment, README.md, api_specification.md, and setup_guide.md as source of truth.
For FR17 Coupon management CRUD, analyse coupon listing, admin coupon creation, and admin coupon deletion.

Generate the initial AI candidate suite before human filtering. The suite must cover:
- missing, malformed, user-token, and admin-token access control;
- coupon list schema and create/delete success paths;
- required fields code, type, discount_value, expired_at, min_order_amount, and max_uses_per_user;
- enum, uniqueness, range, date, numeric type, null/empty, and malformed value partitions;
- boundary values for discount, minimum order amount, usage limit, and expiration date;
- security checks for SQL injection-like coupon code, script-like coupon code, and role enforcement on delete.

Return the raw output as a Markdown test-case table. Keep the original AI candidate rows even if a later human reviewer removes some of them from the final executed suite. Do not add human-added cases in this initial output.
```

## Prompt Context Given To AI

| Field                  | Value                                                                                                                                 |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Feature                | FR17 - Coupon management CRUD                                                                                                         |
| Endpoint(s)            | GET /api/coupons; POST /api/admin/coupons; DELETE /api/admin/coupons/:id                                                              |
| Tooling target         | Postman collection with Newman execution evidence                                                                                     |
| Required evidence rule | Every executed request must include `X-Student-Id` during real execution                                                              |
| Oracle rule            | Expected behaviour must come from README.md, api_specification.md, setup_guide.md, and HW6 assignment, not from implementation source |
| Raw-output status      | Preserved before human filtering and before final testcase pruning                                                                    |

## Raw AI Output - Candidate Test Cases

| ID           | Category | Objective                                            | Expected Status | Expected Response / Schema                                                                                 |
| ------------ | -------- | ---------------------------------------------------- | --------------: | ---------------------------------------------------------------------------------------------------------- |
| FR17-API-001 | Security | Reject GET coupons without token                     |             401 | Unauthorized JSON error                                                                                    |
| FR17-API-002 | Security | Reject GET coupons with malformed token              |             403 | Forbidden JSON error                                                                                       |
| FR17-API-003 | Security | Reject GET coupons with user token                   |             403 | User role cannot access admin coupon list                                                                  |
| FR17-API-004 | Security | Accept GET coupons with admin token                  |             200 | JSON array of coupons                                                                                      |
| FR17-API-005 | Schema   | GET coupons item schema                              |             200 | Each coupon has id, code, type, discount_value, min_order_amount, expired_at, is_active, max_uses_per_user |
| FR17-API-006 | Security | Reject POST coupon without token                     |             401 | Unauthorized JSON error                                                                                    |
| FR17-API-007 | Security | Reject POST coupon with malformed token              |             403 | Forbidden JSON error                                                                                       |
| FR17-API-008 | Security | Reject POST coupon with user token                   |             403 | User role cannot create admin coupon                                                                       |
| FR17-API-009 | Domain   | Create valid percent coupon                          |             200 | message='Coupon created' and numeric id                                                                    |
| FR17-API-010 | Domain   | Create valid fixed coupon                            |             200 | message='Coupon created' and numeric id                                                                    |
| FR17-API-011 | Domain   | Reject missing code                                  |             400 | Code is required                                                                                           |
| FR17-API-012 | Domain   | Reject empty code                                    |             400 | Code is required                                                                                           |
| FR17-API-013 | Domain   | Reject whitespace-only code                          |             400 | Code is required after trimming                                                                            |
| FR17-API-014 | Domain   | Reject duplicate code                                |             400 | Duplicate code rejected without server error                                                               |
| FR17-API-015 | Domain   | Reject invalid type value                            |             400 | Type must be percent or fixed                                                                              |
| FR17-API-016 | Domain   | Reject missing type                                  |             400 | Type is required                                                                                           |
| FR17-API-017 | Domain   | Reject uppercase type if enum is case-sensitive      |             400 | Type must match documented percent/fixed values                                                            |
| FR17-API-018 | Domain   | Reject missing discount_value                        |             400 | discount_value is required                                                                                 |
| FR17-API-019 | Boundary | Reject discount_value 0                              |             400 | discount_value must be positive                                                                            |
| FR17-API-020 | Boundary | Reject negative discount_value                       |             400 | discount_value must be positive                                                                            |
| FR17-API-021 | Domain   | Reject string discount_value                         |             400 | discount_value must be numeric                                                                             |
| FR17-API-022 | Boundary | Reject percent discount over 100                     |             400 | Percent discount must not exceed 100                                                                       |
| FR17-API-023 | Domain   | Reject missing expired_at                            |             400 | expired_at is required                                                                                     |
| FR17-API-024 | Domain   | Reject invalid expired_at format                     |             400 | expired_at must be valid date                                                                              |
| FR17-API-025 | Boundary | Accept future expired_at date                        |             200 | Coupon created                                                                                             |
| FR17-API-026 | Domain   | Reject missing min_order_amount                      |             400 | min_order_amount is required                                                                               |
| FR17-API-027 | Boundary | Accept min_order_amount 0                            |             200 | Coupon created                                                                                             |
| FR17-API-028 | Boundary | Reject min_order_amount -1                           |             400 | min_order_amount must be >= 0                                                                              |
| FR17-API-029 | Domain   | Reject string min_order_amount                       |             400 | min_order_amount must be numeric                                                                           |
| FR17-API-030 | Domain   | Reject missing max_uses_per_user                     |             400 | max_uses_per_user is required                                                                              |
| FR17-API-031 | Boundary | Accept max_uses_per_user 1                           |             200 | Coupon created                                                                                             |
| FR17-API-032 | Boundary | Reject max_uses_per_user 0                           |             400 | max_uses_per_user must be >= 1                                                                             |
| FR17-API-033 | Boundary | Reject max_uses_per_user -1                          |             400 | max_uses_per_user must be >= 1                                                                             |
| FR17-API-034 | Domain   | Reject string max_uses_per_user                      |             400 | max_uses_per_user must be numeric                                                                          |
| FR17-API-035 | Security | Reject SQL injection-looking coupon code safely      |             400 | No database error/server crash                                                                             |
| FR17-API-036 | Security | Reject script payload in coupon code or store safely |             400 | Unsafe display value rejected or escaped downstream                                                        |
| FR17-API-037 | Security | Reject DELETE coupon without token                   |             401 | Unauthorized JSON error                                                                                    |
| FR17-API-038 | Security | Reject DELETE coupon with user token                 |             403 | User role cannot delete admin coupon                                                                       |
| FR17-API-039 | Domain   | Delete existing coupon with admin token              |             200 | message='Coupon deleted'                                                                                   |

## Human Review Note

A human reviewer later checked these AI-generated candidates against the source of truth, execution feasibility, and assignment constraints. Some rows may have been corrected, extended, or removed in the final `test-cases.md`; this file intentionally keeps the raw AI candidate output for auditability.
