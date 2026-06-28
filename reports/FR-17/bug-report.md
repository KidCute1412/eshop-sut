# Bug Report - FR-17 Coupon Management CRUD

## BUG-FR17-001: Non-admin User Can Create and Delete Coupons Through Admin API

- Status: Confirmed
- Severity: High
- Feature: FR-17 Coupon Management CRUD
- Requirements: FR17-R11, FR17-API03, FR17-API04
- Related Test Cases: [FR17-DT-003](./test-cases.md#fr17-dt-003), [FR17-DT-004](./test-cases.md#fr17-dt-004)
- Endpoints:
  - `POST http://localhost:3000/api/admin/coupons`
  - `DELETE http://localhost:3000/api/admin/coupons/:id`

### Description

Admin coupon APIs allow a non-admin authenticated user token to create and delete coupons. These endpoints should require a valid JWT with Admin role.

### Steps to Reproduce

1. Log in as an ordinary non-admin user and obtain a bearer token.
2. Send `POST http://localhost:3000/api/admin/coupons` with the non-admin bearer token and a valid coupon body:

```json
{
  "code": "FR17_003",
  "type": "percent",
  "discount_value": 15,
  "min_order_amount": 200000,
  "expired_at": "2027-12-31",
  "max_uses_per_user": 1
}
```

3. Send `DELETE http://localhost:3000/api/admin/coupons/6` with the non-admin bearer token.
4. Observe the HTTP status and JSON response.

### Expected Result

Both requests are rejected because the caller is authenticated as a non-admin user.

### Actual Result

The non-admin create request returned `200 OK` with `{"message":"Coupon created","id":6}`. The non-admin delete request returned `200 OK` with `{"message":"Coupon deleted"}`.

### Evidence

- [Non-admin create coupon](./evidence/FR17-DT-003.png)
- [Non-admin delete coupon](./evidence/FR17-DT-004.png)

### GitHub Issue

- [GitHub Issue Link](https://github.com/KidCute1412/eshop-sut/issues/43#issue-4761290396)

## BUG-FR17-002: Coupon Create API Accepts Missing Required Fields

- Status: Confirmed
- Severity: High
- Feature: FR-17 Coupon Management CRUD
- Requirements: FR17-R04, FR17-R08
- Related Test Cases: [FR17-DT-010](./test-cases.md#fr17-dt-010), [FR17-DT-012](./test-cases.md#fr17-dt-012)
- Endpoint: `POST http://localhost:3000/api/admin/coupons`

### Description

The coupon create API reports successful creation when required fields are omitted from the request body.

### Steps to Reproduce

1. Send `POST http://localhost:3000/api/admin/coupons` with `code` omitted:

```json
{
  "type": "fixed",
  "discount_value": 50000,
  "expired_at": "2027-12-31",
  "min_order_amount": 0,
  "max_uses_per_user": 1
}
```

2. Send `POST http://localhost:3000/api/admin/coupons` with `expired_at` omitted:

```json
{
  "code": "FR17_NOEXPIRED_001",
  "type": "percent",
  "discount_value": 15,
  "min_order_amount": 200000,
  "max_uses_per_user": 1
}
```

3. Observe the HTTP status and JSON response.

### Expected Result

Both requests are rejected because `code` and `expired_at` are required coupon fields.

### Actual Result

The request without `code` returned `200 OK` with `{"message":"Coupon created","id":10}`. The request without `expired_at` returned `200 OK` with `{"message":"Coupon created","id":12}`.

### Evidence

- [Missing code](./evidence/FR17-DT-010.png)
- [Missing expiration date](./evidence/FR17-DT-012.png)

### GitHub Issue

- [GitHub Issue Link](https://github.com/KidCute1412/eshop-sut/issues/44#issue-4761295030)

## BUG-FR17-003: Coupon Create API Accepts Unsupported Coupon Type

- Status: Confirmed
- Severity: Medium
- Feature: FR-17 Coupon Management CRUD
- Requirement: FR17-R06
- Related Test Case: [FR17-DT-011](./test-cases.md#fr17-dt-011)
- Endpoint: `POST http://localhost:3000/api/admin/coupons`

### Description

The coupon create API accepts a coupon `type` value outside the documented allowed values `percent` and `fixed`.

### Steps to Reproduce

1. Send the following request:

```json
{
  "code": "FR17_BOGUS_001",
  "type": "bogus",
  "discount_value": 15,
  "expired_at": "2027-12-31",
  "min_order_amount": 200000,
  "max_uses_per_user": 1
}
```

2. Observe the HTTP status and JSON response.

### Expected Result

The request is rejected because `type` is not `percent` or `fixed`.

### Actual Result

The API returned `200 OK` with `{"message":"Coupon created","id":11}`.

### Evidence

- [Unsupported type](./evidence/FR17-DT-011.png)

### GitHub Issue

- [GitHub Issue Link](https://github.com/KidCute1412/eshop-sut/issues/45#issue-4761303402)

## BUG-FR17-004: Coupon Create API Accepts Invalid Numeric Coupon Values

- Status: Confirmed
- Severity: High
- Feature: FR-17 Coupon Management CRUD
- Requirements: FR17-R07, FR17-R09, FR17-R10
- Related Test Cases: [FR17-DT-013](./test-cases.md#fr17-dt-013), [FR17-BVA-001](./test-cases.md#fr17-bva-001), [FR17-BVA-004](./test-cases.md#fr17-bva-004), [FR17-BVA-007](./test-cases.md#fr17-bva-007)
- Endpoint: `POST http://localhost:3000/api/admin/coupons`

### Description

The coupon create API accepts numeric values that violate documented lower-bound rules for `discount_value`, `min_order_amount`, and `max_uses_per_user`.

### Tested Variants

| Test Case    | Invalid Field       | Invalid Value | Violated Rule                       | Actual Result                  |
| ------------ | ------------------- | ------------: | ----------------------------------- | ------------------------------ |
| FR17-DT-013  | `discount_value`    |          `-1` | Discount value must be positive     | `200 OK` with success response |
| FR17-BVA-001 | `discount_value`    |           `0` | Discount value must be positive     | `200 OK` with success response |
| FR17-BVA-004 | `min_order_amount`  |          `-1` | Minimum order amount must be `>= 0` | `200 OK` with success response |
| FR17-BVA-007 | `max_uses_per_user` |           `0` | Max uses per user must be `>= 1`    | `200 OK` with success response |

### Steps to Reproduce

1. Prepare a complete coupon create request with a fresh controlled code.
2. Use one invalid numeric value from the table above.
3. Send `POST http://localhost:3000/api/admin/coupons`.
4. Observe the HTTP status and JSON response.

### Expected Result

The API rejects every coupon request that violates the documented numeric constraints.

### Actual Result

Every tested invalid numeric value was accepted with `200 OK`, the success message `Coupon created`, and an `id` value.

### Evidence

- [Negative discount value](./evidence/FR17-DT-013.png)
- [Zero discount value](./evidence/FR17-BVA-001.png)
- [Negative minimum order amount](./evidence/FR17-BVA-004.png)
- [Zero max uses per user](./evidence/FR17-BVA-007.png)

### GitHub Issue

- [GitHub Issue Link](https://github.com/KidCute1412/eshop-sut/issues/46#issue-4761305573)

## Human Review

- Reviewer: Nguyen Thanh Tien
- Review Date and Time: 2026-06-27 09:20 GMT+7
- Human Review Status: Completed
- Human Corrections: Reviewed failed FR-17 cases, grouped related failures, and confirmed 4 bug records.
