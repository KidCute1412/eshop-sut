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

## Supported Boundary Types

- Lower-only and upper-only constraints.
- Inclusive ranges and domain precision.
- Counts, lengths, quantities, attempts, and capacities.
- Dates and times immediately before, at, and after a documented cutoff.
- Ordered public state transitions when the requirement defines an order.

## BVA Table Fields

Record:

- Boundary ID, variable, and rule.
- Test basis and Test Basis Reference.
- On point, off point, and in point when relevant.
- Selected values, expected classification, and justification.

## Classification

A BVA test is justified when the objective is to test a boundary or immediately adjacent value. If the case only samples a category with no ordering, classify it as Domain Testing.
