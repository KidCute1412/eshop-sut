# HW05 Demo Video Record

**Unlisted YouTube URL:**

## Vietnamese narration script

### 0:00–0:40 — Introduction

“Em là sinh viên 23127404. Đây là HW05 Performance Testing cho EShop backend chạy local. Workflow được kiểm thử là login, xem chi tiết sản phẩm, thêm vào giỏ hàng và checkout.”

### 0:40–1:50 — Load

“Đây là Load plan trong JMeter. Summary Report cho thấy bốn endpoint của workflow, số sample và error rate. Bên phải là Task Manager hiển thị tiến trình node.exe của backend trong lúc test chạy.”

### 1:50–3:00 — Stress

“Đây là Stress plan. Aggregate Report tổng hợp kết quả khi tăng số virtual users. Test vẫn dùng cùng workflow và CSV data; khác biệt chỉ là cấu hình tải.”

### 3:00–4:00 — Spike

“Đây là Spike plan với ramp-up ngắn. View Results Tree là report view thứ ba, khác với Load và Stress. Task Manager được mở cùng frame để quan sát backend.”

### 4:00–4:50 — Endurance and raw evidence

“Đây là raw JTL và HTML report. Endurance run kéo dài 10 phút 41 giây, có 4,400 sample thành công và không có lỗi trong JTL. Mọi metric trong report được tính từ raw logs.”

### 4:50–5:35 — Lockout

“Đây là kiểm tra lockout runtime. Hai login sai đầu trả HTTP 401, còn request thứ ba trả HTTP 403. Sau khi restart backend local, login đúng trả HTTP 200. Quy trình reset được lưu làm evidence.”

### 5:35–6:20 — AI review and Agent Skill

“Em dùng Agent Skill jmeter-performance-evidence để kiểm tra evidence và tóm tắt JTL. Skill không tạo số liệu hay ảnh giả; các kết quả đều yêu cầu raw evidence thật. AI output được human review và ghi trong AI Audit Report.”
