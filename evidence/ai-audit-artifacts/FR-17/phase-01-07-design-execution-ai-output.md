# FR-17 Phase 1-7 Reconstructed AI Output Summary

## Phase Summary

### Phase 1-2: Feature Intake and Black-box Basis

FR-17 was analyzed as Coupon Management CRUD for the Web Admin/API surface. The approved bases were the official assignment materials, FR-12 access control, FR-17 coupon requirements, relevant API specification sections, and setup guidance. The analysis retained ambiguities such as exact response bodies, exact UI labels, update/edit scope, coupon code trimming/case sensitivity, and upper numeric bounds.

### Phase 3: Domain Modeling

The domain model separated authentication/authorization state, coupon list/create/delete behaviour, coupon field presence, duplicate code handling, allowed coupon types, numeric discount/min-order/use-count constraints, and date presence. Public admin API access and non-admin access were kept as separate partitions because they produce different observable risks.

### Phase 4: Boundary Value Analysis

BVA focused on ordered or bounded numeric fields: positive `discount_value`, `min_order_amount >= 0`, and `max_uses_per_user >= 1`. Categorical fields such as coupon `type` and authorization role were kept as Domain Testing, not BVA.

### Phase 5-7: Test Cases, Execution, Evidence, and Bugs

The current test suite contains 22 executed cases:

- Pass: 13
- Fail: 9
- Blocked: 0

Confirmed bug reports:

- `BUG-FR17-001`: non-admin user can create and delete coupons through admin API.
- `BUG-FR17-002`: create API accepts missing required coupon fields.
- `BUG-FR17-003`: create API accepts unsupported coupon type.
- `BUG-FR17-004`: create API accepts invalid numeric coupon values.

## Human Review and Corrections Reflected

- Requirement analysis, domain modeling, BVA, and test execution were marked human-reviewed in the FR-17 reports.
- Human corrections clarified access-control expectations, API-only execution scope where UI was unavailable, boundary scope, and bug consolidation.
- Runtime results were recorded from public API execution evidence.

## Integrity Notes

- No implementation source, database schema, internal tests, controllers, services, routes, middleware, or models were used as oracle.
- Expected results were based on requirements and API specification.
- Issue links remain pending unless real GitHub issues are created.
