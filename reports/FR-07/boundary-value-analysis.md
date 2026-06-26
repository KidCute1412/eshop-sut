# Boundary Value Analysis - FR-07 Shopping Cart

## Boundary Values

| Boundary ID            | Variable                   | Rule                                            | Test Basis                   | Test Basis Reference                                          | Boundary Type                | On Point | Off Point | In Point | Selected Value | Expected Classification | Related Partition | Justification                                          |
| ---------------------- | -------------------------- | ----------------------------------------------- | ---------------------------- | ------------------------------------------------------------- | ---------------------------- | -------- | --------- | -------- | -------------- | ----------------------- | ----------------- | ------------------------------------------------------ |
| FR07-SETUP-QTY-MIN-B01 | Add-to-cart setup quantity | Quantity must be a positive integer, minimum 1. | Supporting setup requirement | `requirement-analysis.md` - FR07-SETUP01; `README.md` - FR-06 | Lower-only inclusive minimum | 1        | 0         | 2        | 0              | Invalid                 | SETUP-QTY-I01     | `0` is immediately below the minimum positive integer. |
| FR07-SETUP-QTY-MIN-B02 | Add-to-cart setup quantity | Quantity must be a positive integer, minimum 1. | Supporting setup requirement | `requirement-analysis.md` - FR07-SETUP01; `README.md` - FR-06 | Lower-only inclusive minimum | 1        | 0         | 2        | 1              | Valid                   | SETUP-QTY-V01     | `1` is the inclusive on-point minimum.                 |
| FR07-SETUP-QTY-MIN-B03 | Add-to-cart setup quantity | Quantity must be a positive integer, minimum 1. | Supporting setup requirement | `requirement-analysis.md` - FR07-SETUP01; `README.md` - FR-06 | Lower-only inclusive minimum | 1        | 0         | 2        | 2              | Valid                   | SETUP-QTY-V01     | `2` is the adjacent valid in-point above the minimum.  |

## Non-BVA Domains

- Product identity, delete confirmation, badge visibility, breadcrumbs, labels, navigation highlight, logout label, and API authorization are categorical, not numeric/ordered boundaries.
- Duplicate add is a count/state relationship, but the requirement only distinguishes same-product duplicate merge; it does not define a broader numeric range.
- Decimal, negative, non-numeric, and empty setup quantity values are Domain Testing invalid partitions, not separate BVA boundary points.
- Cart line count, maximum cart quantity, stock, and API response status ranges are unspecified.
- Cart total and line total calculation are arithmetic correctness checks, but no numeric boundary such as maximum price, decimal precision, or rounding threshold is documented.

## Coverage Decisions

- Quantity boundary tests are executed through the public UI add-to-cart flow where the setup quantity control is observable.
- API quantity BVA is not normative because `api_specification.md` provides a sample quantity in the `POST /api/cart` body but does not define min/max/validation behaviour for API quantity.
- The BVA model is lower-bound only because no documented upper bound exists.
- The selected values are `0`, `1`, and `2`, covering `min-1`, `min`, and `min+1`.
- The setup quantity boundary is used to prepare FR-07 cart states, not to redefine FR-07 cart-page quantity adjustment.

## Human Review - Phase 4

- Reviewer: Nguyen Thanh Tien
- Review Date and Time: 2026-06-26 19:00
- Review Scope: FR-07 Boundary Value Analysis
- Human Review Status: Completed
- Missing Boundaries Added: None
- Duplicate Boundaries Removed: None
- Approved for Test-Case Derivation: Yes
- Approved for Test Execution: Yes

## Human Corrections

- Linked the BVA model to supporting setup rule `FR07-SETUP01` instead of treating product-detail quantity as a standalone FR-07 cart-page rule.
- Renamed boundary IDs from `FR07-QTY-MIN-*` to `FR07-SETUP-QTY-MIN-*` to avoid confusion with cart-page plus/minus quantity controls.
- Added related Domain Testing partition references: `SETUP-QTY-I01` for value `0` and `SETUP-QTY-V01` for values `1` and `2`.
- Clarified that decimal, negative, non-numeric, and empty quantity values belong to Domain Testing invalid partitions, not BVA boundary points.
- Confirmed that no upper-bound BVA is created because no maximum quantity, stock limit, cart capacity, or price precision limit is documented.
- Confirmed that API quantity BVA is excluded because the API specification provides only a sample quantity and no numeric validation boundary.
