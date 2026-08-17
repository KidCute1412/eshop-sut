# AI Audit Report

## 1. Declaration and controls

OpenAI Codex was used on 17 August 2026 for specification interpretation, JMeter plan review, raw-JTL analysis, evidence traceability, and report drafting. Local execution, screenshots, and external publication remained student-controlled. AI-generated text was reviewed against source code, JMX, screenshots, and raw JTL logs. No AI-generated performance result, screenshot, GitHub URL, or video URL is treated as evidence.

## 2. Material interaction record

The original chat transcript did not retain per-message clock times. Each interaction below therefore declares `time unavailable` rather than inventing a time; execution timestamps are retained independently in `supporting-materials/execution_manifest.md` and raw JTL files.

| Local date / time | Tool | Student prompt or instruction | AI output | Human validation and outcome |
| --- | --- | --- | --- | --- |
| 17 Aug 2026; time unavailable - scope | OpenAI Codex | Analyse the specification and select endpoint groups/FR traceability using prior work. | Proposed login, product detail, cart, and checkout; classified auth/read/transactional groups. | Checked against backend routes and retained FR-02, FR-06, FR-07, FR-08 only. |
| 17 Aug 2026; time unavailable - plan design | OpenAI Codex | Use JMeter and create equivalent Load, Stress, Spike plans with CSV data. | Generated JMX scaffolds with CSV variables, token extraction, assertions, and unique listener views. | Real preflight exposed a CSV/header mismatch, requiring execution review. |
| 17 Aug 2026; time unavailable - correction | OpenAI Codex | Diagnose login failures in the preflight. | Identified the CSV data-file/header contract as the likely cause. | Header was removed; failed preflight retained separately; final scenarios ran successfully. |
| 17 Aug 2026; time unavailable - evidence | OpenAI Codex | Explain and organise JMeter, Task Manager, dxdiag, lockout, and reset evidence. | Supplied evidence taxonomy and capture guidance. | EV-RUN, EV-HW, and EV-LOCKOUT artifacts were captured and verified on disk. |
| 17 Aug 2026; time unavailable - lockout review | OpenAI Codex | Verify lockout runtime before calling it a bug. | Required a valid-login check after two invalid requests. | Fresh runtime sequence was 401, 401, 403 for valid password; the issue packet records the evidence. |
| 17 Aug 2026; time unavailable - result analysis | OpenAI Codex | Summarise raw JTL files without inference. | Used the submitted skill script to calculate samples, errors, mean, p95, duration, and RPS. | Report values match raw-log summaries. |
| 17 Aug 2026; time unavailable - reporting | OpenAI Codex | Prepare reports, critique, skill mirror, and continuous-testing proposal. | Drafted traceable Markdown and PDF rendering automation. | Main Report and AI Audit Report PDFs were rendered successfully. |

## 3. AI misinterpretation hunt

| AI-proposed claim or omission | Correct evidence | Why it was wrong or incomplete | Effect of review |
| --- | --- | --- | --- |
| A CSV header could coexist with explicit JMeter variable names. | Preflight JTL: 75 failed samples; final headerless CSV: successful runs. | JMeter used the first row as data when explicit variable names were supplied. | Preserved the failure for audit and excluded it from final metrics. |
| Lockout could be labelled a defect from source inspection alone. | Controlled runtime sequence: 401, 401, then valid-password 403. | Source explains a hypothesis but does not prove user-visible behavior. | Performed the valid-login check before writing the issue packet. |
| Task Manager screenshot can establish maximum capacity. | EV-HW-002 is a point-in-time monitor frame. | It has no continuous peak measurement. | Report avoids a fabricated capacity ceiling. |

## 4. Usage conclusion

AI accelerated design and documentation but did not replace testing. JTL plus execution configuration is the acceptance source for performance claims; screenshots establish attribution, not missing metrics. The completed critique in `ai_critique.md` records the collaboration principle.
