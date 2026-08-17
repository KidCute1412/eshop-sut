# HW05 Video 02 - Agent Skill demonstration

**Target duration:** 2 minutes 30 seconds  
**Language:** Vietnamese narration by the student  
**Purpose:** Demonstrate end-to-end use of the reusable `jmeter-performance-evidence` skill on the selected API workflow.

This clip complements Video 01. The combined target duration is 6 minutes 15 seconds. Record both clips as unlisted YouTube videos, then provide the accessible YouTube link or playlist link in the submission README.

## Before recording

- Open `.agents/skills/jmeter-performance-evidence/SKILL.md` and its `references/api-contract.md`.
- Keep the completed Load JTL and the evidence validator ready in a terminal.
- Start a new Codex conversation or agent task in the repository so the prompt and its output can be shown.
- The agent may analyse existing evidence, but it must not generate performance numbers, screenshots, or URLs without source artifacts.

## Copy-paste prompt for the agent

```text
Review the HW05 EShop Load scenario as a read-only evidence audit. Identify and follow any relevant local instructions or skills before reviewing the artifacts. Do not modify, create, delete, stage, commit, or render any file.

Inspect only these real artifacts:

- docs/assignments/HW05/deliverables/plans/23127404_Load_20260817.jmx
- docs/assignments/HW05/deliverables/test-data/workflow.csv
- docs/assignments/HW05/deliverables/raw-results/load/23127404_Load_20260817.jtl
- docs/assignments/HW05/deliverables/html-reports/load/
- docs/assignments/HW05/deliverables/evidence/execution/EV-RUN-LOAD-JMETER-TASKMANAGER.png

Run only read-only validation or analysis commands that are necessary. Return only: (1) workflow/API assertions, (2) computed JTL metrics with source path, (3) evidence gaps if any, and (4) a clear statement that no result was invented. Do not fabricate screenshots, URLs, thresholds, or measurements.
```

## Shot list and Vietnamese narration

| Time | Screen / action | Narration |
| --- | --- | --- |
| 0:00-0:25 | Show the relevant local instructions and API contract identified by the agent. | "Agent tự nhận diện hướng dẫn phù hợp trong repository trước khi audit. Các hướng dẫn yêu cầu đọc API contract, giữ raw JTL, tính metric từ log và kiểm tra evidence trước khi kết luận." |
| 0:25-0:55 | Paste the supplied prompt into the agent and show the selected real artifact paths. | "Em dùng prompt chỉ-đọc này để yêu cầu agent audit một endpoint workflow hoàn chỉnh. Prompt giới hạn agent chỉ được dùng JMX, CSV, raw JTL, HTML report và screenshot đã tồn tại; agent không được sửa file hoặc tự tạo số liệu, ảnh hay link." |
| 0:55-1:35 | Show the agent reviewing the instructions and using the JTL summarizer on the Load JTL. | "Agent review hướng dẫn trước, sau đó chạy summarizer trên raw Load JTL. Kết quả được truy vết về file gốc; đây là cách tránh việc lấy số liệu từ ảnh hoặc suy diễn metric còn thiếu." |
| 1:35-2:05 | Show the read-only evidence-validator output and the evidence register. | "Tiếp theo agent chạy evidence validator ở chế độ chỉ-đọc. Validator kiểm tra sự hiện diện của plan, raw log, HTML report, screenshot, hardware evidence và traceability. Kết quả PASS chỉ xác nhận bộ evidence đầy đủ, không thay thế việc em tự review." |
| 2:05-2:30 | Show the concise audit result and the corresponding report entry. | "Kết quả cuối nêu workflow, số liệu được tính từ JTL và các gap nếu có. Em đối chiếu output đó với raw files trước khi đưa vào Main Report và AI Audit Report. Vì vậy AI hỗ trợ phân tích, còn bằng chứng và quyết định cuối vẫn do người thực hiện kiểm tra." |

## Recording acceptance checklist

- [ ] Show the agent-identified instructions, API contract, prompt, JTL summarizer, and validator in sequence.
- [ ] The agent analyses an existing complete endpoint group without modifying any artifact.
- [ ] Narration explains the human-review boundary.
- [ ] Do not show secrets, access tokens, or unrelated files.
