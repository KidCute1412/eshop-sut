# Checklist chốt nộp HW03 — 23127404

Cập nhật trạng thái: 03/08/2026.

## Quy ước

- `[x]`: artifact đã hoàn thành và vượt qua kiểm tra tự động tương ứng.
- `[ ]`: còn hành động bên ngoài hoặc bằng chứng phải bổ sung trước khi tạo ZIP cuối.

## Nội dung đã hoàn thành

- [x] Phạm vi được chuẩn hóa thành FR-07, FR-10, FR-11, FR-18 và FR-23.
- [x] FR-23 được xác định là Mobile Product Detail, tương đương FR-06 trên Mobile.
- [x] Checklist có đúng 45 mục: 25 Passed, 20 Failed và 0 Not Executed.
- [x] FR-23 có 14 mục: 9 Passed và 5 Failed.
- [x] Có 19 defect runtime được chuẩn hóa: 15 Desktop và 4 Mobile.
- [x] Tất cả 20 checklist item Failed có Bug ID và evidence.
- [x] Chrome và Firefox có năm ảnh cho mỗi nền tảng; mười ảnh Desktop được giữ nguyên.
- [x] Có bốn ảnh runtime Mobile được ánh xạ tới các assertion FR-23 nhìn thấy trực tiếp.
- [x] Usability có một pilot và bảy official participant P1–P7.
- [x] Kết quả usability được đồng bộ: 7/7 independent, median 75 giây, 14 errors, 14 hesitations, 0 interventions và SUS trung bình 73.6/100.
- [x] Tên file Pilot và P1–P7, metadata, SHA-256 và link Drive chung đã được lập chỉ mục.
- [x] README, main report, checklist, bug report và usability workbook dùng cùng một bộ số liệu.
- [x] Email liên hệ là `23127404@student.hcmus.edu.vn`; identity overlay là `23127404@hcmus.edu.vn`.
- [x] AI Audit Report và AI Critique đã hoàn thành; AI Critique nằm trong giới hạn 200–300 từ.
- [x] Unit tests của skill, artifact validator và submission validator đều PASS.
- [x] `main_report.pdf`, `ai_audit_report.pdf` và `ai_critique.pdf` đã được sinh lại từ Markdown hiện hành.

## Hành động bên ngoài còn lại

- [ ] Bổ sung overlay `23127404@hcmus.edu.vn` vào bằng chứng Mobile đủ điều kiện.
- [ ] Ghi chính xác device model, iOS version, Expo version, SUT location và execution date cho CP-03.
- [x] Đã xác minh endpoint Drive công khai trả HTTP 200 và liệt kê đủ Pilot cùng P1–P7 ngày 03/08/2026.
- [x] Đã sửa và xác minh lại MSSV `23127404` trong tiêu đề GitHub Issue #118.
- [x] Video demo Agent Skill đã được tải lên YouTube, ghi trong `demo_video_link.txt` và access-test qua YouTube oEmbed ngày 03/08/2026.
- [x] Đã bổ sung `deliverables/git_commit_log.txt` đến commit `e184e62`.
- [ ] Tạo lại ZIP nộp bài sau khi hoàn tất các hành động trên.

## Kiểm tra tính toàn vẹn trước khi đóng gói

- [x] Không còn `Pool D`, Mobile Cart, Mobile Checkout hoặc Mobile Profile trong phạm vi Task 1.
- [x] Usability Web không được gắn nhãn FR-23.
- [x] Không dùng source inspection để xác lập kết quả runtime Pass/Fail.
- [x] Không còn `not coded`, placeholder participant result hoặc broken notes reference trong workbook usability.
- [x] Công thức và cached value SUS đều đọc được bằng công cụ phân tích XLSX.
- [x] Chỉ các assertion nhìn thấy trong bốn ảnh Mobile được đánh dấu Pass/Fail.
- [x] Timestamp usability được giữ dưới dạng session record; tài liệu không tuyên bố đã tái mã hóa từng timestamp từ video.

## Nội dung không đưa vào ZIP

- [ ] Xác nhận ZIP không chứa `specs/`, `workbench/`, archive hoặc CSV nguồn nội bộ.
- [ ] Xác nhận ZIP không chứa `__pycache__/`, `.pyc`, lock file Excel hoặc script tạm.
- [ ] Xác nhận ZIP không chứa ZIP cũ hoặc bản skill trực tiếp từ `.agents`.
- [ ] Chỉ đưa bản skill mirror đã chuẩn hóa trong `deliverables/agent_skills` vào ZIP.

## Chốt nộp

- [x] Đã xác minh Drive công khai, YouTube demo và tiêu đề GitHub Issue #118.
- [x] Đã chạy lại unit tests, artifact validator và submission validator.
- [x] Đã bổ sung git commit log đến commit `e184e62`.
- [ ] Tạo ZIP chỉ từ nội dung bên trong `deliverables`.
- [ ] Mở thử Markdown, PDF, XLSX, ảnh và liên kết từ chính ZIP trước khi tải lên Moodle.
