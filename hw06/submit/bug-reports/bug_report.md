# HW06 Bug Report

## BUG-FR09-001 - Percent coupon formula returns negative discount

- Endpoint: `POST /api/apply-coupon`
- Evidence test cases: FR09-001, FR09-004, FR09-006, FR09 human formula oracle case
- Expected: `SAVE10` on `500000` should discount `50000` and final amount should be `450000`.
- Actual: implementation computes `Math.floor(total_amount * (1 - coupon.discount_value))`; with discount_value `10`, discount becomes `-4500000` and final amount becomes `5000000`.
- Source: `backend/server.js`, percent branch in `/api/apply-coupon`.
- Severity: High.
- GitHub issue screenshot/link: TODO - must be attached after creating the issue on GitHub.

## BUG-FR13-001 - Admin orders endpoint accepts any valid user token

- Endpoint: `GET /api/admin/orders`
- Evidence test cases: FR13-006 through FR13-010 and human IDOR/role tests
- Expected: only admin users can access all orders; normal user token should receive 403.
- Actual: `authenticateToken` verifies JWT only; `/api/admin/orders` never checks `req.user.role === "admin"`.
- Source: `backend/server.js`, `app.get("/api/admin/orders", authenticateToken, ...)`.
- Severity: Critical.
- GitHub issue screenshot/link: TODO - must be attached after creating the issue on GitHub.

## BUG-FR09-002 - Coupon application is public despite using user_id-sensitive rules

- Endpoint: `POST /api/apply-coupon`
- Expected: coupon usage checks should be tied to authenticated user identity, not client-supplied `user_id`.
- Actual: endpoint is public and trusts optional `user_id` from body.
- Severity: Medium.
- GitHub issue screenshot/link: TODO - must be attached after creating the issue on GitHub.
