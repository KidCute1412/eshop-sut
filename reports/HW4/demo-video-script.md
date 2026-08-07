# HW04 Demo Video Script

Target length: 5-7 minutes. Narration language: Vietnamese.

## Opening

1. Open terminal in the repository.
2. Run:

```powershell
whoami
hostname
```

3. Say: "Day la bang chung tac gia cua bai demo automation HW04. Em se demo Playwright suite cho EShop, gom multi-browser run va HTML report."

## Scope

Explain the selected HW02 features:

- FR-01 Account registration
- FR-07 Shopping cart
- FR-17 Coupon management

Mention that Pool D/mobile is out of scope for HW04.

## Run Demo

Run from `reports/HW4`:

```powershell
$env:HW4_SKIP_WEBSERVER='1'
node scripts\run-with-report-stamp.js --timeout=30000
```

Explain that the suite runs on Chromium, Firefox, and WebKit. Mention the expected final status: 105 passed and 3 failed because FR-01 duplicate email exposes a real SUT bug.

## Human Review Fix

Show [FR-07/tests/fr-07-cart.spec.js](FR-07/tests/fr-07-cart.spec.js). Explain:

- First draft used `page.goto("/cart")`.
- That caused false failures because cart state is stored in React context.
- Final script clicks `a[href='/cart']`, preserving SPA state.

## HTML Report

Open [reports/html-23127539/index.html](reports/html-23127539/index.html). Show:

- The `Run by: 23127539 - <ISO timestamp>` tag.
- The three browsers.
- FR-07 and FR-17 passing.
- FR-01 duplicate email failing on all three browsers.

## Bug Explanation

Open [FR-01/bug-report.md](FR-01/bug-report.md). Explain that the test pre-creates an email, submits the same email through UI, and receives HTTP 200 instead of rejection.

## Closing

Say: "Ket luan: automation da chay that tren 3 browsers, data nam trong JSON rieng, report co Run by va timestamp, va mot bug that duoc ghi nhan tu failing assertion."
