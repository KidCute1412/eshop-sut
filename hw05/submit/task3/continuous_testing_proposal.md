# Task 3 — Continuous Performance Testing Proposal

## 1. Overview

Propose a continuous performance-testing model that integrates with the SUT's development workflow to automatically detect performance regressions.

---

## 2. Proposed Pipeline Flow

```
┌─────────────┐    ┌──────────────┐    ┌─────────────────┐    ┌──────────────────┐
│  Developer   │───▶│  Git Push /  │───▶│  CI/CD Trigger  │───▶│  Decision Engine │
│  Commit      │    │  PR Created  │    │  (GitHub Actions)│    │  (Run Tests?)    │
└─────────────┘    └──────────────┘    └─────────────────┘    └────────┬─────────┘
                                                                      │
                                                              ┌───────▼───────┐
                                                              │  YES: Run     │
                                                              │  Performance  │
                                                              │  Tests        │
                                                              └───────┬───────┘
                                                                      │
                                                          ┌───────────▼───────────┐
                                                          │  Execute Load/Stress  │
                                                          │  Test Suite (JMeter)  │
                                                          └───────────┬───────────┘
                                                                      │
                                                          ┌───────────▼───────────┐
                                                          │  Collect .jtl Logs    │
                                                          │  Generate Reports     │
                                                          └───────────┬───────────┘
                                                                      │
                                                          ┌───────────▼───────────┐
                                                          │  Compare Against      │
                                                          │  Baseline Thresholds  │
                                                          └───────────┬───────────┘
                                                                      │
                                                      ┌───────────────┼───────────────┐
                                                      │               │               │
                                              ┌───────▼──────┐ ┌─────▼─────┐ ┌───────▼──────┐
                                              │  ✅ PASS     │ │  ⚠️ WARN  │ │  ❌ FAIL     │
                                              │  No regression│ │ p95 > 10% │ │ p95 > 25%   │
                                              │  of baseline │ │ above BL  │ │ above BL    │
                                              └───────┬──────┘ └─────┬─────┘ └───────┬──────┘
                                                      │               │               │
                                              ┌───────▼──────┐ ┌─────▼─────┐ ┌───────▼──────┐
                                              │  PR Approved │ │  Warning  │ │  PR Blocked  │
                                              │  Merge Ready │ │  Comment  │ │  Must Fix    │
                                              └──────────────┘ └───────────┘ └──────────────┘
```

---

## 3. Decision Engine: When to Run Performance Tests

### Trigger Conditions
Performance tests run when ANY of the following conditions are met:

| # | Trigger | Rationale |
|---|---------|-----------|
| 1 | **PR touches backend code** (`backend/**`) | Direct impact on API performance |
| 2 | **PR touches database schema/migrations** | Schema changes can degrade queries |
| 3 | **Dependency version bump** (`package.json`, `requirements.txt`) | New versions may introduce performance changes |
| 4 | **Scheduled nightly run** | Catch gradual degradation from accumulated changes |
| 5 | **Manual trigger** (`/run-perf-tests` in PR comment) | On-demand for specific investigations |

### Skip Conditions
Tests are SKIPPED when:
- PR only touches documentation (`docs/**`, `*.md`)
- PR only touches frontend (`frontend/**`) — unless it impacts API calls
- PR only touches test files (`**/*_test.*`, `**/*.test.*`)
- Commit message contains `[skip-perf]` (with justification required)

---

## 4. Baseline Thresholds

Established from initial test runs on target hardware:

| Metric | Baseline Value | Warning Threshold (+10%) | Fail Threshold (+25%) |
|--------|---------------|-------------------------|----------------------|
| Login p95 Response Time | [__] ms | [__] ms | [__] ms |
| Product List p95 Response Time | [__] ms | [__] ms | [__] ms |
| Checkout p95 Response Time | [__] ms | [__] ms | [__] ms |
| Overall Error Rate | [__]% | [__]% | [__]% |
| Max Throughput (RPS) | [__] | [__] | [__] |

### Baseline Update Policy
- Baselines are recalculated monthly or after significant infrastructure changes
- Baseline updates require approval from [team lead / instructor]
- Historical baselines are retained for trend analysis

---

## 5. Test Suite Configuration

### Automated Test Scenarios

| Scenario | VUsers | Duration | Purpose |
|----------|--------|----------|---------|
| Quick Smoke | 5 | 60s | Verify basic functionality under light load |
| Standard Load | 10 | 300s | Compare against baseline |
| Regression Check | 20 | 300s | Detect degradation under moderate load |

### Execution Flow
1. Checkout PR branch
2. Start SUT backend (if not running)
3. Run JMeter test with `.jmx` plan
4. Parse `.jtl` output for p95, p99, error rate, throughput
5. Compare metrics against baseline thresholds
6. Generate report and post results as PR comment

---

## 6. Trade-Off Discussion

### Cost vs. Benefit

| Factor | Discussion |
|--------|------------|
| **CI/CD Build Time** | Adding performance tests increases build time by ~5-10 minutes. Mitigation: run only on backend-related PRs, use quick smoke for PRs and full suite for nightly. |
| **Infrastructure Cost** | Running JMeter on CI runners requires moderate CPU/memory. Mitigation: use self-hosted runners or cloud-based load testing services. |
| **False Alarms** | Network波动 or background processes on shared CI runners can cause flaky results. Mitigation: run tests 3x and use median values; add tolerance margins. |
| **False Negatives** | Thresholds set too loosely may miss real regressions. Mitigation: regularly review and tighten thresholds based on production data. |
| **Maintenance Burden** | Test plans and baselines need ongoing maintenance as the application evolves. Mitigation: version control test plans, automate baseline updates. |
| **Developer Experience** | Blocking PRs on performance failures may frustrate developers. Mitigation: use warnings for minor regressions, only block on severe degradation (>25%). |

### Recommended Approach
- **PR-level**: Quick smoke test (5 VUsers, 60s) — fast feedback, low cost
- **Nightly**: Standard load test (10 VUsers, 5min) — comprehensive comparison
- **Weekly**: Stress test (50 VUsers, 10min) — capacity planning

---

## 7. Implementation Tools

| Component | Tool | Alternative |
|-----------|------|-------------|
| CI/CD | GitHub Actions | GitLab CI, Jenkins |
| Load Testing | JMeter | k6, Gatling |
| Result Parsing | JMeter CLI report | Custom Python script |
| Notification | GitHub PR comments | Slack, Email |
| Dashboard | Grafana + InfluxDB | Datadog, New Relic |

---

## 8. Conclusion

A continuous performance testing pipeline provides early detection of regressions while balancing cost and developer experience. The key is to make tests fast enough for PR feedback and comprehensive enough for nightly regression detection. By setting appropriate thresholds and using tiered testing (smoke → load → stress), the pipeline catches issues before they reach production without becoming a bottleneck in the development workflow.
