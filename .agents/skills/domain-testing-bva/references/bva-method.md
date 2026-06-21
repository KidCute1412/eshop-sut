# Boundary Value Analysis Method

## Use BVA Only When Ordered or Bounded

Apply BVA to numeric ranges, string lengths, dates, counts, attempt limits, quantities, capacities, and ordered state progressions. Do not apply numeric boundary sets to unordered categories such as `percent` vs `fixed` or `admin` vs `user`.

## Boundary Set

For inclusive min/max ranges, consider:

- `min-1`
- `min`
- `min+1`
- nominal
- `max-1`
- `max`
- `max+1`

For lower-only constraints, consider `min-1`, `min`, `min+1`, and a nominal valid value. For upper-only constraints, consider a nominal valid value, `max-1`, `max`, and `max+1`.

## Common EShop Boundaries

- Password minimum length: 7, 8, 9 characters when min is 8.
- Lockout attempts: 2, 3, 4 when threshold is 3.
- Lockout duration: before, at, after expiration.
- Quantity minimum: 0, 1, 2.
- Coupon minimum order amount: threshold-1, threshold, threshold+1.
- Coupon max uses per user: max-1, max, max+1.
- Date expiration: before, on, after expiration date, based on requirement semantics.
- Product price: 0, 1, and negative for positive-only constraints.
- `max_uses_per_user`: 0, 1, 2 when minimum is 1.

## BVA Table Fields

Record:

- Variable.
- Boundary rule.
- Boundary source.
- Test values.
- Expected classification.
- Justification.
- Requirement/code reference.

## Classification

A BVA test is justified when the objective is to test a boundary or immediately adjacent value. If the case only samples a category with no ordering, classify it as Domain Testing.
