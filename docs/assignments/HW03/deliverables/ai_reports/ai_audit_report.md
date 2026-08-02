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
| Human review | Checked screenshot content, corrected the percentage-coupon interpretation, removed the unsupported FR-23 label, and reported Firefox as blocked rather than completed. |
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

## Human-review controls applied

- A static source pattern could create a hypothesis but not a `Passed`, `Failed`, or verified defect result.
- Every counted defect was reproduced in two clean browser runs and mapped to a genuine screenshot.
- Playwright mobile emulation was not accepted as a physical/cloud-device platform.
- Firefox was counted only after the complete flow produced five visually reviewed, browser-identified screenshots.
- No participant name, contact, quotation, rating, duration, consent, or recording was generated.
- No GitHub Issue or video was claimed before an authentic externally accessible artifact existed.
- Summary counts were derived from the canonical checklist rather than entered independently.

## Student attestation

Pending the student's final review and signature after participant, mobile, GitHub Issue, and video evidence are added.
