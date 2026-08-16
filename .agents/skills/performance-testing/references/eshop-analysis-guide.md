# EShop Analysis Guide for HW05

## Startup Source

From `setup_guide.md` and `api_specification.md`:

- Backend API base URL: `http://localhost:3000`.
- Frontend Web default URL: `http://localhost:5173`.
- Web Admin default URL: `http://localhost:5174`.
- Backend command: from `backend`, run `node server.js`.
- Seed/reset command: from `backend`, run `node database.js`.

Important: `backend/database.js` drops and recreates tables. Use it only as deliberate setup and
document the reset.

## Seeded Accounts

From `README.md` and `database.js`:

- User: `test@eshop.com` / `Test1234!`.
- Admin: `admin@eshop.com` / `Admin123!`.

Note: `setup_guide.md` mentions `admin123` for admin, but `database.js` and prior verified HW04
work use `Admin123!`; prefer the seeded database value when testing the current repo.

## Workflow Endpoint Mapping

| Step | Endpoint | Group | Notes |
|---|---|---|---|
| Login | `POST /api/login` | Auth-heavy | Extract `token` from JSON response. |
| Search Product | `GET /api/products?search=${search}` | Read-heavy | Public endpoint; search by product name. |
| View Detail | `GET /api/products/${product_id}` | Read-heavy | Public endpoint. |
| Add to Cart | `POST /api/cart` | Transactional | Requires `Authorization: Bearer ${token}`. |
| Checkout | `POST /api/checkout` | Transactional | Requires token; writes order row to SQLite. |

## Performance Risks

- Login lockout: wrong passwords increment attempts and can lock the account. Use valid credentials
  for normal performance runs.
- Checkout writes to SQLite and can become the stress/spike bottleneck.
- Cart is in-memory by user ID; repeated runs can accumulate cart state.
- Product search currently uses SQL string interpolation; do not use destructive/adversarial search
  strings in performance tests.
- `README.md` requires the backend to recalculate checkout totals, while API accepts
  `total_amount`; note this as a functional risk when interpreting checkout results.

