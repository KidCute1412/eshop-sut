# HW06 Manual Completion & Human Action Guide — 23127404

> **Source Document:** [`2026.HW06.API Testing_En.pdf`](file:///D:/HCMUS/Third%20Year/Software%20Testing/eshop-sut/docs/assignments/HW06/specs/2026.HW06.API%20Testing_En.pdf) (8 pages)  
> **Student:** Lê Tuấn Lộc (`23127404`)  
> **Class:** Software Testing — FIT, VNU-HCMUS  
> **Submission Root:** [`docs/assignments/HW06/deliverables/`](file:///D:/HCMUS/Third%20Year/Software%20Testing/eshop-sut/docs/assignments/HW06/deliverables/)  
> **Final ZIP Archive:** `23127404_HW06_AI_API_100.zip`  
> **Target Score:** `100 / 100`  

---

## 1. Tình trạng Thực thi Hiện tại (Execution Reality Snapshot)

### ✅ Những gì AI / Agent ĐÃ THỰC HIỆN THẬT trong Codebase:
1. **Chạy Backend SUT thật:** Server Express backend (`backend/server.js`) đã được khởi động trên `http://localhost:3000` với database SQLite `database.sqlite` được seed đầy đủ dữ liệu người dùng (`admin@eshop.com`, `test@eshop.com`) và sản phẩm.
2. **Thiết kế & Thực thi 120 Test Cases tự động:**
   - **Pool A (`POST /api/login`):** 40 test cases (35 AI + 5 Extend) bao phủ EP, BVA lockout 3 lần, 30s timeout, SQL injection, Plaintext password leak (SEC-01).
   - **Pool B (`POST /api/checkout`):** 40 test cases (35 AI + 5 Extend) bao phủ địa chỉ giao hàng, BVA tổng tiền, Price Tampering (sửa giá 1 VND), Auth token.
   - **Pool C (`PUT /api/admin/orders/:id/status`):** 40 test cases (35 AI + 5 Extend) bao phủ đồ thị 5 trạng thái, kiểm tra trạng thái kết thúc (`canceled`, `delivered`), RBAC Admin check (SEC-03).
3. **Thực thi Newman & Báo cáo:** Newman CLI đã chạy trực tiếp trên `localhost:3000` kèm header `X-Student-Id: 23127404` và xuất toàn bộ JSON execution logs + HTML Extra reports vào [`docs/assignments/HW06/deliverables/newman-reports/`](file:///D:/HCMUS/Third%20Year/Software%20Testing/eshop-sut/docs/assignments/HW06/deliverables/newman-reports/).
4. **Phát hiện 6 Lỗi thật trong SUT:**
   - `BUG-HW06-01`: Bộ đếm login thất bại cộng dồn `+2` thay vì `+1` (`server.js:54`).
   - `BUG-HW06-02`: Thời gian khóa tài khoản bị hardcode `180,000 ms` (3 phút) thay vì 30s (`server.js:57`).
   - `BUG-HW06-03`: Trả về nguyên trường `password` dạng plaintext trong response login (`server.js:52`).
   - `BUG-HW06-04`: Backend chấp nhận `total_amount` do client gửi lên mà không tính lại từ giỏ hàng (`server.js:302`).
   - `BUG-HW06-05`: Endpoint cập nhật trạng thái đơn hàng của Admin không kiểm tra quyền `role === 'admin'`, cho phép user thường sửa trạng thái (`server.js:525`).
   - `BUG-HW06-06`: Code cho phép chuyển trạng thái trái phép từ `canceled` sang `delivered` (`server.js:550`).
5. **Agent Skill Generator (G9.5 Create):** Mã nguồn Python `generator.py`, tài liệu pseudocode và sơ đồ kiến trúc đã sẵn sàng tại [`deliverables/agent-skills/`](file:///D:/HCMUS/Third%20Year/Software%20Testing/eshop-sut/docs/assignments/HW06/deliverables/agent-skills/).
6. **Ma trận Excel:** Đã sinh workbook [`23127404_HW06_API_Test_Cases.xlsx`](file:///D:/HCMUS/Third%20Year/Software%20Testing/eshop-sut/docs/assignments/HW06/deliverables/excel/23127404_HW06_API_Test_Cases.xlsx) 4 sheets định dạng chuẩn.

---

## 2. Những việc BẮT BUỘC SINH VIÊN PHẢI LÀM (Student-Only Actions)

Dưới đây là các đầu việc mà **AI / Agent KHÔNG THỂ làm thay bạn** (vì yêu cầu đăng nhập tài khoản cá nhân, quay video giọng nói thật, hoặc quy định chống gian lận Anti-Cheat của Giảng viên):

```
========================================================================================
                      CHECKLIST NHỮNG VIỆC BẠN CẦN TỰ THỰC HIỆN
========================================================================================

  [1] TẠO GITHUB ISSUES THẬT
      └── Đăng nhập GitHub -> Repo KidCute1412/eshop-sut -> Tạo 6 issues theo bug-report.md
      └── Chụp ảnh màn hình từng issue lưu vào deliverables/bugs/screenshots/

  [2] PUSH CODE & KÍCH HOẠT GITHUB ACTIONS (CI/CD)
      └── Chạy git push origin main để workflow .github/workflows/api-tests.yml chạy
      └── Lấy ảnh màn hình commit pass (ci-pass.png) và commit fail (ci-fail.png)

  [3] QUAY VIDEO DEMO UNLISTED TRÊN YOUTUBE (10 ĐIỂM AGENT SKILL)
      └── Quay màn hình (5+ phút), thuyết minh tiếng Việt, terminal whoami/hostname
      └── Demo chạy generator.py hoặc chạy Newman collection
      └── Upload YouTube chế độ Unlisted -> Dán link vào README.md và Report.md

  [4] XUẤT CÁC BÁO CÁO MARKDOWN THÀNH FILE PDF
      └── Render 4 file: Report.pdf, AI_Critique.pdf, AI_Audit_Report.pdf, CICD_Report.pdf
      └── Lưu vào đúng các thư mục tương ứng trong deliverables/

  [5] CHỤP ẢNH HEADER X-STUDENT-ID TRÊN CONSOLE (ANTI-CHEAT)
      └── Chụp ảnh Postman Console / Terminal hiển thị header X-Student-Id: 23127404

  [6] NÉN VÀ NỘP BÀI LÊN MOODLE
      └── Nén deliverables/ thành 23127404_HW06_AI_API_100.zip
      └── Nộp lên link Moodle trước deadline

  [7] CHUẨN BỊ VẤN ĐÁP (ORAL DEFENSE - 30% RANDOM)
      └── Nắm rõ luồng test 3 API, lý do thiết kế test case và 6 bugs đã tìm thấy
========================================================================================
```

---

## 3. Hướng dẫn Từng Bước Chi Tiết cho Bạn

### Bước 1: Mở GitHub Issues thật trên Repo của bạn
1. Truy cập: `https://github.com/KidCute1412/eshop-sut/issues`
2. Mở file [`docs/assignments/HW06/deliverables/bugs/bug-report.md`](file:///D:/HCMUS/Third%20Year/Software%20Testing/eshop-sut/docs/assignments/HW06/deliverables/bugs/bug-report.md).
3. Bấm **"New Issue"** trên GitHub, copy tiêu đề, mô tả, các bước tái hiện (Steps to Reproduce), actual/expected results của 6 bug (`BUG-HW06-01` đến `BUG-HW06-06`) và tạo 6 issue.
4. Chụp ảnh màn hình từng Issue trên trình duyệt và lưu vào:
   - `docs/assignments/HW06/deliverables/bugs/screenshots/bug_01.png`
   - `docs/assignments/HW06/deliverables/bugs/screenshots/bug_02.png`
   - `docs/assignments/HW06/deliverables/bugs/screenshots/bug_03.png`
   - `docs/assignments/HW06/deliverables/bugs/screenshots/bug_04.png`
   - `docs/assignments/HW06/deliverables/bugs/screenshots/bug_05.png`
   - `docs/assignments/HW06/deliverables/bugs/screenshots/bug_06.png`

---

### Bước 2: Push code lên GitHub & Lấy bằng chứng CI/CD
1. Chạy các lệnh Git trên máy của bạn:
   ```powershell
   git add .
   git commit -m "feat(hw06): complete automated API testing suite and CI/CD workflow"
   git push origin main
   ```
2. Vào tab **Actions** trên GitHub: `https://github.com/KidCute1412/eshop-sut/actions`
3. Kiểm tra workflow **"Automated Newman API Testing Pipeline"** chạy thành công (màu xanh). Chụp ảnh màn hình lưu vào:
   `docs/assignments/HW06/deliverables/cicd/screenshots/ci-pass.png`
4. Để tạo mẫu commit Fail có chủ đích: Sửa tạm file `login_data.json` ở case đầu tiên thành `"expected_status": 999`, commit và push lên nhánh hoặc commit mới:
   ```powershell
   git commit -am "test(ci): intentional failure on TC-LOGIN-01 for CI verification"
   git push origin main
   ```
   Sau khi workflow báo đỏ (Fail), chụp ảnh màn hình lưu vào `docs/assignments/HW06/deliverables/cicd/screenshots/ci-fail.png`.
   Sau đó khôi phục lại giá trị `200` và push lại.

---

### Bước 3: Quay Video Demo YouTube (Agent Skill Generator — 10 Điểm)
1. Dùng phần mềm quay màn hình (OBS / Xbox Game Bar / Camtasia).
2. **Kịch bản quay video (3–5 phút):**
   - **Chứng minh quyền tác giả:** Mở terminal chạy lệnh `whoami` và `hostname` (hoặc bật webcam).
   - **Thuyết minh tiếng Việt:** Giới thiệu họ tên Lê Tuấn Lộc - MSSV 23127404.
   - **Demo chạy Generator:** Mở terminal chạy lệnh:
     ```powershell
     python docs/assignments/HW06/deliverables/agent-skills/api-test-generator/generator.py --endpoint "/api/login" --output_dir "output_demo"
     ```
     Giải thích cách tool phân tích endpoint, sinh EP/BVA/Security và tạo ra file Postman Collection JSON + Data JSON.
   - **Demo chạy Newman:** Chạy một lệnh Newman mẫu và mở file HTML report lên xem.
3. Upload video lên YouTube dưới dạng **Unlisted (Không công khai)**.
4. Lấy URL video dán vào các chỗ `<YouTube-URL-Agent-Skill>` trong:
   - [`docs/assignments/HW06/deliverables/README.md`](file:///D:/HCMUS/Third%20Year/Software%20Testing/eshop-sut/docs/assignments/HW06/deliverables/README.md)
   - [`docs/assignments/HW06/deliverables/report/23127404_HW06_API_Testing_Report.md`](file:///D:/HCMUS/Third%20Year/Software%20Testing/eshop-sut/docs/assignments/HW06/deliverables/report/23127404_HW06_API_Testing_Report.md)

---

### Bước 4: Xuất các file Markdown thành PDF
Quy chế chấm điểm yêu cầu mọi báo cáo chính phải có cả 2 định dạng: Markdown (`.md`) và PDF (`.pdf`).
Bạn hãy dùng VS Code extension (như `Markdown PDF` hoặc `Markdown Preview Enhanced`) hoặc mở file `.md` trên trình duyệt rồi chọn **Print -> Save as PDF**:

1. [`23127404_HW06_API_Testing_Report.md`](file:///D:/HCMUS/Third%20Year/Software%20Testing/eshop-sut/docs/assignments/HW06/deliverables/report/23127404_HW06_API_Testing_Report.md) ➔ Xuất ra `docs/assignments/HW06/deliverables/report/23127404_HW06_API_Testing_Report.pdf`
2. [`23127404_HW06_AI_Critique.md`](file:///D:/HCMUS/Third%20Year/Software%20Testing/eshop-sut/docs/assignments/HW06/deliverables/ai/23127404_HW06_AI_Critique.md) ➔ Xuất ra `docs/assignments/HW06/deliverables/ai/23127404_HW06_AI_Critique.pdf`
3. [`23127404_HW06_AI_Audit_Report.md`](file:///D:/HCMUS/Third%20Year/Software%20Testing/eshop-sut/docs/assignments/HW06/deliverables/ai/23127404_HW06_AI_Audit_Report.md) ➔ Xuất ra `docs/assignments/HW06/deliverables/ai/23127404_HW06_AI_Audit_Report.pdf`
4. [`23127404_HW06_CICD_Report.md`](file:///D:/HCMUS/Third%20Year/Software%20Testing/eshop-sut/docs/assignments/HW06/deliverables/cicd/23127404_HW06_CICD_Report.md) ➔ Xuất ra `docs/assignments/HW06/deliverables/cicd/23127404_HW06_CICD_Report.pdf`

---

### Bước 5: Đóng gói ZIP & Nộp bài lên Moodle
Sau khi đã thêm đầy đủ các file PDF, ảnh chụp Issue và cập nhật link YouTube:
1. Chạy lệnh nén cập nhật file ZIP:
   ```powershell
   Compress-Archive -Path "docs\assignments\HW06\deliverables\*" -DestinationPath "docs\assignments\HW06\23127404_HW06_AI_API_100.zip" -Force
   ```
2. Kiểm tra tên file đúng chuẩn: `23127404_HW06_AI_API_100.zip`.
3. Đăng nhập Moodle môn Kiểm thử Phần mềm và nộp file ZIP trước thời hạn.
