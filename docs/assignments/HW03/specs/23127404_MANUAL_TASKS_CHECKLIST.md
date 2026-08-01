# CHECKLIST THAO TÁC HUMAN TỐI THIỂU — AUTOMATION-FIRST

**Họ và tên:** Lê Tuấn Lộc  
**MSSV:** 23127404  
**Mã bài tập:** HW03-AI (GUI and Usability Testing)  
**Mục đích:** Human chỉ tạo/cung cấp bằng chứng người thật và thiết bị thật, sau đó review gói cuối. Agent thiết kế kịch bản, chạy kiểm thử tự động, trích dữ liệu, phân tích, lập báo cáo và đóng gói.

> Không nhập lại SUS vào Excel, không viết observation notes, không tự chụp Chrome/Firefox, không tự tính điểm và không tự tạo commit/ZIP. Agent phải sinh các artifact đó từ evidence thật.

---

## 0. NHẬN GÓI HƯỚNG DẪN DO AGENT TẠO

- [ ] Nhận và dùng đúng phiên bản cuối của:
  - goal-oriented task scenario;
  - moderator script và câu consent;
  - 10 câu SUS, thang điểm 1–5;
  - 4 probe questions: clarity, error recovery, speed và trust;
  - quy tắc đặt tên video/ảnh và thư mục intake.

Human không tự soạn các nội dung trên. Nếu tài liệu chưa tồn tại hoặc chưa được agent kiểm tra với đề bài thì chưa bắt đầu ghi hình.

---

## 1. THU VIDEO USABILITY THẬT

### 1.1. Pilot

- [ ] Thực hiện 1 pilot session với một người thật để kiểm tra scenario, flow và thời lượng.
- [ ] Quay pilot nếu thuận tiện để agent tự phân tích và đề xuất chỉnh sửa; PDF bắt buộc thực hiện pilot nhưng không nói rõ bắt buộc nộp recording pilot.
- [ ] Sau pilot, dùng bản moderator script đã được agent cập nhật cho 7 phiên chính thức.

### 1.2. Bảy phiên chính thức

- [ ] Tuyển 7 participant thật bên ngoài lớp HW03; ưu tiên non-IT/non-tester.
- [ ] Quay màn hình đầy đủ 7 phiên, mỗi participant một video.
- [ ] Trong từng recording phải có đủ dữ liệu nguồn sau để agent tự trích xuất:
  1. Participant xác nhận đồng ý ghi màn hình; chỉ ghi audio khi đã đồng ý.
  2. Họ tên và thông tin liên hệ có thể xác minh (Zalo/email/điện thoại). Có thể thu phần này trong một intake clip/file riêng để tránh công khai; agent sẽ che 4 số giữa trong báo cáo.
  3. Lời giao việc đúng goal-oriented scenario do agent tạo, không đọc tên FR, không chỉ từng nút và không đưa leading hints.
  4. Toàn bộ thao tác và think-aloud của participant.
  5. Câu trả lời bằng số 1–5 cho đủ 10 câu SUS.
  6. Câu trả lời thật cho đủ 4 probe questions.
- [ ] Nếu phải can thiệp vì participant hoàn toàn bị kẹt, nói rõ trên recording mức hỗ trợ đã cung cấp để agent ghi nhận.
- [ ] Chép 7 video và intake clip/file vào thư mục intake do agent chỉ định. Human không cần tự tạo transcript, observation notes, bảng SUS hay severity findings.

> Nếu video không chứa SUS/probe responses hoặc agent không đọc được audio, human phải bổ sung raw responses thật. Agent không được suy đoán hoặc tự sinh dữ liệu còn thiếu.

---

## 2. CHỤP ẢNH TRÊN ĐIỆN THOẠI THẬT

- [ ] Mở SUT bằng Expo Go hoặc Android Chrome trên điện thoại vật lý; không dùng Chrome DevTools mobile emulation để thay thế.
- [ ] Chụp các màn hình/flow theo shot list do agent tạo.
- [ ] Bảo đảm evidence thể hiện được nền tảng/thiết bị thật, SUT hoặc địa chỉ truy cập phù hợp và identity overlay tối thiểu `23127404@hcmus.edu.vn`; có thể dùng đầy đủ `Lê Tuấn Lộc - 23127404 - 23127404@hcmus.edu.vn`.
- [ ] Chép ảnh gốc vào thư mục intake do agent chỉ định.

Agent chịu trách nhiệm tự chạy Playwright trên Chrome Desktop và Firefox Desktop, chụp screenshot, thu log, so sánh kết quả và tạo phần cross-platform report. Human chỉ chụp desktop bổ sung nếu automation không tạo được evidence hợp lệ.

---

## 3. VIDEO DEMO AGENT SKILL

- [ ] Quay video end-to-end theo demo script do agent tạo. Human chỉ thao tác/ghi hình; agent chuẩn bị nội dung trình diễn và kiểm tra artifact đầu ra.
- [ ] Upload video lên YouTube ở chế độ Unlisted hoặc Public bằng tài khoản của Human.
- [ ] Cung cấp link thật cho agent để agent tự chèn vào `demo_video_link.txt`, `README.md` và báo cáo.

---

## 4. REVIEW VÀ NỘP BÀI

- [ ] Review bản tóm tắt cuối do agent tạo, tập trung vào:
  - participant/contact đã đúng và đã được che thông tin;
  - SUS inputs khớp recording/raw responses;
  - các mục `Human Review Required`;
  - bug, severity và observation không bị agent suy diễn hoặc bịa;
  - ảnh/video/link đều mở được và đúng người/nền tảng.
- [ ] Xác nhận self-assessed grade dựa trên evidence thực tế; chỉ dùng `_100.zip` nếu thật sự đủ căn cứ.
- [ ] Upload ZIP do agent tạo lên Moodle trước deadline.

---

## 5. CÁC VIỆC AGENT PHẢI TỰ ĐỘNG THỰC HIỆN

Human không cần thao tác thủ công các việc sau:

- Sinh và phản biện GUI checklist hơn 40 items cho FR-07, FR-10, FR-11, FR-18 và FR-23.
- Khởi động SUT khi môi trường cho phép; chạy browser/API/database checks và lưu evidence.
- Chạy Playwright thật trên Chrome Desktop và Firefox Desktop.
- Tạo screenshot web/bug evidence; đánh dấu `Pass`, `Fail` hoặc `Human Review Required`.
- Trích transcript/timeline từ video, tạo observation draft và liên kết evidence.
- Trích SUS/probe responses thật, tính điểm và kiểm tra công thức.
- Nhóm pain points, phân loại severity, tái hiện bug candidates và lập bug report.
- Tạo/cập nhật GitHub Issues khi được cấp quyền; không tạo issue từ bug chưa được xác minh.
- Sinh Excel/CSV/Markdown/PDF, AI Audit Report, AI Critique, README và test summary.
- Tạo Git commits theo các bước công việc thực tế, xuất `git_commit_log.txt`; không tạo hàng loạt commit giả và không ép đúng 13 commit.
- Kiểm tra completeness và tạo ZIP theo self-assessed grade đã được Human xác nhận.

## TÓM TẮT THAO TÁC HUMAN

1. Thu 7 video usability đầy đủ dữ liệu thật; thực hiện pilot và nên quay lại.
2. Chụp ảnh theo shot list trên điện thoại vật lý.
3. Quay/upload video demo Agent Skill và đưa link cho agent.
4. Review gói cuối và upload Moodle.
