# AI Gap Analysis - FR-17 Coupon Management

## Human-Reviewed Fixes

| Area | AI / first-pass issue | Human correction | Why AI missed it |
| --- | --- | --- | --- |
| Admin credentials | Setup references were inconsistent (`admin123` vs `Admin123!`). | Seed data was checked; final fixture uses `admin@eshop.com` / `Admin123!`. | The model followed a secondary setup note instead of verifying the seeded database. |
| Coupon tab selector | Text selectors are brittle because the repo content is mojibake and the app lacks stable IDs. | The final helper clicks the fourth sidebar item and then asserts the coupon form is visible. | The model over-trusted visible text without considering encoding drift and missing test IDs. |
| CRUD assumption | HW02 names the feature CRUD, but the actual UI only implements create/list/delete for coupons. | No edit/update coupon test was automated; the case is documented as not automatable. | The model inferred a standard CRUD flow from the feature title instead of checking the actual UI. |
| Backend confirmation | A purely UI-based create assertion could miss a failed POST followed by stale data. | The final spec waits for POST/DELETE `/api/admin/coupons` responses and checks rows. | First-pass browser tests often assert only DOM reflection and skip network contract checks. |
| BVA oracle alignment | The first HW4 automation used BVA cases for expired coupon display, large fixed discount, and lowercase-to-uppercase transformation. These did not directly exercise the documented numeric lower bounds. | Replaced `FR17-BVA-001` through `FR17-BVA-003` with requirement-based boundary cases: `discount_value = 0` must reject, `min_order_amount = -1` must reject, and `max_uses_per_user = 0` must reject. Kept existing success boundaries through `FR17-DT-003` (`min_order_amount = 0`) and `FR17-DT-004` (`max_uses_per_user = 1`). | The model selected interesting observable UI behaviours, but did not prioritize the documented lower-bound constraints as the automation oracle. |
| Negative numeric assertions | A weak implementation could mark invalid numeric coupons as passing if the row appears after creation. | Added a `rejected` assertion path: native browser validation is accepted only when no POST is sent and invalid inputs exist; otherwise the POST must return HTTP `>= 400`, and the coupon code must not appear in the table. | The first pass assumed valid creation patterns and did not have a reusable negative numeric creation path. |

## Review Result

- Approved: Yes.
- Latest FR-17 multi-browser run: 36 browser executions, 30 passed, 6 failed.
- Failing cases on Chromium, Firefox, and WebKit: `FR17-BVA-001` (`discount_value = 0` accepted with HTTP 200) and `FR17-BVA-002` (`min_order_amount = -1` accepted with HTTP 200).
- Passing boundary control: `FR17-BVA-003` (`max_uses_per_user = 0`) was blocked by native UI validation before create submission.
