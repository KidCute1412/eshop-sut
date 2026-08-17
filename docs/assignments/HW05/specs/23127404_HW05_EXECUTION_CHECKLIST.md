# 23127404 — HW05 Execution Checklist

> Source: `2026.HW05.Performance Testing_En.pdf`  
> Submission root: `docs/assignments/HW05/deliverables/`  
> Deadline: Monday, 17 August 2026, 12:00 PM (Asia/Ho_Chi_Minh)

## Final evidence status

- [x] Student ID `23127404`, public repository, JMeter, local reset policy, and target self-assessment `100` are recorded.
- [x] The selected non-overlapping workflow is `POST /api/login` → `GET /api/products/:id` → `POST /api/cart` → `POST /api/checkout`.
- [x] Three required endpoint groups are covered: auth-heavy FR-02, read-heavy FR-06, transactional FR-07/FR-08.
- [x] Load, Stress, and Spike use the same CSV-driven workflow, token correlation, assertions, and valid JMeter filenames.
- [x] Unique views are assigned: Summary Report (Load), Aggregate Report (Stress), View Results Tree (Spike).
- [x] Complete final JTL logs and HTML dashboards exist for Load, Stress, Spike, and the additional Endurance run.
- [x] Final raw-JTL verification: Load 200/0 errors; Stress 800/0; Spike 500/0; Endurance 4,400/0 over 640.194 seconds.
- [x] Failed header-row preflight is retained separately, explained, and excluded from final performance metrics.
- [x] Same-frame JMeter/Task Manager evidence exists for Load, Stress, and Spike.
- [x] DxDiag and Task Manager hardware evidence exists; report uses only observable point-in-time resource information.
- [x] Runtime lockout defect is reproduced with 401, 401, 403 after a fresh reset and has a copy-ready issue packet.
- [x] Main report, AI Audit Report, AI critique (270 words), continuous-testing proposal, evidence register, execution manifest, and README are complete.
- [x] Main Report and AI Audit Report have rendered PDF versions.
- [x] Reusable local agent skill and submission mirror include instructions, API contract, scripts, and discovery metadata.
- [x] Git history is committed per material artifact group and exported under `deliverables/git-history/`.
- [x] Final evidence validation passes with `agent-skill/jmeter-performance-evidence/scripts/validate_evidence.py`.

## External references

| Reference | URL |
| --- | --- |
| Unlisted Vietnamese demonstration video | |
| GitHub Issue BUG-HW05-LOCKOUT-001 | |

Final archive name: `23127404_HW05_AI_Performance_100.zip`.
