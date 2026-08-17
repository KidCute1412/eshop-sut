# Task 2 - AI Analysis and Review

## 1. Evidence Reviewed

The analysis is based on the completed JMeter runs in:

- `hw05/submit/task1/load`
- `hw05/submit/task1/stress`
- `hw05/submit/task1/spike`

Primary evidence sources:

- Raw JTL: `23127296_Load_20260815.jtl`, `23127296_Stress_20260815.jtl`, `23127296_Spike_20260815.jtl`
- JMeter logs: `23127296_Load_20260815.log`, `stress/jmeter.log`, `spike/jmeter.log`
- Dashboard statistics: `*_html/statistics.json`

All three scenarios have generated HTML dashboards, and their logs include the `Dashboard generated` confirmation.

## 2. Scenario Summary

| Scenario | Status | Samples | Errors | Error Rate | Throughput | Avg | Min | Max | p95 | p99 |
|----------|--------|---------|--------|------------|------------|-----|-----|-----|-----|-----|
| Load | PASS | 2,888 | 0 | 0.00% | 4.83 req/s | 2.06 ms | 0 ms | 249 ms | 6 ms | 7 ms |
| Stress | PASS | 13,488 | 0 | 0.00% | 22.54 req/s | 1.66 ms | 0 ms | 36 ms | 5 ms | 6 ms |
| Spike | PASS | 8,812 | 0 | 0.00% | 49.43 req/s | 1.79 ms | 0 ms | 134 ms | 5 ms | 6 ms |

## 3. Findings By Scenario

### Load Test

The Load test ran with 10 virtual users for approximately 10 minutes. The result was stable: 2,888 samples, 0 errors, and 4.83 req/s throughput. Average response time was 2.06 ms, p95 was 6 ms, and p99 was 7 ms.

The slowest endpoint was `08 POST /api/checkout`, with 6.41 ms average response time and 249 ms maximum response time. This is expected because checkout is a write-heavy flow that creates an order and processes cart data.

### Stress Test

The Stress test ran with 50 virtual users for approximately 10 minutes. The result remained stable: 13,488 samples, 0 errors, and 22.54 req/s throughput. Average response time was 1.66 ms, p95 was 5 ms, and p99 was 6 ms.

Endpoint `08 POST /api/checkout` remained the highest-average endpoint at about 5.10 ms. `09 GET /api/orders/my-orders` had the largest response-byte volume in the dashboard, so it should be monitored when the database grows.

### Spike Test

The Spike test ran with 100 virtual users, a fast 5-second ramp-up, and an approximately 3-minute duration. The result passed: 8,812 samples, 0 errors, and 49.43 req/s throughput. Average response time was 1.79 ms, p95 was 5 ms, and p99 was 6 ms.

The highest maximum response time was 134 ms on `01 POST /api/login`. This is likely related to the burst of simultaneous thread startup and connections, but it did not affect p95 or p99 latency.

## 4. Bottleneck And Risk Review

The clearest current bottleneck candidate is `POST /api/checkout` because it writes data and has a higher average response time than the GET endpoints. However, latency stayed very low across all three scenarios, with no evidence of overload.

The main risk is that the test environment is local, uses SQLite, and has a small dataset; therefore, results may be more optimistic than a production-like environment. Read endpoints such as product list and order history may become slower with a larger database. Checkout may also encounter write contention if user count and cart size increase significantly.

## 5. Recommendations

- Keep the initial CI threshold conservative for local testing: error rate <= 1%, p95 <= 200 ms, and p99 <= 500 ms.
- Monitor `POST /api/checkout` separately because it writes data and is the first optimization candidate if latency increases.
- Add a larger-dataset test to evaluate `GET /api/products?search=` and `GET /api/orders/my-orders`.
- Consider enabling SQLite WAL mode if SQLite remains the database and read/write concurrency needs to improve.
- Do not conclude that the system is production-ready based only on these local results; rerun in a more production-like environment if the course requirements allow it.

## 6. Misinterpretation Hunt

| Possible AI Claim | Correct Review | Evidence |
|-------------------|----------------|----------|
| Stress test failed because no HTML folder existed earlier | Incorrect after rerun | `stress/23127296_Stress_20260815_html/statistics.json` exists and log shows `Dashboard generated`. |
| Spike test has high latency because max is 134 ms | Misleading | p95 is 5 ms and p99 is 6 ms; max is an outlier during burst startup. |
| Checkout is broken because it is slower than GET endpoints | Incorrect | Checkout has 0 errors; it is expected to be slower because it writes order/cart data. |
| Throughput should be compared directly across all scenarios | Needs context | Load, Stress, and Spike use different user counts, ramp-up, and duration. |
