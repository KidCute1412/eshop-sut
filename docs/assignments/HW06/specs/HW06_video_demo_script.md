# HW06 Video Demo Script — API Test Generator

**Target duration:** 6–7 minutes  
**Language:** Vietnamese  
**Upload setting:** YouTube **Unlisted**  
**Purpose:** Demonstrate an AI agent invoking the `api-test-generator` skill, inspect the generated artifacts, and run one real Newman execution. Do not edit or simulate agent, terminal, or test output.

## Before recording

1. Start the backend so that `http://localhost:3000` is available.
2. Open these windows before starting the screen recording:
   - this script;
   - `deliverables/agent-skills/README.md`;
   - `deliverables/agent-skills/diagrams/architecture_diagram.mmd` and `flow_diagram.mmd`;
   - a fresh Codex/agent chat opened at this repository, with no prewritten response;
   - a PowerShell terminal at the repository root;
   - optionally, Postman with the Pool A collection imported.
3. Keep private tokens, cookies, passwords, and browser tabs unrelated to the assignment off-screen. The supplied local demo account is acceptable only inside the test data; do not read its password aloud.

## Recording script

### 0:00–0:35 — Identity and scope

Say:

> Em là Lê Tuấn Lộc, MSSV 23127404. Đây là bài HW06 API Testing. Em sẽ demo Agent Skill API Test Generator, cách nó sinh test cases cho ba API thuộc ba pool khác nhau, và chạy một test suite thật bằng Newman.

In PowerShell, run and leave the output visible briefly:

```powershell
Set-Location 'D:\HCMUS\Third Year\Software Testing\eshop-sut'
whoami
hostname
git branch --show-current
git log -1 --oneline
```

State that the working branch is `23127404-LeTuanLoc` if that is what the terminal shows.

### 0:35–1:25 — Problem and selected APIs

Open `deliverables/report/23127404_HW06_API_Testing_Report.md` and say:

> Bài chọn ba API ở ba pool: Pool A là `POST /api/login`, Pool B là `POST /api/checkout`, và Pool C là `PUT /api/admin/orders/:id/status`. Mỗi API có 35 test case do AI sinh và 5 test case do người kiểm thử bổ sung, tổng cộng 120 case.

Show the test-summary table and the folder `deliverables/postman/data/`. Do not claim every generated case is automatically correct; point out that the Excel workbook and audit labels record the human review.

### 1:25–2:20 — Explain the self-drawn design

Open `architecture_diagram.mmd`, then `flow_diagram.mmd`. Explain each stage in your own words:

> Generator nhận endpoint và contract/rules của API. Nó tạo equivalence partitions, boundary cases, state-transition cases khi endpoint có trạng thái, và security/RBAC cases. Sau đó nó xuất Postman collection, data-driven JSON và dữ liệu cho ma trận test. Kết quả phải được human audit trước khi coi là test suite cuối.

Mention the two design decisions visible in the diagrams:

- protected suites bootstrap fresh user/admin tokens rather than use placeholder JWTs;
- order-status requests bind `order_id` from iteration data, so every boundary/not-found row targets the intended order.

### 2:20–3:45 — Ask the agent to generate tests live

Keep the agent chat and the terminal visible. In a **new** chat, type this prompt yourself and submit it:

```text
Read `docs/assignments/HW06/deliverables/openapi/eshop-openapi.yaml`. Create a fresh API test suite for `POST /api/login`, covering equivalence partitions, boundary values, and relevant security cases. Export it to a temporary output directory, explain the generated partitions, and do not modify the submission deliverables.
```

Say while it runs:

> Đây là một agent nhận yêu cầu tạo API test suite. Agent tự chọn skill và công cụ phù hợp, đọc OpenAPI của HW06, sinh bộ test mới cho login vào thư mục tạm và giải thích các partition. Em giữ output tạm ngoài deliverables để không làm thay đổi evidence đã nộp.

Show the agent inspecting the input and the real terminal/tool call it performs. If the UI displays a selected skill, leave it visible, but do not force or claim a skill choice the agent did not make. Do not cut away a failure; if it needs a local prerequisite, resolve it on camera or re-record only after it genuinely succeeds.

After the generated files appear, open the output folder and show its collection/data JSON. Say:

> Đây là output vừa được agent tạo thông qua skill: data file chứa case ID, input và expected status; collection chứa request, pre-request header và assertion. Output tự động vẫn cần human audit trước khi trở thành test suite cuối.

### 3:45–4:30 — Show source and pseudocode

Open these files side-by-side:

- `deliverables/agent-skills/api-test-generator/generator.py`
- `deliverables/agent-skills/api-test-generator/pseudocode.md`

Say:

> Đây là source code và pseudocode của skill. Phần pre-request script gắn `X-Student-Id: 23127404`. Với endpoint cần xác thực, collection có bootstrap login để lấy token thật. Với API order status, `order_id` lấy từ từng dòng iteration data chứ không hard-code một ID.

Scroll only to the relevant code blocks; do not imply you wrote code you cannot explain. Briefly show the `--help` output:

```powershell
& 'D:\Python\Python312\python.exe' '.\docs\assignments\HW06\deliverables\agent-skills\api-test-generator\generator.py' --help
```

### Fallback only if the agent UI is unavailable

Do **not** present this fallback as an agent invocation. It only proves the underlying executable used by the skill. Generate the same temporary Pool A demo with:

```powershell
$demoOutput = Join-Path $env:TEMP 'hw06-generator-demo'
& 'D:\Python\Python312\python.exe' '.\docs\assignments\HW06\deliverables\agent-skills\api-test-generator\generator.py' --endpoint '/api/login' --method POST --output_dir $demoOutput
Get-ChildItem -LiteralPath $demoOutput
```

### 4:30–5:35 — Show testing techniques and audit

Open `deliverables/postman/data/login_data.json` and show representative rows: a valid login, invalid credentials, boundary/lockout, and a security case. Then open the Excel workbook or `deliverables/ai/23127404_HW06_AI_Audit_Report.md`.

Say:

> EP/BVA được dùng cho credential và input validation. State testing được dùng cho lockout và lifecycle đơn hàng. Security cases kiểm tra role authorization, token và parameter tampering. Sau khi sinh, từng case AI đều có nhãn `VALID`, `INVALID` hoặc `INCOMPLETE` cùng lý do audit; ngoài ra có năm case human extension cho mỗi API.

Do not call a reproduced defect a passing contract result. Explain that the test report separates the contract oracle from observed SUT behavior.

### 5:35–6:30 — Real Newman execution and evidence

Run one real data-driven Pool A iteration. Keep the backend terminal visible if practical:

```powershell
npx.cmd newman run docs/assignments/HW06/deliverables/postman/collections/pool_a_login.postman_collection.json -e docs/assignments/HW06/deliverables/postman/environments/local.postman_environment.json -d docs/assignments/HW06/deliverables/postman/data/login_data.json --iteration-count 1
```

Say:

> Đây là Newman chạy collection thật với data file thật. Pre-request script gắn `X-Student-Id: 23127404`; ảnh Postman Console trong deliverables cho thấy header này trực tiếp. Raw Newman JSON và HTML report được lưu trong `deliverables/newman-reports/`.

If `npx.cmd newman` is unavailable, do **not** fake the run. Show the already preserved raw report and state that the live command was blocked by the local dependency; fix the environment, then re-record this segment.

### 6:30–7:00 — Defects, CI, and close

Open `deliverables/bugs/bug-report.md`, then `deliverables/cicd/23127404_HW06_CICD_Report.md`. Say:

> Bài ghi nhận sáu root-cause bugs, đã tạo GitHub Issues và lưu ảnh chụp thật. CI chạy các collection bằng Newman và report lưu một run xanh cùng một run đỏ có chủ đích. Toàn bộ raw evidence, report và ZIP đều nằm trong thư mục HW06.

Close with:

> Em kết thúc phần demo HW06 API Test Generator của MSSV 23127404. Link video Unlisted được đặt trong README và báo cáo trước khi nộp.

## After upload

1. Upload as **Unlisted**, not Private.
2. Copy the YouTube URL into the three `<YouTube-URL-Agent-Skill>` placeholders in `deliverables/README.md`, `deliverables/report/23127404_HW06_API_Testing_Report.md`, and `deliverables/agent-skills/README.md`.
3. Re-render the affected PDFs, rebuild `23127404_HW06_AI_API_100.zip`, inspect the archive, then commit only the intended HW06 files.
