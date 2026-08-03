# Kịch Bản Demo Agent Skill (HW03 - GUI & Usability Testing)

- **Mã sinh viên:** 23127404
- **Skill được demo:** `gui-usability-tester` (`.agents/skills/gui-usability-tester`)
- **Thời lượng dự kiến:** 2 - 3 phút
- **Mục tiêu:** Thể hiện cách AI Agent tự động hóa và tuân thủ quy trình kiểm thử GUI/Usability theo tiêu chuẩn bài tập HW03.

---

## 📽️ Cấu Trúc Kịch Bản Video Demo

### Phân đoạn 1: Giới thiệu Agent Skill (0:00 - 0:30)
1. **Thao tác trên màn hình:**
   - Mở thư mục `.agents/skills/gui-usability-tester/`.
   - Mở file `SKILL.md` để cho thấy định nghĩa skill, 4 chế độ làm việc (`DESIGN`, `EXECUTE`, `ANALYZE`, `AUDIT`) và các file tham chiếu (`references/`).
2. **Lời thoại/Ghi chú:**
   - "Xin chào, đây là video demo sử dụng Agent Skill `gui-usability-tester` cho HW03."
   - "Skill được thiết kế dạng quy trình chuẩn gồm thiết kế checklist 4 IA (IA-01 đến IA-04), thực thi kiểm thử, phân tích Usability SUS và kiểm tra tính hợp lệ artifact."

---

### Phân đoạn 2: Kích hoạt & Chạy Mode DESIGN (0:30 - 1:15)
1. **Thao tác trên màn hình:**
   - Gửi prompt cho Agent: 
     > *"Dùng skill gui-usability-tester ở mode DESIGN để thiết kế GUI checklist >40 items cho màn hình EShop Checkout và Home, phủ 4 khía cạnh IA-01 đến IA-04."*
   - Quay màn hình Agent đọc `SKILL.md` và tạo bảng Checklist theo chuẩn HW03.
2. **Lời thoại/Ghi chú:**
   - "Agent tự động đọc quy tắc traceability, phân loại các tiêu chí UI standards, Forms, Navigation, Feedback/State, bổ sung các item mà AI thông thường dễ bỏ sót (Dark mode, Keyboard focus, RTL)."

---

### Phân đoạn 3: Thực thi Mode EXECUTE & AUDIT (1:15 - 2:15)
1. **Thao tác trên màn hình:**
   - Gửi prompt tiếp theo:
     > *"Chạy mode EXECUTE và AUDIT để đánh giá kết quả kiểm thử và chạy script validate_artifacts.py."*
   - Mở Terminal chạy câu lệnh validation:
     ```bash
     python .agents/skills/gui-usability-tester/scripts/validate_artifacts.py docs/assignments/HW03
     ```
   - Cho thấy kết quả validation trả về thành công (`VALID / PASS`).
2. **Lời thoại/Ghi chú:**
   - "Agent tổng hợp kết quả Pass/Fail, lập danh sách Defect và tự động chạy script audit dữ liệu để đảm bảo không có thông tin bị hư cấu hay sai lệch thống kê."

---

### Phân đoạn 4: Tổng kết & Cập nhật README (2:15 - 2:45)
1. **Thao tác trên màn hình:**
   - Mở file `README.md` của bài nộp, trỏ đến phần **Demo Videos / Self-Assessment Table**.
   - Dán link YouTube video demo vào file `README.md`.
2. **Lời thoại/Ghi chú:**
   - "Skill giúp chuẩn hóa 100% quy trình kiểm thử GUI Usability. Video link được nhúng trực tiếp vào file README.md phục vụ nộp bài. Cảm ơn thầy cô đã theo dõi."

---

## 📌 Checklist chuẩn bị trước khi quay
- [x] Đã cài đặt skill tại `.agents/skills/gui-usability-tester/`.
- [x] Đã chuẩn bị sẵn môi trường SUT (EShop local / BrowserStack).
- [x] Đảm bảo Terminal mở sẵn thư mục project để chạy script validation.
- [x] Đã tạo sẵn link unlisted / public trên YouTube để điền vào `README.md`.
