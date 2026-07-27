# HW04 Automation Bundle — 23127404

This portable bundle runs `FR06-DT-01` against EShop on Chromium, Firefox,
and WebKit. The EShop backend and frontend are external prerequisites; the
bundle does not modify or package the SUT.

## Prerequisites

- Node.js 20 or newer.
- EShop backend available at `http://localhost:3000`.
- EShop frontend available at `http://localhost:5173`.

The defaults can be overridden with `BACKEND_URL` and `BASE_URL`.

## Install and run

```powershell
npm ci
npm run install:browsers
npm test
npm run report
```

For a SUT hosted elsewhere in PowerShell:

```powershell
$env:BACKEND_URL = "http://example.test:3000"
$env:BASE_URL = "http://example.test:5173"
npm test
```

On Bash:

```bash
BACKEND_URL=http://example.test:3000 BASE_URL=http://example.test:5173 npm test
```

The test command exits with a non-zero status when the SUT violates FR-06.
That failure is expected for the current SUT because the product category is
not displayed. Open `playwright-report/index.html` or run `npm run report` to
inspect the combined evidence for all three browser projects.
