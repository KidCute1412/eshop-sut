# Performance Method

## Scenario Intent

| Scenario | Purpose | Typical Local Starting Point |
|---|---|---|
| Load | Normal sustained usage | 10-25 VUs, gradual ramp-up, realistic think time |
| Stress | Find degradation point | Step up or high VUs until latency/errors degrade |
| Spike | Recovery after abrupt burst | Low baseline, abrupt high VUs, then recovery |
| Endurance | Sustained stability threshold | 10-15 minutes at chosen stable load |

Tune these numbers after a smoke run; do not reuse generic cloud-scale values on a student laptop.

## Metrics

Report at least:

- Samples.
- Pass/fail count.
- Error rate.
- Average, median, p90, p95, p99 response time.
- Min/max response time.
- Throughput/RPS.
- Backend CPU/memory observations.
- Endurance threshold with concrete load and stability criteria.

## Review Questions

- Does the test measure successful e-commerce workflow completion, or just HTTP traffic?
- Are failed login/cart/checkout requests counted as failures?
- Does the plan include realistic think time?
- Does the plan avoid account lockout unless intentionally testing lockout?
- Does the plan document database reset and seed state?

