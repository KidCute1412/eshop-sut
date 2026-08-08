# Automation Test Cases - FR-07 Shopping Cart

Seeded from `reports/HW2/FR-07/test-cases.md`. Fourteen cases were selected around empty cart, add-to-cart, duplicate product consolidation, remove confirmation, navigation, checkout redirect, totals, exact headers, quantity display, and quantity controls.

| ID | Type | Steps | Test Data | Expected Result | Assertion Pattern(s) | Automatable | Spec File |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FR07-DT-001 | Positive | Open cart with no added product | `FR07-DT-001` | Empty-cart state and continue link visible | Visibility, count | Yes | `FR-07/tests/fr-07-cart.spec.js` |
| FR07-DT-002 | Positive | Add first product, open cart | `FR07-DT-002` | One cart row appears | Count | Yes | `FR-07/tests/fr-07-cart.spec.js` |
| FR07-DT-003 | Positive | Add two distinct products, open cart | `FR07-DT-003` | Two cart rows appear | Count | Yes | `FR-07/tests/fr-07-cart.spec.js` |
| FR07-DT-004 | Edge | Add same product twice, open cart | `FR07-DT-004` | One row appears and quantity is `2` | Count, text content | Yes | `FR-07/tests/fr-07-cart.spec.js` |
| FR07-DT-005 | Positive | Add one product, click remove, confirm deletion | `FR07-DT-005` | Confirmation dialog appears before deletion; after Confirm, cart returns to empty state | Dialog, count, visibility | Yes | `FR-07/tests/fr-07-cart.spec.js` |
| FR07-DT-006 | Positive | Add two products, click remove on first row, confirm deletion | `FR07-DT-006` | Confirmation dialog appears before deletion; after Confirm, one row remains | Dialog, count | Yes | `FR-07/tests/fr-07-cart.spec.js` |
| FR07-DT-007 | Negative | Guest adds product and proceeds checkout | `FR07-DT-007` | Alert accepted and user redirects to Login | URL | Yes | `FR-07/tests/fr-07-cart.spec.js` |
| FR07-DT-008 | Positive | Continue shopping from empty cart | `FR07-DT-008` | Redirects to home | URL | Yes | `FR-07/tests/fr-07-cart.spec.js` |
| FR07-DT-009 | Positive | Continue shopping from non-empty cart | `FR07-DT-009` | Redirects to home | URL | Yes | `FR-07/tests/fr-07-cart.spec.js` |
| FR07-DT-010 | Positive | Add product and inspect table | `FR07-DT-010` | Exact headers are `Sản phẩm`, `Đơn giá`, `Số lượng`, `Thành tiền`, `Thao tác` | Text content | Yes | `FR-07/tests/fr-07-cart.spec.js` |
| FR07-DT-011 | Positive | Add product and inspect total | `FR07-DT-011` | Total label is exactly `Tổng cộng` | Text content, visibility | Yes | `FR-07/tests/fr-07-cart.spec.js` |
| FR07-BVA-001 | Edge | Add one product and inspect quantity cell | `FR07-BVA-001` | Quantity displays `1` | Text content | Yes | `FR-07/tests/fr-07-cart.spec.js` |
| FR07-BVA-002 | Edge | Add one product and use the `+` quantity control | `FR07-BVA-002` | `+` control is visible and increases quantity from `1` to `2` | Visibility, text content | Yes | `FR-07/tests/fr-07-cart.spec.js` |
| FR07-BVA-003 | Edge | Add same product twice and use the `-` quantity control | `FR07-BVA-003` | `-` control is visible and decreases quantity from `2` to `1` | Visibility, text content | Yes | `FR-07/tests/fr-07-cart.spec.js` |

## Not Automated

| ID | Reason |
| --- | --- |
| Custom delete confirmation cancel path | Not automated in this suite because the current web cart does not expose a confirmation dialog to cancel; the automated delete cases assert the required confirmation exists before confirming deletion. |

## Human Review

- Reviewer: Nguyen Thanh Tien
- Review Date and Time: 2026-08-06T14:03:05Z
- Confirmed at least 12 cases selected with a genuine positive/negative/edge mix: Yes, 14 cases selected after quantity-control review.
- Confirmed every "Not Automated" row has a real, specific reason: Yes
