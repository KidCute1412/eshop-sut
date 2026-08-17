---
name: log-analysis-skill
description: Analyze and compare raw performance-test logs and metrics from JMeter, k6, Locust, Gatling, access logs, tracing exports, or equivalent structured sources. Use to validate schemas and units; calculate latency percentiles, throughput, error rates, concurrency, and trends; isolate warm-up and steady-state windows; detect saturation and recovery; propose evidence-grounded thresholds; audit AI or human metric claims; investigate discrepancies; and evaluate optimization recommendations. Use performance-test-skill when the primary task is designing or executing the tests.
---

# Analyze performance logs

Treat raw records as primary evidence and derived dashboards as cross-checks. Separate observations, calculations, hypotheses, and recommendations. Never invent missing samples, units, objectives, root causes, or system components.

## Establish provenance

Collect the raw logs plus enough run context to interpret them:

- scenario and workload configuration;
- test and application versions;
- environment, topology, hardware, and load-generator details;
- run timestamps, time zone, duration, and monitoring interval;
- relevant service objectives, baselines, and reports.

Inventory each input by path, format, size, row/event count, time range, schema, encoding, and integrity warnings. Preserve the original files and write derived outputs separately.

If only screenshots or summaries exist, analyze them as limited secondary evidence and state that raw-sample verification is unavailable.

## Normalize semantics

Inspect actual headers, configuration, and tool documentation before mapping fields. Normalize available fields to concepts such as:

- timestamp and time zone;
- sample or transaction label;
- total duration, network/connect time, server wait time, and units;
- status, success flag, response code, assertion failure, and error message;
- bytes, active users/threads, arrival rate, iteration, and tags.

Do not assume every tool defines latency, iteration, throughput, or failure identically. Detect CSV/XML/JSON variations, locale-specific decimals, missing headers, duplicate exports, truncation, clock skew, and mixed runs.

Account for redirects, retries, embedded resources, setup/teardown records, controller parent samples, cached responses, coordinated omission, and client-side saturation when relevant.

## Checkpoint 1 - approve data treatment

Present the inventory, field mapping, units, quality problems, exclusions, and aggregation scope. Obtain approval before excluding warm-up periods, outliers, failed samples, controller parents, or incomplete intervals. Without approval, retain the data and label the limitation.

## Calculate metrics

Compute overall, per-scenario, per-label, and time-bucket metrics when supported:

- total, successful, and failed samples with error rate;
- minimum, mean, median, p90, p95, p99, and maximum duration;
- observed duration, throughput, iteration rate, and concurrency range;
- response-code and error-message distributions;
- bytes transferred and available network/connect/server timing metrics;
- resource utilization, queue depth, saturation, and recovery trends.

State formulas, percentile method, window boundaries, inclusion rules, rounding, and denominators. Preserve unrounded values for verification. Compute percentiles from raw samples for the intended population; never average percentiles across labels or runs.

Throughput means completed work per observed time interval, not concurrency. A successful transport status does not prove business success. Verify assertion and content failures when available.

## Compare runs fairly

Normalize comparisons by workload model, steady-state duration, dataset, application version, environment, and aggregation level. Separate warm-up, ramp, steady state, overload, and recovery phases.

Quantify absolute and relative changes. Report confidence limits or run-to-run variation when repeated runs exist. Avoid declaring a regression from a single noisy difference without an agreed tolerance or supporting evidence.

## Checkpoint 2 - verify calculations

Recompute representative counts, error rates, throughput, and percentiles independently. Cross-check dashboards or reports against raw totals. Resolve or document discrepancies before drawing conclusions.

## Interpret without overclaiming

Classify every conclusion:

- `Observed`: directly supported by a calculation or raw event.
- `Correlated`: two measured signals change together without proven causation.
- `Hypothesis`: a plausible explanation requiring another measurement or experiment.
- `Unknown`: evidence is insufficient or contradictory.

Use temporal alignment across client, server, database, dependency, and infrastructure metrics. Distinguish server saturation from load-generator saturation. Require a post-load window before claiming recovery.

## Propose thresholds and regression gates

Prefer explicit service objectives. Otherwise derive provisional thresholds from a stable baseline, business risk, measurement noise, and repeated runs. Document the scope, formula, tolerance, minimum sample count, evaluation window, and failure policy.

Do not turn one environment's observed capacity into a universal objective. Label every unsupplied threshold as a proposal requiring owner approval.

## Audit metric claims

Check AI-generated, report-generated, or human claims line by line. Test for:

- unit conversion errors;
- confusion among mean, median, percentile, and maximum;
- throughput/concurrency confusion;
- wrong denominator or time window;
- aggregation across incompatible labels or runs;
- double-counted parent and child samples;
- ignored assertion failures, retries, or expected errors;
- client saturation presented as server capacity;
- correlation presented as root cause;
- recovery claimed without evidence.

For each discrepancy record: claim, verdict, correct value, source locator, calculation, likely reason, and corrected interpretation. If no error is supported, report the checks performed instead of manufacturing one.

## Evaluate recommendations

Inspect architecture, source, configuration, queries, and telemetry before recommending a change. Classify each proposal as:

- `Supported`: evidence and system structure justify a validation experiment.
- `Conditional`: plausible, but a named measurement or code check is missing.
- `Unsupported`: generic advice with no evidence for the alleged bottleneck.
- `Contradicted`: assumes a component or behavior that the system does not use.

For every proposal state the mechanism, supporting evidence, expected metric impact, risks, validation experiment, and rollback or comparison plan. Prefer the smallest experiment that can distinguish competing hypotheses.

## Checkpoint 3 - reproducibility gate

Confirm that cited files, labels, time ranges, rows/events, commands, formulas, and exclusions allow another analyst to reproduce the result. List unresolved discrepancies and confidence limits.

## Deliver

Provide:

1. Input provenance and data-quality report.
2. Schema/semantic mapping and analysis rules.
3. Metric tables and time-window comparisons.
4. Observations, correlations, hypotheses, and unknowns with exact evidence locators.
5. Proposed thresholds or regression gates with assumptions.
6. Claim-audit table and corrected interpretations.
7. Recommendation evidence matrix and validation experiments.
8. Reproducibility notes, limitations, and required next data.

Keep original logs immutable. Clearly distinguish exact evidence from rounded presentation values.
