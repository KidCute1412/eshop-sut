# Automation Test Cases - FR-17 Coupon Management

Seeded from `reports/HW2/FR-17/test-cases.md`. Twelve cases were selected around coupon creation, deletion, required fields, duplicate code, fixed/percent type handling, and requirement-based numeric lower boundaries.

| ID | Type | Steps | Test Data | Expected Result | Assertion Pattern(s) | Automatable | Spec File |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FR17-DT-001 | Positive | Login admin, create percent coupon | `FR17-DT-001` | Coupon appears in table | API response, visibility | Yes | `FR-17/tests/fr-17-coupons.spec.js` |
| FR17-DT-002 | Positive | Login admin, create fixed coupon | `FR17-DT-002` | Coupon appears in table | API response, visibility | Yes | `FR-17/tests/fr-17-coupons.spec.js` |
| FR17-DT-003 | Edge | Create coupon with minimum order zero | `FR17-DT-003` | Coupon appears in table | API response, visibility | Yes | `FR-17/tests/fr-17-coupons.spec.js` |
| FR17-DT-004 | Edge | Create coupon with max uses one | `FR17-DT-004` | Coupon appears in table | API response, visibility | Yes | `FR-17/tests/fr-17-coupons.spec.js` |
| FR17-DT-005 | Positive | Create coupon then delete it | `FR17-DT-005` | Row removed after DELETE | API response, count | Yes | `FR-17/tests/fr-17-coupons.spec.js` |
| FR17-DT-006 | Negative | Submit coupon form without code | `FR17-DT-006` | Browser required validation blocks submit | Native validity state | Yes | `FR-17/tests/fr-17-coupons.spec.js` |
| FR17-DT-007 | Negative | Submit coupon form without discount | `FR17-DT-007` | Browser required validation blocks submit | Native validity state | Yes | `FR-17/tests/fr-17-coupons.spec.js` |
| FR17-DT-008 | Negative | Submit coupon form without expiry date | `FR17-DT-008` | Browser required validation blocks submit | Native validity state | Yes | `FR-17/tests/fr-17-coupons.spec.js` |
| FR17-DT-009 | Negative | Create duplicate coupon code | `FR17-DT-009` | Server rejects duplicate code | API response | Yes | `FR-17/tests/fr-17-coupons.spec.js` |
| FR17-BVA-001 | Edge / Negative | Create coupon with `discount_value = 0` | `FR17-BVA-001` | Coupon creation is rejected because `discount_value` must be `> 0` | Native validity/API response, absence | Yes | `FR-17/tests/fr-17-coupons.spec.js` |
| FR17-BVA-002 | Edge / Negative | Create coupon with `min_order_amount = -1` | `FR17-BVA-002` | Coupon creation is rejected because `min_order_amount` must be `>= 0` | Native validity/API response, absence | Yes | `FR-17/tests/fr-17-coupons.spec.js` |
| FR17-BVA-003 | Edge / Negative | Create coupon with `max_uses_per_user = 0` | `FR17-BVA-003` | Coupon creation is rejected because `max_uses_per_user` must be `>= 1` | Native validity/API response, absence | Yes | `FR-17/tests/fr-17-coupons.spec.js` |

## Boundary Pair Coverage

| Field | Reject boundary | Success boundary | Automated by |
| --- | --- | --- | --- |
| `discount_value` | `0` -> reject | `> 0` -> success | `FR17-BVA-001`; `FR17-DT-001`, `FR17-DT-002`, `FR17-DT-003`, `FR17-DT-004` |
| `min_order_amount` | `-1` -> reject | `0` -> success | `FR17-BVA-002`; `FR17-DT-003` |
| `max_uses_per_user` | `0` -> reject | `1` -> success | `FR17-BVA-003`; `FR17-DT-004` |

## Not Automated

None. All 12 selected FR-17 test cases were automated.

## Human Review

- Reviewer: Nguyen Thanh Tien
- Review Date and Time: 2026-08-06T14:03:05Z
- Confirmed at least 12 cases selected with a genuine positive/negative/edge mix: Yes
- Confirmed every "Not Automated" row has a real, specific reason: Yes
