# FR17 - Coupon management CRUD API Mapping

| Field | Value |
|---|---|
| Feature | FR-17 Coupon management CRUD |
| Pool | C - Web Admin |
| Primary endpoints | GET /api/coupons; POST /api/admin/coupons; DELETE /api/admin/coupons/:id |
| Actor | Admin |
| Authentication | Valid JWT with role=admin required by FR-12/SEC-03 |
| Request body | `code`, `type`, `discount_value`, `expired_at`, `min_order_amount`, `max_uses_per_user` |
| Source of truth | `README.md` FR-12/FR-17, SEC-02/SEC-03/SEC-05; `api_specification.md` 5.2, 6.4 |
| Key rules | Admin can add/view/delete coupons; required fields; `code` unique; `type` percent/fixed; positive discount; `min_order_amount >= 0`; `max_uses_per_user >= 1` |
| Documented ambiguity | `api_specification.md` lists `GET /api/coupons` as admin endpoint with Authorization header, while route path is not under `/api/admin`; FR-12 still requires admin role for admin coupon management. |
