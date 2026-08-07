# Automation Test Cases - FR-17 Coupon Management

Seeded from `reports/HW2/FR-17/test-cases.md`. Twelve cases were selected around coupon creation, deletion, required fields, duplicate code, expired display, fixed/percent type handling, uppercase transform, and numeric boundaries.

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
| FR17-BVA-001 | Edge | Create already-expired coupon | `FR17-BVA-001` | Expired label visible | Visibility | Yes | `FR-17/tests/fr-17-coupons.spec.js` |
| FR17-BVA-002 | Edge | Create large fixed discount | `FR17-BVA-002` | Coupon appears in table | API response, visibility | Yes | `FR-17/tests/fr-17-coupons.spec.js` |
| FR17-BVA-003 | Edge | Enter lowercase code | `FR17-BVA-003` | Uppercase code appears | Text/visibility | Yes | `FR-17/tests/fr-17-coupons.spec.js` |

## Not Automated

| ID | Reason |
| --- | --- |
| Edit coupon flow | Not automated because the actual Admin UI exposes create/list/delete only; there is no coupon edit/update control. |

## Human Review

- Reviewer: Nguyen Thanh Tien
- Review Date and Time: 2026-08-06T14:03:05Z
- Confirmed at least 12 cases selected with a genuine positive/negative/edge mix: Yes
- Confirmed every "Not Automated" row has a real, specific reason: Yes
