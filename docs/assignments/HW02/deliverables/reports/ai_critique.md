# AI Critique

---

## 1. AI Critique (Mandatory, 200–300 words)

Trong quá trình làm bài tập kiểm thử ứng dụng eShop bằng phương pháp Domain Testing và Boundary Value Analysis (BVA), tôi nhận thấy công cụ AI (Gemini) có cả những điểm mạnh và điểm yếu rất rõ ràng.

**Về điểm mạnh**, AI giống như một trợ lý viết tài liệu rất nhanh. Nó giúp tôi lập các bảng phân tích, chia các nhóm giá trị đầu vào đúng/sai dựa trên tài liệu mô tả yêu cầu, và tự động tạo ra danh sách các kịch bản kiểm thử (test cases) rất đầy đủ về mặt lý thuyết. Nó cũng giúp tôi dò và liên kết mã test case với các lớp giá trị một cách nhanh chóng.

**Về điểm yếu**, AI thường bị phụ thuộc hoàn toàn vào lý thuyết mô tả và không tự đoán được các lỗi thực tế khi chạy chương trình:
1. **Lỗi nút bấm trên web (BUG-010)**: AI nghĩ rằng cứ nhấn nút "Thêm vào giỏ hàng" là hệ thống sẽ xử lý ngay. Nhưng thực tế giao diện web bị lỗi nên tôi phải click đúp (2 lần liên tiếp) thì mới thêm thành công.
2. **Lỗi phân quyền hệ thống (BUG-003, BUG-004, BUG-014)**: AI nghĩ rằng hệ thống đã tự động chặn các tài khoản thường. Nhưng thực tế code backend chỉ kiểm tra xem mã token có hợp lệ không chứ không kiểm tra vai trò của tài khoản đó có đúng là admin hay không, dẫn đến việc tài khoản thường vẫn gọi được các API admin.
3. **Lỗi nhập liệu trên di động (BUG-006, BUG-008)**: AI không phát hiện ra lỗi khi để trống ô nhập liệu hoặc nhập số lượng bằng 0/số âm thì hệ thống vẫn tự động đổi thành 1 để thêm vào giỏ hàng.

**Bài học rút ra**: Tôi không thể tin hoàn toàn vào các kịch bản do AI tự tạo ra. Con người vẫn phải là người trực tiếp chạy thử phần mềm, so sánh giao diện thực tế để tìm ra những lỗi ẩn mà AI không thể tự thấy được.

---
