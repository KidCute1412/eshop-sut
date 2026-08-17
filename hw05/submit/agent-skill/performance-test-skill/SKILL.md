---
name: performance-test-skill
description: Design, review, execute, and document performance tests for APIs, services, web applications, and end-to-end workflows using JMeter, k6, Locust, Gatling, or the project's existing tooling. Use for workload modeling; load, stress, spike, endurance, capacity, scalability, or baseline tests; data-driven scenarios; correlation and assertions; safe execution; resource monitoring; evidence collection; bottleneck experiments; and reusable performance-test plans. Use log-analysis-skill when the primary task is analyzing completed raw performance logs or auditing metric conclusions.
---

# Design and execute performance tests

Build tests from observed system behavior and explicit objectives. Keep assumptions visible and results reproducible. Never fabricate executions, logs, reports, resource measurements, screenshots, or capacity claims.

## Establish context

Inspect available requirements, architecture, API definitions, source code, existing tests, deployment configuration, seed data, and observability. Prefer verified routes and responses over guessed behavior.

Resolve or explicitly record any missing information:

- the system under test, environment, base URLs, version, and deployment topology;
- authorization to generate load and any prohibited targets or operations;
- business-critical journeys and success conditions;
- expected traffic, concurrency, arrival rate, seasonality, and service objectives;
- test tool, load-generator resources, server resources, and monitoring access;
- accounts, datasets, cleanup rules, rate limits, security controls, and external dependencies.

Ask only for facts that materially block a safe or valid design. Never direct substantial load at production or third-party systems without explicit authorization.

## Model the workload

Represent real usage instead of testing isolated endpoints by default. Decompose each journey into named transactions and map requests to business actions, dependencies, and expected frequency.

Choose only the test types needed for the objective:

- `Baseline`: establish low-load behavior and measurement noise.
- `Load`: validate expected sustained demand.
- `Stress`: increase demand in controlled steps to find saturation and failure behavior.
- `Spike`: test sudden demand changes and recovery.
- `Endurance`: expose leaks, degradation, and resource accumulation over time.
- `Capacity/Scalability`: measure the largest stable workload or scaling efficiency.

For every scenario define the workload model, virtual users or arrival rate, ramp pattern, steady duration, think time, pacing, iterations, data volume, expected request count, timeouts, stop conditions, and rationale. Derive starting values from traffic evidence, service objectives, a baseline run, or hardware constraints. Label unmeasured values as hypotheses.

## Build realistic test flows

Preserve cookies, sessions, tokens, CSRF values, generated identifiers, and other dynamic values through extraction and correlation. Parameterize credentials, entity IDs, search terms, payloads, and user-specific data. Prevent concurrent users from unintentionally sharing mutable state.

Define:

- dataset schema, source, encoding, uniqueness, reuse, exhaustion, and secret handling;
- setup, teardown, idempotency, and cleanup behavior;
- transport, schema, content, and business-outcome assertions;
- expected negative responses, redirects, retries, and rate-limit behavior;
- transaction names and tags that remain consistent across plans and reports.

Avoid hard-coded dynamic values, weak status-only assertions, unrealistic zero think time, and GUI-heavy result listeners during high load.

Select tooling that fits the repository and team constraints. Reuse established tooling when practical; otherwise explain the choice using protocol support, scripting needs, reporting, CI integration, and load-generation capacity.

## Checkpoint 1 - approve the design

Present the journey map, dataset plan, workload table, assertions, observability plan, risks, and assumptions. Confirm the target environment and load authorization before generating substantial traffic.

## Generate and review artifacts

Create the test plans, scripts, configurations, and non-secret data templates. Review them for:

- correct methods, paths, headers, bodies, protocols, and authentication;
- correct variable scope, extraction order, session isolation, and data sharing;
- realistic timing, workload, timeouts, retries, and connection behavior;
- adequate functional assertions and failure recording;
- safe cleanup, bounded load, secrets handling, and environment selection;
- consistent naming, tags, commands, and output locations.

Record each discovered defect as `issue -> correction -> reason -> verification`.

## Checkpoint 2 - pass a smoke test

Run one user or the smallest meaningful arrival rate for one complete iteration. Verify every request, assertion, correlation value, test-data mutation, and cleanup action. Fix failures before scaling. Distinguish test-script defects from application defects.

## Execute controlled experiments

Run scenarios independently in a stable environment. Prefer non-interactive execution for real load. Before every run record:

- test and application versions;
- exact command, configuration, dataset, and environment;
- start time, duration, load-generator specification, and server topology;
- monitoring configuration and known background activity.

Collect raw sample logs, console output, reports, server and load-generator metrics, application/database telemetry, and observed errors. Monitor both the load generator and the system so client saturation is not mistaken for server capacity.

Stop or reduce load when safety limits, destructive side effects, uncontrolled cost, widespread corruption, or environment instability appear. Preserve partial evidence and explain why the run stopped.

## Checkpoint 3 - verify evidence

Confirm that raw logs are non-empty and parseable, run metadata matches the artifacts, clocks and time zones are understood, reports can be regenerated, and monitoring covers the relevant interval. Mark gaps rather than synthesizing replacements.

## Iterate and determine limits

Use one-variable-at-a-time experiments when practical. Compare against the baseline, identify the first violated stability criterion, and rerun boundary points to test repeatability.

Define stability before claiming a threshold. Consider error rate, tail latency, throughput trend, queue growth, CPU saturation, memory growth, dependency health, and recovery. Report capacity as an observed result for the measured workload, environment, dataset, and duration, not as universal system capacity.

For detailed calculations, comparisons, and claim auditing, hand the preserved raw outputs to `log-analysis-skill`.

## Deliver

Provide:

1. Scope, objectives, assumptions, risks, and environment description.
2. Journey/transaction map and workload model.
3. Test plans, scripts, configurations, and data templates.
4. Review corrections and smoke-test results.
5. Reproducible execution commands and evidence index.
6. Observed issues, stop conditions, and recovery notes.
7. Capacity or endurance findings with explicit stability criteria when measured.
8. Remaining uncertainties and the next discriminating experiment.

Keep claimed results separate from planned or hypothetical results. Preserve original evidence and do not overwrite prior runs.
