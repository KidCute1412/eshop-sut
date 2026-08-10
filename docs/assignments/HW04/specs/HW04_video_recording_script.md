# HW04 Video Recording Script — 23127404

## Trước khi quay

1. Mở repository `https://github.com/KidCute1412/eshop-sut`.
2. Mở terminal tại `docs/assignments/HW04/deliverables/automation`.
3. Chuẩn bị SUT đang chạy và database seed sạch.
4. Tắt thông báo riêng tư, mật khẩu, JWT và email khỏi màn hình.
5. Chạy trước `whoami` và `hostname` để biết output cần xuất hiện trong video.

## Video 1 — Main Automation Demo (bắt buộc, tối thiểu 5 phút)

### 0:00–0:30 — Identity và phạm vi

**Mở:** repository, `deliverables/README.md`.

**Nói:**

> Tôi là Lê Tuấn Lộc, MSSV 23127404, lớp CSC13003_23KTPM3. Đây là bài HW04 Automation Testing. Tôi chọn FR-06, FR-10 và FR-12; trong video này tôi trình bày FR-10 — Order State Machine.

Chạy và để terminal hiển thị:

```powershell
whoami
hostname
```

### 0:30–1:10 — External test data

**Mở:** `automation/test-data/fr10-order-state-machine.json`.

**Chỉ:** các trường `id`, `actor`, `from`, `to`, `expectedStatus`, `expectedFinalState`.

**Nói:**

> Các test case được lưu ngoài source code dưới dạng JSON. Mỗi dòng là một case có ID ổn định, actor, trạng thái đầu, trạng thái đích và oracle kết quả. Cách này cho phép cùng một spec chạy nhiều dữ liệu mà không hard-code case array trong test.

### 1:10–1:50 — Playwright spec

**Mở:** `automation/tests/fr10-order-state-machine.spec.ts`.

**Chỉ:** phần import JSON, vòng lặp case, test title có case ID, setup order và assertions.

**Nói:**

> Spec đọc JSON ở runtime, tạo test title có FR10 case ID, chuẩn bị order ở trạng thái cần thiết, gọi đúng flow và kiểm tra HTTP status cùng trạng thái cuối. Playwright dùng web-first assertions và chạy serial để hạn chế phụ thuộc dữ liệu giữa các case.

### 1:50–2:20 — Human correction

**Mở:** phần FR10-02 trong spec hoặc `reports/main_report.md`, mục AI review.

**Nói:**

> Một lỗi do AI tạo ra là locator order ID dùng substring. Order `#2` có thể match cả `#20`. Tôi đã sửa thành exact table-cell locator, sau đó chạy lại cả Chromium, Firefox và WebKit. Đây là một ví dụ về human review trước khi chấp nhận kết quả automation.

### 2:20–3:25 — Chạy automation

**Mở terminal tại:** `docs/assignments/HW04/deliverables/automation`.

Chạy từng lệnh sau, không chạy lệnh có thể làm thay đổi code:

```powershell
npm.cmd run test:fr10 -- --project=chromium
npm.cmd run test:fr10 -- --project=firefox
npm.cmd run test:fr10 -- --project=webkit
```

**Nói:**

> Cùng một FR-10 data set được chạy trên ba browser projects. Tôi không thay đổi test hoặc che kết quả trong quá trình chạy.

Nếu demo chạy lại tạo report mới, hãy nói rõ đó là demo run; không gán demo run vào số liệu final nếu chưa được ghi nhận trong manifest.

### 3:25–4:25 — HTML report

**Mở:** một report đã có sẵn, ví dụ:

`automation/reports/fr10-firefox-2026-08-09T18-21-10-553Z/index.html`

Mở bằng Live Server hoặc trình duyệt. Chỉ rõ:

- `Run by: 23127404`;
- browser và timestamp;
- FR10 case IDs;
- pass/fail summary;
- một screenshot, trace hoặc video attachment.

**Nói:**

> HTML report là evidence của execution. Browser được xác định từ metadata/report, không phụ thuộc vào trình duyệt tôi dùng để mở file HTML. Firefox final run đã vượt qua setup và các failure còn lại là assertion failures của test.

### 4:25–5:05 — Kết luận

**Mở:** `supporting-materials/execution_manifest.md`, sau đó `bugs/issue-register.md`.

**Nói:**

> Final matrix có 51 logical cases trên ba browsers, tổng cộng 153 attempts, 96 pass và 57 assertion failures. Các failure đã được triage thành 17 confirmed defects và 2 oracle-gap candidates. 17 defect Issue URLs được đối chiếu trong issue-register.

Kết thúc bằng câu:

> Đây là toàn bộ quy trình từ external data, Playwright spec, multi-browser execution đến HTML evidence và defect tracking.

## Video 2 — Agent Skill Demo (tuỳ chọn, khoảng 5 phút)

Video này chỉ quay nếu muốn claim điểm Agent Skills.

### 0:00–0:35 — Skill source

**Mở:** `deliverables/agent-skill/playwright-data-driven-multibrowser/SKILL.md`.

**Nói:**

> Đây là reusable Agent Skill cho workflow Playwright data-driven và multi-browser. Skill mô tả input, output contract, evidence rules và cách kiểm tra artefact.

### 0:35–1:10 — Contract và validator

**Mở lần lượt:**

- `agent-skill/playwright-data-driven-multibrowser/references/contracts.md`;
- `agent-skill/playwright-data-driven-multibrowser/scripts/validate_playwright_artifacts.py`.

**Nói:**

> Contract yêu cầu case ID, data mapping, browser result và evidence có thể truy vết. Validator kiểm tra cấu trúc và tính nhất quán của Playwright artefacts.

### 1:10–2:00 — Prompt và agent

Tạo branch demo riêng, ví dụ `demo/agent-skill-hw04`. Dán prompt thật đã lưu trong audit record.

**Nói:**

> Tôi sử dụng prompt thật để yêu cầu agent áp dụng skill cho một feature có ít nhất 12 cases. Branch demo tách khỏi branch nộp bài để không làm thay đổi submission source.

Không đưa password, JWT, database đầy đủ hoặc dữ liệu cá nhân vào prompt.

### 2:00–3:00 — Agent output

**Mở:** output/source mà agent tạo hoặc kiểm tra:

- một external JSON file;
- một Playwright spec;
- `playwright.config.ts`;
- report metadata.

**Nói:**

> Agent tạo cấu trúc có thể truy vết từ requirement đến JSON, spec, browser project và report. Tôi không coi việc agent sinh code là bằng chứng; code vẫn phải được chạy và review.

### 3:00–4:10 — Validator và execution

Chạy validator thật trong thư mục skill, sau đó mở một report đã tạo.

**Nói:**

> Validator xác nhận artefact có cấu trúc hợp lệ. Tiếp theo tôi kiểm tra report có student ID, browser, timestamp, case outcomes và evidence assets.

### 4:10–5:00 — Human review

**Mở:** một thay đổi human review trong source hoặc `reports/main_report.md`, mục AI review.

**Nói:**

> Tôi đã review locator, Firefox context, assertion oracle và defect classification. Những phần agent đề xuất nhưng không đủ bằng chứng phải được sửa hoặc từ chối. Vì vậy skill này là workflow reusable có validation, không chỉ là một prompt.

## Quy tắc upload

- Video chính: YouTube **Unlisted**, tối thiểu 5:00, tiếng Việt.
- Video Agent Skill: YouTube **Unlisted**, khoảng 5:00, chỉ cần nếu claim 10 điểm.
- Kiểm tra cả hai link bằng Incognito/logged-out.
- Dán URL vào các file link record trong `deliverables/video/` và các trường tương ứng trong README/main report.
