# Thiết Kế Kiểm Thử: Bảng Quyết Định và Pairwise (FR-12: Access Control)

Tài liệu này mô tả cách thiết kế kiểm thử cho FR-12 dựa trên hành vi mong đợi của chính sách phân quyền, sau đó đối chiếu với hành vi thực tế trong [server.js](file:///D:/HCMUS/Third%20Year/Software%20Testing/eshop-sut/backend/server.js).

Phạm vi tuần 4 tập trung vào các nhóm endpoint đại diện sau:

- `GET /api/products`: công khai (public), không yêu cầu token.
- `POST /api/cart`: endpoint cần xác thực, cho phép mọi user có token hợp lệ.
- `GET /api/admin/users`, `POST|PUT|DELETE /api/categories/:id`: endpoint mang tính chất admin, hiện tại có `authenticateToken` nhưng không có kiểm tra vai trò (role).
- `POST|PUT|DELETE /api/products/:id`: endpoint mang tính chất admin, hiện tại thiếu cả middleware xác thực.

---

## 1. Điều kiện và hành động

### 1.1. Các Điều Kiện (Conditions)

1. `C1 - Endpoint class` (Loại endpoint)
   - `E1`: Public endpoint (Endpoint công khai).
   - `E2`: Authenticated user endpoint (Endpoint yêu cầu đăng nhập).
   - `E3`: Admin endpoint (Endpoint yêu cầu quyền Admin).
2. `C2 - Token status` (Trạng thái Token)
   - `T1`: Missing (Không gửi token).
   - `T2`: Invalid or expired (Token hỏng hoặc hết hạn).
   - `T3`: Valid (Token hợp lệ).
3. `C3 - Role in valid token` (Vai trò trong token hợp lệ)
   - `R1`: `admin` (Hợp lệ)
   - `R2`: `user` (Người dùng thường)
   - `R3`: Malformed role (Sai định dạng vai trò), ví dụ: `admin ` (có khoảng trắng)
   - `R4`: Missing role claim (Token thiếu thông tin vai trò)

### 1.2. Các Hành Động (Actions)

- `A1`: Allow (Cho phép truy cập), HTTP `200/201`.
- `A2`: Reject unauthenticated (Từ chối do chưa xác thực), HTTP `401`.
- `A3`: Reject unauthorized (Từ chối do sai quyền hạn), HTTP `403`.

---

## 2. Bảng quyết định đầy đủ theo chính sách mong đợi (Full Decision Table)

Bảng này la cơ sở thiết kế test. Nó mô tả kết quả mong đợi theo chính sách kiểm soát truy cập (access control policy) đúng, không mô tả lỗi hiện tại của hệ thống (SUT).

| Điều kiện / Quy tắc | R01 | R02 | R03 | R04 | R05 | R06 | R07 | R08 | R09 | R10 | R11 | R12 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `C1 - Endpoint class` | E1 | E1 | E1 | E2 | E2 | E2 | E3 | E3 | E3 | E3 | E3 | E3 |
| `C2 - Token status` | T1 | T2 | T3 | T1 | T2 | T3 | T1 | T2 | T3 | T3 | T3 | T3 |
| `C3 - Role` | - | - | - | - | - | R1/R2/R3/R4 | - | - | R1 | R2 | R3 | R4 |
| **Hành động (Actions)** | | | | | | | | | | | | |
| `A1 - 200/201` | X | X | X |  |  | X |  |  | X |  |  |  |
| `A2 - 401` |  |  |  | X | X |  | X | X |  |  |  |  |
| `A3 - 403` |  |  |  |  |  |  |  |  |  | X | X | X |

**Giải thích:**
- `E1` là công khai, token có hay không đều không ảnh hưởng đến khả năng truy cập.
- `E2` yêu cầu token hợp lệ, nhưng không yêu cầu vai trò admin.
- `E3` yêu cầu token hợp lệ và vai trò bắt buộc phải là `admin`.

---

## 3. Bảng quyết định rút gọn (Reduced Decision Table)

| Quy tắc | Loại Endpoint | Trạng thái Token | Vai trò | Kết quả mong đợi |
| :--- | :--- | :--- | :--- | :--- |
| `Rule 1` | `E1` | `T1/T2/T3` | `-` | `200/201` |
| `Rule 2` | `E2` | `T1/T2` | `-` | `401` |
| `Rule 3` | `E2` | `T3` | `R1/R2/R3/R4` | `200/201` |
| `Rule 4` | `E3` | `T1/T2` | `-` | `401` |
| `Rule 5` | `E3` | `T3` | `R1` | `200/201` |
| `Rule 6` | `E3` | `T3` | `R2/R3/R4` | `403` |

---

## 4. Ánh xạ Endpoint thực tế trong bài (Mapping Endpoints)

| Endpoint cụ thể | Loại Endpoint | Hành vi thực tế trong `server.js` | Ghi chú |
| :--- | :--- | :--- | :--- |
| `GET /api/products` | `E1` | Không có middleware xác thực | Đúng với chính sách công khai |
| `POST /api/cart` | `E2` | Có middleware `authenticateToken` | Đúng với chính sách yêu cầu đăng nhập |
| `GET /api/admin/users` | `E3` | Chỉ có middleware `authenticateToken` | **LỖI**: Thiếu kiểm tra vai trò admin |
| `POST /api/categories` | `E3` | Chỉ có middleware `authenticateToken` | **LỖI**: Thiếu kiểm tra vai trò admin |
| `PUT /api/categories/:id` | `E3` | Chỉ có middleware `authenticateToken` | **LỖI**: Thiếu kiểm tra vai trò admin |
| `DELETE /api/categories/:id`| `E3` | Chỉ có middleware `authenticateToken` | **LỖI**: Thiếu kiểm tra vai trò admin |
| `POST /api/products` | `E3` | Không có middleware xác thực | **LỖI**: Thiếu cả xác thực và phân quyền |
| `PUT /api/products/:id` | `E3` | Không có middleware xác thực | **LỖI**: Thiếu cả xác thực và phân quyền |
| `DELETE /api/products/:id` | `E3` | Không có middleware xác thực | **LỖI**: Thiếu cả xác thực và phân quyền |

---

## 5. Thiết kế phối hợp cặp (Pairwise Design)

### 5.1. Tham số độc lập

Để đảm bảo thuật toán Pairwise hoạt động chính xác, các tham số đầu vào được định nghĩa độc lập:

1. `P_ENDPOINT_CLASS`: `E1_Public`, `E2_AuthUser`, `E3_Admin`
2. `P_TOKEN_STATUS`: `Missing` (Không gửi), `Invalid` (Không hợp lệ), `Valid` (Hợp lệ)
3. `P_ROLE`: `Admin`, `User`, `AdminWithSpace` (`admin `), `None` (Không có)
4. `P_METHOD_KIND`: `Read` (Đọc/GET), `Create` (Tạo/POST), `UpdateDelete` (Sửa/Xóa - PUT/DELETE)

### 5.2. Ràng buộc ánh xạ thực tế

- Nếu `P_TOKEN_STATUS != Valid` thì `P_ROLE` chỉ là giá trị kỹ thuật để bao phủ cặp kiểm thử, không tham gia quyết định logic (Don't care).
- `E1_Public` được ánh xạ với endpoint đọc danh sách, sử dụng `GET /api/products`.
- `E2_AuthUser` được ánh xạ với endpoint giỏ hàng, sử dụng `POST /api/cart`.
- `E3_Admin` được ánh xạ với các endpoint của Admin. Endpoint cụ thể được chọn dựa trên loại phương thức `P_METHOD_KIND`:
  - `Read` $\rightarrow$ `GET /api/admin/users`
  - `Create` $\rightarrow$ `POST /api/categories` hoặc `POST /api/products`
  - `UpdateDelete` $\rightarrow$ `PUT/DELETE /api/categories/:id` hoặc `PUT/DELETE /api/products/:id`

### 5.3. Bộ Pairwise 12 cấu hình đề xuất

| PW | Loại Endpoint | Trạng thái Token | Vai trò | Loại Phương thức | Kết quả mong đợi theo chính sách |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `PW01` | `E1_Public` | `Missing` | `Admin` | `Read` | `200` |
| `PW02` | `E1_Public` | `Invalid` | `User` | `Read` | `200` |
| `PW03` | `E1_Public` | `Valid` | `AdminWithSpace` | `Read` | `200` |
| `PW04` | `E2_AuthUser` | `Missing` | `None` | `Create` | `401` |
| `PW05` | `E2_AuthUser` | `Invalid` | `Admin` | `Create` | `401` |
| `PW06` | `E2_AuthUser` | `Valid` | `User` | `Create` | `200` |
| `PW07` | `E3_Admin` | `Missing` | `AdminWithSpace` | `Read` | `401` |
| `PW08` | `E3_Admin` | `Invalid` | `None` | `Create` | `401` |
| `PW09` | `E3_Admin` | `Valid` | `Admin` | `Read` | `200` |
| `PW10` | `E3_Admin` | `Valid` | `User` | `UpdateDelete` | `403` |
| `PW11` | `E3_Admin` | `Valid` | `AdminWithSpace` | `Create` | `403` |
| `PW12` | `E3_Admin` | `Valid` | `None` | `UpdateDelete` | `403` |

**Lý do chọn 12 cấu hình này:**
- Đảm bảo bao phủ 100% các cặp giá trị quan trọng giữa `Loại Endpoint`, `Trạng thái Token`, và `Vai trò`.
- Loại bỏ các tổ hợp mâu thuẫn nghiệp vụ thực tế giữa Đường dẫn (Path) và Phương thức (Method).
- Thuận tiện để ánh xạ trực tiếp sang các endpoint thực tế khi thiết kế kịch bản chi tiết.
