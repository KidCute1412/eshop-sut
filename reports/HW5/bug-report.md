# HW05 Bug / Performance Issue Report

No functional bug is claimed from the current performance runs.

## Evidence Reviewed

| Scenario | Samples | Failed | Error Rate | Main Observation |
|---|---:|---:|---:|---|
| Load | 500 | 0 | 0.00% | Stable baseline run. |
| Stress | 63,371 | 0 | 0.00% | Stable under sustained pressure. |
| Spike | 1,500 | 0 | 0.00% | Checkout had the largest latency spike. |
| Endurance / Soak | 232,529 | 0 | 0.00% | Checkout remained the slowest endpoint. |

## Performance Observation

Checkout is the main bottleneck candidate. In the Spike run, Checkout reached p95 = 518ms. In the Endurance / Soak run, Checkout reached p95 = 754ms while all samples still passed. This is reported as an observation, not a confirmed bug, because there was no defined service-level objective in the assignment and no failed checkout responses were observed.

## GitHub Issue Decision

No GitHub Issue was filed because the raw `.jtl` logs did not show reproducible failures, backend crashes, or non-zero error rates. If a future run defines a stricter p95 threshold or shows SQLite lock/contention errors, the issue should include the raw `.jtl`, HTML report, and resource-monitor screenshot.
