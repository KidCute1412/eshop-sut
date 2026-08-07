# HW04 Automation Report

- Student: Nguyen Thanh Tien, Student ID 23127539
- SUT: EShop
- Framework: Playwright
- Browsers: Chromium, Firefox, WebKit
- Final command: `node scripts/run-with-report-stamp.js --timeout=30000`
- Final HTML report: [reports/html-23127539/index.html](reports/html-23127539/index.html)
- Report tag validation: Passed with `Run by: 23127539 - 2026-08-06T14:03:05.859Z`

## Run Matrix

| Feature | Browser | Executed | Passed | Failed | Result |
| --- | --- | ---: | ---: | ---: | --- |
| FR-01 Account registration | Chromium | 15 | 11 | 4 | Failed |
| FR-01 Account registration | Firefox | 15 | 11 | 4 | Failed |
| FR-01 Account registration | WebKit | 15 | 11 | 4 | Failed |
| FR-07 Shopping cart | Chromium | 12 | 12 | 0 | Passed |
| FR-07 Shopping cart | Firefox | 12 | 12 | 0 | Passed |
| FR-07 Shopping cart | WebKit | 12 | 12 | 0 | Passed |
| FR-17 Coupon management | Chromium | 12 | 12 | 0 | Passed |
| FR-17 Coupon management | Firefox | 12 | 12 | 0 | Passed |
| FR-17 Coupon management | WebKit | 12 | 12 | 0 | Passed |

## Summary

- Features automated: **3**
- Design-time test cases automated: **39** (15 FR-01 + 12 FR-07 + 12 FR-17)
- Browser executions: **117**
- Passed browser executions: **105**
- Failed browser executions: **12**
- Confirmed bugs from automation: **2** (`BUG-HW04-FR01-001`, `BUG-HW04-FR01-002`)

## Assertion Pattern Coverage

| Pattern | Example use |
| --- | --- |
| URL/navigation | FR-01 success redirects to `/login`; FR-07 checkout redirects guest to `/login`. |
| Visibility/existence | FR-01 password error banner; FR-17 coupon row appears. |
| Count | FR-07 cart row count; FR-17 deleted coupon row count. |
| Text/value content | FR-07 quantity cell equals `1`. |
| Element/native validity state | FR-01 and FR-17 required-field cases inspect `checkValidity()`. |
| API/network response | FR-01 registration POST status; FR-17 coupon POST/DELETE response status. |

## Final Failure

FR-01 currently has two confirmed defect classes. `FR01-DT-011` shows duplicate email registration is accepted. `FR01-DT-006`, `FR01-BVA-009`, and `FR01-BVA-010` show documented special-character passwords using `!` or `@` are rejected by the UI before any register API request is sent. The `FR01-BVA-011` control case shows a 20-character password with whitespace passes, so the long-password symptom is caused by the wrong special-character regex, not by a documented maximum length.
