# AI Audit Report

## 1. Declaration and controls

OpenAI Codex was used on 17 August 2026 for specification interpretation, JMeter-plan generation and review, raw-JTL analysis, evidence traceability, and report drafting. Local execution, screenshots, and external publication remained student-controlled. AI-generated text was reviewed against source code, JMX, screenshots, and raw JTL logs before inclusion. No AI-generated performance result, screenshot, GitHub URL, or video URL is treated as evidence.

## 2. Material interaction record

| Local date / stage | Tool | Student prompt or instruction | AI output | Human validation and outcome |
| --- | --- | --- | --- | --- |
| 17 Aug - scope | OpenAI Codex | Analyse the HW05 specification and select endpoint groups/FR traceability using prior HW03/HW04 work. | Proposed login, product detail, cart, and checkout; classified auth/read/transactional groups. | Checked against backend routes and retained FR-02, FR-06, FR-07, FR-08 only. |
| 17 Aug - plan design | OpenAI Codex | Use JMeter and create equivalent Load, Stress, Spike plans with CSV data. | Generated JMX scaffolds with CSV variables, token extraction, assertions, and unique listener views. | Real preflight exposed a CSV/header mismatch, requiring execution review. |
| 17 Aug - correction | OpenAI Codex | Diagnose login failures in the preflight. | Identified the CSV data-file/header contract as the likely cause. | Header was removed; the failed preflight was retained separately. Final Load, Stress, Spike, and Endurance JTLs ran successfully. |
| 17 Aug - evidence | OpenAI Codex | Explain and organise JMeter/Task Manager, dxdiag, lockout, and reset evidence. | Supplied an evidence taxonomy and capture guidance. | EV-RUN, EV-HW, and EV-LOCKOUT artifacts were captured and verified on disk. |
| 17 Aug - lockout review | OpenAI Codex | Verify lockout runtime before calling it a bug. | Required a valid-login check after two invalid requests rather than relying only on source. | Fresh runtime sequence was 401, 401, 403 for a valid password; the issue packet records the evidence. |
| 17 Aug - result analysis | OpenAI Codex | Summarise raw JTL files without inference. | Used the submitted skill script to calculate samples, errors, mean, p95, duration, and RPS. | Main-report values match script output: Load 200; Stress 800; Spike 500; Endurance 4,400; all zero errors. |
| 17 Aug - reporting | OpenAI Codex | Prepare professional reports, critique, skill mirror, and continuous-testing proposal. | Drafted traceable Markdown materials and PDF-rendering automation. | Main Report and AI Audit Report PDFs were rendered successfully; content was reviewed against the registered evidence. |

## 3. AI misinterpretation hunt

| AI-proposed claim or omission | Correct evidence | Why it was wrong or incomplete | Effect of review |
| --- | --- | --- | --- |
| A CSV header could coexist with explicit JMeter variable names. | Preflight JTL: 75 failed samples; final headerless CSV: successful runs. | JMeter used the first row as data when explicit variable names were supplied. | Preserved the failure for audit and excluded it from final metrics. |
| Lockout could be labelled a defect from source inspection alone. | Controlled runtime sequence after fresh start: 401, 401, then valid-password 403. | Source explains a hypothesis but does not prove user-visible behavior. | Performed the additional valid-login check before writing the issue packet. |
| Task Manager screenshot can establish a system maximum. | EV-HW-002 is a point-in-time monitor frame only. | It has no per-process, continuous peak measurement. | Report states a measured throughput lower bound and avoids a fabricated capacity ceiling. |

## 4. Usage conclusion

AI accelerated design and documentation but did not replace testing. The acceptance source for performance claims is the JTL plus its execution configuration; screenshots establish attribution, not missing metrics. The completed critique in `ai_critique.md` records the resulting collaboration principle.
