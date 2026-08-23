# HW06 verified bug report

This register contains only independently reproducible findings from the three selected APIs. Checkout symptoms are deduplicated into one root cause: the endpoint bypasses the cart entirely.

| Bug | Evidence test | Raw evidence |
|---|---|---|
| BUG-HW06-01 | EXT-LOGIN-01, EXT-LOGIN-02 | `newman-reports/pool-a/cases/EXT-LOGIN-01.json` |
| BUG-HW06-02 | EXT-LOGIN-03 | `newman-reports/pool-a/cases/EXT-LOGIN-03.json` |
| BUG-HW06-03 | EXT-LOGIN-04 | `newman-reports/pool-a/cases/EXT-LOGIN-04.json` |
| BUG-HW06-04 | EXT-CHK-01..03 | `newman-reports/pool-b/report.json` |
| BUG-HW06-05 | EXT-ADM-01 | `newman-reports/pool-c/report.json` |
| BUG-HW06-06 | EXT-ADM-02 | `newman-reports/pool-c/report.json` |

## BUG-HW06-01: Login attempt counter increments by two

- Severity: **High**
- Endpoint: `POST /api/login`
- Oracle: `FR-02`
- Reproduction summary: A failed password changes `login_attempts` from 0 to 2; the contract requires exactly 1.
- Expected result: behavior must conform to FR-02; see the contract status in the matching Excel row.
- Actual result: reproduced in the raw Newman evidence referenced by the mapped test cases.
- GitHub Issue: [#162](https://github.com/KidCute1412/eshop-sut/issues/162)
- GitHub Issue screenshot: [bug_01.png](screenshots/bug_01.png)

## BUG-HW06-02: Login lock duration is 180 seconds

- Severity: **Medium**
- Endpoint: `POST /api/login`
- Oracle: `FR-02`
- Reproduction summary: An account remains locked for 180 seconds although demo requirement specifies 30 seconds.
- Expected result: behavior must conform to FR-02; see the contract status in the matching Excel row.
- Actual result: reproduced in the raw Newman evidence referenced by the mapped test cases.
- GitHub Issue: [#163](https://github.com/KidCute1412/eshop-sut/issues/163)
- GitHub Issue screenshot: [bug_02.png](screenshots/bug_02.png)

## BUG-HW06-03: Login response exposes plaintext password

- Severity: **Critical**
- Endpoint: `POST /api/login`
- Oracle: `SEC-01`
- Reproduction summary: The successful JSON response serializes `user.password`.
- Expected result: behavior must conform to SEC-01; see the contract status in the matching Excel row.
- Actual result: reproduced in the raw Newman evidence referenced by the mapped test cases.
- GitHub Issue: [#164](https://github.com/KidCute1412/eshop-sut/issues/164)
- GitHub Issue screenshot: [bug_03.png](screenshots/bug_03.png)

## BUG-HW06-04: Checkout bypasses cart-derived business rules

- Severity: **Critical**
- Endpoint: `POST /api/checkout`
- Oracle: `FR-08`
- Reproduction summary: The endpoint does not read, validate, total, or clear the in-memory cart; it accepts client amount and can create an empty-cart order.
- Expected result: behavior must conform to FR-08; see the contract status in the matching Excel row.
- Actual result: reproduced in the raw Newman evidence referenced by the mapped test cases.
- GitHub Issue: [#165](https://github.com/KidCute1412/eshop-sut/issues/165)
- GitHub Issue screenshot: [bug_04.png](screenshots/bug_04.png)

## BUG-HW06-05: Customer token can change an admin order

- Severity: **Critical**
- Endpoint: `PUT /api/admin/orders/:id/status`
- Oracle: `SEC-03 / FR-18`
- Reproduction summary: The route verifies JWT only and never verifies `role === admin`.
- Expected result: behavior must conform to SEC-03 / FR-18; see the contract status in the matching Excel row.
- Actual result: reproduced in the raw Newman evidence referenced by the mapped test cases.
- GitHub Issue: [#166](https://github.com/KidCute1412/eshop-sut/issues/166)
- GitHub Issue screenshot: [bug_05.png](screenshots/bug_05.png)

## BUG-HW06-06: Canceled order can transition to delivered

- Severity: **High**
- Endpoint: `PUT /api/admin/orders/:id/status`
- Oracle: `FR-10`
- Reproduction summary: A hard-coded exception accepts the terminal transition `canceled → delivered`.
- Expected result: behavior must conform to FR-10; see the contract status in the matching Excel row.
- Actual result: reproduced in the raw Newman evidence referenced by the mapped test cases.
- GitHub Issue: [#167](https://github.com/KidCute1412/eshop-sut/issues/167)
- GitHub Issue screenshot: [bug_06.png](screenshots/bug_06.png)
