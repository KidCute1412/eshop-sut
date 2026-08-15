# HW05 Performance Testing Submission

## Student Information

- Student ID: 23127296
- Name: Nguyen Thanh Luan
- Self-assessed grade: PENDING_REAL_RUN

## Self-Assessment Table

Final scores must be filled after the real JMeter runs, screenshots, video, and `.jtl` logs are attached.

| No. | Criteria | Grade | Self-Assessed Grade |
|-----|----------|-------|---------------------|
| 1 | Task 1 - Load Testing | 20 | PENDING_REAL_RUN |
| 2 | Task 1 - Stress Testing | 20 | PENDING_REAL_RUN |
| 3 | Task 1 - Spike Testing | 20 | PENDING_REAL_RUN |
| 4 | Task 2 - AI Analysis + Misinterpretation Hunt | 10 | PENDING_JTL_LOGS |
| 5 | Task 3 - Continuous Performance Testing Proposal | 10 | READY_FOR_REVIEW |
| 6 | Agent Skills | 10 | READY_FOR_REVIEW |
| | Total | 100 | PENDING_REAL_RUN |

## Test Summary Report

| Scenario | Plan File | VUsers | Duration | Status |
|----------|-----------|--------|----------|--------|
| Load Test | `task1/23127296_Load_20260815.jmx` | 10 | 600s | Ready, not executed in this terminal |
| Stress Test | `task1/23127296_Stress_20260815.jmx` | 50 | 600s | Ready, not executed in this terminal |
| Spike Test | `task1/23127296_Spike_20260815.jmx` | 5 -> 100 -> 5 | 60s + 30s + 120s | Ready, not executed in this terminal |

## Endpoint Groups Covered

- Auth-heavy: `POST /api/login`
- Read-heavy: `GET /api/products`, `GET /api/products?search=`, `GET /api/products/:id`, `GET /api/categories`
- Transactional: `POST /api/cart`, `GET /api/cart`, `POST /api/checkout`, `GET /api/orders/my-orders`

## Execution Notes

- JMeter is required but was not available on PATH in this terminal.
- Node.js is required to start the backend and seed performance users, but `node` was not available on PATH in this terminal.
- Use `task1/runbook.md` to run the SUT, seed data, execute JMeter, generate `.jtl` logs, and create HTML reports.
- Use `task2/analyze_jtl.mjs` after the `.jtl` files exist to compute p95, p99, error rate, and throughput.

## Endurance Threshold

These values must be filled from the real 10 to 15 minute soak run.

| Metric | Value |
|--------|-------|
| Maximum Stable RPS | PENDING_JTL_LOGS |
| Memory Ceiling | PENDING_SCREENSHOT |
| Response Time Degradation Point | PENDING_JTL_LOGS |

## Bugs / Performance Issues

- Number of bugs found: PENDING_REAL_RUN
- Number of performance issues found: PENDING_REAL_RUN
- GitHub Issues link: https://github.com/KidCute1412/eshop-sut/issues

## Demo Video

- YouTube link: PENDING_USER_INPUT
- Duration: PENDING_USER_INPUT

## File Structure

```text
submit/
  README.md
  ai_audit_report.md
  ai_critique.md
  task1/
    23127296_Load_20260815.jmx
    23127296_Stress_20260815.jmx
    23127296_Spike_20260815.jmx
    test_data_users.csv
    test_data_products.csv
    test_data_checkout.csv
    seed_performance_data.js
    runbook.md
    test_plan_review_notes.md
  task2/
    ai_analysis_and_review.md
    analyze_jtl.mjs
  task3/
    continuous_testing_proposal.md
  screenshots/
```

## Required Files Still To Add After Real Execution

- `task1/23127296_Load_20260815.jtl`
- `task1/23127296_Stress_20260815.jtl`
- `task1/23127296_Spike_20260815.jtl`
- `task1/23127296_Load_20260815_html/`
- `task1/23127296_Stress_20260815_html/`
- `task1/23127296_Spike_20260815_html/`
- Resource-monitor screenshots for Load, Stress, and Spike
- Hardware-spec screenshot
- Unlisted YouTube demo video link
- `git_commit_log.txt`
