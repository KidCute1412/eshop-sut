# Task 1 - AI Assisted Test Design and Execution

## 1. Workflow Design

The three JMeter plans exercise the same end-to-end e-commerce workflow:

1. `POST /api/login`
2. `GET /api/products`
3. `GET /api/products?search=...`
4. `GET /api/products/:id`
5. `GET /api/categories`
6. `POST /api/cart`
7. `GET /api/cart`
8. `POST /api/checkout`
9. `GET /api/orders/my-orders`

This represents a realistic user journey: login, browse/search products, inspect an item, add it to cart, checkout, then view order history.

## 2. Final Test Plans

| Scenario | File | VUsers | Ramp-up | Duration | Status |
|----------|------|--------|---------|----------|--------|
| Load | `load/23127296_Load_20260815.jmx` | 10 | 60s | 600s | Executed |
| Stress | `stress/23127296_Stress_20260815.jmx` | 50 | 120s | 600s | Executed |
| Spike | `spike/23127296_Spike_20260815.jmx` | 100 | 5s | 180s | Executed |

The plans use CSV files for credentials, products, and checkout data:

- `test_data_users.csv`
- `test_data_products.csv`
- `test_data_checkout.csv`

## 3. Human Review and Fixes

| # | Issue Found | Correction Applied | Reason |
|---|-------------|--------------------|--------|
| 1 | Original JMX files used sample student ID/date. | Renamed final files to `23127296_*_20260815.jmx`. | Matches the required naming convention. |
| 2 | CSV users were not guaranteed to exist in SQLite. | Added `seed_performance_data.js`. | Prevents login failures during protected workflows. |
| 3 | Some generated JMX files nested `HeaderManager` inside HTTP samplers. | Rebuilt Load, Stress, and Spike plans with valid JMeter 5.6.3 structure. | Fixes `ClassCastException` when loading plans. |
| 4 | Stress/Spike needed separate result folders. | Split execution folders into `load`, `stress`, and `spike`. | Keeps raw logs, HTML reports, and related artifacts organized. |
| 5 | JMeter dashboard failed when an interrupted JTL had a partial row. | Reran Stress fully and verified `Dashboard generated`. | Ensures the submitted `.jtl` and HTML dashboard are complete. |

## 4. Assertions and Auth Handling

- Login response assertion checks HTTP 200.
- JWT token is extracted from `$.token`.
- Protected requests send `Authorization: Bearer ${auth_token}`.
- CSV files drive users, products, quantities, search keywords, and checkout data.

## 5. Execution Evidence Status

| Required Evidence | Status | Location |
|-------------------|--------|----------|
| Load `.jtl` raw log | Done | `load/23127296_Load_20260815.jtl` |
| Stress `.jtl` raw log | Done | `stress/23127296_Stress_20260815.jtl` |
| Spike `.jtl` raw log | Done | `spike/23127296_Spike_20260815.jtl` |
| Load HTML report folder | Done | `load/23127296_Load_20260815_html/` |
| Stress HTML report folder | Done | `stress/23127296_Stress_20260815_html/` |
| Spike HTML report folder | Done | `spike/23127296_Spike_20260815_html/` |
| JMeter + Task Manager screenshots | Done | `/screenshots/load1.png`, `/screenshots/stress1.png`, `/screenshots/spike1.png` |
| Hardware spec screenshot | Done | `/screenshots/dxdiag.png` |

## 6. Result Summary

| Scenario | Samples | Errors | Error Rate | Throughput | Avg | Max | p95 | p99 |
|----------|---------|--------|------------|------------|-----|-----|-----|-----|
| Load | 2,888 | 0 | 0.00% | 4.83 req/s | 2.06 ms | 249 ms | 6 ms | 7 ms |
| Stress | 13,488 | 0 | 0.00% | 22.54 req/s | 1.66 ms | 36 ms | 5 ms | 6 ms |
| Spike | 8,812 | 0 | 0.00% | 49.43 req/s | 1.79 ms | 134 ms | 5 ms | 6 ms |

## 7. Endurance Threshold

The Load run is used as the 10-minute soak baseline.

| Metric | Value | Source |
|--------|-------|--------|
| Max Stable RPS | 4.83 req/s | Load JTL |
| Avg Response Time | 2.06 ms | Load JTL |
| p95 Response Time | 6 ms | Load JTL |
| p99 Response Time | 7 ms | Load JTL |
| Error Rate | 0.00% | Load JTL |
| CPU/Memory Evidence | Captured | Task Manager screenshots |

## 8. Bugs and Performance Issues

No reproducible bugs or performance issues were filed because all three runs completed successfully with 0.00% error rate. The main endpoint to monitor in future tests is `POST /api/checkout`, which had the highest average latency because it performs write operations.
