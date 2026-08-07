# EShop Analysis Guide (Automation-Specific)

## Confirmed Ports and Startup

- Backend API: `http://localhost:3000` (`backend/server.js`). Start with `node server.js` after
  `npm install` and (first run only) `node database.js` to seed data — see `setup_guide.md`.
- Frontend Web (customer-facing): `http://localhost:5173` (Vite default; no override in
  `frontend-web/vite.config.js`).
- Frontend Admin: `http://localhost:5174` (`frontend-admin/vite.config.js` sets
  `server: { port: 5174, strictPort: true }`). Only relevant if the selected Pool C feature is a web
  admin feature.
- Both frontends must be running (alongside the backend) for any browser-driven automation to work;
  `frontend-mobile` is out of scope for HW04 (web-only).

## HW02 Feature Selection (Reused for HW04)

Per `reports/HW2/main-report.md`, the 3 features already selected and already carrying HW02
Domain Testing + BVA test cases are:

| Pool | Feature | Name | HW02 test cases |
| --- | --- | --- | --- |
| A | FR-01 | Account registration | `reports/HW2/FR-01/test-cases.md` (37 cases) |
| B | FR-07 | Shopping cart | `reports/HW2/FR-07/test-cases.md` (20 cases) |
| C | FR-17 | Coupon management (CRUD) | `reports/HW2/FR-17/test-cases.md` (22 cases) |

Each already has more than 12 cases designed and human-reviewed — Phase 1 of `SKILL.md` is
selecting a well-mixed subset of at least 12 per feature, not designing new ones from scratch.

## Critical Selector Risk: No `data-testid`/`id` Anywhere

Across the pages relevant to these 3 features, **no element carries a `data-testid` or `id`
attribute**. Every selector an AI (or a human) writes must rely on text content, CSS class, tag
structure, or ARIA role/accessible name. This is the single biggest source of fragile selectors an
AI's first pass will produce, and it is exactly the kind of gap Phase 5's human review is meant to
catch — prefer role + accessible name locators (e.g. `getByRole('button', { name: 'Đăng Ký' })`)
over raw class selectors (e.g. `.bg-red-500`) wherever the page structure allows it, since class
names are purely presentational and can change without any functional intent.

## FR-01 — Register (`frontend-web/src/pages/Register.jsx`)

- Fields: Full Name, Email, Password (single field, no Confirm Password — see HW03's
  `BUG-GUI-004`). Submit button text "Đăng Ký".
- Known real defect already documented in HW03: the client-side password regex requires a
  whitespace character where the UI copy says "special character" — a password like `Aa1!aaaa`
  fails, but `Aa1 aaaa` (with a literal space) passes. Automation for password-related cases should
  account for this actual behavior, not the documented/intended behavior, when writing an
  *automation* assertion — but should still be flagged as a bug in Phase 7, not silently accepted as
  correct.
- On success, redirects to `/login`.

## FR-07 — Cart (`frontend-web/src/pages/Cart.jsx`, state in `context/CartContext.jsx`)

- Empty-cart state: heading text "Giỏ hàng của bạn đang trống"; link "Tiếp tục mua sắm" back to `/`.
- Cart table columns: Sản phẩm / Giá / Số lượng / Thành tiền / Thao tác.
- **Quantity is display-only on this page** — there is no increment/decrement control or quantity
  input on the Cart page itself; quantity is only set at add-to-cart time (product listing/detail
  page, outside `Cart.jsx`). Do not write a Cart-page test case that assumes an in-cart quantity
  editor exists; verify on the actual product page first if a case needs to test quantity changes.
- Row action: "Xóa" button (`.text-red-500`) removes that row via `removeFromCart(index)`.
- Footer: "Tổng tạm tính:" total; "Tiến hành thanh toán" button (`.bg-green-500`) — redirects to
  `/login` with an alert if not authenticated, otherwise to `/checkout`.

## FR-17 — Coupon Management (`frontend-admin/src/App.jsx`, inline, `activeTab === "coupons"`)

- No separate page file or router — it's a tab within the single-file admin app (`App.jsx`,
  roughly lines 612-775 at the time of writing; re-check if the file has since changed).
- Nav: `<li>` with text "Mã Giảm Giá" switches `activeTab`.
- Create form (by placeholder/label): coupon code input (placeholder "Mã coupon (VD: SAVE10)",
  uppercased), type `<select>` ("Phần trăm (%)" / "Số tiền cố định (₫)"), discount value input,
  "Đơn tối thiểu (₫)", expiry date input, "Số lần dùng tối đa/người" (`min="1"`). Submit button text
  "Tạo mã" (`.bg-orange-500`).
- Table columns: Mã / Loại / Giá trị / Đơn tối thiểu / Hết hạn / Giới hạn / Hành động; an expired
  coupon shows red "Hết hạn" text.
- **Only Create and Delete exist for coupons** — there is no Edit/Update flow (unlike Products,
  which does have one). Do not write or expect an "edit coupon" test case; if HW02's test cases
  included one, flag it in Phase 1 as not automatable and explain why (matches Phase 7's
  non-automatable-case documentation requirement).
- API calls used: `POST /api/admin/coupons`, `GET /api/coupons`, `DELETE /api/admin/coupons/:id`.
  These are legitimate targets for API/network-response assertions (Phase 4's assertion-pattern
  diversity requirement).
- Requires an authenticated admin session before this tab is reachable — the default admin
  credentials are documented in `setup_guide.md` (`admin@eshop.com` / `admin123`) if a fixture needs
  to log in first.
