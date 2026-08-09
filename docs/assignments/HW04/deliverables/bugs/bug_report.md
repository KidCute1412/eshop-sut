# HW04 Runtime Failure and Defect-Candidate Report

> **Canonical defect-entry file.** Agent triage has completed: **17 confirmed defects** and **2 rejected candidates**.
> Update this file only with the public Issue URL after filing; `issue-register.md` is the compact reconciliation
> index and is refreshed from this file by the automation agent.

## Evidence status

The nine selected final runs scheduled 153 browser cases: all 153 reached assertions (96 passed and 57 assertion-failed). The final Firefox configuration produced no page-fixture failures.

- **57 assertion failures** across **19 unique logical cases**: FR-06 has 18 assertion failures, FR-10 has 12, and FR-12 has 27.

The assertion-failing cases below were triaged against the FR requirements, fresh Firefox reruns, and the test-design audit. Seventeen are confirmed defect packets with public Issue URLs; two are rejected because the feedback oracle is too strict. Prior HW02/HW03 issues may be consulted as regression context only; they are not new HW04 Issues.

The complete decision table is in [`triage-decisions.md`](triage-decisions.md). Each confirmed defect has a copy-ready packet under `issue-packets/BUG-###/issue-body.md` and authentic evidence under `evidence/HW04-CAND-###/`.

## Selected evidence

| Feature | Chromium report | Firefox report | WebKit report |
|---|---|---|---|
| FR-06 | `automation/reports/fr06-chromium-2026-08-09T17-11-54-712Z/` | `automation/reports/fr06-firefox-2026-08-09T18-19-41-178Z/` | `automation/reports/fr06-webkit-2026-08-09T17-16-10-035Z/` |
| FR-10 | `automation/reports/fr10-chromium-2026-08-09T17-17-32-516Z/` | `automation/reports/fr10-firefox-2026-08-09T18-21-10-553Z/` | `automation/reports/fr10-webkit-2026-08-09T17-21-22-978Z/` |
| FR-12 | `automation/reports/fr12-chromium-2026-08-09T17-22-38-418Z/` | `automation/reports/fr12-firefox-2026-08-09T18-22-31-674Z/` | `automation/reports/fr12-webkit-2026-08-09T17-27-20-694Z/` |

All nine HTML/JSON/metadata directories passed structural identity, timestamp, case-count, completion, and totals validation. Interactive rendering and links still require the documented manual opening step.

## Candidate register

The recurrence column counts assertion failures across all three browsers.

| Candidate | Case | Runtime-observed mismatch | Assertion recurrence | Severity | Public Issue |
|---|---|---|---:|---|---|
| `HW04-CAND-001` | `FR06-07` | Required category text `Điện thoại` was not found | 3/3 browsers | Medium | [`BUG-001`](https://github.com/KidCute1412/eshop-sut/issues/141) |
| `HW04-CAND-002` | `FR06-09` | Quantity input lacked required `min="1"` attribute | 3/3 browsers | Medium | [`BUG-002`](https://github.com/KidCute1412/eshop-sut/issues/142) |
| `HW04-CAND-003` | `FR06-11` | First add click left button text as `Thêm vào giỏ hàng`; expected visible feedback | 3/3 browsers | Medium | Rejected — feedback oracle gap |
| `HW04-CAND-004` | `FR06-12` | Valid quantity add left button text unchanged; expected visible feedback | 3/3 browsers | Medium | Rejected — feedback oracle gap |
| `HW04-CAND-005` | `FR06-13` | Quantity `0` remained HTML-valid | 3/3 browsers | High | [`BUG-003`](https://github.com/KidCute1412/eshop-sut/issues/143) |
| `HW04-CAND-006` | `FR06-14` | Quantity `-1` remained HTML-valid | 3/3 browsers | High | [`BUG-004`](https://github.com/KidCute1412/eshop-sut/issues/144) |
| `HW04-CAND-007` | `FR10-06` | After `confirmed → shipping`, Customer UI still exposed one cancel button | 3/3 browsers | Medium | [`BUG-005`](https://github.com/KidCute1412/eshop-sut/issues/145) |
| `HW04-CAND-008` | `FR10-11` | Shipping-order UI still exposed one cancel button after rejected Admin cancellation | 3/3 browsers | Medium | [`BUG-006`](https://github.com/KidCute1412/eshop-sut/issues/146) |
| `HW04-CAND-009` | `FR10-12` | User cancellation of `shipping` returned 200 success instead of rejection | 3/3 browsers | High | [`BUG-007`](https://github.com/KidCute1412/eshop-sut/issues/147) |
| `HW04-CAND-010` | `FR10-16` | `canceled → delivered` returned 200 instead of preserving the final state | 3/3 browsers | High | [`BUG-008`](https://github.com/KidCute1412/eshop-sut/issues/148) |
| `HW04-CAND-011` | `FR12-03` | User JWT read `/api/admin/users` with 200 and received user data | 3/3 browsers | Critical | [`BUG-009`](https://github.com/KidCute1412/eshop-sut/issues/149) |
| `HW04-CAND-012` | `FR12-06` | User JWT read `/api/admin/orders` with 200 | 3/3 browsers | Critical | [`BUG-010`](https://github.com/KidCute1412/eshop-sut/issues/150) |
| `HW04-CAND-013` | `FR12-08` | Anonymous `POST /api/products` returned 200 and created a product | 3/3 browsers | Critical | [`BUG-011`](https://github.com/KidCute1412/eshop-sut/issues/151) |
| `HW04-CAND-014` | `FR12-09` | User JWT `POST /api/products` returned 200 and created a product | 3/3 browsers | Critical | [`BUG-012`](https://github.com/KidCute1412/eshop-sut/issues/152) |
| `HW04-CAND-015` | `FR12-11` | Anonymous `PUT /api/products/999999` returned 200 | 3/3 browsers | Critical | [`BUG-013`](https://github.com/KidCute1412/eshop-sut/issues/153) |
| `HW04-CAND-016` | `FR12-12` | User JWT `DELETE /api/products/999999` returned 200 | 3/3 browsers | Critical | [`BUG-014`](https://github.com/KidCute1412/eshop-sut/issues/154) |
| `HW04-CAND-017` | `FR12-14` | User JWT `POST /api/categories` returned 200 and created a category | 3/3 browsers | Critical | [`BUG-015`](https://github.com/KidCute1412/eshop-sut/issues/155) |
| `HW04-CAND-018` | `FR12-17` | User JWT `POST /api/admin/coupons` returned 200 and created a coupon | 3/3 browsers | Critical | [`BUG-016`](https://github.com/KidCute1412/eshop-sut/issues/156) |
| `HW04-CAND-019` | `FR12-19` | User JWT reached import validation and returned 400, not authorization rejection 403 | 3/3 browsers | Critical | [`BUG-017`](https://github.com/KidCute1412/eshop-sut/issues/157) |

Severity is an initial risk-based classification grounded in FR-06/FR-10/FR-12 impact. The student must confirm it during GitHub Issue triage.

## Environment finding — not an SUT defect

### `ENV-FIREFOX-NEWPAGE` — superseded setup diagnosis

| Field | Value |
|---|---|
| Environment | Playwright 1.55.0; Firefox 141.0 headless; Windows 10 Home Single Language / NT `10.0.26200.0` |
| Symptom | `Test timeout of 30000ms exceeded while setting up "page"` and `browserContext.newPage: Test timeout of 30000ms exceeded` |
| Affected executions | Historical diagnostic runs only; excluded from the nine selected final runs |
| Classification | Environment/runtime failure; excluded from SUT defect candidates |
| Rationale | Failure occurred before the test could observe the target application behavior |

The earlier failures were traced to the `Desktop Firefox` device options. The final option-free headless rerun reached all 51 Firefox assertions, so this diagnostic record is not part of the final failure totals and is not an SUT defect.

## Human-correction evidence

An earlier WebKit FR-10 run produced a false `FR10-02` failure because substring row matching allowed order `#2` to match another order such as `#20`. Human review changed the locator to require an exact order-ID cell and reran all three FR-10 browser runs. `FR10-02` passes in the selected final Chromium, Firefox, and WebKit reports; it is not included as a candidate.

## Issue filing gate

Before promoting a candidate to a GitHub Issue:

1. record the exact SUT commit, URLs, OS, and browser version;
2. reproduce the behavior from a controlled seed/state and rule out assertion/data defects;
3. preserve the relevant final report, trace, and authentic screenshot;
4. deduplicate cases that share one root behavior;
5. create the public Issue with steps, expected/actual result, severity rationale, case/run IDs, and screenshot; and
6. verify the URL and attachment while logged out where practical.

Multiple failing cases may map to one root defect. The current count is **19 assertion-failing logical cases**, not a claim of 19 deduplicated product defects.
