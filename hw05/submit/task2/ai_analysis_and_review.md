# Task 2 - AI Analysis and Misinterpretation Hunt

## 1. Current Status

Real `.jtl` logs are not present yet, and this terminal cannot run JMeter because `jmeter` is not available on PATH. Therefore, no final performance values are claimed in this document.

After running the three JMeter plans, place the raw logs here:

- `../task1/23127296_Load_20260815.jtl`
- `../task1/23127296_Stress_20260815.jtl`
- `../task1/23127296_Spike_20260815.jtl`

Then run:

```powershell
node hw05\submit\task2\analyze_jtl.mjs `
  hw05\submit\task1\23127296_Load_20260815.jtl `
  hw05\submit\task1\23127296_Stress_20260815.jtl `
  hw05\submit\task1\23127296_Spike_20260815.jtl
```

## 2. AI Analysis Prompt To Use After Logs Exist

```text
You are reviewing JMeter CSV .jtl logs for an Express + SQLite e-commerce SUT.

Analyze the attached Load, Stress, and Spike logs. For each scenario, report:
1. total samples,
2. error count and error rate,
3. average response time,
4. p95 and p99 response time,
5. throughput in requests/second,
6. endpoints with the highest latency or error rate,
7. suggested baseline thresholds for future CI performance checks.

Do not invent values. Cite the exact value from the raw .jtl log or from the computed summary. If a metric is missing, say it is missing.
```

## 3. Expected AI Output Fields

| Field | Status |
|-------|--------|
| Overall Load result | PENDING_JTL_LOGS |
| Overall Stress result | PENDING_JTL_LOGS |
| Overall Spike result | PENDING_JTL_LOGS |
| Bottleneck endpoint(s) | PENDING_JTL_LOGS |
| Suggested thresholds | PENDING_JTL_LOGS |
| Optimization recommendations | Ready for source-code feasibility review |

## 4. Misinterpretation Hunt Template

Fill this table after comparing the AI's claims with `analyze_jtl.mjs` output and raw `.jtl` rows.

| # | AI Claim | Correct Raw Value | Evidence | Why AI Was Wrong |
|---|----------|-------------------|----------|------------------|
| 1 | PENDING_AI_ANALYSIS | PENDING_JTL_LOGS | `.jtl` row or computed summary | PENDING_REVIEW |
| 2 | PENDING_AI_ANALYSIS | PENDING_JTL_LOGS | `.jtl` row or computed summary | PENDING_REVIEW |
| 3 | PENDING_AI_ANALYSIS | PENDING_JTL_LOGS | `.jtl` row or computed summary | PENDING_REVIEW |

Common mistakes to check:

- Dividing request count by configured duration instead of actual first-to-last sample timestamp.
- Treating failed samples as successful latency measurements without reporting error rate.
- Reporting p95/p99 from average values instead of sorted elapsed times.
- Comparing Spike throughput directly with Load throughput without accounting for different duration and user profile.

## 5. Optimization Recommendation Review

These feasibility notes are based on the actual backend source code. Update the final classification after the AI gives its recommendations.

| AI Recommendation | Feasibility | Source-Based Reasoning |
|-------------------|-------------|------------------------|
| Add an index for product search | Partially feasible | `GET /api/products?search=` uses `LIKE '%keyword%'`, so a normal index may not help much with leading wildcards. A safer fix is parameterized query plus search design review. |
| Enable SQLite WAL mode | Feasible | The SUT uses SQLite and checkout writes orders. WAL can improve read/write concurrency for local SQLite workloads, but it must be tested. |
| Add a database connection pool | Partially feasible | Generic advice. The current app uses `sqlite3.Database`; SQLite does not behave like client/server DB pooling. A queue or migration to a server DB may be more appropriate. |
| Add Redis cache for product list | Partially feasible | Product listing is read-heavy and mostly static, but this adds infrastructure complexity beyond the demo app. |
| Switch to PostgreSQL | Feasible but high cost | Could improve concurrent write behavior, but it is an architectural migration, not a quick performance fix for HW05. |
| Optimize checkout transaction handling | Feasible | `POST /api/checkout` performs writes without explicit transaction/validation of cart state. This is a realistic area to inspect under stress. |

## 6. Threshold Comparison

Fill after real logs exist.

| Metric | AI-Suggested Threshold | Validated Threshold | Agreement |
|--------|------------------------|---------------------|-----------|
| Max RPS | PENDING_AI_ANALYSIS | PENDING_JTL_LOGS | PENDING |
| p95 Response Time | PENDING_AI_ANALYSIS | PENDING_JTL_LOGS | PENDING |
| p99 Response Time | PENDING_AI_ANALYSIS | PENDING_JTL_LOGS | PENDING |
| Error Rate Threshold | PENDING_AI_ANALYSIS | PENDING_JTL_LOGS | PENDING |
| Memory Ceiling | PENDING_AI_ANALYSIS | PENDING_SCREENSHOT | PENDING |
