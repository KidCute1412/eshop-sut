# Test Case Design — FR-13 Admin Dashboard

Spec reference: `README.md` FR-13 ("Hiển thị tổng doanh thu: chỉ tính tổng `total_amount` của các đơn có `status = 'delivered'`", "Hiển thị tổng số đơn hàng"), FR-12 (Access control — admin-only), UI `frontend-admin/src/App.jsx` (dashboard tab, no client-side router).

Data file: `tests/data/fr13-dashboard.json`

| TC ID | Type | Actor | Scenario | Expected (per spec) | Notes |
|---|---|---|---|---|---|
| FR13-TC01 | Positive | admin | Login as admin, open dashboard | Dashboard renders with "Tổng doanh thu" and order count cards | |
| FR13-TC02 | Positive | admin | Revenue card value vs. sum of `total_amount` for `delivered` orders only | Revenue == sum(delivered.total_amount) | **known bug**: UI computes `total_amount * 2`, revenue is exactly double the correct value |
| FR13-TC03 | Negative (Access control) | non-admin (`test@eshop.com`) | Call `GET /api/admin/orders` with a valid non-admin JWT | Should be 403 Forbidden per FR-12 | **known bug**: `authenticateToken` only checks token validity, not `role === 'admin'` — any logged-in user can read admin data |
| FR13-TC04 | Negative (Access control) | anonymous | Call `GET /api/admin/orders` with no token | 401 Unauthorized | |
| FR13-TC05 | Negative (Access control) | non-admin | Call `GET /api/admin/users` with a valid non-admin JWT | Should be 403 per FR-12 | **known bug**: same missing role check |
| FR13-TC06 | Boundary | — | Dashboard with zero delivered orders | Revenue shows 0, not NaN/undefined | |
| FR13-TC07 | Edge | admin | Orders in `pending`/`canceled` status excluded from revenue | Revenue unaffected by non-delivered orders | |
| FR13-TC08 | Positive | admin | Total order count matches count of all orders returned by `/api/admin/orders` regardless of status | count(orders) == count returned by API | |
| FR13-TC09 | UI | admin | Only one `<h1>`/page heading rule (FR-21) on the dashboard tab | Single primary heading "Dashboard" | |
| FR13-TC10 | Negative | non-admin | Login form rejects non-admin credentials with an explicit message | alert "Bạn không phải là admin!", dashboard not rendered | |
| FR13-TC11 | Edge | admin | Multiple delivered orders with varying `total_amount` (data-driven sum) | Revenue == correct arithmetic sum (still fails vs. the ×2 bug) | |
| FR13-TC12 | E2E | admin | Change an order's status to `delivered` via `PUT /api/admin/orders/:id/status`, then reload dashboard | Revenue increases by that order's `total_amount` (not ×2) | |

Total: **12 test cases** (meets the ≥ 12 minimum), split across UI dashboard rendering and API-level access-control checks (FR-12 is exercised here because the dashboard's data endpoints are the same admin APIs).
