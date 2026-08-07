# Automation Test Cases - FR-07 Shopping Cart

Seeded from `reports/HW2/FR-07/test-cases.md`. Twelve cases were selected around empty cart, add-to-cart, duplicate product rows, remove behavior, navigation, checkout redirect, totals, headers, and quantity display.

| ID | Type | Steps | Test Data | Expected Result | Assertion Pattern(s) | Automatable | Spec File |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FR07-DT-001 | Positive | Open cart with no added product | `FR07-DT-001` | Empty-cart state and continue link visible | Visibility, count | Yes | `FR-07/tests/fr-07-cart.spec.js` |
| FR07-DT-002 | Positive | Add first product, open cart | `FR07-DT-002` | One cart row appears | Count | Yes | `FR-07/tests/fr-07-cart.spec.js` |
| FR07-DT-003 | Positive | Add two distinct products, open cart | `FR07-DT-003` | Two cart rows appear | Count | Yes | `FR-07/tests/fr-07-cart.spec.js` |
| FR07-DT-004 | Edge | Add same product twice, open cart | `FR07-DT-004` | Two rows appear under current implementation | Count | Yes | `FR-07/tests/fr-07-cart.spec.js` |
| FR07-DT-005 | Positive | Add one product, remove it | `FR07-DT-005` | Cart returns to empty state | Count, visibility | Yes | `FR-07/tests/fr-07-cart.spec.js` |
| FR07-DT-006 | Positive | Add two products, remove first | `FR07-DT-006` | One row remains | Count | Yes | `FR-07/tests/fr-07-cart.spec.js` |
| FR07-DT-007 | Negative | Guest adds product and proceeds checkout | `FR07-DT-007` | Alert accepted and user redirects to Login | URL | Yes | `FR-07/tests/fr-07-cart.spec.js` |
| FR07-DT-008 | Positive | Continue shopping from empty cart | `FR07-DT-008` | Redirects to home | URL | Yes | `FR-07/tests/fr-07-cart.spec.js` |
| FR07-DT-009 | Positive | Continue shopping from non-empty cart | `FR07-DT-009` | Redirects to home | URL | Yes | `FR-07/tests/fr-07-cart.spec.js` |
| FR07-DT-010 | Positive | Add product and inspect table | `FR07-DT-010` | Five cart headers visible | Count | Yes | `FR-07/tests/fr-07-cart.spec.js` |
| FR07-DT-011 | Positive | Add product and inspect total | `FR07-DT-011` | Total amount visible | Visibility | Yes | `FR-07/tests/fr-07-cart.spec.js` |
| FR07-BVA-001 | Edge | Add one product and inspect quantity cell | `FR07-BVA-001` | Quantity displays `1` | Text content | Yes | `FR-07/tests/fr-07-cart.spec.js` |

## Not Automated

| ID | Reason |
| --- | --- |
| Quantity edit in cart | Not automated because the actual Cart page has no quantity editor; quantity is display-only after add-to-cart. |

## Human Review

- Reviewer: Nguyen Thanh Tien
- Review Date and Time: 2026-08-06T14:03:05Z
- Confirmed at least 12 cases selected with a genuine positive/negative/edge mix: Yes
- Confirmed every "Not Automated" row has a real, specific reason: Yes
