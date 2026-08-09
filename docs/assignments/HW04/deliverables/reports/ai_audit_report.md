# AI Audit Report

## Declaration

**I use AI tools for the following tasks,** including automation planning and implementation, review of assertions and evidence integrity, and preparation of submission documentation.

This audit distinguishes exact retained records from reconstructed summaries. Missing historical prompts, outputs, or times are explicitly marked unavailable; they are not invented. The student must append every later AI interaction before submission.

## Interaction AI-001 — Historical planning interaction

| Field | Record |
|---|---|
| AI tool | OpenAI Codex |
| Date/time | 27 July 2026; **exact interaction time not preserved** |
| Evidence source | Existing `docs/assignments/HW04/schools/23127404.md` |
| Prompt status | **Exact prompt unavailable — mandatory audit field remains noncompliant** |

The only surviving description of the prompt/intent is:

```text
Clarify the requirement “one test case on three drivers” and plan the implementation.
```

This is a faithful English rendering of the legacy summary, not a claim that it is the verbatim original prompt.

### Retained output description

The legacy record says the interaction interpreted the three drivers as three Playwright browser projects, selected `FR06-DT-01`, and planned a portable TypeScript bundle with one combined HTML report. No complete verbatim AI response is preserved.

### Human review/disposition

- Accepted Playwright with Chromium, Firefox, and WebKit.
- Accepted FR-06 as a small historical scope, while explicitly acknowledging that it did not complete HW04.
- The decision to use one combined report does not satisfy the final nine-report submission design and must be replaced for the full assignment.

## Interaction AI-002 — Historical implementation interaction

| Field | Record |
|---|---|
| AI tool | OpenAI Codex |
| Date/time | 27 July 2026; **exact interaction time not preserved** |
| Evidence source | Existing `docs/assignments/HW04/schools/23127404.md` and preserved bundle |
| Exact prompt | `Implement the plan.` |

### Retained output description

The repository preserves the resulting bundle: Playwright configuration, `fr06-product-detail.spec.ts`, external JSON data, a SUT-readiness script, package files, a bundle README, and a combined Playwright HTML report. The script checks URL, heading count and visibility, image visibility/source, exact price and description text, and exact category text.

No verbatim conversational response beyond the summarized legacy record is preserved. The generated runtime artifacts are Playwright outputs, not AI-created evidence.

### Human review/disposition

- Retained the category assertion because it is part of FR-06, even though it caused the historical run to fail.
- Used role/accessible-name/text locators rather than styling selectors.
- Kept test data in external JSON and pinned Playwright to 1.55.0.
- Documented that the first Firefox launch symptom required environment diagnosis before product-defect classification.

## Interaction AI-003 — Submission-documentation preparation

| Field | Record |
|---|---|
| AI tool | OpenAI Codex |
| Date/time | `2026-08-09T16:26:33.7787688+07:00` (workspace clock captured during the interaction) |
| Request source | Current Codex orchestration task for student 23127404 |

### Exact prompt

```text
Create professional English HW04 submission documentation/templates under docs/assignments/HW04/deliverables except automation/ and agent-skill/, plus docs/assignments/HW04/specs/manual.md. Read official PDF and current checklist/HW02 scope. Identity 23127404, repo https://github.com/KidCute1412/eshop-sut, FR-06/FR-10/FR-12. Create README.md, reports/main_report.md, reports/ai_critique.md (200-300 words), reports/ai_audit_report.md with truthful current interactions/output descriptions and honest placeholders for real execution evidence/URLs, bugs/bug_report.md + issue-register.md, video/demo_video.md + agent_skill_demo.md + Vietnamese narration script, supporting manifests/templates. Explicitly state 4-day Git history remains noncompliant if relevant; never invent results, timestamps, issues, videos, or reports. Use polished AI-grader-friendly wording, complete fields and traceability templates. Use apply_patch. Preserve unrelated changes. Return created files and any required integration assumptions.
```

### AI output

The interaction initially produced the English submission scaffold under `docs/assignments/HW04/deliverables/` and the manual guide under `docs/assignments/HW04/specs/manual.md`. Subsequent evidence reconciliation replaced the planning matrix with the actual 51-row case/data/spec/browser-result matrix, recorded 153 attempts with all 153 reaching assertions (96 passed and 57 assertion failures), and exported nine qualifying HW04 test-script commits across two days. Student-controlled identity fields, Issue URLs, screenshots, videos, and public-link verification remain unfilled.

### Human review required

- Verify the student's class and final identity fields.
- Confirm that the documented interaction prompt is appropriate to include in the personal audit log.
- Replace planned entries only after inspecting final code and authentic run evidence.
- Review the critique against the completed automation and revise it if later interactions materially change the conclusions.
- Export the final Markdown reports to PDF only after all reconciliations pass.

## Interaction AI-004 — Full-assignment orchestration and implementation

| Field | Record |
|---|---|
| AI tool | OpenAI Codex with delegated Codex agents |
| Date/time | 9 August 2026; **exact message times were not exposed in the retained conversation view** |
| Feature/case | FR-06, FR-10, FR-12; reports; Agent Skill; submission package |
| Prompt status | Exact user messages retained below; complete transient assistant commentary was not exported |

### Exact retained user prompt sequence

```text
lên kế hoạch để hoàn thành tối đa mọi phần của bài tập trên, lưu ý zip nộp bài chỉ ở docs\assignments\HW04\deliverables nên mọi thứ cần nộp đều để trong đây. cấu trúc thư mục rõ ràng, agents tự động hóa tối đa. những phần nào cần tôi làm thì ghi ra 1 file manual.md trong specs. thắc mắc gì thì hỏi lại tôi. câu từ trong phần nộp bài đều là câu từ của report thật chuyên nghiệp. bài làm khả năng cao được chấm bằng AI nên các trường thông tin, nội dung ghi thật đầy đủ, càng chi tiết càng tốt.

cứ commit thôi, không cần  trải dài 4 ngày đâu

oke, switch tới model sol high và thực hiện implement

oke thực hiện plan trên
```

### Retained output and evidence

The durable output is preserved in the repository rather than reconstructed as a conversational transcript:

- automation source and external data: `../automation/`, including 51 case rows and three browser projects;
- eight new qualifying deliverables-suite commits from `f732b2c` through `aa316e0`, plus the earlier qualifying HW04 commit recorded in `../git/23127404_HW04_git_commit_log.txt`;
- nine selected HTML/JSON/metadata report directories and the exact 51-row traceability matrix;
- reusable skill source at `../agent-skill/playwright-data-driven-multibrowser/`;
- professional reports, bug/Issue registers, video scripts, PDFs, checklist, and manual-action guide.

The `domain-bva-tester` guidance was used to structure equivalence partitions and boundaries. The official `skill-creator` guidance shaped the reusable skill manifest, instruction hierarchy, validator, and forward-use review. Material runtime and review facts are recorded in `main_report.md`, `../supporting-materials/execution_manifest.md`, and `../supporting-materials/evidence_register.md`.

### Human review/disposition

- Accepted the 51-case external-data architecture and three-browser matrix after TypeScript discovery produced 153 scheduled cells.
- Corrected the FR-10 substring row locator to exact order-ID cell matching and repeated the FR-10 matrix.
- Rejected classification of the original Firefox page-fixture failures as SUT defects; removing incompatible device options produced a successful 51-case Firefox rerun.
- Retained 57 assertion failures as candidates pending student reproduction and public Issue evidence.
- Accepted the student's explicit direction to make the required commit count immediately, while disclosing that the four-calendar-day condition remains unmet.
- Commissioned an independent read-only quality audit; its traceability, wording, validator-scope, critique, and Git-log findings were incorporated before packaging.

## Completeness warning

This log is not yet a fully compliant transcript. At least one historical prompt/time and the exact internal delegation prompts for the automation suite and reusable Agent Skill were not preserved in the accessible conversation record. Durable outputs, commits, validators, and human dispositions are linked above, but missing exact text must not be reconstructed or fabricated. Before submission, append any authentic conversation export that the student can recover. Screenshots, HTML reports, videos, Issue pages, and run results must originate from genuine execution or student-controlled publication, never from document generation.

## Template for subsequent interactions

### Interaction AI-___ — [short purpose]

| Field | Record |
|---|---|
| AI tool | **PENDING** |
| Date/time | **PENDING — ISO 8601** |
| Feature/case | **PENDING** |
| Prompt | Reproduce exactly below |
| Output | Preserve exact response below or attach a stable transcript path |

```text
PENDING — exact prompt
```

```text
PENDING — exact AI output, or a path to the complete retained output
```

**Human decision:** PENDING — accepted / modified / rejected / added manually.

**Reason and final evidence:** PENDING — explain the technical judgment and link the final spec/data/report/commit.
