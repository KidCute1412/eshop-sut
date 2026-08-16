# HW05 Assignment Requirements

## Scope

- SUT: EShop backend API.
- Test one end-to-end workflow covering three endpoint groups:
  - Read-heavy.
  - Auth-heavy.
  - Transactional.
- Default workflow for this repository:
  `Login -> Search Product -> View Detail -> Add to Cart -> Checkout`.

## Task 1

- Use AI step by step to design and generate Load, Stress, and Spike plans.
- All three plans must exercise the same end-to-end workflow.
- Use CSV data for credentials, product IDs, order payloads, or similar runtime values.
- Use three distinct JMeter listener/report views, or k6 equivalents.
- Name each plan `{StudentID}_{ScenarioType}_{YYYYMMDD}`.
- Human-review and correct AI-generated plans.
- Execute all scenarios as completely as possible.
- Produce raw `.jtl` logs and HTML report folders.
- Capture tool + backend resource monitor screenshots per run.
- Capture hardware report/screenshot and spec table.
- Run a 10-15 minute Endurance/Soak test and report an empirical threshold.
- Record a Vietnamese narrated demo video of at least 6 minutes.
- Report genuine bugs/performance issues with GitHub Issues and screenshots when found.

## Task 2

- Prompt AI to analyse raw logs and suggest thresholds.
- Human-review the analysis and identify metric misinterpretations.
- Cite exact correct values from raw `.jtl` logs.
- Classify AI optimization recommendations as feasible or hallucinated.

## Task 3

- Propose continuous performance testing that watches commits, decides what to run, compares p95
  regressions, and discusses cost/false alarms.

## Required Packaging

- Main report in Markdown and PDF, including performance report and AI-analysis critique.
- Public GitHub repository link.
- Three test plans.
- Three raw `.jtl` logs and three HTML report folders.
- Resource-monitor and hardware screenshots.
- Demo video link.
- AI Critique and AI Audit Report in Markdown and PDF.
- Git commit log.
- Bug report with GitHub Issue screenshots if issues exist.
- README with self-assessment and test summary.

