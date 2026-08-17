---
name: jmeter-performance-evidence
description: Design, execute, analyse, and validate real JMeter API performance-testing evidence. Use when an EShop or REST workflow needs Load, Stress, Spike, or endurance plans, raw JTL analysis, evidence validation, or an AI review that must not fabricate execution results.
---

# JMeter Performance Evidence

Require a verified API contract, a local SUT, JMeter plan/data paths, and output directory. Read `references/api-contract.md` before generating a plan.

1. Keep the selected workflow identical across Load, Stress, and Spike; parameterize every request through CSV data and correlate authentication tokens.
2. Run a smoke test before evidence collection. Preserve failed preflights separately and never report them as final results.
3. Run load tests with JMeter CLI; retain the JMX, complete JTL, HTML report, run metadata, and same-frame tool/resource screenshots.
4. Use `scripts/summarize_jtl.py` for reproducible metrics. Never infer missing values from a screenshot or HTML summary.
5. Before publishing, use `scripts/validate_evidence.py` to identify missing plans, JTLs, HTML reports, screenshots, hardware evidence, videos, or traceability fields.
6. Treat video narration, resource-monitor captures, and GitHub publication as student-controlled evidence. Prepare materials but never claim they occurred without supplied artifacts.

## Output contract

Return a scenario matrix, exact artifact paths, calculated metrics with raw-log sources, detected gaps, and human-review decisions. Refuse to create performance numbers, issue URLs, screenshots, video URLs, or AI-audit entries that lack real source evidence.
