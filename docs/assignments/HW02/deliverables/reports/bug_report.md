# Bug Report

This document records the details of all bugs discovered during Domain and Boundary Value Analysis testing. 
*Note: Make sure to submit these on your group's GitHub Issues page and attach the corresponding screenshots.*

---

## Bug List Summary

| Bug ID | Feature | Title | Severity | Status | GitHub Issue Link |
| :--- | :--- | :--- | :--- | :--- | :--- |
| BUG-001 | FR-10 | Người dùng thường (User) tự hủy được đơn hàng đang ở trạng thái đang giao (shipping) | High | Open | |
| BUG-002 | FR-10 | Cho phép chuyển trạng thái đơn hàng đã hủy (canceled) sang trạng thái đã giao (delivered) | High | Open | |
| BUG-003 | FR-12 | Người dùng thường (User) truy cập trái phép lấy danh sách tài khoản từ API Admin | Critical | Open | |
| BUG-004 | FR-12 | Người dùng thường (User) cập nhật danh mục sản phẩm thành công qua API Admin | Critical | Open | |
| BUG-005 | FR-12 | Khách vãng lai (Guest) tạo sản phẩm mới thành công không cần token xác thực | Critical | Open | |
| BUG-006 | FR-23 | Lỗi bất đồng bộ dữ liệu UI và giỏ hàng khi nhập số lượng <= 0 trên Mobile | High | Open | |
| BUG-007 | FR-23 | Lỗi tự động làm tròn số lượng thập phân không cảnh báo trên Mobile | High | Open | |
| BUG-008 | FR-23 | Lỗi tự động thêm số lượng bằng 1 khi để trống ô nhập liệu trên Mobile | High | Open | |

---

## Detailed Bug Reports

### BUG-001: Người dùng thường (User) tự hủy được đơn hàng đang giao (shipping)
* **Feature**: FR-10 (Order State Machine)
* **Description**: Theo sơ đồ máy trạng thái và ràng buộc quyền hạn, khi đơn hàng đã chuyển sang trạng thái đang giao (`shipping`), người dùng thường (User) không được phép tự hủy đơn hàng, nút hủy phải bị ẩn/vô hiệu hóa ở phía Client và API của Backend phải từ chối yêu cầu hủy. Tuy nhiên, hệ thống cho phép User thực hiện hủy thành công đơn hàng đang giao và Backend trả về kết quả cập nhật trạng thái đơn hàng thành `canceled`.
* **Steps to Reproduce**:
  1. Đăng nhập vào trang Admin (`admin@eshop.com` / `Admin123!`).
  2. Tìm một đơn hàng ở trạng thái `pending` hoặc `confirmed`, chuyển trạng thái của đơn hàng đó sang `shipping`.
  3. Đăng nhập vào trang Frontend Client với tài khoản người dùng thường của đơn hàng đó.
  4. Truy cập vào trang Lịch sử đơn hàng (Order History).
  5. Tìm đơn hàng vừa được chuyển sang `shipping`, thấy nút "Hủy đơn hàng" vẫn khả dụng. Click chọn nút này.
  6. Đơn hàng bị cập nhật trạng thái thành "Đã hủy" (`canceled`) thành công.
* **Expected Result**: Nút "Hủy đơn hàng" không xuất hiện đối với đơn hàng đang ở trạng thái `shipping` trong giao diện lịch sử đơn hàng của User. Nếu có request gửi thủ công lên API Backend để hủy đơn hàng `shipping` từ tài khoản User thường, hệ thống phải từ chối và trả về mã lỗi `400 Bad Request`.
* **Actual Result**: User vẫn có nút hủy đơn hàng, bấm hủy thành công và backend cập nhật trạng thái đơn hàng sang `canceled` mà không có cơ chế ngăn chặn nào.
* **Screenshots**:
  ![Lỗi User tự hủy đơn hàng khi đang giao](images/fr10-DT05-fail.png)

### BUG-002: Cho phép chuyển trạng thái đơn hàng đã hủy (canceled) sang đã giao (delivered)
* **Feature**: FR-10 (Order State Machine)
* **Description**: Theo sơ đồ máy trạng thái, trạng thái "Đã hủy" (`canceled`) là một trạng thái kết thúc (Final State). Sau khi đơn hàng đã ở trạng thái kết thúc, hệ thống không được phép thực hiện bất kỳ hành động chuyển tiếp trạng thái nào khác. Tuy nhiên, giao diện của Admin vẫn hiển thị nút "Đánh dấu Đã giao" đối với đơn hàng có trạng thái "Đã hủy", và khi bấm cập nhật, hệ thống vẫn cho phép đổi trạng thái thành "Đã giao" (`delivered`) thành công.
* **Steps to Reproduce**:
  1. Đăng nhập vào trang Admin (`admin@eshop.com` / `Admin123!`).
  2. Truy cập vào trang Quản lý đơn hàng (Order Management).
  3. Tìm một đơn hàng đang ở trạng thái "Đã hủy" (`canceled`).
  4. Nhìn sang cột "Hành động", thấy nút "Đánh dấu Đã giao" vẫn hiển thị. Click chọn nút này.
  5. Trạng thái đơn hàng bị cập nhật trái phép thành "Đã giao" (`delivered`) thành công.
* **Expected Result**: Giao diện Quản lý Đơn hàng của Admin không hiển thị bất kỳ nút cập nhật trạng thái nào ở cột Hành động khi đơn hàng đã ở trạng thái kết thúc (`canceled` hoặc `delivered`). API Backend cũng cần validate để chặn việc thay đổi trạng thái từ trạng thái kết thúc và trả về `400 Bad Request`.
* **Actual Result**: Hệ thống vẫn hiển thị nút "Đánh dấu Đã giao" và cho phép Admin cập nhật đổi trạng thái từ `canceled` sang `delivered` thành công.
* **Screenshots**:
  ![Lỗi Admin chuyển trạng thái từ canceled sang delivered](images/fr10-BVA04-fail.png)

### BUG-003: Người dùng thường (User) truy cập trái phép lấy danh sách tài khoản từ API Admin
* **Feature**: FR-12 (Access Control)
* **Description**: Middleware `authenticateToken` ở backend chỉ kiểm tra tính hợp lệ của token JWT (signature và expiration) chứ hoàn toàn không kiểm tra giá trị của trường vai trò (`req.user.role === 'admin'`). Do đó, người dùng thường có JWT token hợp lệ vẫn có thể gửi request truy cập vào API Admin và lấy danh sách thông tin nhạy cảm của tất cả các tài khoản khác.
* **Steps to Reproduce**:
  1. Đăng nhập tài khoản User thường qua API `POST /api/login` để lấy token JWT.
  2. Dùng Postman gửi request `GET /api/admin/users` kèm theo token vừa nhận được ở bước 1 trong Header Authorization.
  3. API trả về toàn bộ thông tin tài khoản người dùng của hệ thống với mã trạng thái `200 OK`.
* **Expected Result**: Hệ thống phải chặn request này và trả về mã trạng thái `403 Forbidden`.
* **Actual Result**: Hệ thống vẫn cho phép truy cập thành công và trả về dữ liệu danh sách người dùng.
* **Screenshots**:
  ![Lỗi User thường sử dụng token truy cập thành công API Admin](images/fr12-DT03-fail.png)

### BUG-004: Người dùng thường (User) cập nhật danh mục sản phẩm thành công qua API Admin
* **Feature**: FR-12 (Access Control)
* **Description**: Middleware backend bỏ sót việc kiểm tra vai trò admin khi cập nhật danh mục. Điều này cho phép tài khoản có quyền User thường gửi request chỉnh sửa danh mục sản phẩm của cửa hàng thành công.
* **Steps to Reproduce**:
  1. Đăng nhập tài khoản User thường qua API `POST /api/login` để lấy token JWT.
  2. Dùng Postman gửi request `PUT /api/categories/1` (cập nhật danh mục) kèm theo body request là tên danh mục mới và token ở bước 1 trong Header Authorization.
  3. Hệ thống cập nhật danh mục thành công và trả về mã trạng thái `200 OK`.
* **Expected Result**: Hệ thống từ chối và trả về mã trạng thái `403 Forbidden`.
* **Actual Result**: Hệ thống cập nhật danh mục thành công mà không có cảnh báo hay ngăn chặn nào.
* **Screenshots**:
  ![Lỗi User thường cập nhật danh mục sản phẩm thành công](images/fr12-DT04-fail.png)

### BUG-005: Khách vãng lai (Guest) tạo sản phẩm mới thành công không cần token xác thực
* **Feature**: FR-12 (Access Control)
* **Description**: API thêm mới sản phẩm (`POST /api/products`) hoàn toàn không khai báo middleware `authenticateToken` trong file `server.js`. Do đó, bất kỳ ai, kể cả khách vãng lai (không cần đăng nhập, không cần truyền token), vẫn có thể gửi request để thêm sản phẩm vào hệ thống.
* **Steps to Reproduce**:
  1. Mở Postman, cấu hình request `POST /api/products` với body JSON chứa thông tin sản phẩm mới (name, price, description, v.v.). Không đính kèm Header Authorization.
  2. Gửi request.
  3. Hệ thống tạo mới sản phẩm thành công và trả về mã trạng thái `200 OK`.
* **Expected Result**: Hệ thống phải từ chối truy cập và trả về mã lỗi `401 Unauthorized` vì đây là API quản trị của Admin.
* **Actual Result**: Hệ thống vẫn cho phép tạo sản phẩm mới thành công mà không cần token xác thực.
* **Screenshots**:
  ![Lỗi Guest tạo sản phẩm mới thành công không cần token](images/fr12-BVA02-fail.png)

### BUG-006: Lỗi bất đồng bộ dữ liệu UI và giỏ hàng khi nhập số lượng <= 0 trên Mobile
* **Feature**: FR-23 (Product detail view (mobile))
* **Description**: Khi người dùng nhập số lượng bằng `"0"` hoặc số âm trên ô nhập liệu ở màn hình chi tiết sản phẩm của thiết bị di động, giao diện UI vẫn hiển thị số nhập đó. Tuy nhiên, khi bấm nút "Thêm vào giỏ hàng", hàm `normalizeQuantity` trong `App.js` lại âm thầm chuyển đổi giá trị không hợp lệ này thành `1` và thực hiện thêm vào giỏ hàng thành công với số lượng là 1. Việc này làm sai lệch dữ liệu hiển thị (UI hiển thị 0 nhưng thực tế thêm vào giỏ hàng là 1).
* **Steps to Reproduce**:
  1. Chạy ứng dụng mobile và truy cập vào trang chi tiết của một sản phẩm bất kỳ.
  2. Tại ô nhập số lượng, nhập giá trị `0` (hoặc `-3`).
  3. Bấm nút "Thêm vào giỏ hàng". Giao diện hiển thị Alert thông báo "Thành công - Đã thêm vào giỏ hàng".
  4. Mở giỏ hàng kiểm tra, thấy sản phẩm được thêm thành công với số lượng là 1 (mặc dù ô nhập bên ngoài đang hiển thị 0).
* **Expected Result**: Hệ thống phải từ chối hoặc reset ô nhập về 1 khi người dùng nhập số lượng nhỏ hơn 1, tránh trường hợp UI hiển thị số 0 nhưng giỏ hàng vẫn nhận số lượng là 1.
* **Actual Result**: Ứng dụng vẫn báo thêm thành công và tăng số lượng trong giỏ lên 1 mặc dù trên ô nhập UI hiển thị 0.
* **Screenshots**:
  ![Lỗi thêm số lượng bằng 0 nhưng giỏ hàng tăng lên 1 (FR23-DT-03)](images/fr23-DT03-fail.png)

### BUG-007: Lỗi tự động làm tròn số lượng thập phân không cảnh báo trên Mobile
* **Feature**: FR-23 (Product detail view (mobile))
* **Description**: Khi người dùng nhập số lượng là một số thập phân (ví dụ: `2.5`) trên giao diện chi tiết sản phẩm của thiết bị di động, hệ thống vẫn cho phép bấm nút "Thêm vào giỏ hàng" và thông báo thành công. Tuy nhiên, hệ thống tự động làm tròn xuống giá trị này thành `2` khi lưu vào giỏ hàng mà không hiển thị bất kỳ cảnh báo hay thông báo nào cho người dùng biết.
* **Steps to Reproduce**:
  1. Chạy ứng dụng mobile và mở chi tiết một sản phẩm bất kỳ.
  2. Tại ô nhập số lượng, nhập `2.5`.
  3. Bấm nút "Thêm vào giỏ hàng". Giao diện thông báo thêm thành công.
  4. Mở giỏ hàng kiểm tra, thấy sản phẩm được thêm với số lượng là 2 (bị làm tròn xuống) mà không có bất kỳ thông báo lỗi hay thông tin cảnh báo về việc làm tròn.
* **Expected Result**: Hệ thống từ chối nhận số thập phân (báo lỗi đầu vào không hợp lệ) hoặc hiển thị cảnh báo cho người dùng trước khi thực hiện làm tròn số lượng.
* **Actual Result**: Hệ thống chấp nhận số thập phân nhập vào, tự động làm tròn xuống mà không hiển thị bất kỳ cảnh báo nào.
* **Screenshots**:
  ![Lỗi nhập số lượng 2.5 bị làm tròn thành 2 (FR23-DT-04)](images/fr23-DT04-fail.png)

### BUG-008: Lỗi tự động thêm số lượng bằng 1 khi để trống ô nhập liệu trên Mobile
* **Feature**: FR-23 (Product detail view (mobile))
* **Description**: Khi người dùng xóa trống ô nhập liệu số lượng (state `quantity` rỗng `""`) trên giao diện chi tiết sản phẩm của thiết bị di động, hệ thống vẫn cho phép bấm nút "Thêm vào giỏ hàng" và thông báo thành công. Tuy nhiên, hệ thống tự động gán giá trị mặc định là `1` để thêm vào giỏ hàng mà không hiển thị bất kỳ cảnh báo lỗi hay yêu cầu người dùng nhập lại giá trị hợp lệ trên giao diện.
* **Steps to Reproduce**:
  1. Chạy ứng dụng mobile và mở chi tiết một sản phẩm bất kỳ.
  2. Tại ô nhập số lượng, xóa trắng toàn bộ ký tự (ô nhập trống `""`).
  3. Bấm nút "Thêm vào giỏ hàng". Giao diện hiển thị Alert thông báo thành công.
  4. Mở giỏ hàng kiểm tra, thấy sản phẩm được thêm thành công với số lượng là 1.
* **Expected Result**: Hệ thống phải ngăn chặn hành động thêm vào giỏ hàng và báo lỗi yêu cầu người dùng nhập số lượng hợp lệ khi trường số lượng bị bỏ trống.
* **Actual Result**: Hệ thống vẫn báo thêm thành công và tự gán số lượng bằng 1 vào giỏ hàng.
* **Screenshots**:
  ![Lỗi để trống số lượng nhưng vẫn thêm thành công là 1 (FR23-DT-05)](images/fr23-DT05-fail.png)

