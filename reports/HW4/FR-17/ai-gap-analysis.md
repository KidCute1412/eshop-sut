# AI Gap Analysis - FR-17 Coupon Management

## Human-Reviewed Fixes

| Area | AI / first-pass issue | Human correction | Why AI missed it |
| --- | --- | --- | --- |
| Admin credentials | Setup references were inconsistent (`admin123` vs `Admin123!`). | Seed data was checked; final fixture uses `admin@eshop.com` / `Admin123!`. | The model followed a secondary setup note instead of verifying the seeded database. |
| Coupon tab selector | Text selectors are brittle because the repo content is mojibake and the app lacks stable IDs. | The final helper clicks the fourth sidebar item and then asserts the coupon form is visible. | The model over-trusted visible text without considering encoding drift and missing test IDs. |
| CRUD assumption | HW02 names the feature CRUD, but the actual UI only implements create/list/delete for coupons. | No edit/update coupon test was automated; the case is documented as not automatable. | The model inferred a standard CRUD flow from the feature title instead of checking the actual UI. |
| Backend confirmation | A purely UI-based create assertion could miss a failed POST followed by stale data. | The final spec waits for POST/DELETE `/api/admin/coupons` responses and checks rows. | First-pass browser tests often assert only DOM reflection and skip network contract checks. |

## Review Result

- Approved: Yes.
- Final FR-17 result: 36/36 browser executions passed.
