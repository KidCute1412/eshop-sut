# Boundary Value Analysis - FR-17 Coupon Management CRUD

## Boundary Values

| Boundary ID           | Variable            | Rule              | Test Basis           | Test Basis Reference                                                      | Boundary Type                           | On Point | Off Point | In Point | Selected Value | Expected Classification | Partition Covered | Justification                                                                          |
| --------------------- | ------------------- | ----------------- | -------------------- | ------------------------------------------------------------------------- | --------------------------------------- | -------- | --------- | -------- | -------------- | ----------------------- | ----------------- | -------------------------------------------------------------------------------------- |
| FR17-DISCOUNT-POS-B01 | `discount_value`    | Must be positive. | Official requirement | `requirement-analysis.md` - FR17-R07; `domain-testing.md` - DISCOUNT-I01  | Lower-only exclusive minimum above 0    | 1        | 0         | 2        | 0              | Invalid                 | DISCOUNT-I01      | Zero is not positive.                                                                  |
| FR17-DISCOUNT-POS-B02 | `discount_value`    | Must be positive. | Official requirement | `requirement-analysis.md` - FR17-R07; `domain-testing.md` - DISCOUNT-V01  | Lower-only valid minimum                | 1        | 0         | 2        | 1              | Valid                   | DISCOUNT-V01      | One is the smallest positive integer representative.                                   |
| FR17-DISCOUNT-POS-B03 | `discount_value`    | Must be positive. | Official requirement | `requirement-analysis.md` - FR17-R07; `domain-testing.md` - DISCOUNT-V01  | Lower-only in-point above valid minimum | 1        | 0         | 2        | 2              | Valid                   | DISCOUNT-V01      | Two is the adjacent valid in-point above the smallest positive integer representative. |
| FR17-MINORDER-B01     | `min_order_amount`  | Must be `>= 0`.   | Official requirement | `requirement-analysis.md` - FR17-R09; `domain-testing.md` - MIN-ORDER-I01 | Lower-only inclusive minimum            | 0        | -1        | 1        | -1             | Invalid                 | MIN-ORDER-I01     | `-1` is immediately below the inclusive minimum.                                       |
| FR17-MINORDER-B02     | `min_order_amount`  | Must be `>= 0`.   | Official requirement | `requirement-analysis.md` - FR17-R09; `domain-testing.md` - MIN-ORDER-V01 | Lower-only inclusive minimum            | 0        | -1        | 1        | 0              | Valid                   | MIN-ORDER-V01     | `0` is the on-point minimum.                                                           |
| FR17-MINORDER-B03     | `min_order_amount`  | Must be `>= 0`.   | Official requirement | `requirement-analysis.md` - FR17-R09; `domain-testing.md` - MIN-ORDER-V01 | Lower-only in-point above minimum       | 0        | -1        | 1        | 1              | Valid                   | MIN-ORDER-V01     | `1` is the adjacent valid in-point above the inclusive minimum.                        |
| FR17-MAXUSES-B01      | `max_uses_per_user` | Must be `>= 1`.   | Official requirement | `requirement-analysis.md` - FR17-R10; `domain-testing.md` - MAX-USES-I01  | Lower-only inclusive minimum            | 1        | 0         | 2        | 0              | Invalid                 | MAX-USES-I01      | `0` is immediately below the inclusive minimum.                                        |
| FR17-MAXUSES-B02      | `max_uses_per_user` | Must be `>= 1`.   | Official requirement | `requirement-analysis.md` - FR17-R10; `domain-testing.md` - MAX-USES-V01  | Lower-only inclusive minimum            | 1        | 0         | 2        | 1              | Valid                   | MAX-USES-V01      | `1` is the on-point minimum.                                                           |
| FR17-MAXUSES-B03      | `max_uses_per_user` | Must be `>= 1`.   | Official requirement | `requirement-analysis.md` - FR17-R10; `domain-testing.md` - MAX-USES-V01  | Lower-only in-point above minimum       | 1        | 0         | 2        | 2              | Valid                   | MAX-USES-V01      | `2` is the adjacent valid in-point above the inclusive minimum.                        |

## Non-BVA Domains

- Coupon code uniqueness, required code presence, type enum, date presence, auth role, and delete id existence are categorical/state domains.
- Percent vs fixed is an unordered category and remains Domain Testing.
- Coupon `code` maximum length, allowed characters, trimming, and case sensitivity are unspecified, so no code-related BVA is created.
- Expiration date format and past/future validity are insufficiently specified for BVA; only date presence is normative.
- No upper-bound BVA is created for `discount_value`, `min_order_amount`, or `max_uses_per_user` because the requirements omit maximum values.

## Coverage Decisions

- BVA uses integer representatives because the requirement and API examples use integer values.
- `discount_value` is treated as a positive numeric domain with the smallest practical integer representative `1`.
- `min_order_amount` uses lower-bound values `-1`, `0`, and `1`.
- `max_uses_per_user` uses lower-bound values `0`, `1`, and `2`.
- These BVA values are used in coupon create requests with all unrelated fields kept nominal.

## Human Review - Phase 4

- Reviewer: Nguyen Thanh Tien
- Review Date and Time: 2026-06-26 11:15
- Review Scope: FR-17 Boundary Value Analysis
- Human Review Status: Completed
- Missing Boundaries Added: None
- Duplicate Boundaries Removed: None
- Approved for Test-Case Derivation: Yes
- Approved for Test Execution: Yes

## Human Corrections

- Added `min+1` in-point values for all documented lower-bound numeric domains.
- Linked every boundary value to the reviewed `requirement-analysis.md` rule and `domain-testing.md` partition.
- Confirmed that no upper-bound BVA is possible because no maximum values are documented.
- Confirmed that coupon code, type, date presence, auth role, and delete id existence remain Domain Testing domains rather than BVA domains.
