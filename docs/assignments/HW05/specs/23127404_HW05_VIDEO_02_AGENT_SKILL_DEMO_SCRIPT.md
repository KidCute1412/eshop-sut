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
Use the local skill `.agents/skills/jmeter-performance-evidence` to audit the HW05 EShop Load scenario. First read the skill and its API contract. Then inspect these real artifacts only:

- docs/assignments/HW05/deliverables/plans/23127404_Load_20260817.jmx
- docs/assignments/HW05/deliverables/test-data/workflow.csv
- docs/assignments/HW05/deliverables/raw-results/load/23127404_Load_20260817.jtl
- docs/assignments/HW05/deliverables/html-reports/load/
- docs/assignments/HW05/deliverables/evidence/execution/EV-RUN-LOAD-JMETER-TASKMANAGER.png

Run the skill's JTL summarizer and evidence validator. Return only: (1) workflow/API assertions, (2) computed JTL metrics with source path, (3) evidence gaps if any, and (4) a clear statement that no result was invented. Do not modify files and do not fabricate screenshots, URLs, thresholds, or measurements.
```

## Shot list and Vietnamese narration

| Time | Screen / action | Narration |
| --- | --- | --- |
| 0:00-0:25 | Show the skill folder, `SKILL.md`, and API contract. | "Đây là Agent Skill `jmeter-performance-evidence` được tạo để tái sử dụng quy trình performance testing. Skill yêu cầu đọc API contract, giữ raw JTL, tính metric bằng script và kiểm tra evidence trước khi kết luận." |
| 0:25-0:55 | Paste the supplied prompt into the agent and show the selected real artifact paths. | "Em dùng prompt này để yêu cầu agent audit một endpoint workflow hoàn chỉnh. Prompt giới hạn agent chỉ được dùng JMX, CSV, raw JTL, HTML report và screenshot đã tồn tại; agent không được tự tạo số liệu hay ảnh." |
| 0:55-1:35 | Show the agent reading the skill and using `summarize_jtl.py` on the Load JTL. | "Agent đọc skill và API contract trước, sau đó chạy summarizer trên raw Load JTL. Kết quả được truy vết về file gốc; đây là cách tránh việc lấy số liệu từ ảnh hoặc suy diễn metric còn thiếu." |
| 1:35-2:05 | Show `validate_evidence.py` output and the evidence register. | "Tiếp theo agent chạy evidence validator. Validator kiểm tra sự hiện diện của plan, raw log, HTML report, screenshot, hardware evidence và traceability. Kết quả PASS chỉ xác nhận bộ evidence đầy đủ, không thay thế việc em tự review." |
| 2:05-2:30 | Show the concise audit result and the corresponding report entry. | "Kết quả cuối nêu workflow, số liệu được tính từ JTL và các gap nếu có. Em đối chiếu output đó với raw files trước khi đưa vào Main Report và AI Audit Report. Vì vậy AI hỗ trợ phân tích, còn bằng chứng và quyết định cuối vẫn do người thực hiện kiểm tra." |

## Recording acceptance checklist

- [ ] Show the skill, API contract, prompt, JTL summarizer, and validator in sequence.
- [ ] The agent analyses an existing complete endpoint group without modifying evidence.
- [ ] Narration explains the human-review boundary.
- [ ] Do not show secrets, access tokens, or unrelated files.

