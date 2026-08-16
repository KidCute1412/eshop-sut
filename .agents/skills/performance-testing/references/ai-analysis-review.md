# AI Analysis Review

## Prompting AI for Log Analysis

Ask AI to analyse raw `.jtl` logs and return:

- Samples and failures.
- Error rate.
- Average, median, p90, p95, p99.
- Throughput/RPS.
- Slowest endpoint labels.
- Suggested endurance threshold.
- Optimization recommendations.

## Human Misinterpretation Hunt

Check whether AI:

- Confused average latency with p95 or p99.
- Ignored failed samples.
- Treated client-side timeouts as backend success.
- Generalized from one scenario to all scenarios.
- Missed that checkout writes to SQLite.
- Proposed infrastructure that does not exist in this local SUT.

## Recommendation Classification

Examples:

- Feasible: add indexes for product search/order lookup, parameterize product search query, enable
  SQLite WAL for local write concurrency, add a bounded DB connection strategy if supported.
- Needs evidence: caching product search, batching writes, reducing response payloads.
- Likely hallucinated: Kubernetes autoscaling, Kafka, CDN for backend checkout bottleneck, Redis
  cluster without deployment context.

## Continuous Testing Proposal

Include a flow like:

`Commit -> Change classifier -> Smoke workflow -> Full Load run for API/DB changes -> Compare p95/error rate with baseline -> Flag regression -> Attach report artifacts`

Discuss cost, false positives, noisy local machines, seed database reset, and threshold tuning.

