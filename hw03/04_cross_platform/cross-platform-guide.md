# Cross-Platform Testing — Step-by-Step Guide (Least-Effort Path)

You're running the SUT locally on your laptop and testing via BrowserStack on the same laptop. BrowserStack Live has a **Local Testing** feature built exactly for this — it connects to your `localhost` directly, no tunnel (ngrok/localtunnel), no deploying anywhere. This is the fastest path.

**Hard constraint (per §11):** every screenshot must show real browser/OS/device chrome (address bar, tabs — proof of which platform it is) and must have `23127296@hcmus.edu.vn` visible somewhere on it.

**Shortcut — no manual stamping needed for most screens:** you already have a real test account with email `23127296@hcmus.edu.vn` / password `Password 1`. Use it to log in throughout the session:
- **Login screen:** type `23127296@hcmus.edu.vn` into the Username field (and the password into the password field — note the field is plaintext, that's BUG-11, not a mistake on your part) before screenshotting. The email is now visibly on-screen, in-app — no annotation needed.
- **Register screen:** type the same email into the email field before screenshotting — same effect (just don't actually submit, or use a throwaway variant if you need the account to stay unregistered for a real register test).
- **Profile screen** (`/profile`, not in the required list but free to grab once you're logged in): shows a disabled `Email (Không đổi)` field with `23127296@hcmus.edu.vn` in it — the cleanest, unambiguous proof shot. Worth capturing once per platform alongside the 5 required screens as extra evidence.
- **Home / Cart / Checkout:** the app only shows the logged-in user's *name* in the header, not email, so these 3 screens still need BrowserStack's one-click screenshot+annotate to stamp the email — can't be avoided since nothing on those screens displays it naturally.

---

## Step 1 — Run the SUT locally

```bash
cd backend
npm install
node database.js   # first time only, or to reset seed data
node server.js      # → http://localhost:3000
```

New terminal:
```bash
cd frontend-web
npm install
npm run dev          # → http://localhost:5173
```

Optional but recommended — seed a product + a valid coupon via the admin panel (`cd frontend-admin && npm run dev` → `http://localhost:5174`, login `admin@eshop.com` / `Admin123!`) so Cart/Checkout aren't empty when you screenshot them.

Leave both terminals running for the rest of this guide.

---

## Step 2 — Turn on BrowserStack Local Testing (one-time per session)

1. Log into BrowserStack → **Live**.
2. Before picking a browser, find the **Local Testing** toggle (usually top of the device/browser picker) and switch it on.
3. If prompted, click to install the small BrowserStack Local binary/extension — accept it, it auto-connects in a few seconds. You only do this once; it stays connected until you close the tab.
4. That's it — no ngrok, no localtunnel, no public URL to manage.

---

## Step 3 — Capture Chrome (in the same Local session)

1. Pick **Windows + Chrome** (any recent version) and start the Live session.
2. In the remote browser's address bar, type `http://localhost:5173` directly — it resolves to your laptop through the Local connection from Step 2.
3. Go to **Register**, type `23127296@hcmus.edu.vn` in the email field → screenshot as-is (email visible in the field, no annotate needed) → `chrome_register.png`.
4. Go to **Login**, type `23127296@hcmus.edu.vn` / `Password 1`, and log in → screenshot before submitting (email + plaintext password both visible) → `chrome_login.png`.
5. While logged in, visit **Profile** → screenshot (email shown in the disabled field) → `chrome_profile.png` (bonus proof shot, not in the required list but free).
6. Add a product to cart, go to **Home**, **Cart**, **Checkout** → these 3 need BrowserStack's screenshot+annotate button (stamp `23127296@hcmus.edu.vn` before downloading) since nothing on these screens shows the email natively → `chrome_home.png`, `chrome_cart.png`, `chrome_checkout.png`.

---

## Step 4 — Capture Firefox (swap browser, same session)

Without restarting Local Testing: just switch the browser selector to **Firefox** (same Windows machine), reload `http://localhost:5173`, repeat Step 3's 6 screens (Register/Login/Profile via typed credentials, Home/Cart/Checkout via annotate) → save as `screenshots/firefox_*.png`.

---

## Step 5 — Third platform (pick whichever is less friction for you)

**Fastest: Android Chrome via the same BrowserStack Local session** — swap the device picker to a real Android device (Local Testing works for real devices too, still no extra setup), open `http://localhost:5173` in its Chrome, repeat Step 3's 6 screens the same way → `screenshots/androidchrome_*.png`.

**Alternative: Expo Go on your own phone** (if you'd rather test the actual mobile app instead of mobile browser) — only worth it if phone and laptop are already on the same Wi-Fi:
```bash
cd frontend-mobile
npm install
npx expo start
```
Scan the QR with Expo Go, walk through the same screens (same shortcut applies — type `23127296@hcmus.edu.vn` into the mobile Login/Register/Profile screens so the email is visible in-app), take normal phone screenshots, and only mark up Home/Cart/Checkout with any photo-markup app; transfer to `screenshots/expogo_*.png`.

---

## Step 6 — Fill in the deliverables

1. Fill `Cross_Platform_Test_Log.md`'s per-platform tables (renders correctly? notes/visual bugs) for Chrome, Firefox, and your third platform.
2. Fill the "Cross-platform inconsistencies observed" table — compare the same screen across the 3 platforms (e.g. does the Admin sidebar's fixed `w-64` from BUG-09 look broken identically everywhere?).
3. Any genuine new visual bug found → file it the same way as Task 1 (GitHub Issue + screenshot, see `../02_bug_reports/HOWTO_create_github_issues.md`).

---

## Optional: automating the click-through / username stamping yourself

If you'd rather drive the browser yourself with a script instead of manually clicking Register→Login→Cart→Checkout each time (e.g. testing more than 3 platforms), or batch-stamp your username on many screenshots at once instead of BrowserStack's per-image annotate button, two ready scripts are in `scripts/`:

- `scripts/capture_screens.mjs` — Playwright script that opens a real, visible Chromium/Firefox window and auto-navigates through all 5 screens, pausing at each so you take the actual OS-level screenshot yourself.
- `scripts/overlay_username.mjs` — batch-stamps `23127296@hcmus.edu.vn` onto every PNG already in `screenshots/` in one command (`node scripts/overlay_username.mjs`), instead of opening each in an editor.

Setup: `npm install -D playwright sharp && npx playwright install chromium firefox`. Not needed for the BrowserStack-only path above — only use these if you want to skip BrowserStack's own annotate tool or add more platforms than 3.

## Troubleshooting

- **Local Testing won't connect:** make sure no VPN/proxy is intercepting the connection; toggling Local Testing off and back on usually reconnects the binary.
- **`localhost:5173` doesn't load in the remote browser:** confirm `npm run dev` is still running in your terminal and Local Testing shows "Connected" (green) before opening the URL.
- **Cart/Checkout empty in screenshots:** make sure you actually clicked "Thêm vào giỏ hàng" **twice** on the product page — BUG-25 means the first click is a no-op.
