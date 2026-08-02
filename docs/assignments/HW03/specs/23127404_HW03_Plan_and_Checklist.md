# HW03 - KẾ HOẠCH BÀI TẬP VÀ CHECKLIST HOÀN THIỆN (GUI & USABILITY TESTING)

**Thông tin sinh viên:**
- Họ và tên: Lê Tuấn Lộc
- MSSV: 23127404
- Mã bài tập: HW03-AI (GUI and Usability Testing)
- Phạm vi FR được phân công: **FR-07** (Shopping cart), **FR-10** (Order state machine), **FR-11** (Order history view - user), **FR-18** (Order management - admin), **FR-23** (Product detail view - mobile - FR-06 trên Mobile App).
- Thư mục nộp bài: `docs/assignments/HW03/deliverables`
- Tên file zip nộp bài: `23127404_HW03_AI_GUIUsability_100.zip`

---

## I. PHÂN TÍCH YÊU CẦU ĐỀ BÀI (REQUIREMENTS ANALYSIS)

### 1. Phân bổ điểm số & Các cột mốc chính (Total: 100 điểm)
| STT | Hạng mục | Trọng số | Yêu cầu cốt lõi |
| :---: | :--- | :---: | :--- |
| **Task 1** | **GUI Checklist** (Thiết kế + Thực thi + Bug report) | **30 điểm** | • Checklist **> 40 items** bao phủ 4 khía cạnh giao diện (IA-01 -> IA-04) cho cả 5 FRs (FR-07, FR-10, FR-11, FR-18, FR-23).<br>• Dùng AI sinh bộ checklist ban đầu, tự rà soát & bổ sung các items AI bỏ sót (giải thích lý do).<br>• Thực thi checklist, đánh dấu Pass/Fail + ghi chú nguyên do Fail.<br>• Log bug trên file Markdown & GitHub Issues (kèm ảnh chụp). |
| **Task 2** | **Usability Evaluation** (Kịch bản + 7 phiên thử nghiệm + Phân tích) | **40 điểm** | • Giữ trên Customer Web với luồng **FR-07 → thao tác hỗ trợ tạo đơn → FR-10 → FR-11**. Web Product Detail là bước hỗ trợ thuộc FR-06, không phải FR-23; **không mô tả FR-10 là Checkout**.<br>• *Lưu ý:* FR-18 chỉ thuộc Task 1; không tuyên bố participant đã kiểm thử FR-23.<br>• **Quay màn hình 7 phiên chính thức**; nên quay thêm pilot.<br>• Thực hiện **7 phiên thử nghiệm** với **7 người thật**.<br>• Chỉ phân tích từ dữ liệu phiên thử nghiệm thật đã được human review. |
| **Task 3** | **Cross-Browser / Cross-Platform** (≥ 3 nền tảng) | **20 điểm** | • Kiểm thử trên 3 nền tảng thực sự: **Chrome (Desktop)**, **Firefox (Desktop)**, và **Expo Go / Chrome trên Điện thoại thật (Real Physical Mobile Device)** hoặc cloud testing (BrowserStack/LambdaTest). *Không dùng Chrome DevTools Mobile Emulation*.<br>• **Bắt buộc:** Mọi ảnh chụp màn hình phải hiển thị rõ Tên trình duyệt/OS/Thiết bị, URL localhost, cùng Overlay Watermark định dạng: `Lê Tuấn Lộc - 23127404 - 23127404@hcmus.edu.vn`. |
| **Task 4** | **Agent Skill** | **10 điểm** | • Xây dựng Agent Skill kiểm thử GUI/Usability tái sử dụng được.<br>• Đính kèm link YouTube video minh họa thao tác end-to-end của Agent Skill. |

---

### 2. Chi tiết 4 khía cạnh giao diện (Interface Aspects - IA) cần phủ trong Task 1
1. **IA-01: General UI Standards** (Tiêu chuẩn giao diện chung): Font chữ, bảng màu, độ tương phản, khoảng cách padding/margin, tính nhất quán (alignment), responsive layout trên Desktop vs Mobile.
2. **IA-02: Forms** (Biểu mẫu & Ô nhập liệu): Validation số lượng, định dạng dữ liệu, ô bắt buộc (required fields), trạng thái disabled/active, thông báo lỗi ô nhập liệu.
3. **IA-04: Feedback / State** (Phản hồi & Trạng thái): Trạng thái loading, empty state (giỏ hàng trống, lịch sử đơn hàng trống), thông báo thành công (toast/modal), trạng thái lỗi hệ thống/API.
4. **IA-03: Navigation** (Điều hướng): Nút chuyển trang, link breadcrumbs, nút quay lại, CTA mua hàng/thanh toán/chuyển trạng thái đơn hàng.

---

## II. CẤU TRÚC THƯ MỤC VÀ HỒ SƠ NỘP BÀI (DELIVERABLES STRUCTURE)

Thư mục nộp bài local: `docs/assignments/HW03/deliverables/`
File nén zip cuối cùng để nộp Moodle: `23127404_HW03_AI_GUIUsability_100.zip`

### 1. Cấu trúc cây thư mục trong ZIP nộp bài
```text
23127404_HW03_AI_GUIUsability_100/
├── README.md                                    # File tổng quan, bảng tự đánh giá, thống kê & link video
├── git_commit_log.txt                           # Log commit Git chi tiết từng bước (gồm commit riêng cho từng usability session)
├── main_report.md                               # Báo cáo chính (bao gồm GUI Checklist Report & Usability Report)
├── main_report.pdf                              # Báo cáo chính xuất dạng PDF
├── ai_reports/
│   ├── ai_audit_report.md                       # Log chi tiết các lần tương tác AI (Tool, Date, Prompt, Output)
│   ├── ai_audit_report.pdf                      # File PDF AI Audit Report
│   ├── ai_critique.md                           # Bài viết đánh giá AI (200 - 300 từ)
│   └── ai_critique.pdf                          # File PDF AI Critique
├── checklist/
│   ├── gui_checklist.xlsx                       # File Excel checklist > 40 items (Pass/Fail/Notes/Summary)
│   └── gui_checklist.csv                        # Bản CSV của checklist
├── bugs/
│   ├── bug_report.md                            # Danh sách các bug phát hiện từ Task 1 & Task 2
│   ├── github_issues_screenshots/               # Ảnh chụp từng bug đã tạo trên GitHub Issues
│   │   ├── bug_001_github.png
│   │   └── ...
│   └── evidence_images/                         # Ảnh chụp màn hình lỗi trên ứng dụng (SUT evidence)
│       ├── bug_001_evidence.png
│       └── ...
├── usability/
│   ├── task_scenario.md                         # Kịch bản giao việc cho người dùng (Customer role)
│   ├── participant_list.md                      # Bảng thông tin 7 người tham gia (đã che 4 số giữa SĐT/Zalo)
│   ├── recordings/                              # Video quay màn hình phiên thử nghiệm (8 videos: 1 pilot + 7 official)
│   │   ├── pilot_session_recording.mp4
│   │   ├── p1_session_recording.mp4
│   │   └── ...
│   ├── raw_responses/                           # Bản ghi câu trả lời SUS & câu hỏi probe của 7 người
│   │   ├── p1_response.md
│   │   └── ...
│   └── observation_notes.md                     # Ghi chép quan sát khó khăn, ngập ngừng của 7 người
├── cross_platform/
│   ├── chrome_desktop/                          # Ảnh chụp Chrome Desktop (có identity + URL + watermark)
│   ├── firefox_desktop/                         # Ảnh chụp Firefox Desktop (có identity + URL + watermark)
│   └── mobile_real_device/                      # Ảnh chụp Expo Go / Android Phone thật (có identity + URL + watermark)
└── agent_skills/
    ├── gui-usability-tester/                    # Skill folder chứa SKILL.md & scripts
    │   └── SKILL.md
    └── demo_video_link.txt                      # Link YouTube demo Agent Skill end-to-end
```

---

## III. KỊCH BẢN QUAY VIDEO VÀ THAO TÁC THỰC TẾ (VIDEO SCRIPTS & GUIDES)

### 🎬 1. Kịch bản quay Video Demo Agent Skill (Task 4)
- **Thời lượng khuyến nghị**: 2 – 3 phút.
- **Công cụ quay**: OBS Studio / Loom / Windows Game Bar (`Win + Alt + R`).
- **Kịch bản thao tác màn hình theo đúng thứ tự**:
  1. **[0:00 - 0:30] Giới thiệu Skill**: Mở thư mục Agent Skill `docs/assignments/HW03/deliverables/agent_skills/gui-usability-tester/SKILL.md` và giải thích cấu trúc Skill giúp tự động hóa việc sinh GUI Checklist & phân tích Usability bugs.
  2. **[0:30 - 1:30] Thực thi Skill bằng Prompt**: Nhập lệnh gọi Agent Skill trong terminal / chat UI (ví dụ: `gọi skill gui-usability-tester rà soát tính năng FR-23 và FR-07`). Cho người xem thấy Agent đọc file giao diện, sinh danh sách test items phân loại theo 4 khía cạnh `IA-01` -> `IA-04`.
  3. **[1:30 - 2:30] Phân tích Bug & Xuất Báo cáo**: Cho xem Agent phát hiện lỗi (ví dụ: số lượng thập phân, nút bấm không phản hồi lần 1), xuất ra file `gui_checklist.xlsx` và tự động tổng hợp báo cáo bug Markdown.
  4. **[2:30 - 3:00] Kết luận**: Trình bày kết quả hoàn thành bài test và dừng video.

---

### 🎥 2. Kịch bản điều phối 7 phiên Usability Testing (Task 2)
Agent sinh sẵn moderator script; người điều phối đọc đúng phần dành cho participant và không tiết lộ đường đi mong đợi:
- **Lời chào & Đặt vấn đề**: *"Chào bạn, hôm nay mình nhờ bạn trải nghiệm giúp một ứng dụng mua sắm di động (EShop). Mục đích là để tìm điểm chưa thân thiện của ứng dụng, không phải kiểm tra bạn. Bạn cứ vừa thao tác vừa nói ra suy nghĩ của mình (think-aloud) nhé!"*
- **Nhiệm vụ cụ thể (Goal-oriented Scenario)**: *"Bạn muốn mua một chiếc iPhone trên ứng dụng EShop. Hãy hoàn tất việc mua sản phẩm và kiểm tra xem đơn hàng vừa tạo hiện đang ở trạng thái nào."*
- **Quy tắc điều phối**: Không đọc tên FR, không chỉ người dùng phải mở màn hình nào hoặc bấm nút nào, không đưa leading hints. Chỉ can thiệp nếu participant hoàn toàn bị kẹt; ghi lại thời điểm, nguyên nhân và mức hỗ trợ đã cung cấp.
- **Ánh xạ nội bộ cho người quan sát (không đọc cho participant)**: Web Product Detail (bước hỗ trợ FR-06) → FR-07 Shopping Cart → thao tác hỗ trợ tạo đơn → FR-10 Order State Machine → FR-11 Order History.
- **Sau khi kết thúc thao tác**: Đưa phiếu khảo sát 10 câu hỏi SUS (thang điểm 1-5 từ Rất không đồng ý đến Rất đồng ý) và hỏi 4 câu probe ngắn:
  - *Clarity*: "Bạn thấy thông tin trên trang nào khó hiểu nhất?"
  - *Error Recovery*: "Khi gặp sự cố hoặc nhập sai, bạn có dễ dàng quay lại không?"
  - *Speed*: "Tốc độ xử lý và phản hồi của app thế nào?"
  - *Trust*: "Ứng dụng này có mang lại cảm giác tin cậy để mua hàng thực tế không?"

---

## IV. PHÂN ĐỊNH RANH GIỚI TỰ ĐỘNG HÓA CỦA AGENT & THAO TÁC CỦA SINH VIÊN

### 🤖 1. Nhiệm vụ Agent tự động hóa tối đa (automation-first):
1. **Xây dựng toàn bộ mã nguồn Agent Skill**: Viết file `agent_skills/gui-usability-tester/SKILL.md`.
2. **Sinh và tự phản biện bộ GUI Checklist > 40 items**: Bao phủ IA-01..IA-04 cho đúng 5 FR được phân công; lưu rõ checklist ban đầu của AI, các item được bổ sung và giả thuyết lý do bản đầu bỏ sót. Human review và chấp nhận hoặc sửa các kết luận này.
3. **Thực thi kiểm thử tự động trên SUT**: Dùng browser/mobile automation và API/database observation khi phù hợp để chạy các kiểm tra có thể tự động hóa; lưu timestamp, môi trường, input, expected, actual, Pass/Fail và evidence. Các tiêu chí mang tính cảm nhận như thẩm mỹ, clarity hoặc trust được agent phân tích sơ bộ nhưng phải gắn cờ `Human Review Required`.
4. **Phân tích mã nguồn và xác minh lỗi động**: Static analysis chỉ tạo bug candidate. Chỉ ghi nhận bug chính thức sau khi tái hiện trên SUT chạy thật hoặc có bằng chứng runtime tương đương; đánh số BUG-001, BUG-002,... và lưu traceability về checklist/FR/IA.
5. **Tự động hóa usability workflow**: Agent sinh objective, goal-oriented scenario, moderator script, SUS form, probe questions, observation template và script tính điểm. Sau mỗi phiên, agent chỉ xử lý transcript/notes/responses thật do phiên thử nghiệm tạo ra; không tự bịa participant, hành vi, câu trả lời, SUS score hoặc consent.
6. **Xuất hồ sơ báo cáo**:
   - `checklist/gui_checklist.xlsx` và `gui_checklist.csv`.
   - `bugs/bug_report.md` và bài viết `ai_critique.md` (200-300 từ).
   - `ai_reports/ai_audit_report.md`.
   - `usability/task_scenario.md`, bản nháp `observation_notes.md`, tính điểm SUS trung bình từ raw responses thật.
   - `README.md` chứa bảng tự đánh giá dựa trên evidence thực tế (chỉ ghi 100/100 khi đủ căn cứ).
   - `git_commit_log.txt`; số commit phản ánh các bước thực tế, không có yêu cầu cố định đúng 13 commit.
   - Chuyển đổi Markdown sang PDF và nén file ZIP `23127404_HW03_AI_GUIUsability_100.zip`.

### 👤 2. Vai trò Human: cung cấp bằng chứng thật và review:
1. **Participant và consent**: Tuyển đúng 7 người thật ngoài lớp, xác minh thông tin liên hệ, xin consent; không giao cho agent tạo hoặc giả lập danh tính.
2. **Bằng chứng vật lý**: Bật quay màn hình cho 7 phiên chính thức (nên quay pilot), thực hiện/chứng kiến các cross-platform runs trên thiết bị hoặc cloud thật, chụp ảnh có identity overlay, và quay video demo Agent Skill.
3. **Human-in-the-loop review**: Duyệt checklist, expected results, các mục `Human Review Required`, observation notes, SUS inputs, bug candidates, severity và báo cáo cuối. Human không cần lặp lại thủ công các test đã được automation chạy và lưu evidence đầy đủ, nhưng phải bác bỏ hoặc yêu cầu chạy lại kết quả thiếu căn cứ.
4. **Cung cấp artifact ngoài hệ thống cho Agent**: Đưa raw SUS/probe responses, observation/video/transcript, ảnh chụp và link video thật để agent phân tích, chèn vào báo cáo và hoàn thiện ZIP.

---

## V. CHECKLIST CÔNG VIỆC VÀ TIẾN TRÌNH THỰC HIỆN CHI TIẾT (ACTION PLAN)

### 🚀 Giai đoạn 1: Chuẩn bị & Thiết kế GUI Checklist (Task 1 - Part A)
- [ ] **Bước 1.1**: Khởi động SUT (Eshop Frontend Web `localhost:3000`, Backend API `localhost:5000`, Mobile App Expo).
- [ ] **Bước 1.2**: Rà soát giao diện và mã nguồn của cả 5 tính năng được phân công:
  - Mobile Product Detail (`FR-23`)
  - Shopping Cart (`FR-07`)
  - Order State Machine (`FR-10`)
  - Order History View (`FR-11`)
  - Admin Order Management (`FR-18`)
- [ ] **Bước 1.3**: Dùng AI sinh bộ checklist ban đầu (> 40 items) bao phủ 4 khía cạnh `IA-01` (Giao diện chung), `IA-02` (Biểu mẫu), `IA-03` (Điều hướng), `IA-04` (Trạng thái/Phản hồi).
- [ ] **Bước 1.4**: Phân tích phản biện các items AI sinh ra, bổ sung thêm ít nhất 5-10 items nâng cao (accessibility, error states đặc thù, responsive boundary) và ghi rõ lý do AI bỏ sót.
- [ ] **Bước 1.5**: Xuất file `gui_checklist.xlsx` và `gui_checklist.csv`.
- [ ] **Commit Git #1**: `git commit -m "feat(hw03): design GUI checklist for FR07, FR10, FR11, FR18, FR23"`

### 🧪 Giai đoạn 2: Thực thi GUI Checklist & Logging Bugs (Task 1 - Part B)
- [ ] **Bước 2.1**: Agent chuyển các checklist item có thể tự động hóa thành executable checks và chạy chúng trên SUT thực tế; lưu command/script, môi trường, expected/actual và timestamp để có thể tái lập.
- [ ] **Bước 2.2**: Agent cập nhật `Pass`, `Fail` hoặc `Human Review Required` vào Excel/CSV/Markdown. Human chỉ review các mục chủ quan, không tự chạy lại những mục đã có evidence tự động đầy đủ.
- [ ] **Bước 2.3**: Với mỗi item `Fail`, agent tự chụp screenshot/trace/log khi công cụ cho phép và đặt tên `bug_xxx_evidence.png`; human chỉ bổ sung ảnh từ thiết bị thật hoặc bối cảnh agent không truy cập được.
- [ ] **Bước 2.4**: Agent tái hiện bug candidate, loại false positive và soạn `bug_report.md` có steps, expected, actual, environment, severity và traceability.
- [ ] **Bước 2.5**: Sau human approval, agent tạo/cập nhật GitHub Issue nếu đã được cấp quyền; human cung cấp ảnh chụp trang Issue khi đây là evidence nộp bài bắt buộc.
- [ ] **Commit Git #2**: `git commit -m "test(hw03): execute GUI checklist and log bug reports on GitHub"`

### 👥 Giai đoạn 3: Chuẩn bị & Thực hiện Usability Evaluation (Task 2)
- [ ] **Bước 3.1**: Định nghĩa mục tiêu đánh giá usability và soạn Kịch bản nhiệm vụ (Task Scenario) thuần túy vai trò Khách hàng (Customer):
  - *Kịch bản đọc cho participant*: "Bạn muốn mua một chiếc iPhone trên ứng dụng EShop. Hãy hoàn tất việc mua sản phẩm và kiểm tra xem đơn hàng vừa tạo hiện đang ở trạng thái nào." Không nêu FR hoặc chỉ dẫn từng bước.
  - *Ánh xạ nội bộ*: Web Product Detail hỗ trợ (FR-06) → FR-07 → thao tác hỗ trợ tạo đơn → FR-10 → FR-11; không gắn usability Web với FR-23.
- [ ] **Bước 3.2**: Thiết lập phiếu khảo sát Thang đo SUS (10 câu hỏi tiêu chuẩn) kèm 4 câu hỏi định tính probe (Độ rõ ràng, Khả năng phục hồi lỗi, Tốc độ, Độ tin cậy).
- [ ] **Bước 3.3**: Lập danh sách 7 người tham gia thực tế bên ngoài lớp học (che 4 số giữa SĐT/Zalo).
- [ ] **Bước 3.4**: Tiến hành 1 pilot session; nên bật quay màn hình để agent có thể trích transcript/interaction timeline, phát hiện câu chữ gây dẫn dắt và đề xuất tinh chỉnh kịch bản.
  - **Commit Git #3**: `git commit -m "docs(hw03): complete usability pilot session and refine scenario"`
- [ ] **Bước 3.5**: Tiến hành 7 phiên chính thức với participant thật và quay màn hình. Agent tiếp nhận recording/transcript/raw responses để tự động dựng interaction timeline, observation draft và SUS record; human review, sửa sai và xác nhận từng phiên:
  - **Commit Git #4**: `git commit -m "test(hw03): conduct usability session 1 with participant P1"`
  - **Commit Git #5**: `git commit -m "test(hw03): conduct usability session 2 with participant P2"`
  - **Commit Git #6**: `git commit -m "test(hw03): conduct usability session 3 with participant P3"`
  - **Commit Git #7**: `git commit -m "test(hw03): conduct usability session 4 with participant P4"`
  - **Commit Git #8**: `git commit -m "test(hw03): conduct usability session 5 with participant P5"`
  - **Commit Git #9**: `git commit -m "test(hw03): conduct usability session 6 with participant P6"`
  - **Commit Git #10**: `git commit -m "test(hw03): conduct usability session 7 with participant P7"`
- [ ] **Bước 3.6**: Agent tính SUS từng người và trung bình từ raw responses, kiểm tra công thức, nhóm pain points, phân loại severity và soạn bug report; human xác nhận dữ liệu đầu vào và các diễn giải định tính.
  - **Commit Git #11**: `git commit -m "docs(hw03): synthesize usability findings and SUS score analysis"`

### 🌐 Giai đoạn 4: Thử nghiệm Cross-Browser / Cross-Platform (Task 3)
- [ ] **Bước 4.1**: Agent chạy cùng cross-platform suite trên **Chrome Desktop**, thu screenshot, console log, viewport và kết quả từng check.
- [ ] **Bước 4.2**: Agent chạy lại suite tương đương trên **Firefox Desktop**, tự động diff và đánh dấu khác biệt cần review.
- [ ] **Bước 4.3**: Agent điều phối test trên **điện thoại thật (Expo Go / Android Chrome)** hoặc cloud device khi có kết nối automation; human chỉ khởi tạo/cấp quyền thiết bị và bổ sung ảnh thực tế khi agent không thể tự capture. *Không dùng DevTools Mobile Emulation để thay thế platform thật*.
- [ ] **Bước 4.4**: Đảm bảo tất cả các ảnh chụp ở Bước 4.1, 4.2, 4.3 đều hiển thị đầy đủ:
  1. Tên trình duyệt / Hệ điều hành / Thiết bị
  2. Đường dẫn URL localhost (`http://localhost:3000` / IP Expo)
  3. Watermark / Overlay thông tin sinh viên: `Lê Tuấn Lộc - 23127404 - 23127404@hcmus.edu.vn`.
- [ ] **Bước 4.5**: Agent tổng hợp screenshot diff, log và kết quả để nhận xét khác biệt giữa 3 nền tảng trong `main_report.md`; human review các kết luận thị giác/chủ quan.
- [ ] **Commit Git #12**: `git commit -m "test(hw03): capture cross-platform screenshots on Chrome, Firefox, and Real Mobile Device with identity watermark"`

### 🤖 Giai đoạn 5: Đóng gói Agent Skill & Viết AI Reports (Task 4 & Mandatory Appendix)
- [ ] **Bước 5.1**: Tạo thư mục Agent Skill `agent_skills/gui-usability-tester/SKILL.md`.
- [ ] **Bước 5.2**: Quay video màn hình minh họa Agent Skill thực thi end-to-end, tải video lên YouTube và lấy đường dẫn.
- [ ] **Bước 5.3**: Tổng hợp nhật ký AI thành `ai_reports/ai_audit_report.md`.
- [ ] **Bước 5.4**: Viết đoạn văn `ai_reports/ai_critique.md` (200 - 300 từ) phản biện AI theo quy định.
- [ ] **Bước 5.5**: Tạo file `git_commit_log.txt` trích xuất từ lệnh `git log --oneline`.
- [ ] **Bước 5.6**: Đóng gói file `README.md` hoàn chỉnh.
- [ ] **Commit Git #13**: `git commit -m "docs(hw03): finalize agent skill, ai audit report and submission README"`

> Các số commit ở kế hoạch này là thứ tự dự kiến để dễ theo dõi, không phải con số bắt buộc của đề. Nếu một bước phát sinh nhiều thay đổi độc lập, agent được phép tạo thêm commit có nội dung rõ ràng.

### 📦 Giai đoạn 6: Đóng gói hồ sơ nộp bài (Final Package)
- [ ] **Bước 6.1**: Chuyển đổi các file markdown (`main_report.md`, `ai_audit_report.md`, `ai_critique.md`) sang định dạng PDF.
- [ ] **Bước 6.2**: Kiểm tra đầy đủ sự tồn tại của tất cả các file trong cây thư mục `docs/assignments/HW03/deliverables/`.
- [ ] **Bước 6.3**: Nén thư mục thành file `23127404_HW03_AI_GUIUsability_100.zip` trong `docs/assignments/HW03/deliverables/`.
- [ ] **Bước 6.4**: Rà soát theo checklist cuối cùng để đảm bảo không thiếu bất kỳ tài liệu bắt buộc nào.
