# Task 3 — Cross-Browser / Cross-Platform Testing: Results

**Student ID:** 23127296

## Summary

The EShop web frontend was tested across 3 platforms: **Chrome** (Windows, local), **Firefox** (Windows, local), and **Safari 26 on macOS 26** (via a Sauce Labs Live real-device session, substituted for BrowserStack per the assignment's allowance for an equivalent cloud tool). Each platform covered Home, Login, Register, and Cart; Chrome and Firefox additionally covered Checkout. Every screenshot carries `23127296@hcmus.edu.vn` visibly on-screen, entered as the value of an in-app field (Login/Register username, Home search box, or Checkout coupon code) rather than added as a post-hoc image overlay.

Full per-screen results and screenshots: `../04_cross_platform/Cross_Platform_Test_Log.md` and `../04_cross_platform/screenshots/`.

## Key finding

No browser-specific rendering differences were found. Every defect visible in the screenshots — the Login page's wrong "Đăng Ký" heading (BUG-01), the plaintext password field (BUG-11), and the freely-editable Checkout total (BUG-14) — reproduces identically on Chrome, Firefox, and Safari, confirming these are logic/content bugs in the React app rather than browser-specific CSS/rendering issues. This is consistent with the app being a Tailwind-based SPA tested only on modern evergreen browser engines.

## Deliverables

| File | Contents |
|---|---|
| `../04_cross_platform/Cross_Platform_Test_Log.md` | Per-platform screen-by-screen results table and cross-platform inconsistency findings. |
| `../04_cross_platform/screenshots/` | 14 screenshots (5 Chrome, 5 Firefox, 4 Safari), each with the student ID visible on-screen. |
