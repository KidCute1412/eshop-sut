# Task 3 — Cross-Browser / Cross-Platform Test Log

**Student ID:** 23127296 — every screenshot must overlay the username `23127296@hcmus.edu.vn` per §6/§11.

## Required coverage (minimum 3 platforms)

Pick at least 3 rows below (Expo Go may replace one of the 3 required browser platforms, e.g. in place of Safari):

| # | Platform | Tool | Screens to cover | Status |
|---|---|---|---|---|
| 1 | Chrome (desktop or BrowserStack/LambdaTest) | | Home, Login/Register, Cart, Checkout | [ ] |
| 2 | Firefox (desktop or BrowserStack/LambdaTest) | | Home, Login/Register, Cart, Checkout | [ ] |
| 3 | Safari (BrowserStack/LambdaTest/real Mac) **or** Android Chrome **or** Expo Go (mobile app) | | Home, Login/Register, Cart, Checkout | [ ] |

## Per-platform findings

Duplicate this block once per platform tested.

### Platform: [Chrome / Firefox / Safari / Android Chrome / Expo Go]
- **Tool/device used:** (e.g. BrowserStack live session, real iPhone 13 via Expo Go, etc.)
- **OS/Browser version:**
- **SUT URL used:** `http://localhost:5173` (or your tunneled/LAN URL) — must be visible in the screenshot alongside the browser/OS chrome.
- **Screenshots:** `screenshots/[platform]_[screen].png` (each must overlay `23127296@hcmus.edu.vn`)

| Screen | Renders correctly? | Notes / visual bugs found |
|---|---|---|
| Home | | |
| Login | | |
| Register | | |
| Cart | | |
| Checkout | | |
| Admin Dashboard (optional) | | |

### Cross-platform inconsistencies observed (fill in after testing all platforms)

| Issue | Platforms affected | Screenshot(s) | Severity |
|---|---|---|---|
| | | | |

---

## How to overlay your username on screenshots

Any of the following work:
- BrowserStack/LambdaTest: use their built-in annotation tool to add a text overlay before exporting.
- Any image editor (Paint, Preview, GIMP, Photopea) — add a text layer `23127296@hcmus.edu.vn` in a corner, flatten, export as PNG.
- On mobile screenshots (Expo Go), overlay the same text using any photo-markup app.

## Why this section is a template, not filled-in data

Cross-browser screenshots require an actual BrowserStack/LambdaTest trial (or a real device) and cannot be captured from within this Claude Code session — there is no browser-automation/screenshot tool available here, and per §11 these screenshots specifically must not be AI-generated. Set up your trial at BrowserStack or LambdaTest, run the SUT locally (`eshop-clone/setup_guide.md`), and fill in the tables above with real screenshots saved to `screenshots/`.
