# Task 3 - Continuous Performance Testing Proposal

## 1. Goal

The proposed model continuously watches SUT changes, decides when performance tests are worth running, compares p95 latency against a baseline, and flags regressions before merge.

## 2. Pipeline Flow

```text
Developer commit / PR
        |
        v
GitHub Actions trigger
        |
        v
Decision engine checks changed files
        |
        +-- docs-only or frontend-only change --> Skip performance suite
        |
        +-- backend / database / dependency change
                |
                v
        Start SUT on CI runner
                |
                v
        Seed performance data
                |
                v
        Run quick JMeter load plan
                |
                v
        Collect .jtl + HTML report
                |
                v
        Parse p95, p99, error rate, throughput
                |
                v
        Compare against baseline
                |
                +-- p95 <= baseline + 10% and errors within limit --> PASS
                |
                +-- p95 > baseline + 10% but <= +25% --> WARN in PR
                |
                +-- p95 > baseline + 25% or error rate too high --> FAIL / block PR
```

## 3. Decision Engine

Performance tests run when at least one condition is true:

| Trigger | Reason |
|---------|--------|
| `backend/**` changed | Direct API performance impact |
| `backend/database.js` or database files changed | Query shape, seed data, or write behavior may change |
| `package.json` or lockfile changed | Dependency upgrades can change runtime behavior |
| Manual workflow dispatch | Allows investigation before release |
| Nightly schedule | Detects accumulated regressions |

Performance tests are skipped when:

- Only Markdown/report files changed.
- Only screenshots or homework documents changed.
- Only frontend styling changed and API calls are unaffected.
- Commit message contains `[skip-perf]` with a written reason.

## 4. Baseline Thresholds

The baseline values below come from the completed local JMeter runs. Warn/fail values are intentionally conservative because CI hardware can be noisier than the local test machine.

| Metric | Baseline Value | Warn Threshold | Fail Threshold | Source |
|--------|----------------|----------------|----------------|--------|
| Login p95 response time | 3 ms | > 3.3 ms | > 3.75 ms | Load dashboard statistics |
| Product list p95 response time | 2 ms | > 2.2 ms | > 2.5 ms | Load dashboard statistics |
| Checkout p95 response time | 7 ms | > 7.7 ms | > 8.75 ms | Load dashboard statistics |
| Overall p95 response time | 6 ms | > 6.6 ms | > 7.5 ms | Load `.jtl` |
| Overall error rate | 0.00% | > 1% | > 5% | Load/Stress/Spike `.jtl` |
| Max stable throughput | 4.83 req/s | < 4.35 req/s | < 3.62 req/s | 10-minute Load run |

## 5. Test Suite Tiers

| Tier | Trigger | Scenario | Duration | Purpose |
|------|---------|----------|----------|---------|
| PR smoke | Backend-related PR | 5 VUsers | 60s | Fast feedback |
| PR load check | High-risk backend/database PR | 10 VUsers | 300s | Regression detection |
| Nightly load | Schedule | 10 VUsers | 600s | Stable baseline tracking |
| Weekly stress | Schedule/manual | 50 VUsers | 600s | Capacity trend and breaking-point check |

## 6. Implementation Sketch

```yaml
name: performance-check

on:
  pull_request:
  workflow_dispatch:
  schedule:
    - cron: "0 18 * * *"

jobs:
  decide-and-run:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Decide whether to run performance tests
        run: |
          echo "Check changed files and skip docs-only changes"
      - name: Install backend dependencies
        working-directory: backend
        run: npm ci
      - name: Start backend
        working-directory: backend
        run: nohup node server.js &
      - name: Seed performance data
        run: node hw05/submit/task1/seed_performance_data.js
      - name: Run JMeter
        run: |
          jmeter -n -t hw05/submit/task1/23127296_Load_20260815.jmx \
            -l hw05/submit/task1/ci_load.jtl \
            -e -o hw05/submit/task1/ci_load_html
      - name: Analyze JTL
        run: node hw05/submit/task2/analyze_jtl.mjs hw05/submit/task1/ci_load.jtl
```

## 7. Trade-Offs

| Trade-off | Discussion | Mitigation |
|-----------|------------|------------|
| CI time | Performance tests add minutes to feedback time. | Run smoke checks on PRs and longer tests nightly. |
| Hardware noise | Shared runners can vary in CPU, memory, and I/O. | Use medians across repeated runs or a stable self-hosted runner. |
| False alarms | Temporary machine load can make p95 exceed threshold. | Warn at +10%, fail only at +25% or repeated regression. |
| False negatives | Loose thresholds can miss smaller regressions. | Review trend history monthly and tighten baselines gradually. |
| Maintenance cost | JMeter plans and CSV data must evolve with the API. | Version plans with backend changes and keep seed data scripted. |
| Data pollution | Checkout tests create orders repeatedly. | Use dedicated performance users and reset/clean test data after runs. |

## 8. Conclusion

The recommended continuous model is tiered: quick PR smoke tests for fast feedback, nightly load tests for baseline tracking, and weekly/manual stress tests for capacity insight. This balances cost and regression detection while keeping p95 latency, error rate, and throughput visible in every backend change.
