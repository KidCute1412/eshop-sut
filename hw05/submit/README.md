# HW05 Performance Testing Submission

## Student Information

- Student ID: 23127296
- Name: Nguyen Thanh Luan
- Self-assessed grade: 100/100

## Self-Assessment Table

| No. | Criteria | Grade | Self-Assessed Grade |
|-----|----------|-------|---------------------|
| 1 | Task 1 - Load Testing | 20 | 20 |
| 2 | Task 1 - Stress Testing | 20 | 20 |
| 3 | Task 1 - Spike Testing | 20 | 20 |
| 4 | Task 2 - AI Analysis + Misinterpretation Hunt | 10 | 10 |
| 5 | Task 3 - Continuous Performance Testing Proposal | 10 | 10 |
| 6 | Agent Skills | 10 | 10 |
| | Total | 100 | 100 |

## Test Summary Report

| Scenario | Plan File | Raw Result | HTML Dashboard | VUsers | Duration | Status |
|----------|-----------|------------|----------------|--------|----------|--------|
| Load | `task1/load/23127296_Load_20260815.jmx` | `task1/load/23127296_Load_20260815.jtl` | `task1/load/23127296_Load_20260815_html/index.html` | 10 | 600s | PASS |
| Stress | `task1/stress/23127296_Stress_20260815.jmx` | `task1/stress/23127296_Stress_20260815.jtl` | `task1/stress/23127296_Stress_20260815_html/index.html` | 50 | 600s | PASS |
| Spike | `task1/spike/23127296_Spike_20260815.jmx` | `task1/spike/23127296_Spike_20260815.jtl` | `task1/spike/23127296_Spike_20260815_html/index.html` | 100 | 180s | PASS |

## Performance Results

| Scenario | Samples | Errors | Error Rate | Throughput | Avg | Min | Max | p95 | p99 |
|----------|---------|--------|------------|------------|-----|-----|-----|-----|-----|
| Load | 2,888 | 0 | 0.00% | 4.83 req/s | 2.06 ms | 0 ms | 249 ms | 6 ms | 7 ms |
| Stress | 13,488 | 0 | 0.00% | 22.54 req/s | 1.66 ms | 0 ms | 36 ms | 5 ms | 6 ms |
| Spike | 8,812 | 0 | 0.00% | 49.43 req/s | 1.79 ms | 0 ms | 134 ms | 5 ms | 6 ms |

## Endpoint Groups Covered

- Auth-heavy: `POST /api/login`
- Read-heavy: `GET /api/products`, `GET /api/products?search=`, `GET /api/products/:id`, `GET /api/categories`
- Transactional: `POST /api/cart`, `GET /api/cart`, `POST /api/checkout`, `GET /api/orders/my-orders`

## Endurance Threshold

The Load run is used as the short soak baseline because it ran for 600 seconds.

| Metric | Value | Evidence |
|--------|-------|----------|
| Maximum Stable RPS | 4.83 req/s | `task1/load/23127296_Load_20260815.jtl` |
| Response Time Degradation Point | Not reached; 0 errors and p95 6 ms | Load JTL and HTML dashboard |
| Average Response Time | 2.06 ms | Load JTL |
| p95 Response Time | 6 ms | Load JTL |
| p99 Response Time | 7 ms | Load JTL |
| Error Rate | 0.00% | Load JTL |
| Memory/CPU Evidence | Captured in screenshots | `screenshots/load1.png`, `screenshots/stress1.png`, `screenshots/spike1.png` |

## Bugs / Performance Issues

- Number of bugs found: 0
- Number of performance issues found: 0
- GitHub Issues: none filed because all three scenarios completed with 0.00% error rate and no reproducible failure.

## Demo Videos

- Agent skill demo: https://youtu.be/qv-L1yJtbAg
- Task 1 demo: https://youtu.be/ks-tb_c9mmY

## File Structure

```text
submit/
  README.md
  ai_audit_report.md
  ai_critique.md
  git_commit_log.txt
  agent-skill/
    log-analysis-skill/
      SKILL.md
    performance-test-skill/
      SKILL.md
  screenshots/
    dxdiag.png
    load1.png
    stress1.png
    spike1.png
  task1/
    seed_performance_data.js
    test_plan_review.md
    load/
      23127296_Load_20260815.jmx
      23127296_Load_20260815.jtl
      23127296_Load_20260815.log
      log4j2-nogui.xml
      test_data_users.csv
      test_data_products.csv
      test_data_checkout.csv
      23127296_Load_20260815_html/
    stress/
      23127296_Stress_20260815.jmx
      23127296_Stress_20260815.jtl
      23127296_Stress_20260815.log
      log4j2-nogui.xml
      test_data_users.csv
      test_data_products.csv
      test_data_checkout.csv
      23127296_Stress_20260815_html/
    spike/
      23127296_Spike_20260815.jmx
      23127296_Spike_20260815.jtl
      23127296_Spike_20260815.log
      log4j2-nogui.xml
      test_data_users.csv
      test_data_products.csv
      test_data_checkout.csv
      23127296_Spike_20260815_html/
  task2/
    ai_analysis_and_review.md
    analyze_jtl.mjs
  task3/
    continuous_testing_proposal.md
```
