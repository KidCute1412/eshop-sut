# Danh Sách Các Kịch Bản Kiểm Thử (Test Cases) - FR-12: Access Control

Tài liệu này được sinh từ bảng quyết định và cấu hình pairwise trong tài liệu thiết kế [test_design.md](file:///D:/HCMUS/Third%20Year/Software%20Testing/eshop-sut/decision_table_week4/test_design/test_design.md). Mỗi ca kiểm thử đều được ánh xạ rõ ràng để đảm bảo độ bao phủ.

---

## 1. Các Ca Kiểm Thử Sinh Ra Từ Bảng Quyết Định (Decision Table Test Cases)

| Mã Test Case | Quy tắc Ánh xạ | Endpoint cụ thể | Trạng thái Token đầu vào | Vai trò trong Token | Kết quả mong đợi theo chính sách | Kết quả thực tế của SUT | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| `FR12-DT-01` | `Rule 1` | `GET /api/products` | Không gửi token | - | `200 OK` | `200 OK` | **Pass** |
| `FR12-DT-02` | `Rule 2` | `POST /api/cart` | Không gửi token | - | `401 Unauthorized` | `401 Unauthorized` | **Pass** |
| `FR12-DT-03` | `Rule 2` | `POST /api/cart` | Token không hợp lệ | - | `401 Unauthorized` | `403 Forbidden` | **Fail** |
| `FR12-DT-04` | `Rule 3` | `POST /api/cart` | Token hợp lệ | `user` | `200 OK` | `200 OK` | **Pass** |
| `FR12-DT-05` | `Rule 4` | `GET /api/admin/users`| Không gửi token | - | `401 Unauthorized` | `401 Unauthorized` | **Pass** |
| `FR12-DT-06` | `Rule 4` | `GET /api/admin/users`| Token không hợp lệ | - | `401 Unauthorized` | `403 Forbidden` | **Fail** |
| `FR12-DT-07` | `Rule 5` | `GET /api/admin/users`| Token hợp lệ | `admin` | `200 OK` | `200 OK` | **Pass** |
| `FR12-DT-08` | `Rule 6` | `GET /api/admin/users`| Token hợp lệ | `user` | `403 Forbidden` | `200 OK` | **Fail** |
| `FR12-DT-09` | `Rule 6` | `GET /api/admin/users`| Token hợp lệ | `admin ` (dấu cách) | `403 Forbidden` | `200 OK` | **Fail** |
| `FR12-DT-10` | `Rule 6` | `GET /api/admin/users`| Token hợp lệ | Không có vai trò | `403 Forbidden` | `200 OK` | **Fail** |
| `FR12-DT-11` | `Rule 4` | `POST /api/products` | Không gửi token | - | `401 Unauthorized` | `200 OK` | **Fail** |
| `FR12-DT-12` | `Rule 6` | `PUT /api/categories/1` | Token hợp lệ | `user` | `403 Forbidden` | `200 OK` | **Fail** |

**Ghi chú:**
- Mã lỗi `403 Forbidden` trả về cho trường hợp token không hợp lệ (không phải do sai quyền hạn) là hành vi thực tế của middleware `authenticateToken` trong mã nguồn, nhưng không khớp với thiết kế chuẩn (policy mong đợi là `401`).
- Các ca kiểm thử từ `DT-08` đến `DT-12` phản ánh lỗi kiểm soát truy cập thực tế của hệ thống.

---

## 2. Các Ca Kiểm Thử Sinh Ra Từ Phối Hợp Cặp (Pairwise Test Cases)

| Mã Test Case | Cấu hình PW | Endpoint thực thi | Trạng thái Token | Vai trò trong Token | Kết quả mong đợi theo chính sách | Kết quả thực tế của SUT | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| `FR12-PW-01` | `PW01` | `GET /api/products` | Không gửi token | `admin` | `200 OK` | `200 OK` | **Pass** |
| `FR12-PW-02` | `PW02` | `GET /api/products` | Không hợp lệ | `user` | `200 OK` | `200 OK` | **Pass** |
| `FR12-PW-03` | `PW03` | `GET /api/products` | Hợp lệ | `admin ` (dấu cách) | `200 OK` | `200 OK` | **Pass** |
| `FR12-PW-04` | `PW04` | `POST /api/cart` | Không gửi token | Không có | `401 Unauthorized` | `401 Unauthorized` | **Pass** |
| `FR12-PW-05` | `PW05` | `POST /api/cart` | Không hợp lệ | `admin` | `401 Unauthorized` | `403 Forbidden` | **Fail** |
| `FR12-PW-06` | `PW06` | `POST /api/cart` | Hợp lệ | `user` | `200 OK` | `200 OK` | **Pass** |
| `FR12-PW-07` | `PW07` | `GET /api/admin/users`| Không gửi token | `admin ` | `401 Unauthorized` | `401 Unauthorized` | **Pass** |
| `FR12-PW-08` | `PW08` | `POST /api/categories` | Không hợp lệ | Không có | `401 Unauthorized` | `403 Forbidden` | **Fail** |
| `FR12-PW-09` | `PW09` | `GET /api/admin/users`| Hợp lệ | `admin` | `200 OK` | `200 OK` | **Pass** |
| `FR12-PW-10` | `PW10` | `PUT /api/categories/1` | Hợp lệ | `user` | `403 Forbidden` | `200 OK` | **Fail** |
| `FR12-PW-11` | `PW11` | `POST /api/categories` | Hợp lệ | `admin ` | `403 Forbidden` | `200 OK` | **Fail** |
| `FR12-PW-12` | `PW12` | `DELETE /api/products/1`| Hợp lệ | Không có | `403 Forbidden` | `200 OK` | **Fail** |

---

## 3. Độ Bao Phủ Các Lỗi Chính (Vulnerability Coverage Mapping)

| Lỗi phát hiện | Ca kiểm thử bao phủ |
| :--- | :--- |
| Endpoint của Admin không kiểm tra vai trò (BUG-01, BUG-02, BUG-03, BUG-04) | `FR12-DT-08`, `FR12-DT-09`, `FR12-DT-10`, `FR12-DT-12`, `FR12-PW-10`, `FR12-PW-11` |
| Endpoint sửa đổi Sản phẩm thiếu middleware xác thực (BUG-05, BUG-06) | `FR12-DT-11`, `FR12-PW-12` |
| Hệ thống trả về `403` thay vì `401` khi token hỏng | `FR12-DT-03`, `FR12-DT-06`, `FR12-PW-05`, `FR12-PW-08` |
