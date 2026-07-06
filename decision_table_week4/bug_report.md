# Báo Cáo Phát Hiện Lỗi Bảo Mật (Bug Report) - FR-12: Access Control

Tài liệu này báo cáo các lỗi bảo mật phát hiện được khi đối chiếu giữa thiết kế kiểm thử (`test_design/test_design.md`) và mã nguồn thực tế của hệ thống.

---

## BUG-01: API Admin quản lý tài khoản chỉ xác thực, không kiểm tra vai trò (role)

- **Mức độ nghiêm trọng**: Critical
- **Endpoint**: `GET /api/admin/users`
- **Vị trí code**: backend/server.js (Dòng 494)
- **Test case liên quan**: `FR12-DT-08`, `FR12-DT-09`, `FR12-DT-10`
- **Mô tả**:
  Endpoint được đặt tên theo miền admin nhưng chỉ sử dụng middleware xác thực `authenticateToken`. Mọi token hợp lệ, kể cả của người dùng thường (`role = 'user'`), tài khoản có vai trò sai định dạng hoặc thiếu vai trò, đều có thể đọc được danh sách người dùng kèm theo thông tin nhạy cảm.
- **Kết quả thực tế**: `200 OK`
- **Kết quả mong đợi**: `403 Forbidden` nếu vai trò không phải là `admin`.

---

## BUG-02: Các API ghi dữ liệu Danh mục thiếu kiểm tra vai trò admin

- **Mức độ nghiêm trọng**: High
- **Endpoint**:
  - `POST /api/categories`
  - `PUT /api/categories/:id`
  - `DELETE /api/categories/:id`
- **Vị trí code**:
  - backend/server.js (Dòng 249)
  - backend/server.js (Dòng 257)
  - backend/server.js (Dòng 269)
- **Test case liên quan**: `FR12-DT-12`, `FR12-PW-10`, `FR12-PW-11`
- **Mô tả**:
  Các endpoint thay đổi danh mục có gắn `authenticateToken` nhưng không có middleware kiểm tra vai trò admin, do đó người dùng thông thường vẫn có thể tạo, sửa đổi và xóa danh mục sản phẩm.
- **Kết quả thực tế**: `200 OK`
- **Kết quả mong đợi**: `403 Forbidden`

---

## BUG-03: Các API ghi dữ liệu Sản phẩm thiếu hoàn toàn xác thực và phân quyền

- **Mức độ nghiêm trọng**: High
- **Endpoint**:
  - `POST /api/products`
  - `PUT /api/products/:id`
  - `DELETE /api/products/:id`
- **Vị trí code**:
  - backend/server.js (Dòng 167)
  - backend/server.js (Dòng 179)
  - backend/server.js (Dòng 191)
- **Test case liên quan**: `FR12-DT-11`, `FR12-PW-12`
- **Mô tả**:
  Các API thay đổi thông tin sản phẩm không sử dụng middleware `authenticateToken`. Bất kỳ khách vãng lai nào (Guest) cũng có thể trực tiếp gửi request để tạo mới, chỉnh sửa hoặc xóa sản phẩm khỏi cơ sở dữ liệu.
- **Kết quả thực tế**: `200 OK`
- **Kết quả mong đợi**: `401 Unauthorized` khi thiếu token, và `403 Forbidden` nếu có token nhưng không phải admin.

---

## BUG-04: Token không hợp lệ trả về mã lỗi `403` thay vì `401`

- **Mức độ nghiêm trọng**: Medium
- **Endpoint đại diện**:
  - `POST /api/cart`
  - `GET /api/admin/users`
  - `POST /api/categories`
- **Vị trí code**: backend/server.js (Dòng 100)
- **Test case liên quan**: `FR12-DT-03`, `FR12-DT-06`, `FR12-PW-05`, `FR12-PW-08`
- **Mô tả**:
  Middleware `authenticateToken` đang trả về mã lỗi `403 Forbidden` khi phát hiện token sai chữ ký hoặc hết hạn. Theo chính sách thiết kế kiểm thử chuẩn, đây được coi là lỗi xác thực nên kết quả mong đợi phải là `401 Unauthorized`.
- **Kết quả thực tế**: `403 Forbidden`
- **Kết quả mong đợi**: `401 Unauthorized`

---

## Đề xuất khắc phục

1. Xây dựng middleware `requireAdmin` và áp dụng cho tất cả endpoint yêu cầu quyền quản trị.
2. Thêm middleware xác thực cho nhóm endpoint `POST|PUT|DELETE /api/products/:id`.
3. Chuẩn hóa mã phản hồi lỗi `401 Unauthorized` khi token không hợp lệ/hết hạn.
