# Task 3 — Cross-Browser / Cross-Platform Test Log

**Student ID:** 23127296 — every screenshot below overlays `23127296@hcmus.edu.vn`, either typed into an in-app field (Login/Register username field, Home search box, Checkout coupon field) or visible as the logged-in test account.

## Coverage (3 platforms)

| # | Platform | Tool | Screens covered | Status |
|---|---|---|---|---|
| 1 | Chrome (Windows, local) | Local browser against `http://localhost:5173` | Home, Login, Register, Cart, Checkout | Done |
| 2 | Firefox (Windows, local) | Local browser against `http://localhost:5173` | Home, Login, Register, Cart, Checkout | Done |
| 3 | Safari 26 / macOS 26 | Sauce Labs Live (real macOS session) | Home, Login, Register, Cart | Done |

## Per-platform findings

### Platform: Chrome (Windows)
- **SUT URL used:** `http://localhost:5173`
- **Screenshots:** `screenshots/chrome_home.png`, `chrome_login.png`, `chrome_register.png`, `chrome_cart.png`, `chrome_checkout.png`

| Screen | Renders correctly? | Notes / visual bugs found |
|---|---|---|
| Home | Yes | Product grid, search box, header all render as expected. |
| Login | Yes (content bug, not visual) | Confirms BUG-01: heading reads "Đăng Ký" instead of "Đăng Nhập". |
| Register | Yes | Form, password hint text, and layout render correctly. |
| Cart / Product | Yes | Product detail and cart flow render correctly; quantity input and "Thêm vào giỏ hàng" button both functional. |
| Checkout | Yes (content bug, not visual) | Confirms BUG-14: "Tổng tiền thanh toán" is a plain editable number input, not a read-only computed value. |

### Platform: Firefox (Windows)
- **SUT URL used:** `http://localhost:5173`
- **Screenshots:** `screenshots/firefox_home.png`, `firefox_login.png`, `firefox_register.png`, `firefox_cart.png`, `firefox_checkout.png`

| Screen | Renders correctly? | Notes / visual bugs found |
|---|---|---|
| Home | Yes | Identical layout to Chrome. |
| Login | Yes | Form renders identically to Chrome; password field is plaintext on both (BUG-11). |
| Register | Yes | Identical to Chrome. |
| Cart | Yes | Empty/populated cart states render identically to Chrome. |
| Checkout | Yes (content bug, not visual) | Same editable-total behavior as Chrome (BUG-14); coupon code input auto-uppercases as typed, confirming that checklist item passes on Firefox too. |

### Platform: Safari 26 / macOS 26 (Sauce Labs Live)
- **Tool/device used:** Sauce Labs Live session, Safari 26 on macOS 26 (real browser engine, not emulated)
- **SUT URL used:** `http://192.168.0.9:5173` (LAN IP, same network as the Sauce Labs tunnel)
- **Screenshots:** `screenshots/safari_home.png`, `safari_login.png`, `safari_register.png`, `safari_cart.png`

| Screen | Renders correctly? | Notes / visual bugs found |
|---|---|---|
| Home | Yes | Layout matches Chrome/Firefox. |
| Login | Yes (content bug, not visual) | Same BUG-01 heading mismatch and BUG-11 plaintext password field, confirmed on Safari too. |
| Register | Yes | Form and password hint render identically to Chrome/Firefox. |
| Cart | Yes | Empty-cart state renders identically. |

## Cross-platform inconsistencies observed

| Issue | Platforms affected | Screenshot(s) | Severity |
|---|---|---|---|
| None found — every code-level bug already logged in Task 1 (BUG-01, BUG-11, BUG-14) reproduces identically on Chrome, Firefox, and Safari; no browser-specific rendering difference was observed. | Chrome, Firefox, Safari | `chrome_login.png`, `firefox_login.png`, `safari_login.png`, `chrome_checkout.png`, `firefox_checkout.png` | N/A |

This is the expected result for a Tailwind-based React SPA tested only on modern evergreen browsers (Tailwind's utility classes are broadly cross-browser-consistent, and no old-IE/legacy-engine testing was in scope) — the bugs found in this app are logic/content bugs, not CSS-rendering bugs, so they were expected to reproduce identically across platforms rather than being browser-specific.
