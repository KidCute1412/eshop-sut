# EShop API Guide for HW6

Use this guide with `README.md`, `api_specification.md`, and `setup_guide.md`.

## Base Environment

- Backend base URL: `http://localhost:3000`
- Backend startup: `cd backend`, then `npm install`, optionally `node database.js`, then
  `node server.js`.
- Seeded user: `test@eshop.com` / `Test1234!`
- Seeded admin in `README.md`: `admin@eshop.com` / `Admin123!`
- `setup_guide.md` contains an older/lowercase admin password note. Treat this as a contradiction
  to verify during environment setup, not as an excuse to invent credentials.

## Pool A Candidates

- FR-01 registration: `POST /api/register`
- FR-02 login/lockout: `POST /api/login`
- FR-03 forgot/reset password: `POST /api/forgot-password`, `POST /api/reset-password`
- FR-04 profile: `GET /api/users/me`, `PUT /api/users/me`
- FR-05 product listing/search: `GET /api/products?search=keyword`
- FR-06 product detail: `GET /api/products/:id`

## Pool B Candidates

- FR-07 cart: `GET /api/cart`, `POST /api/cart`
- FR-08 checkout: `POST /api/checkout`
- FR-09 coupon application: `POST /api/apply-coupon`
- FR-10/FR-11 order history/detail/cancel: `GET /api/orders/my-orders`, `GET /api/orders/:id`,
  `PUT /api/orders/:id/cancel`

## Pool C Candidates

- FR-12 admin access control applies to all `/api/admin/*` and mutating product/category/coupon
  APIs.
- FR-14 categories: `GET /api/categories`, `POST /api/categories`, `PUT /api/categories/:id`,
  `DELETE /api/categories/:id`
- FR-15 products: `POST /api/products`, `PUT /api/products/:id`, `DELETE /api/products/:id`
- FR-17 coupons: `GET /api/coupons`, `POST /api/admin/coupons`,
  `DELETE /api/admin/coupons/:id`
- FR-18 admin orders: `GET /api/admin/orders`, `PUT /api/admin/orders/:id/status`
- FR-19 admin users: `GET /api/admin/users`, `DELETE /api/admin/users/:id`

## Security Rules to Map

- SEC-01: passwords must not be stored as plaintext. API tests may only verify observable leakage;
  do not inspect the database unless the assignment explicitly permits it.
- SEC-02: protected APIs require a valid JWT.
- SEC-03: admin APIs require role `admin`, not merely any token.
- SEC-04: user-controlled data displayed in UI must be escaped. For API testing, include payloads
  that later reveal XSS risk where the API stores unsafe values.
- SEC-05: database queries must be parameterized. Include SQL injection probes through public API
  inputs and verify no auth bypass, data leakage, or server crash.
- SEC-06: profile update must not allow client-side role changes.
- SEC-07: OTP reset token must be six digits, time-limited, scoped to the email, and invalidated
  after use.

## State-Machine Rules

Order statuses are `pending`, `confirmed`, `shipping`, `delivered`, and `canceled`.

Allowed transitions:

- `pending -> confirmed -> shipping -> delivered`
- `pending -> canceled`
- `confirmed -> canceled`

Final states:

- `delivered` cannot transition to any other state.
- `canceled` cannot transition to any other state.

Other important rule:

- User cannot cancel once an order is in `shipping`; only admin may operate from that state.

For state APIs, include both valid transition cases and invalid transition attempts. Preserve setup
steps that create or move an order into the required state.
