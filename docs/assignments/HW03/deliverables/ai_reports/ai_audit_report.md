# AI Audit Report

## Declaration

I use AI tools for the following tasks.

OpenAI Codex assisted with requirement analysis, deliverable restructuring, checklist review, Playwright automation, runtime-result reconciliation, evidence indexing, defect documentation, cross-platform reporting, document generation, and final validation. AI output was reviewed against the assignment specification, the SUT source, live browser behavior, and generated artifacts. AI was not used to invent participant data, usability results, device evidence, GitHub Issues, or video links.

## Interaction log

The conversation interface exposed the interaction date but not message-level clock times. The unavailable time component is stated explicitly rather than reconstructed.

### AI-01 — Submission-structure review

| Field | Record |
|---|---|
| Tool | OpenAI Codex |
| Date and time | 2 August 2026; message-level time unavailable |
| Prompt | `cấu trúc thư mục của docs\assignments\HW03\deliverables đã phù hợp để nộp bài chưa... theo yêu cầu chính là ở "docs\assignments\HW03\specs\2026.HW03.GUI Usability_En.pdf"` |
| AI output | Compared the proposed package with the PDF requirements and identified submission-only versus internal authoring artifacts. |
| Human review | Confirmed English submission documents, externalized utilities, and separate pilot/P1–P7 records. |
| Affected artifacts | `deliverables/`, `workbench/` |

### AI-02 — Professional restructuring

| Field | Record |
|---|---|
| Tool | OpenAI Codex |
| Date and time | 2 August 2026; message-level time unavailable |
| Prompt | `vậy hãy fix sao cho cấu trúc format là thật chuẩn. nội dung hiện tại của mỗi file trong phần đó cũng phải chuẩn hóa câu từ cho 1 report chuyên nghiệp, không phải viết giỡn giỡn.` |
| AI output | Reorganized the package, rewrote professional templates, separated workbench tools, and generated initial PDF/XLSX files. |
| Human review | Removed generated mock evidence and retained explicit evidence-integrity gates. |
| Affected artifacts | All HW03 submission templates and derived files |

### AI-03 — Runtime-completion request

| Field | Record |
|---|---|
| Tool | OpenAI Codex |
| Date and time | 2 August 2026; message-level time unavailable |
| Prompt | `hãy tiến hành thực hiện test, và điền mọi nội dung có thể điền (trừ link video và screenshot của màn hình điện thoại)... hoàn thiện docs\assignments\HW03\deliverables tới 90%... quy trình thực hiện cần liên tục test lại và review lại` |
| AI output | Inspected the specification, source, database, existing checklist, browser availability, and evidence constraints; proposed a test–review–retest workflow. |
| Human review | Chose to keep Mobile items as `Not Executed`, defer real participant sessions, and let the student create GitHub Issues. |
| Affected artifacts | Execution plan and evidence policy |

### AI-04 — Screenshot-metadata clarification

| Field | Record |
|---|---|
| Tool | OpenAI Codex |
| Date and time | 2 August 2026; message-level time unavailable |
| Prompt | `Ảnh có overlay gồm 23127404@hcmus.edu.vn, browser, OS, URL, timestamp và test/checklist ID. này là gì, có cần thiết không hay chỉ đơn giản là chụp screen thôi` |
| AI output | Distinguished ordinary defect screenshots from the assignment's cross-platform identity/environment requirement. Removed unnecessary timestamp and checklist-ID overlays. |
| Human review | Approved simple bug captures and a compact identity/browser/OS/URL caption only for cross-platform images. |
| Affected artifacts | Evidence-capture rules and Chrome screenshots |

### AI-05 — Playwright execution and retest

| Field | Record |
|---|---|
| Tool | OpenAI Codex with Playwright 1.57.0 |
| Date and time | Final Google Chrome run: 2 August 2026, 08:31–08:32 ICT |
| Prompt | `Implement the plan.` |
| AI output | Built the internal runtime harness; executed Customer Web, Admin, and API checks; captured failed-item evidence; reset and repeated the run; produced 16 Passed, 15 Failed, and 14 Not Executed results. |
| Human review | Automation-only failures involving dialog handling, navigation timing, revenue parsing, and browser selection were corrected and rerun. The final run used installed Google Chrome rather than Playwright Chromium. |
| Affected artifacts | `checklist/`, `bugs/evidence_images/`, `cross_platform/chrome_desktop/`, `workbench/automation/` |

### AI-06 — Defect and report reconciliation

| Field | Record |
|---|---|
| Tool | OpenAI Codex |
| Date and time | 2 August 2026, after the final runtime execution |
| Prompt | Continuation of `Implement the plan.` |
| AI output | Reconciled the 45 checklist rows; documented 15 verified defects; isolated four unverified Mobile hypotheses; updated the main report, README, cross-platform status, and self-assessment. |
| Human review | Checked screenshot content and corrected the percentage-coupon interpretation. The contemporaneous removal of FR-23 in favor of an unnumbered Mobile pool was later found to conflict with the confirmed personal scope; that history is retained and corrected by AI-10 below. |
| Affected artifacts | All submission-facing Markdown, CSV, XLSX, and PDF artifacts |

### AI-07 — Firefox blocker diagnosis and rerun

| Field | Record |
|---|---|
| Tool | OpenAI Codex with Playwright 1.57.0 and Firefox 144.0.2 |
| Date and time | 2 August 2026; message-level time unavailable |
| Prompt | `Firefox Desktop: chưa có ảnh vì Playwright không tạo được page (browserContext.newPage bị lỗi), nên được ghi là Blocked. Cần sửa lỗi đi, bạn cần chạy được và lấy được ảnh` |
| AI output | Reproduced the failure with browser diagnostics, identified that the restricted sandbox blocked Firefox tab subprocesses, reran Firefox with the required process permission, completed the five-screen customer flow, and captured five authentic images. |
| Human review | Required the blocker to be resolved rather than accepted; the resulting Product List, Product Detail, Cart, Checkout, and Order History images were visually reviewed. |
| Affected artifacts | `cross_platform/firefox_desktop/`, cross-platform report, main report, audit, critique, and validation rules |

### AI-08 — Usability recording runbook and reference verification

| Field | Record |
|---|---|
| Tool | OpenAI Codex with Google Chrome 151 and Playwright 1.57.0 |
| Date and time | 2 August 2026; message-level time unavailable |
| Prompt | `kịch bản quay và thao tác cụ thể tiết lộ luôn. tôi cần bạn hoàn thiện mọi kịch bản quay và cả thao tác và cả kết quả từng phần... tôi chỉ cung cấp video quay theo kịch bản thôi` |
| AI output | Produced a complete moderated-session runbook, an explicit source/runtime-based reference path, standardized Pilot and P1–P7 checkpoint forms, and a recording-content checklist. Reran the selected Chrome flow to verify the technical reference results. |
| Human review | Selected a guided usability-test model and required expected/reference results while reserving participant behavior, timing, quotations, SUS responses, and recording links for genuine video evidence. |
| Affected artifacts | `usability/`, moderator guide, runtime reference verifier, main report, and validation rules |

### AI-09 — Evidence-gated SUS and findings workflow

| Field | Record |
|---|---|
| Tool | OpenAI Codex |
| Date and time | 2 August 2026; message-level time unavailable |
| Prompt | `Implement the plan.` after confirming that seven genuine participants will act and respond naturally |
| AI output | Added a canonical session-results dataset, SUS validation/calculation tooling, a traceable findings matrix, participant/timestamp evidence rules, and validation gates for completed sessions and response sets. |
| Human review | Confirmed that video will be supplied later and that participant actions, reactions, and SUS answers will be independently provided during the sessions. |
| Affected artifacts | Usability metrics, SUS workflow, findings synthesis, main report, audit, and submission validator |

### AI-10 — FR-23 scope-source correction

| Field | Record |
|---|---|
| Tool | OpenAI Codex |
| Date and time | 3 August 2026; message-level time unavailable |
| Prompt | Implement the approved plan to standardize FR-23 and the HW03 source of truth. |
| AI output | Restored FR-23 as Mobile Product Detail, replaced six out-of-scope Mobile checks, assigned all 14 pending Mobile rows to FR-23, separated report email from screenshot identity overlay, and strengthened generation and validation. |
| Human review | Confirmed personal scope supersedes the earlier unnumbered-pool interpretation. Existing desktop images remain unchanged, Web usability remains FR-07 → FR-10 → FR-11 with Product Detail as an FR-06 support step, and no Mobile status was promoted without runtime evidence. |
| Affected artifacts | Scope notes, checklist CSV/XLSX, submission reports, bug candidates, usability and cross-platform plans, generators, and validators |

### AI-11 — Source-derived Mobile checklist completion

| Field | Record |
|---|---|
| Tool | OpenAI Codex |
| Date and time | 3 August 2026; message-level time unavailable |
| Prompt | Complete the missing Mobile checklist information from source; screenshots will be supplied later. |
| AI output | Classified all 14 FR-23 checks from `frontend-mobile/App.js` as 8 Passed and 6 Failed, deduplicated the failures into five Mobile defects, and recorded source locations plus pending real-device evidence. |
| Human review | Explicitly selected Pass/Fail from source and requested the five Mobile defects be treated as official before screenshots are supplied. Each artifact retains the source-derived qualification so runtime evidence can supersede it later. |
| Affected artifacts | GUI checklist source/workbook, Mobile source-review evidence, defect report, README, main report, summaries, and validation rules |

### AI-12 — Replace unexecuted missing-product check with a happy path

| Field | Record |
|---|---|
| Tool | OpenAI Codex |
| Date and time | 3 August 2026; message-level time unavailable |
| Prompt | Remove the unconfirmed missing-product bug and replace CHK-GUI-044 with an easier valid Mobile case, synchronizing conflicting artifacts. |
| AI output | Replaced CHK-GUI-044 with verification that Product Detail initializes quantity to `1`, retired BUG-024, initially held the row as Not Executed, then promoted it to Passed after the authentic Mobile capture appeared and was visually reviewed. Reports, summaries, evidence mappings, and validators were reconciled. |
| Human review | Rejected source inspection as runtime confirmation and required evidence-based reporting. The four Mobile screenshots appeared in the workspace during implementation, were visually reviewed, and were mapped only to claims visible in them; their missing identity overlays remain disclosed. |
| Affected artifacts | Checklist CSV/XLSX, defect report, Mobile evidence plan, README, main report, submission checklist, AI audit, generator, and validator |

### AI-13 — Usability-recording reconciliation and workbook recovery

| Field | Record |
|---|---|
| Tool | OpenAI Codex |
| Date and time | 3 August 2026; message-level time unavailable |
| Prompt | Review the local Pilot and P1–P7 videos in `D:\OBS Videos\Testing HW3`, repair `usability_results.xlsx`, remove unacceptable `Not coded` values, clarify the Recordings sheet, and add the supplied shared Google Drive folder where required. |
| AI output | Inspected the eight local recording files, restored the original coded session results, standardized the Recordings sheet, and indexed each session by filename, duration, size, SHA-256, resolution, local-verification state, Drive folder, and access-verification state. Updated the Pilot row to reflect the verified local recording without inventing missing consent evidence. |
| Human review | Closed Excel before workbook replacement, rejected `Not coded` as an inappropriate final result label, confirmed the shared-folder URL, and requested that the Pilot wording reflect the actual recording state. Signed-out Drive access remains explicitly unverified. |
| Affected artifacts | `usability/usability_results.xlsx`, `usability/recordings/video_links.md`, usability source data, README, main report, generator, and validator |

### AI-14 — Authentic Mobile evidence review and checklist mapping

| Field | Record |
|---|---|
| Tool | OpenAI Codex |
| Date and time | 3 August 2026; message-level time unavailable |
| Prompt | Review the four screenshots added under `cross_platform/mobile_real_device`, map them to the appropriate Mobile checklist items, and synchronize every conflicting report. |
| AI output | Visually reviewed the four 1284×2778 Mobile captures and mapped only visible claims to FR-23 checks. Confirmed the Product Detail layout, default quantity, valid add result, invalid-zero acceptance and success feedback; retired BUG-024; reconciled the checklist to 25 Passed and 20 Failed; and documented BUG-020 through BUG-023 as runtime-observed Mobile defects. |
| Human review | Supplied the authentic captures and required the unsupported missing-product case to be replaced by a valid case. Accepted the evidence mapping while retaining disclosure that the images lack the assignment-required identity overlay and exact device/OS/Expo metadata. Still images were not treated as proof of loading, repeated-add, or price-calculation sequences. |
| Affected artifacts | Checklist CSV/XLSX, Mobile evidence directory and README, defect report, cross-platform report, README, main report, AI reports, generators, and validators |

### AI-15 — Defect-evidence presentation and GitHub Issue preparation

| Field | Record |
|---|---|
| Tool | OpenAI Codex |
| Date and time | 3 August 2026; message-level time unavailable |
| Prompt | Embed evidence in the bug report, explain what to copy into GitHub Issues, and determine whether Mobile images should be duplicated into the defect-evidence directory. |
| AI output | Embedded each defect image below its detail record, retained relative evidence references for traceability, and added Issue-copy instructions covering environment, reproducibility, direct GitHub image upload, and Mobile metadata. Recommended one canonical local Mobile image copy referenced by both cross-platform and defect artifacts to avoid ZIP duplication. |
| Human review | Chose to retain the canonical Mobile files under `cross_platform/mobile_real_device` and to upload the relevant image directly to each GitHub Issue. Genuine Issue URLs and Issue-page screenshots remain external evidence requirements and are not inferred from local report text. |
| Affected artifacts | `bugs/bug_report.md` and GitHub Issue preparation guidance |

### AI-16 — Submission-readiness audit of Agent Skill and AI reports

| Field | Record |
|---|---|
| Tool | OpenAI Codex |
| Date and time | 3 August 2026; message-level time unavailable |
| Prompt | Audit `deliverables/agent_skills` and then `deliverables/ai_reports` for missing, excessive, inconsistent, or poorly written submission content; update the AI reports to completion. |
| AI output | Verified the Agent Skill mirror, YAML, Python syntax, four unit tests, and artifact validator; identified the missing demonstration URL. Audited the AI Critique word count and both PDFs, then identified stale audit claims and the missing post-AI-12 interaction history. Updated this report to the current evidence state and regenerated the submission PDFs. |
| Human review | Authorized completion of the AI reports. The report continues to disclose rather than conceal remaining external evidence gaps: Agent Skill demonstration URL, signed-out Drive access, Mobile overlay/environment metadata, and incomplete GitHub Issue evidence. |
| Affected artifacts | `agent_skills/`, `ai_reports/ai_audit_report.md`, `ai_reports/ai_audit_report.pdf`, `ai_reports/ai_critique.md`, and `ai_reports/ai_critique.pdf` |

### AI-17 — Defect-report normalization and public Issue verification

| Field | Record |
|---|---|
| Tool | OpenAI Codex with the public GitHub REST API |
| Date and time | 3 August 2026; message-level time unavailable |
| Prompt | Audit and normalize `deliverables/bugs` so the defect section meets the highest submission standard without losing points. |
| AI output | Reconciled 20 failed checks to 19 defects and 20 embedded images; verified 19/19 public Issue URLs and GitHub-hosted image attachments; standardized severity to Critical/High/Medium/Low; added environment, preconditions, test data, reproducibility, severity rationale, steps, and runtime-focused actual results; and updated stale evidence notes. |
| Human review | Authorized the local normalization. Exact Mobile environment metadata was not inferred. Public verification found that Issue #118 has a missing digit in its student-ID title prefix; this external correction remains assigned to the student. |
| Affected artifacts | Bug report, evidence README files, Mobile source review, README, main report, AI audit, and regenerated PDFs |

### AI-18 — Checklist rubric and evidence-integrity normalization

| Field | Record |
|---|---|
| Tool | OpenAI Codex with Microsoft Excel recalculation |
| Date and time | 3 August 2026; message-level time unavailable |
| Prompt | Audit and complete `deliverables/checklist` as a professional, submission-ready workbook with full fields and no misleading AI-data disclaimers. |
| AI output | Audited all 45 rows, replaced three source-only Mobile classifications with narrowly scoped screenshot-backed checks, removed unsupported quantity/timing/device claims, separated 4 AI, 17 Human-added, and 24 Hybrid items, rewrote human-added omission rationales, added formula-driven FR/IA/provenance summaries, data validation, evidence hyperlinks, professional formatting, and stronger validator gates. |
| Human review | Required a polished final artifact without language implying fabricated or invalid data. The resulting checklist contains only evidence-backed Passed/Failed claims; remaining Mobile overlay and exact-environment limitations are recorded as evidence-compliance facts, not as simulated results. |
| Affected artifacts | Checklist CSV/XLSX, checklist generator and validator, README, main report/PDF, bug report, final submission checklist, and AI audit/PDF |

## Human-review controls applied

- The original policy treated static source patterns only as hypotheses. AI-11 preserves the earlier decision history; AI-12 records the later correction that source inspection does not establish runtime confirmation.
- The 15 desktop defects were reproduced in two clean Google Chrome runs. BUG-020 through BUG-023 were confirmed from authentic Mobile captures; their missing identity overlay and environment metadata are disclosed separately.
- Playwright mobile emulation was not accepted as a physical/cloud-device platform.
- Firefox was counted only after the complete flow produced five visually reviewed, browser-identified screenshots.
- AI did not fabricate participant identities, consent, behavior, timing, SUS responses, or recordings. Participant and recording data currently reported were supplied by the student and reconciled against the available local files; unresolved evidence fields remain explicit.
- No GitHub Issue or video was claimed before an authentic externally accessible artifact existed.
- Summary counts were derived from the canonical checklist rather than entered independently.

## Final reconciliation

At this revision, the canonical checklist contains 45 classified rows: 25 Passed and 20 Failed. All 14 FR-23 rows reference authentic Mobile captures and are limited to visible claims; no Passed or Failed row relies on source inspection as execution evidence. The defect report contains 15 repeatedly executed desktop defects and four Mobile runtime-observed defects. Pilot and P1–P7 local recordings are indexed individually, and their shared Drive folder is recorded; signed-out access is not independently verified. The required Mobile identity overlay and exact environment metadata remain pending. All 19 public GitHub Issues and their hosted images were verified; Issue #118 retains one disclosed student-ID title typo for the student to correct. The Agent Skill demonstration URL is supplied and its YouTube endpoint returned HTTP 200 without authentication on 3 August 2026. The remaining limitations concern external evidence completion and are not represented as completed AI work.
