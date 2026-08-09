# HW04 Bug Evidence Workflow

`bug_report.md` is the only file that requires manual URL entry. Agent triage and evidence are already prepared:

- `triage-decisions.md` — decision for all 19 candidates;
- `evidence/HW04-CAND-###/` — authentic screenshot, trace, and metadata;
- `issue-packets/BUG-###/issue-body.md` — one-copy GitHub Issue body for each confirmed defect;
- `issue-register.md` — generated reconciliation index.

For each confirmed packet, copy `issue-body.md` into a GitHub Issue, attach the neighboring `screenshot.png`, and
send the resulting URL back to the agent. Do not file the two rejected candidates (`HW04-CAND-003` and
`HW04-CAND-004`).
