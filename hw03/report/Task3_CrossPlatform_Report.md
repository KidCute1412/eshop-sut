# Task 3 — Cross-Browser / Cross-Platform Testing: Plan (Execution Pending Real Trial)

**Student ID:** 23127296

## Status of this deliverable

Per §6 and §11, this task requires real screenshots from a BrowserStack/LambdaTest trial (or physical devices/Expo Go) with the browser/OS/device chrome visible and the student's username overlaid — these must not be AI-generated. This cannot be produced inside this Claude Code session (no browser-automation or live device access here). `04_cross_platform/Cross_Platform_Test_Log.md` provides a ready-to-fill log covering the required ≥3 platforms (Chrome, Firefox, and Safari/Android Chrome/Expo Go), with a per-screen checklist (Home, Login, Register, Cart, Checkout) and a cross-platform inconsistency table.

## What the student must still do

1. Sign up for a BrowserStack or LambdaTest free trial (or use Expo Go on a real phone for the mobile app, which satisfies one of the 3 required platforms).
2. Run the SUT locally per `eshop-clone/setup_guide.md` and expose it (tunnel/LAN IP) so the remote browser/device can reach it.
3. For each of the 3+ platforms, screenshot Home, Login, Register, Cart, and Checkout, overlaying `23127296@hcmus.edu.vn` on each image.
4. Save screenshots to `04_cross_platform/screenshots/`, fill in `Cross_Platform_Test_Log.md`'s tables, and note any rendering differences/bugs found between platforms (report genuine bugs the same way as Task 1 — GitHub Issue + screenshot).
5. Replace this report's status section with a real summary once testing is complete.

## Candidate visual risks to specifically check across platforms (from Task 1's code review)

- Tailwind's default breakpoints (`sm:`, `md:`) are used throughout `Home.jsx`'s product grid — verify the 1/2/3-column layout actually reflows correctly on Safari and small Android viewports, not just Chrome desktop.
- The Admin sidebar (`frontend-admin/src/App.jsx`) is a fixed `w-64` with no responsive breakpoint (BUG-09 from Task 1) — expect this to look broken on any narrower viewport across all browsers, not just one; confirm it's consistent (not browser-specific).
- Mobile app product images use `resizeMode="stretch"` (BUG-08) — this will visibly distort images on Expo Go regardless of device, useful to confirm it's a code bug and not a device quirk.
