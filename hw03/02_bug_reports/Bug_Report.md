# Bug Report — EShop (eshop-clone), frontend-web

10 bugs found during Task 1 checklist execution, all reproducible on frontend-web alone. Each bug is written in GitHub-issue format (Title / Labels / Steps to Reproduce / Expected / Actual / Evidence) based on manually reproducing the issue on the running app, and filed as a real GitHub Issue (with screenshot) on `KidCute1412/eshop-sut` — see the URL column below.

## Index

| Bug ID | Title | Screen | Severity | Checklist Item | Screenshots needed | GitHub Issue URL |
|---|---|---|---|---|---|---|
| BUG-01 | Login page shows "Đăng Ký" heading instead of "Đăng Nhập" | Login | Minor | #3 | 1 | [#106](https://github.com/KidCute1412/eshop-sut/issues/106) |
| BUG-11 | Login password field shows plaintext instead of masked dots | Login | **Critical** | #11 | 1 | [#107](https://github.com/KidCute1412/eshop-sut/issues/107) |
| BUG-13 | OTP field label says "4 digits" but the code shown is 6 digits | ForgotPassword | Major | #12 | 2 | [#108](https://github.com/KidCute1412/eshop-sut/issues/108) |
| BUG-14 | Checkout total amount can be freely edited by the user | Checkout | Major | #13 | 1-2 | [#109](https://github.com/KidCute1412/eshop-sut/issues/109) |
| BUG-15 | Quantity input on Product Detail accepts 0 / negative values | ProductDetail | Major | #14 | 1-2 | [#110](https://github.com/KidCute1412/eshop-sut/issues/110) |
| BUG-19 | Reflected XSS via the search box | Home | **Critical** | #15 | 1 | [#111](https://github.com/KidCute1412/eshop-sut/issues/111) |
| BUG-24 | Login-required redirect from Checkout doesn't return to Checkout | Cart → Login | Major | #28 | 2 | [#112](https://github.com/KidCute1412/eshop-sut/issues/112) |
| BUG-25 | "Add to cart" does nothing on the first click | ProductDetail | Major | #30 | 2 | [#113](https://github.com/KidCute1412/eshop-sut/issues/113) |
| BUG-34 | No "no results found" message after an empty search | Home | Minor | #31 | 1 | [#114](https://github.com/KidCute1412/eshop-sut/issues/114) |
| BUG-37 | Debug string shown as the product-not-found message | ProductDetail | Minor | #32 | 1 | [#115](https://github.com/KidCute1412/eshop-sut/issues/115) |

---

## Bug details (GitHub-issue-ready)

### BUG-01 — [Minor] Login page shows the Register heading
**Labels:** `bug`, `severity:minor`, `IA-01-general-ui`
**Screen:** `/login`
**Steps to reproduce:**
1. Go directly to the Login page (`/login`), not by clicking through Register.
2. Look at the page heading.
**Expected:** Heading reads "Đăng Nhập" (Login).
**Actual:** Heading reads "Đăng Ký" (Register) — the wrong heading for this screen.
**Screenshot needed:** 1 — the Login page with the visible wrong heading.

---

### BUG-11 — [Critical] Login password field is not masked
**Labels:** `bug`, `severity:critical`, `security`, `IA-02-forms`
**Screen:** `/login`
**Steps to reproduce:**
1. Go to `/login`.
2. Click into the password field and type a password.
**Expected:** Characters are masked (••••••).
**Actual:** Every character typed into the password field is fully visible as plain text.
**Screenshot needed:** 1 — the password field mid-typing, showing plaintext characters.

---

### BUG-13 — [Major] OTP field label doesn't match the actual code length
**Labels:** `bug`, `severity:major`, `IA-02-forms`
**Screen:** `/forgot-password` (step 2)
**Steps to reproduce:**
1. Go to Forgot Password, enter an email, and request an OTP.
2. Look at the OTP shown on screen, then look at the field label right below it.
**Expected:** The label matches the length of the code actually shown (per `api_specification.md`, the token is 6 digits, e.g. "123456").
**Actual:** The screen displays a 6-digit code, but the input field is labeled "Mã OTP (4 số)" (4-digit code).
**Screenshot needed:** 2 — (a) the 6-digit code displayed on screen, (b) the field label saying 4 digits, ideally both visible in one screenshot.

---

### BUG-14 — [Major] Checkout total amount is a freely editable field
**Labels:** `bug`, `severity:major`, `IA-02-forms`
**Screen:** `/checkout`
**Steps to reproduce:**
1. Add an item to the cart and go to Checkout.
2. Click into the "Tổng tiền thanh toán" total field and type a different number.
**Expected:** The total should be a read-only, computed value the shopper cannot edit.
**Actual:** The field accepts direct free-text edits, changing the amount that will be charged.
**Screenshot needed:** 1-2 — the total field with an edited (clearly different/suspicious) value typed in.

---

### BUG-15 — [Major] Quantity input accepts 0 or negative values
**Labels:** `bug`, `severity:major`, `IA-02-forms`
**Screen:** Product Detail page
**Steps to reproduce:**
1. Open any product's detail page.
2. Clear the quantity field and type `0` (or `-1`).
3. Click "Thêm vào giỏ hàng" (Add to cart).
**Expected:** The field should reject 0/negative values (minimum 1).
**Actual:** The value is accepted with no warning, and the action proceeds.
**Screenshot needed:** 1-2 — the quantity field showing 0 (or negative), ideally alongside the cart afterward.

---

### BUG-19 — [Critical] Reflected XSS via the Home search box
**Labels:** `bug`, `severity:critical`, `security`, `IA-02-forms`
**Screen:** Home
**Steps to reproduce:**
1. Go to Home.
2. In the search box, enter: `<img src=x onerror=alert(1)>`
3. Submit the search.
**Expected:** The literal text of the query is shown next to "Kết quả tìm kiếm cho:".
**Actual:** A JavaScript alert box fires instead of the text being shown literally — the search query is being executed as HTML.
**Screenshot needed:** 1 — the alert() popup firing on the search results page (very visual/dramatic, easy single screenshot).

---

### BUG-24 — [Major] Login-required redirect from Checkout doesn't return to Checkout
**Labels:** `bug`, `severity:major`, `IA-03-navigation`
**Screen:** Cart → Login
**Steps to reproduce:**
1. While logged out, add an item to the cart and click "Tiến hành thanh toán" (Checkout).
2. Log in when prompted.
3. Observe which page you land on after login.
**Expected:** After logging in, the user should land back on Checkout.
**Actual:** The user lands on Home instead, losing the checkout flow context.
**Screenshot needed:** 2 — (a) the login prompt/redirect from Checkout, (b) the page shown right after successful login (Home, not Checkout).

---

### BUG-25 — [Major] "Add to cart" does nothing on the first click
**Labels:** `bug`, `severity:major`, `IA-04-feedback`
**Screen:** Product Detail page
**Steps to reproduce:**
1. Open any product's detail page.
2. Click "Thêm vào giỏ hàng" (Add to cart) exactly once, then check the cart.
3. Click the same button a second time.
**Expected:** The very first click should add the item and show confirmation.
**Actual:** The first click does nothing (no confirmation, item not added); the second click works normally.
**Screenshot needed:** 2 — (a) after the first click (no change/no confirmation), (b) after the second click (item added, confirmation shown).

---

### BUG-34 — [Minor] No "no results found" message after an empty search
**Labels:** `bug`, `severity:minor`, `IA-04-feedback`
**Screen:** Home
**Steps to reproduce:**
1. Go to Home.
2. Search for a nonsense term with no matching products (e.g. "zzqxnonexistent").
**Expected:** An explicit "No products found" message should appear.
**Actual:** The page just shows an empty product grid with no explanatory text at all.
**Screenshot needed:** 1 — the blank results area after a no-match search.

---

### BUG-37 — [Minor] Debug string shown as the product-not-found message
**Labels:** `bug`, `severity:minor`, `IA-04-feedback`
**Screen:** Product Detail page
**Steps to reproduce:**
1. Manually edit the URL to point at a non-existent product ID (e.g. `/product/999999`).
**Expected:** A plain, user-facing "product not found" message.
**Actual:** The page displays the literal text "Sản phẩm không tồn tại (Lỗi trắng trang do data rỗng)" — reads as an internal/developer debug note, not normal user-facing copy.
**Screenshot needed:** 1 — the debug-style message on screen.
