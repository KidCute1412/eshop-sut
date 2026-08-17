# HW02 – Domain Testing trên hệ thống EShop



# 1. Thông tin sinh viên và môn học

| Mục | Thông tin |
| --- | --- |
| Môn học | Kiểm thử phần mềm |
| Bài tập | HW02 – Domain Testing |
| Lớp | 23KTPM3 |
| Mã số sinh viên | 23127296 |
| Họ và tên | Nguyễn Thành Luân |

---

# 3. Tổng quan hệ thống được kiểm thử

## 3.1 Thông tin hệ thống

| Mục | Thông tin |
| --- | --- |
| Tên hệ thống | `EShop` |
| Repository | `https://github.com/ttbhanh/eshop-sut` |
| Môi trường kiểm thử | `Local`|

## 3.2 Môi trường kiểm thử

| Mục | Thông tin |
| --- | --- |
| Hệ điều hành | `Windows` |
| Trình duyệt | `Chrome phiên bản 149.0.7827.115` |
| Công cụ kiểm thử API | `Postman` |
| Công cụ kiểm thử UI | `Thủ công` |

---

# 4. Các tính năng được chọn

| Nhóm tính năng | Mã tính năng | Tên tính năng |
| --- | --- | --- |
| Pool A | `FR-03` | `Forgot password and password reset (two steps)` |
| Pool B | `FR-09` | `Discount coupons` |
| Pool C | `FR-13` | `Dashboard` |
| Pool D | `FR-03(Mobile)` | `Mobile: Forgot password and password reset (two steps)` |

---

# 5. Cơ sở kiểm thử và quy trình kiểm thử

## 5.2 Cơ sở kiểm thử

| Basis ID | Nguồn | Vị trí | 
| --- | --- | --- |
| `BASIS-01` | `GitHub Repository` | `https://github.com/ttbhanh/eshop-sut` | 
| `BASIS-02` | `Frontend Web` | `http://localhost:5173/` | 
| `BASIS-03` | `API` | `http://localhost:3000/` | 
| `BASIS-04` | `Frontend Admin` | `http://localhost:5174/` | 

## 5.3 Quy trình kiểm thử chung

1. Xác định hành vi của tính năng và cơ sở kiểm thử.
2. Xác định biến đầu vào, điều kiện đầu ra, trạng thái, vai trò người dùng và ràng buộc.
3. Chia không gian đầu vào thành các miền hợp lệ và không hợp lệ.
4. Thiết kế test case Domain Testing từ các miền đã chia.
5. Xác định các biến có giá trị biên và các giá trị biên cần kiểm thử.
6. Thiết kế test case Boundary Value Analysis.
7. Thực thi test case bằng UI, API hoặc script.
8. Ghi nhận kết quả thực tế, minh chứng và trạng thái kiểm thử.
9. Báo cáo lỗi trong Markdown và GitHub Issues.
10. Review output do AI tạo và ghi nhận các thiếu sót của AI.

## 5.4 Định nghĩa trạng thái test case

| Trạng thái | Ý nghĩa |
| --- | --- |
| `Passed` | Kết quả thực tế khớp với kết quả mong đợi. |
| `Failed` | Kết quả thực tế không khớp với kết quả mong đợi. |
| `Blocked` | Không thể thực thi test case do lỗi môi trường hoặc phụ thuộc bên ngoài. |
| `Not Executed` | Test case đã được thiết kế nhưng chưa thực thi. |

---

# 6. Báo cáo tính năng FR-03

## 6.1 Mô tả tính năng

FR-03 là tính năng **quên mật khẩu và đặt lại mật khẩu** của hệ thống EShop. Tính năng này dành cho người dùng đã có tài khoản. Luồng chính gồm hai bước:

1. Người dùng truy cập trang `/forgot-password`, nhập email đã đăng ký và gửi yêu cầu đặt lại mật khẩu.
2. Hệ thống tạo mã OTP và hiển thị trên màn hình trong môi trường demo.
3. Người dùng nhập OTP và mật khẩu mới để hoàn tất đặt lại mật khẩu.
4. Nếu dữ liệu hợp lệ, hệ thống cập nhật mật khẩu mới và chuyển người dùng về trang đăng nhập.

## 6.2 Cơ sở kiểm thử riêng của tính năng

| Basis ID | Nguồn | Vị trí | Yêu cầu / Quy tắc | 
| --- | --- | --- | --- |
| `FR-03:C1` | `README.md` | FR-03, L50 | Người dùng nhập email đã đăng ký để yêu cầu đặt lại mật khẩu. | 
| `FR-03:C2` | `README.md` | FR-03, L51 | Hệ thống tạo OTP gồm 6 chữ số và hiển thị trên màn hình. | 
| `FR-03:C3` | `README.md` | FR-03, L52 | Giao diện phải hiển thị chỉ báo bước, ví dụ `Bước 1 / 2`. | 
| `FR-03:C4` | `README.md` | FR-03, L57–59 | Người dùng nhập OTP, mật khẩu mới và xác nhận mật khẩu mới. | 
| `FR-03:C5` | `README.md` | FR-03, L59 | Mật khẩu mới phải thỏa quy tắc FR-01: tối thiểu 8 ký tự, có chữ hoa, chữ thường, chữ số và ký tự đặc biệt `@$!%*?&`. | 
| `FR-03:C6` | `README.md` | FR-03, L60 | OTP chỉ hợp lệ với email đã yêu cầu đặt lại mật khẩu. | 

## 6.3 Domain Testing

### 6.3.1 Biến miền và ràng buộc

| Variable ID | Biến / Trạng thái | Kiểu  | Ràng buộc | Kết quả có thể quan sát | Basis ID |
| --- | --- | --- | --- | --- | --- |
| `FR03-VAR-01` | `email` | Chuỗi  | Bắt buộc nhập, đúng định dạng email và phải tồn tại trong hệ thống để tạo OTP thành công. | Hiển thị OTP/reset token nếu email hợp lệ và đã đăng ký; hiển thị lỗi nếu email không tồn tại hoặc bỏ trống. | `FR-03:C1` |
| `FR03-VAR-02` | `resetToken`  | Chuỗi  | OTP phải khớp với token đang lưu cho đúng email. Theo đặc tả là 6 chữ số, nhưng backend thực tế dùng OTP 4 chữ số `1000–9999`. | Đặt lại mật khẩu thành công nếu OTP đúng; trả lỗi nếu OTP sai, ngoài miền hoặc thuộc email khác. | `FR-03:C2`, `FR-03:C6` |
| `FR03-VAR-03` | `newPassword` | Chuỗi  | Theo đặc tả, mật khẩu phải có ít nhất 8 ký tự, gồm chữ hoa, chữ thường, chữ số và ký tự đặc biệt. | Mật khẩu mạnh được chấp nhận; mật khẩu yếu phải bị từ chối. | `FR-03:C5` |
| `FR03-VAR-04` | `confirmPassword` | Chuỗi | Phải tồn tại trên form bước 2 và phải trùng với `newPassword`. | Nếu trùng thì tiếp tục đặt lại mật khẩu; nếu không trùng thì hiển thị lỗi. Hiện tại UI thiếu trường này. | `FR-03:C4` |
| `FR03-VAR-05` | `Trạng thái bước của form` | Trạng thái UI | Phải hiển thị đúng bước hiện tại | Giao diện hiển thị đúng chỉ báo bước `Bước 1 / 2`. | `FR-03:C3` |

### 6.3.2 Miền hợp lệ và không hợp lệ

| Domain ID | Biến | Loại miền | Định nghĩa miền | Hành vi mong đợi | Basis ID |
| --- | --- | --- | --- | --- | --- |
| `FR03-D-V-01` | `email` | Hợp lệ | Email đúng định dạng và đã đăng ký, ví dụ `gmail.com`. | Hệ thống tạo OTP/reset token và chuyển sang bước đặt lại mật khẩu. | `FR-03:C1` |
| `FR03-D-I-01` | `email` | Không hợp lệ | Email đúng định dạng nhưng chưa đăng ký, ví dụ `nonexistent@test.com`. | Hệ thống từ chối và báo lỗi `User not found`. | `FR-03:C1` |
| `FR03-D-I-02` | `email` | Không hợp lệ | Email bị bỏ trống hoặc không được gửi. | Giao diện HTML5 chặn submit hoặc backend trả lỗi. | `FR-03:C1` |
| `FR03-D-V-02` | `resetToken` | Hợp lệ | OTP khớp với token đã tạo cho cùng email. | Hệ thống cho phép đặt lại mật khẩu nếu mật khẩu mới hợp lệ. | `FR-03:C6` |
| `FR03-D-I-03` | `resetToken` | Không hợp lệ | OTP không khớp với token đã lưu, ví dụ `0000`. | Hệ thống từ chối và báo lỗi token/email không hợp lệ. | `FR-03:C6` |
| `FR03-D-I-04` | `resetToken` | Không hợp lệ | OTP được tạo cho email khác, ví dụ dùng OTP của admin cho tài khoản customer. | Hệ thống từ chối vì OTP không thuộc email yêu cầu. | `FR-03:C6` |
| `FR03-D-V-03` | `newPassword` | Hợp lệ | Mật khẩu thỏa FR-01, ví dụ `NewPass123!`. | Hệ thống chấp nhận mật khẩu mới và đặt lại mật khẩu thành công. | `FR-03:C5` |
| `FR03-D-I-05` | `newPassword` | Không hợp lệ | Mật khẩu yếu, thiếu độ dài hoặc thiếu nhóm ký tự bắt buộc, ví dụ `weak`. | Hệ thống phải từ chối mật khẩu yếu. | `FR-03:C5` |
| `FR03-D-V-04` | `confirmPassword` | Hợp lệ | Trường xác nhận mật khẩu tồn tại và giá trị trùng với mật khẩu mới. | Form cho phép gửi yêu cầu đặt lại mật khẩu. | `FR-03:C4` |
| `FR03-D-I-06` | `confirmPassword` | Không hợp lệ | Trường xác nhận mật khẩu bị thiếu hoặc không trùng với mật khẩu mới. | Form phải hiển thị lỗi hoặc không cho gửi. Hiện tại UI thiếu trường này. | `FR-03:C4` |
| `FR03-D-V-05` | `Trạng thái bước của form` | Hợp lệ | Bước 1 hoặc 2 đúng với giao diện | Form hiển thị số bước chính xác | `FR-03:C3` |
| `FR03-D-I-07` | `Trạng thái bước của form` | Không hợp lệ | Không đúng với giao diện hoặc quá lớn | Form phải hiển thị lỗi chỉ báo bước sai hoặc thiếu. | `FR-03:C3` |

### 6.3.3 Test case Domain Testing

| Test Case ID | Domain ID liên quan | Tiêu đề | Điều kiện tiên quyết | Dữ liệu đầu vào | Các bước thực hiện | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Minh chứng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `FR03-DT-01` | `FR03-D-V-01` | Yêu cầu đặt lại mật khẩu với email đã đăng ký | SUT đang chạy; tài khoản `gmail` tồn tại. | `email = gmail` | 1. Mở `/forgot-password`.<br>2. Nhập email đã đăng ký.<br>3. Gửi yêu cầu. | Hệ thống tạo OTP/reset token và hiển thị trên màn hình. | API trả `{"message":"Mã đặt lại mật khẩu đã được tạo","resetToken":"5143"}`. | Passed | `evidence/FR-03/FR03-DT-01.png` |
| `FR03-DT-02` | `FR03-D-I-01` | Yêu cầu đặt lại mật khẩu với email chưa đăng ký | SUT đang chạy. | `email = hello@gmail` | 1. Mở `/forgot-password`.<br>2. Nhập email chưa đăng ký.<br>3. Gửi yêu cầu. | Hệ thống từ chối và báo lỗi người dùng không tồn tại. | Hệ thống trả `{"error":"User not found"}` với HTTP 404. | Passed | `evidence/FR-03/FR03-DT-02.png` |
| `FR03-DT-03` | `FR03-D-I-02` | Bỏ trống email khi yêu cầu đặt lại mật khẩu | SUT đang chạy; kiểm thử cần thực hiện qua UI. | `email = empty` | 1. Mở `/forgot-password`.<br>2. Để trống email.<br>3. Nhấn submit. | Trình duyệt hoặc hệ thống chặn submit và yêu cầu nhập email. | Hệ thống yêu cầu điền vào trường | Passed | `evidence/FR-03/FR03-DT-03.png` |
| `FR03-DT-04` | `FR03-D-V-01`, `FR03-D-V-02`, `FR03-D-V-03` | Đặt lại mật khẩu thành công với email, OTP và mật khẩu mạnh hợp lệ | Đã tạo OTP cho `gmail`. | `email = gmail`<br>`resetToken = 7508`<br>`newPassword = NewPass123!` | 1. Gửi yêu cầu quên mật khẩu để lấy OTP.<br>2. Nhập đúng OTP.<br>3. Nhập mật khẩu mới mạnh.<br>4. Gửi yêu cầu đặt lại mật khẩu. | Hệ thống đặt lại mật khẩu thành công và chuyển về trang đăng nhập. | Hệ thống báo "Mật khẩu quá yếu!" | Failed | `evidence/FR-03/FR03-DT-04.png` |
| `FR03-DT-05` | `FR03-D-I-03` | Đặt lại mật khẩu với OTP sai | Đã có email hợp lệ. | `email = gmail`<br>`resetToken = 0000`<br>`newPassword = Password 1` | 1. Nhập email hợp lệ.<br>2. Nhập OTP sai.<br>3. Nhập mật khẩu mạnh.<br>4. Gửi yêu cầu đặt lại mật khẩu. | Hệ thống từ chối OTP sai. | API trả `{"error":"Invalid token or email"}` với HTTP 400. | Passed | `evidence/FR-03/FR03-DT-05.png` |
| `FR03-DT-06` | `FR03-D-I-05` | Đặt lại mật khẩu với mật khẩu yếu | Đã tạo OTP hợp lệ cho `gmail`. | `email = gmail`<br>`resetToken = 2420`<br>`newPassword = weak` | 1. Tạo OTP hợp lệ.<br>2. Nhập OTP đúng.<br>3. Nhập mật khẩu yếu.<br>4. Gửi yêu cầu đặt lại mật khẩu thông qua API. | Hệ thống phải từ chối mật khẩu yếu. | API trả `{"message":"Password reset successfully"}` — backend chấp nhận mật khẩu yếu. | Failed | `evidence/FR-03/FR03-DT-06.png` |
| `FR03-DT-07` | `FR03-D-I-04` | Dùng OTP của email khác để đặt lại mật khẩu | Có OTP được tạo từ tài khoản admin. | `email = gmail`<br>`resetToken = 6480` từ admin<br>`newPassword = Password 1!` | 1. Tạo OTP cho tài khoản admin.<br>2. Dùng OTP đó cho email `gmail`.<br>3. Gửi yêu cầu đặt lại mật khẩu. | Hệ thống từ chối vì OTP không thuộc email hiện tại. | API trả `{"error":"Invalid token or email"}` với HTTP 400. | Passed | `evidence/FR-03/FR03-DT-07.png` |
| `FR03-DT-08` | `FR03-D-V-05` | Reset mật khẩu | SUT đang chạy |  | 1. Nhấn vào Quên mật khẩu ? <br> 2. Quan sát chỉ báo bước. | Hệ thống hiển thị chỉ báo bước đúng | Không thấy chỉ báo bước | Failed | `evidence/FR-03/FR03-DT-08.png` |

### 6.3.4 Tổng kết Domain Testing

| Chỉ số | Số lượng |
| --- | ---: |
| Tổng số test case Domain Testing | 8 |
| Passed | 5 |
| Failed | 3 |
| Blocked | 0 |
| Not Executed | 0 |

## 6.4 Boundary Value Analysis

### 6.4.1 Biến có giá trị biên

| Boundary Variable ID | Biến | Quy tắc biên | Giá trị nhỏ nhất | Giá trị lớn nhất | Giá trị bình thường | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| `FR03-BVAR-01` | `resetToken` | nằm trong khoảng `100000–999999`. | `100000` | `999999` | OTP hợp lệ được tạo từ bước 1 | Không có |
| `FR03-BVAR-02` | độ dài `newPassword`  | Mật khẩu phải có tối thiểu 8 ký tự. | `8 ký tự` | Không rõ | `NewPass123!` | Không có |
| `FR03-BVAR-03` | `OTP`  | nằm trong khoảng `100000–999999` | `100000` | `999999` | Giá trị OTP được tạo ngẫu nhiên trong khoảng hợp lệ | Không có |

### 6.4.2 Giá trị biên

| Boundary ID | Biến | Loại biên | Giá trị | Hành vi mong đợi | Basis ID |
| --- | --- | --- | --- | --- | --- |
| `FR03-B-001` | `resetToken` | `min-1` | `99999` | Bị từ chối vì nhỏ hơn miền OTP thực tế. | `FR-03:C2`, `FR-03:C6` |
| `FR03-B-002` | `resetToken` | `min` | `100000` | Được chấp nhận nếu đúng là token đang lưu cho email. | `FR-03:C2`, `FR-03:C6` |
| `FR03-B-003` | `resetToken` | `min+1` | `100001` | Được chấp nhận nếu đúng là token đang lưu cho email. | `FR-03:C2`, `FR-03:C6` |
| `FR03-B-004` | `resetToken` | `max-1` | `999998` | Được chấp nhận nếu đúng là token đang lưu cho email. | `FR-03:C2`, `FR-03:C6` |
| `FR03-B-005` | `resetToken` | `max` | `999999` | Được chấp nhận nếu đúng là token đang lưu cho email. | `FR-03:C2`, `FR-03:C6` |
| `FR03-B-006` | `resetToken` | `max+1` | `1000000` | Bị từ chối vì lớn hơn miền OTP thực tế. | `FR-03:C2`, `FR-03:C6` |
| `FR03-B-007` | `newPassword` length | `min-1` | 7 ký tự, ví dụ `Abc1!xy` | Bị từ chối vì ngắn hơn 8 ký tự. | `FR-03:C5` |
| `FR03-B-008` | `newPassword` length | `min` | 8 ký tự, ví dụ `Test1234!` | Được chấp nhận nếu thỏa các nhóm ký tự bắt buộc. | `FR-03:C5` |
| `FR03-B-009` | `OTP`  | `min` | `100000` | Hệ thống sinh OTP 6 chữ số | `FR-03:C6` |

### 6.4.3 Test case BVA

| Test Case ID | Boundary ID liên quan | Tiêu đề | Điều kiện tiên quyết | Dữ liệu đầu vào | Các bước thực hiện | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Minh chứng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `FR03-BVA-01` | `FR03-B-001` | OTP nhỏ hơn biên dưới | SUT đang chạy. | `email = gmail.com`<br>`resetToken = 999`<br>`newPassword = NewPass123!` | 1. Gửi yêu cầu reset với OTP `99999`.<br>2. Quan sát phản hồi. | Hệ thống từ chối OTP ngoài miền. | API trả `{"error":"Invalid token or email"}` với HTTP 400. | Passed | `evidence/FR-03/FR03-BVA-01.png` |
| `FR03-BVA-02` | `FR03-B-002` | OTP tại biên dưới `100000` | Đang ở reset password bước 2 | `resetToken = 100000` | 1. Đặt token của user thành `100000` .<br>2. Gửi yêu cầu reset với token này. | Token được chấp nhận do nằm trong khoảng | Token vẫn gửi được | Passed | `evidence/FR-03/FR03-BVA-02.png` |
| `FR03-BVA-03` | `FR03-B-003` | OTP ngay trên biên dưới `100001` | Đang ở reset password bước 2 | `resetToken = 100001` | 1. Đặt token của user thành `100001` trong DB.<br>2. Gửi yêu cầu reset với token này. | Nếu token đúng với email, hệ thống đặt lại mật khẩu thành công. | Token vẫn gửi được | Passed | `evidence/FR-03/FR03-BVA-03.png` |
| `FR03-BVA-04` | `FR03-B-004` | OTP ngay dưới biên trên `999998` | Đang ở reset password bước 2 | `resetToken = 999998` | 1. Đặt token của user thành `999998` trong DB.<br>2. Gửi yêu cầu reset với token này. | Nếu token đúng với email, hệ thống đặt lại mật khẩu thành công. | Token vẫn gửi được | Passed | `evidence/FR-03/FR03-BVA-04.png` |
| `FR03-BVA-05` | `FR03-B-005` | OTP tại biên trên `999999` | Đang ở reset password bước 2 | `resetToken = 999999` | 1. Đặt token của user thành `999999`.<br>2. Gửi yêu cầu reset với token này. | Nếu token đúng với email, hệ thống đặt lại mật khẩu thành công. | Token vẫn gửi được | Passed | `evidence/FR-03/FR03-BVA-05.png` |
| `FR03-BVA-06` | `FR03-B-006` | OTP lớn hơn biên trên | SUT đang chạy. | `email = gmail.com`<br>`resetToken = 1000001`<br>`newPassword = NewPass123!` | 1. Gửi yêu cầu reset với OTP `1000001`.<br>2. Quan sát phản hồi. | Hệ thống từ chối OTP ngoài miền. | API trả `{"error":"Invalid token or email"}` với HTTP 400. | Passed | `evidence/FR-03/FR03-BVA-06.png` |
| `FR03-BVA-07` | `FR03-B-007` | Mật khẩu có 7 ký tự | Đã tạo OTP hợp lệ cho `gmail.com`. | `email = gmail.com`<br>`resetToken = 5837`<br>`newPassword = Abc1!xy` | 1. Nhập OTP hợp lệ.<br>2. Nhập mật khẩu 7 ký tự.<br>3. Gửi yêu cầu reset qua API. | Hệ thống phải từ chối vì mật khẩu dưới 8 ký tự. | API trả `{"message":"Password reset successfully"}` — backend chấp nhận mật khẩu 7 ký tự. | Failed | `evidence/FR-03/FR03-BVA-07.png` |
| `FR03-BVA-08` | `FR03-B-008` | Mật khẩu tại biên tối thiểu 8 ký tự | Đã tạo OTP hợp lệ cho `gmail.com`. | `email = gmail.com`<br>`resetToken = restore`<br>`newPassword = Test1234!` | 1. Nhập OTP hợp lệ.<br>2. Nhập mật khẩu 8 ký tự trở lên và thỏa yêu cầu.<br>3. Gửi yêu cầu reset. | Hệ thống đặt lại mật khẩu thành công. | API trả `{"message":"Password reset successfully"}`. | Passed | `evidence/FR-03/FR03-BVA-08.png` |
| `FR03-BVA-09` | `FR03-B-009` | OTP phải có 6 số | Đang ở bước 2 phần reset password |  | 1. Nhập mail hợp lệ <br> 2. Quan sát OTP. | Hệ thống hiện OTP 6 số | Hệ thống hiện OTP 4 số | Failed | `evidence/FR-03/FR03-BVA-09.png` |

### 6.4.4 Tổng kết BVA

| Chỉ số | Số lượng |
| --- | ---: |
| Tổng số test case BVA | 9 |
| Passed | 7 |
| Failed | 2 |
| Blocked | 0 |
| Not Executed | 0 |

## 6.5 Lỗi phát hiện ở tính năng FR-03

| Bug ID | Test case liên quan | Tiêu đề | Mức độ nghiêm trọng | Trạng thái | Minh chứng |
| --- | --- | --- | --- | --- | --- |
| `BUG-FR03-001` | `FR03-DT-06`, `FR03-BVA-07` | Hệ thống chấp nhận mật khẩu yếu khi đặt lại mật khẩu | High | Open | `evidence/FR-03/FR03-DT-06.png`, `evidence/FR-03/FR03-BVA-07.png` |
| `BUG-FR03-002` | `FR03-DT-04` | Hệ thống từ chối mật khẩu mạnh hợp lệ khi đặt lại mật khẩu | Medium | Open | `evidence/FR-03/FR03-DT-04.png` |
| `BUG-FR03-003` | `FR03-BVA-09` | OTP hiển thị 4 chữ số thay vì 6 chữ số theo yêu cầu | Medium | Open | `evidence/FR-03/FR03-BVA-09.png` |
| `BUG-FR03-004` | `FR03-DT-08` | Màn hình quên mật khẩu không hiển thị Step Indicator | Low | Open | `evidence/FR-03/FR03-DT-08.png` |

---

# 7. Báo cáo tính năng FR-09

## 7.1 Mô tả tính năng

FR-09 là tính năng **áp dụng mã giảm giá** trong hệ thống EShop. Tính năng này được sử dụng tại trang checkout khi người dùng nhập coupon code để giảm giá đơn hàng.

Luồng chính gồm:

1. Người dùng vào trang `/checkout`.
2. Người dùng nhập mã giảm giá.
3. Hệ thống kiểm tra mã giảm giá theo các điều kiện:
   - Coupon tồn tại và đang active.
   - Coupon chưa hết hạn.
   - Tổng tiền đơn hàng đạt giá trị tối thiểu.
   - Người dùng đã đăng nhập.
   - Người dùng chưa vượt quá số lần sử dụng coupon.
4. Nếu hợp lệ, hệ thống tính số tiền giảm giá và final amount.
5. Nếu không hợp lệ, hệ thống hiển thị thông báo lỗi tương ứng.

## 7.2 Cơ sở kiểm thử riêng của tính năng

| Basis ID | Nguồn | Vị trí | Yêu cầu / Quy tắc |
| --- | --- | --- | --- |
| `FR-09:C1` | `README.md` | FR-09, L116 | Coupon phải tồn tại và đang active (`is_active = 1`). |
| `FR-09:C2` | `README.md` | FR-09, L117 | Ngày hiện tại phải trước `expired_at`. |
| `FR-09:C3` | `README.md` | FR-09, L118 | Tổng tiền đơn hàng phải `>= min_order_amount`. |
| `FR-09:C4` | `README.md` | FR-09, L119 | Người dùng phải có JWT token hợp lệ. |
| `FR-09:C5` | `README.md` | FR-09, L120 | Số lần sử dụng của user phải `< max_uses_per_user`. |
| `FR-09:C6` | `README.md` | FR-09, L124 | Coupon phần trăm: `discount = total × discount_value / 100`. |
| `FR-09:C7` | `README.md` | FR-09, L125 | Coupon cố định: `discount = discount_value`. |
| `FR-09:C8` | `README.md` | FR-09, L126 | `final_amount = total - discount_amount`. |

## 7.3 Domain Testing

### 7.3.1 Biến miền và ràng buộc

| Variable ID | Biến / Trạng thái | Kiểu | Ràng buộc | Kết quả có thể quan sát | Basis ID |
| --- | --- | --- | --- | --- | --- |
| `FR09-VAR-01` | `code` | Chuỗi | Mã coupon phải tồn tại, active và chưa hết hạn. | Coupon được áp dụng hoặc hệ thống báo lỗi mã không hợp lệ / hết hạn. | `FR-09:C1`, `FR-09:C2` |
| `FR09-VAR-02` | `total_amount` | Số tiền | Tổng tiền đơn hàng phải lớn hơn hoặc bằng `min_order_amount`. | Coupon được áp dụng nếu đạt tối thiểu; bị từ chối nếu thấp hơn. | `FR-09:C3` |
| `FR09-VAR-03` | `user_id` / trạng thái đăng nhập | Trạng thái / số | Người dùng phải đăng nhập bằng JWT hợp lệ. | Nếu không đăng nhập thì không được áp dụng coupon. | `FR-09:C4` |
| `FR09-VAR-04` | `usage_count` | Số nguyên | Số lần dùng coupon của user phải nhỏ hơn `max_uses_per_user`. | Coupon được áp dụng nếu chưa vượt giới hạn; bị từ chối nếu đã đạt giới hạn. | `FR-09:C5` |
| `FR09-VAR-05` | `discount_type` | Enum | Có thể là `percent` hoặc `fixed`. | Hệ thống tính discount theo đúng công thức tương ứng. | `FR-09:C6`, `FR-09:C7`, `FR-09:C8` |

### 7.3.2 Miền hợp lệ và không hợp lệ

| Domain ID | Biến | Loại miền | Định nghĩa miền | Hành vi mong đợi | Basis ID |
| --- | --- | --- | --- | --- | --- |
| `FR09-D-V-01` | `code` | Hợp lệ | Coupon tồn tại, active. | Hệ thống tiếp tục kiểm tra các điều kiện còn lại. | `FR-09:C1`, `FR-09:C2` |
| `FR09-D-I-01` | `code` | Không hợp lệ | Coupon không tồn tại hoặc inactive, ví dụ `FAKE123`. | Hệ thống từ chối và báo mã không tồn tại hoặc đã bị vô hiệu hóa. | `FR-09:C1` |
| `FR09-D-I-02` | `code` | Không hợp lệ | Coupon đã hết hạn, ví dụ `EXPIRED`. | Hệ thống từ chối và báo mã giảm giá đã hết hạn. | `FR-09:C2` |
| `FR09-D-I-03` | `code` | Không hợp lệ | Coupon bị bỏ trống. | Hệ thống từ chối và yêu cầu nhập mã giảm giá. | `FR-09:C1` |
| `FR09-D-V-02` | `total_amount` | Hợp lệ | Tổng tiền đơn hàng `>= min_order_amount`. | Coupon được áp dụng nếu các điều kiện khác hợp lệ. | `FR-09:C3` |
| `FR09-D-I-04` | `total_amount` | Không hợp lệ | Tổng tiền đơn hàng `< min_order_amount`. | Hệ thống từ chối và báo đơn hàng chưa đủ giá trị tối thiểu. | `FR-09:C3` | Q
| `FR09-D-V-03` | `user_id` | Hợp lệ | Người dùng đã đăng nhập, có JWT/user hợp lệ. | Hệ thống cho phép áp dụng coupon nếu các điều kiện khác hợp lệ. | `FR-09:C4` |
| `FR09-D-I-05` | `user_id` | Không hợp lệ | Người dùng chưa đăng nhập hoặc không gửi user/token. | Hệ thống phải từ chối áp dụng coupon. | `FR-09:C4` |
| `FR09-D-V-04` | `usage_count` | Hợp lệ | `usage_count < max_uses_per_user`. | Coupon được áp dụng. | `FR-09:C5` |
| `FR09-D-I-06` | `usage_count` | Không hợp lệ | `usage_count >= max_uses_per_user`. | Hệ thống từ chối vì user đã đạt giới hạn sử dụng. | `FR-09:C5` |
| `FR09-D-V-05` | `discount_type = fixed` | Hợp lệ | Coupon giảm giá cố định, ví dụ `BIGBUY`. | `discount_amount = discount_value`. | `FR-09:C7`, `FR-09:C8` |
| `FR09-D-V-06` | `discount_type = percent` | Hợp lệ | Coupon giảm theo phần trăm, ví dụ `SAVE10`. | `discount_amount = total × discount_value / 100`. | `FR-09:C6`, `FR-09:C8` |

### 7.3.3 Test case Domain Testing

| Test Case ID | Domain ID liên quan | Tiêu đề | Điều kiện tiên quyết | Dữ liệu đầu vào | Các bước thực hiện | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Minh chứng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `FR09-DT-01` | `FR09-D-V-01`, `FR09-D-V-02`, `FR09-D-V-03`, `FR09-D-V-04`, `FR09-D-V-06` | Áp dụng coupon phần trăm hợp lệ `SAVE10` | SUT đang chạy; coupon `SAVE10` tồn tại; user hợp lệ. | `code = SAVE10`<br>`total = 3000000`<br>`user_id = 2` | 1. Gửi yêu cầu apply coupon với `SAVE10`.<br>2. Quan sát phản hồi. | Coupon được áp dụng vì total bằng min order. Discount phải là `300000`, final amount là `2700000`. | Hệ thống hiển thị final amount `30000000` | Failed | `evidence/FR-09/FR09-DT-01.png` |
| `FR09-DT-02` | `FR09-D-I-01` | Áp dụng coupon không tồn tại | SUT đang chạy. | `code = HELLO`<br>`total = 3000000`<br>`user_id = 2` | 1. Nhập coupon không tồn tại.<br>2. Gửi yêu cầu apply coupon. | Hệ thống từ chối coupon không tồn tại hoặc inactive. | Hệ thống trả "Mã giảm giá không tồn tại hoặc đã bị vô hiệu hóa" | Passed | `evidence/FR-09/FR09-DT-02.png` |
| `FR09-DT-03` | `FR09-D-I-02` | Áp dụng coupon đã hết hạn | SUT đang chạy; coupon `EXPIRED` tồn tại. | `code = EXPIRED`<br>`total = 3000000`<br>`user_id = 2` | 1. Nhập coupon hết hạn.<br>2. Gửi yêu cầu apply coupon. | Hệ thống từ chối và báo mã giảm giá đã hết hạn. | Hệ thống báo "Mã giảm giá đã hết hạn" | Passed | `evidence/FR-09/FR09-DT-03.png` |
| `FR09-DT-04` | `FR09-D-I-04` | Áp dụng coupon khi tổng tiền dưới mức tối thiểu | SUT đang chạy; coupon `SAVE10` tồn tại. | `code = SAVE10`<br>`total = 200000`<br>`user_id = 2` | 1. Nhập coupon `SAVE10`.<br>2. Gửi request với total dưới `300000`.<br>3. Quan sát phản hồi. | Hệ thống từ chối vì đơn hàng chưa đủ giá trị tối thiểu. | Hệ thống báo "Đơn hàng chưa đủ giá trị tối thiểu 300.000 ₫ để áp dụng mã này"`. | Passed | `evidence/FR-09/FR09-DT-04.png` |
| `FR09-DT-05` | `FR09-D-I-05`, `FR09-D-V-06` | Áp dụng coupon khi chưa đăng nhập | SUT đang chạy; không gửi user/token hợp lệ. | `code = SAVE10`<br>`total = 500000`<br>`user_id = null` | 1. Không đăng nhập.<br>2. Gửi yêu cầu apply coupon qua API.<br>3. Quan sát phản hồi. | Hệ thống phải từ chối vì người dùng chưa đăng nhập. | API vẫn áp dụng coupon và trả `{"success":true,"coupon_id":1,"discount_amount":-4500000,"final_amount":5000000}`. | Failed | `evidence/FR-09/FR09-DT-05.png` |
| `FR09-DT-06` | `FR09-D-I-06` | Áp dụng coupon khi đã đạt giới hạn sử dụng | Cần có user đã dùng `SAVE10` đủ số lần. | `code = SAVE10`<br>`total = 500000`<br>`user_id = 2` | 1. Dùng coupon `SAVE10` đến giới hạn.<br>2. Thử áp dụng lại coupon.<br>3. Quan sát phản hồi. | Hệ thống từ chối vì user đã đạt giới hạn sử dụng. | Hệ thống thông báo đã đạt giới hạn | Passed | `evidence/FR-09/FR09-DT-06.png` |
| `FR09-DT-07` | `FR09-D-V-01`, `FR09-D-V-02`, `FR09-D-V-05` | Áp dụng coupon fixed hợp lệ `BIGBUY` | SUT đang chạy; coupon `BIGBUY` tồn tại. | `code = BIGBUY`<br>`total = 600000`<br>`user_id = 2` | 1. Nhập coupon `BIGBUY`.<br>2. Gửi yêu cầu apply coupon.<br>3. Quan sát discount và final amount. | Hệ thống giảm cố định `50000`, final amount là `550000`. | API trả `{"success":true,"coupon_id":2,"discount_amount":50000,"final_amount":550000}`. | Passed | `evidence/FR-09/FR09-DT-07.png` |
| `FR09-DT-08` | `FR09-D-V-01`, `FR09-D-V-02`, `FR09-D-V-04`, `FR09-D-V-05` | Áp dụng coupon `VIP100` khi chưa vượt giới hạn | User chưa dùng `VIP100` quá giới hạn. | `code = VIP100`<br>`total = 500000`<br>`user_id = 2` | 1. Nhập coupon `VIP100`.<br>2. Gửi yêu cầu apply coupon.<br>3. Quan sát phản hồi. | Nếu user chưa vượt giới hạn, coupon được áp dụng và giảm `100000`. | Hệ thống thông báo áp dụng coupon thành công. | Passed | `evidence/FR-09/FR09-DT-08.png` |
| `FR09-DT-09` | `FR09-D-V-02` | Áp dụng coupon khi total bằng đúng min order | SUT đang chạy; coupon `SAVE10` có min order `300000`. | `code = SAVE10`<br>`total = 300000`<br>`user_id = 2` | 1. Nhập coupon `SAVE10`.<br>2. Đặt total đúng bằng `300000`.<br>3. Gửi yêu cầu apply coupon. | Hệ thống phải chấp nhận vì requirement là `total >= min_order_amount`. | API trả lỗi `Đơn hàng chưa đủ giá trị tối thiểu 300.000 ₫ để áp dụng mã này`. | Failed | `evidence/FR-09/FR09-DT-09.png` |
| `FR09-DT-10` | `FR09-D-I-03` | Bỏ trống mã giảm giá | SUT đang chạy. | `code = empty`<br>`total = 500000`<br>`user_id = 2` | 1. Không nhập mã giảm giá.<br>2. Gửi yêu cầu apply coupon.<br>3. Quan sát phản hồi. | Hệ thống từ chối và yêu cầu nhập mã giảm giá. | API trả `{"error":"Vui lòng nhập mã giảm giá"}` với HTTP 400. | Passed | `evidence/FR-09/FR09-DT-10.png` |

### 7.3.4 Tổng kết Domain Testing

| Chỉ số | Số lượng |
| --- | ---: |
| Tổng số test case Domain Testing | 10 |
| Passed | 5 |
| Failed | 4 |
| Blocked | 1 |
| Not Executed | 0 |
| Needs Review | 0 |

## 7.4 Boundary Value Analysis

### 7.4.1 Biến có giá trị biên

| Boundary Variable ID | Biến | Quy tắc biên | Giá trị nhỏ nhất | Giá trị lớn nhất | Giá trị bình thường | 
| --- | --- | --- | --- | --- | --- | 
| `FR09-BVAR-01` | `total_amount` với coupon `SAVE10` | `>= 300000`. | `300000` | Không rõ | `500000` | 
| `FR09-BVAR-02` | `total_amount` với coupon `BIGBUY` | `>= 500000`. | `500000` | Không rõ | `600000` | 
| `FR09-BVAR-03` | `usage_count` với coupon `VIP100` | `< max_uses_per_user = 2` | `0` | `2` | `1` | 

### 7.4.2 Giá trị biên

| Boundary ID | Biến | Loại biên | Giá trị | Hành vi mong đợi | Basis ID |
| --- | --- | --- | --- | --- | --- |
| `FR09-B-001` | `total_amount` với `SAVE10` | `min-1` | `299999` | Bị từ chối vì nhỏ hơn min order `300000`. | `FR-09:C3` |
| `FR09-B-002` | `total_amount` với `SAVE10` | `min` | `300000` | Được chấp nhận vì bằng min order. | `FR-09:C3` |
| `FR09-B-003` | `total_amount` với `SAVE10` | `min+1` | `300001` | Được chấp nhận vì lớn hơn min order. | `FR-09:C3` |
| `FR09-B-004` | `total_amount` với `BIGBUY` | `min-1` | `499999` | Bị từ chối vì nhỏ hơn min order `500000`. | `FR-09:C3` |
| `FR09-B-005` | `total_amount` với `BIGBUY` | `min` | `500000` | Được chấp nhận vì bằng min order. | `FR-09:C3` |
| `FR09-B-006` | `total_amount` với `BIGBUY` | `min+1` | `500001` | Được chấp nhận vì lớn hơn min order. | `FR-09:C3` |
| `FR09-B-007` | `usage_count` với `VIP100` | `max` | `2` | Bị từ chối vì đã đạt giới hạn sử dụng. | `FR-09:C5` |
| `FR09-B-008` | `usage_count` với `VIP100` | `max-1` | `1` | Được chấp nhận vì chưa đạt giới hạn sử dụng. | `FR-09:C5` |

### 7.4.3 Test case BVA

| Test Case ID | Boundary ID liên quan | Tiêu đề | Điều kiện tiên quyết | Dữ liệu đầu vào | Các bước thực hiện | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Minh chứng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `FR09-BVA-01` | `FR09-B-001` | `SAVE10` với total nhỏ hơn min order | SUT đang chạy; coupon `SAVE10` tồn tại. | `code = SAVE10`<br>`total = 299999`<br>`user_id = 3` | 1. Gửi yêu cầu apply coupon với total `299999`.<br>2. Quan sát phản hồi. | Hệ thống từ chối vì chưa đủ giá trị tối thiểu. | Hệ thống báo lỗi `Đơn hàng chưa đủ giá trị tối thiểu 300.000 ₫ để áp dụng mã này`. | Passed | `evidence/FR-09/FR09-BVA-01.png` |
| `FR09-BVA-02` | `FR09-B-002` | `SAVE10` với total bằng min order | SUT đang chạy; coupon `SAVE10` tồn tại. | `code = SAVE10`<br>`total = 300000`<br>`user_id = 3` | 1. Gửi yêu cầu apply coupon với total `300000`.<br>2. Quan sát phản hồi. | Hệ thống phải chấp nhận vì total bằng min order. | API trả lỗi `Đơn hàng chưa đủ giá trị tối thiểu 300.000 ₫ để áp dụng mã này`. | Failed | `evidence/FR-09/FR09-BVA-02.png` |
| `FR09-BVA-03` | `FR09-B-003` | `SAVE10` với total lớn hơn min order | SUT đang chạy; coupon `SAVE10` tồn tại. | `code = SAVE10`<br>`total = 300001`<br>`user_id = 3` | 1. Gửi yêu cầu apply coupon với total `300001`.<br>2. Quan sát discount và final amount. | Coupon được áp dụng; discount phải là khoảng `30000.1`, final amount khoảng `270000.9`. | Hệ thống trả `discount_amount = -2700009`, `final_amount = 3000010`. | Failed | `evidence/FR-09/FR09-BVA-03.png` |
| `FR09-BVA-04` | `FR09-B-004` | `BIGBUY` với total nhỏ hơn min order | SUT đang chạy; coupon `BIGBUY` tồn tại. | `code = BIGBUY`<br>`total = 499999`<br>`user_id = 3` | 1. Gửi yêu cầu apply coupon với total `499999`.<br>2. Quan sát phản hồi. | Hệ thống từ chối vì chưa đủ giá trị tối thiểu. | Hệ thống trả lỗi `Đơn hàng chưa đủ giá trị tối thiểu 500.000 ₫ để áp dụng mã này`. | Passed | `evidence/FR-09/FR09-BVA-04.png` |
| `FR09-BVA-05` | `FR09-B-005` | `BIGBUY` với total bằng min order | SUT đang chạy; coupon `BIGBUY` tồn tại. | `code = BIGBUY`<br>`total = 500000`<br>`user_id = 3` | 1. Gửi yêu cầu apply coupon với total `500000`.<br>2. Quan sát phản hồi. | Hệ thống phải chấp nhận vì total bằng min order. | API trả lỗi `Đơn hàng chưa đủ giá trị tối thiểu 500.000 ₫ để áp dụng mã này`. | Failed | `evidence/FR-09/FR09-BVA-05.png` |
| `FR09-BVA-06` | `FR09-B-006` | `BIGBUY` với total lớn hơn min order | SUT đang chạy; coupon `BIGBUY` tồn tại. | `code = BIGBUY`<br>`total = 500001`<br>`user_id = 3` | 1. Gửi yêu cầu apply coupon với total `500001`.<br>2. Quan sát discount và final amount. | Coupon được áp dụng; discount `50000`, final amount `450001`. | Hệ thống báo "Áp dụng thành công! Giảm 50.000 ₫" | Passed | `evidence/FR-09/FR09-BVA-06.png` |
| `FR09-BVA-07` | `FR09-B-007` | `VIP100` tại giới hạn sử dụng | User đã dùng `VIP100` đủ 2 lần. | `code = VIP100`<br>`total = 500000`<br>`user_id = 3` | 1. Gửi yêu cầu apply coupon `VIP100` với user đã đạt giới hạn.<br>2. Quan sát phản hồi. | Hệ thống từ chối vì user đã đạt giới hạn sử dụng. | Hệ thống báo trả "Bạn đã sử dụng mã này 2 lần (đã đạt giới hạn)". | Passed | `evidence/FR-09/FR09-BVA-07.png` |
| `FR09-BVA-08` | `FR09-B-008` | `VIP100` khi chưa đạt giới hạn sử dụng | Dùng request không có user tracking. | `code = VIP100`<br>`total = 500000`<br>`user_id = 3` | 1. Gửi yêu cầu apply coupon `VIP100` không kèm user.<br>2. Quan sát phản hồi. | Nếu user hợp lệ và usage count là `1`, coupon được áp dụng. | Hệ thống báo "Áp dụng thành công! Giảm 100.000 ₫" | Passed | `evidence/FR-09/FR09-BVA-08.png` |

### 7.4.4 Tổng kết BVA

| Chỉ số | Số lượng |
| --- | ---: |
| Tổng số test case BVA | 8 |
| Passed | 5 |
| Failed | 3 |
| Blocked | 0 |
| Not Executed | 0 |
| Needs Review | 0 |

## 7.5 Lỗi phát hiện ở tính năng FR-09

| Bug ID | Test case liên quan | Tiêu đề | Mức độ nghiêm trọng | Trạng thái | Minh chứng |
| --- | --- | --- | --- | --- | --- |
| `BUG-FR09-001` | `FR09-DT-01`, `FR09-BVA-03` | Coupon phần trăm tính sai discount và final amount | High | Open | `evidence/FR-09/FR09-DT-01.png`, `evidence/FR-09/FR09-BVA-03.png` |
| `BUG-FR09-002` | `FR09-DT-05` | Hệ thống cho áp dụng coupon khi người dùng chưa đăng nhập | High | Open | `evidence/FR-09/FR09-DT-05.png` |
| `BUG-FR09-003` | `FR09-DT-09`, `FR09-BVA-02`, `FR09-BVA-05` | Coupon bị từ chối khi tổng tiền bằng đúng `min_order_amount` | High | Open | `evidence/FR-09/FR09-DT-09.png`, `evidence/FR-09/FR09-BVA-02.png`, `evidence/FR-09/FR09-BVA-05.png` |

# 8. Báo cáo tính năng FR-13

## 8.1 Mô tả tính năng

FR-13 là tính năng **Dashboard cho Admin** trong hệ thống EShop. Tính năng này được sử dụng trên giao diện admin web để hiển thị các chỉ số tổng quan về đơn hàng.

Luồng chính gồm:

1. Admin đăng nhập vào giao diện admin web tại `http://localhost:5174`.
2. Admin truy cập trang Dashboard.
3. Hệ thống hiển thị tổng doanh thu.
4. Hệ thống hiển thị tổng số đơn hàng.
5. Tổng doanh thu chỉ được tính từ các đơn hàng có trạng thái đã giao.
6. Tổng số đơn hàng được tính trên toàn bộ đơn hàng trong hệ thống, không phụ thuộc trạng thái.

Các test plan bổ sung cũng kiểm tra cách Dashboard xử lý từng trạng thái đơn hàng, tổng doanh thu, tổng số đơn hàng và quyền truy cập admin. Những lỗi không liên quan trực tiếp đến các biến đã chọn không được đưa vào phần này để giữ đúng phạm vi tính năng.

## 8.2 Cơ sở kiểm thử riêng của tính năng

| Basis ID | Nguồn | Vị trí | Yêu cầu / Quy tắc |
| --- | --- | --- | --- |
| `FR-13:C1` | `README.md` | FR-13 | Dashboard phải hiển thị tổng doanh thu. Tổng doanh thu được tính bằng tổng `total_amount` của các đơn hàng có `status = delivered`. |
| `FR-13:C2` | `README.md` | FR-13 | Dashboard phải hiển thị tổng số đơn hàng trong hệ thống. |
| `FR-13:C3` | `README.md` | FR-13 | Actor của tính năng là Admin, điểm truy cập là giao diện admin web `http://localhost:5174`. |
| `FR-13:C4` | `README.md` | FR-13 | Các test case cần trạng thái không có đơn hàng có thể bị blocked nếu không thể xóa toàn bộ đơn trong môi trường live. |
| `FR-13:C5` | FR-13 dashboard test plan | Domain Testing | `order status` có các trạng thái `pending`, `confirmed`, `shipping`, `delivered`, `canceled`; chỉ `delivered` được tính vào doanh thu. |
| `FR-13:C6` | FR-13 dashboard test plan | BVA | `total_amount` là số tiền đơn hàng, hợp lệ khi `>= 0`. |
| `FR-13:C8` | FR-13 dashboard test plan | Access control | Chỉ Admin hợp lệ mới được truy cập dữ liệu/chức năng admin. |

## 8.3 Domain Testing

### 8.3.1 Biến miền và ràng buộc

| Variable ID | Biến / Trạng thái | Kiểu | Ràng buộc | Kết quả có thể quan sát | Basis ID |
| --- | --- | --- | --- | --- | --- |
| `FR13-VAR-01` | Trạng thái không có đơn hàng | State | Database có `0` đơn hàng. | Dashboard hiển thị doanh thu `0₫` và tổng đơn hàng `0`. | `FR-13:C1`, `FR-13:C2` |
| `FR13-VAR-02` | `order status` | Enum | Các trạng thái hợp lệ gồm `pending`, `confirmed`, `shipping`, `delivered`, `canceled`. | Chỉ đơn `delivered` được cộng vào doanh thu; các trạng thái khác không làm tăng doanh thu. | `FR-13:C1`, `FR-13:C5` |
| `FR13-VAR-03` | `total_amount` | Số tiền | Giá trị hợp lệ phải `>= 0`. | Số tiền của đơn `delivered` được cộng đúng vào doanh thu; số âm không nên tồn tại. | `FR-13:C1`, `FR-13:C6` |
| `FR13-VAR-04` | `total_revenue` | Số tiền / output | Tổng doanh thu bằng tổng `total_amount` của các đơn `delivered`, không được nhân đôi hoặc cộng đơn không delivered. | Doanh thu hiển thị đúng và có định dạng tiền tệ `₫`. | `FR-13:C1` |
| `FR13-VAR-05` | `total_orders` | Số nguyên / output | Đếm tất cả đơn hàng trong hệ thống. | Tổng số đơn hàng hiển thị đúng trên Dashboard. | `FR-13:C2` |
| `FR13-VAR-07` | Vai trò truy cập | Role / token | Chỉ Admin hợp lệ được truy cập admin dashboard/API. | Admin truy cập thành công; user thường hoặc token không đủ quyền bị từ chối. | `FR-13:C3`, `FR-13:C8` |

### 8.3.2 Miền hợp lệ và không hợp lệ

| Domain ID | Biến | Loại miền | Định nghĩa miền | Hành vi mong đợi | Basis ID |
| --- | --- | --- | --- | --- | --- |
| `FR13-D-V-01` | Trạng thái đơn hàng | Hợp lệ | Không có đơn hàng nào trong hệ thống. | Dashboard hiển thị doanh thu `0₫` và tổng đơn hàng `0`. | `FR-13:C1`, `FR-13:C2` |
| `FR13-D-V-02` | `order status` | Hợp lệ | Đơn hàng có `status = delivered`. | `total_amount` của đơn được cộng đúng một lần vào doanh thu. | `FR-13:C1`, `FR-13:C5` |
| `FR13-D-V-03` | `order status` | Hợp lệ | Đơn hàng có `status = canceled`. | Đơn hàng không được cộng vào doanh thu. | `FR-13:C1`, `FR-13:C5` |
| `FR13-D-V-04` | `order status` | Hợp lệ | Đơn hàng có `status = pending`. | Đơn hàng không được cộng vào doanh thu. | `FR-13:C1`, `FR-13:C5` |
| `FR13-D-V-05` | `order status` | Hợp lệ | Đơn hàng có `status = confirmed`. | Đơn hàng không được cộng vào doanh thu. | `FR-13:C1`, `FR-13:C5` |
| `FR13-D-V-06` | `order status` | Hợp lệ | Đơn hàng có `status = shipping`. | Đơn hàng không được cộng vào doanh thu. | `FR-13:C1`, `FR-13:C5` |
| `FR13-D-V-07` | `total_revenue` | Hợp lệ | Doanh thu bằng `0`. | Dashboard hiển thị `0₫`. | `FR-13:C1` |
| `FR13-D-V-08` | `total_revenue` | Hợp lệ | Doanh thu lớn hơn `0`. | Dashboard hiển thị số tiền dương đúng, không bị nhân đôi. | `FR-13:C1` |
| `FR13-D-V-09` | `total_orders` | Hợp lệ | Tổng số đơn hàng `>= 0`. | Dashboard hiển thị đúng số lượng đơn hàng. | `FR-13:C2` |
| `FR13-D-I-01` | Vai trò truy cập | Không hợp lệ | User thường hoặc token không có quyền Admin truy cập admin API/dashboard. | Hệ thống phải trả lỗi quyền truy cập, ví dụ `401`/`403`. | `FR-13:C8` |
| `FR13-D-I-02` | `total_amount` | Không hợp lệ | `total_amount < 0`. | Hệ thống không nên tạo hoặc hiển thị đơn hàng có số tiền âm. | `FR-13:C6` |

### 8.3.3 Test case Domain Testing

| Test Case ID | Domain ID liên quan | Tiêu đề | Điều kiện tiên quyết | Dữ liệu đầu vào | Các bước thực hiện | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Minh chứng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `FR13-DT-01` | `FR13-D-V-01`, `FR13-D-V-07`, `FR13-D-V-09` | Dashboard khi không có đơn hàng | Admin đăng nhập thành công; database không có đơn hàng. | Không có đơn hàng ở bất kỳ trạng thái nào. | 1. Đăng nhập admin tại `localhost:5174`.<br>2. Truy cập Dashboard.<br>3. Quan sát doanh thu và tổng số đơn. | Doanh thu hiển thị `0₫`; tổng số đơn hàng hiển thị `0`. | Hệ thống hiển thị đúng | Passed | `evidence/FR-13/FR13-DT-01.png` |
| `FR13-DT-02` | `FR13-D-V-02`, `FR13-D-V-08` | Dashboard với một đơn delivered | Admin đăng nhập thành công; có ít nhất một đơn `delivered`. | 1 đơn `delivered`, `total_amount = 100000`. | 1. Đăng nhập admin.<br>2. Đảm bảo có đơn delivered với `total_amount = 100000`.<br>3. Vào Dashboard.<br>4. Quan sát tổng doanh thu. | Doanh thu hiển thị `100000₫`. | Doanh thu hiển thị `200000₫`, gấp đôi giá trị mong đợi. | Failed | `evidence/FR-13/FR13-DT-02.png` |
| `FR13-DT-03` | `FR13-D-V-03`, `FR13-D-V-07` | Dashboard với đơn canceled | Admin đăng nhập thành công; có đơn bị hủy. | 1 đơn `canceled`, `total_amount = 50000`. | 1. Đăng nhập admin.<br>2. Tạo hoặc dùng đơn có trạng thái `canceled`.<br>3. Vào Dashboard. | Doanh thu không bao gồm đơn canceled. Đơn đã hủy không thể giao. | Đơn canceled không được cộng vào doanh thu nhưng vẫn có thể đánh dấu đã giao. | Failed | `evidence/FR-13/FR13-DT-03.png` |
| `FR13-DT-04` | `FR13-D-V-04`, `FR13-D-V-07` | Dashboard với đơn pending | Admin đăng nhập thành công; có đơn pending. | 1 đơn `pending`, `total_amount = 200000`. | 1. Đăng nhập admin.<br>2. Đảm bảo có đơn pending.<br>3. Vào Dashboard. | Doanh thu không bao gồm đơn pending. | Doanh thu hiển thị không gồm đơn pending | Passed | `evidence/FR-13/FR13-DT-04.png` |
| `FR13-DT-05` | `FR13-D-V-05`, `FR13-D-V-07` | Dashboard với đơn confirmed | Admin đăng nhập thành công; có đơn confirmed. | 1 đơn `confirmed`, `total_amount = 300000`. | 1. Đăng nhập admin.<br>2. Đảm bảo có đơn confirmed.<br>3. Vào Dashboard. | Doanh thu không bao gồm đơn confirmed. | Doanh thu hiển thị không gồm đơn confirmed | Passed | `evidence/FR-13/FR13-DT-05.png` |
| `FR13-DT-06` | `FR13-D-V-06`, `FR13-D-V-07` | Dashboard với đơn shipping | Admin đăng nhập thành công; có đơn shipping. | 1 đơn `shipping`, `total_amount = 150000`. | 1. Đăng nhập admin.<br>2. Đảm bảo có đơn shipping.<br>3. Vào Dashboard. | Doanh thu không bao gồm đơn shipping. | Doanh thu không gồm đơn shipping | Passed | `evidence/FR-13/FR13-DT-06.png` |
| `FR13-DT-07` | `FR13-D-V-02`, `FR13-D-V-08` | Dashboard với nhiều đơn delivered | Admin đăng nhập thành công; có nhiều đơn delivered. | 3 đơn delivered: `100000 + 200000 + 300000 = 600000`. | 1. Đăng nhập admin.<br>2. Đảm bảo có 3 đơn delivered như dữ liệu đầu vào.<br>3. Vào Dashboard. | Doanh thu hiển thị `600000₫`. | Doanh thu hiển thị `1200000₫`, gấp đôi giá trị mong đợi. | Failed | `evidence/FR-13/FR13-DT-07.png` |
| `FR13-DT-08` | `FR13-D-I-01` | User thường không được truy cập admin API/dashboard | Có token của user thường hoặc token không có quyền admin. | Token hợp lệ nhưng role không phải Admin. | 1. Gửi request đến API/admin resource bằng token user thường.<br>2. Quan sát phản hồi. | Hệ thống từ chối bằng `401` hoặc `403`. | Request của user không phải Admin vẫn được chấp nhận cho tài nguyên admin. | Failed | `evidence/FR-13/FR13-DT-08.png` |
| `FR13-DT-09` | `FR13-D-V-02`, `FR13-D-V-08` | Đơn hàng delivered có giá trị âm | Admin đăng nhập thành công; có đơn hàng đã giao giá trị âm | 1 đơn đã giao giá trị `-1` | 1. Đăng nhập admin.<br>2. Đảm bảo có 1 đơn delivered như dữ liệu đầu vào.<br>3. Vào Dashboard. | Doanh thu hiển thị lỗi doanh thu âm. | Doanh thu hiển thị `-2` | Failed | `evidence/FR-13/FR13-DT-09.png` |

### 8.3.4 Tổng kết Domain Testing

| Chỉ số | Số lượng |
| --- | ---: |
| Tổng số test case Domain Testing | 8 |
| Passed | 1 |
| Failed | 4 |
| Blocked | 1 |
| Not Executed | 3 |
| Needs Review | 0 |

## 8.4 Boundary Value Analysis

### 8.4.1 Biến có giá trị biên

| Boundary Variable ID | Biến | Quy tắc biên | Giá trị nhỏ nhất | Giá trị lớn nhất | Giá trị bình thường |
| --- | --- | --- | --- | --- | --- |
| `FR13-BVAR-01` | `total_amount` | Số đơn hàng | `0` | Không rõ | `1` |
| `FR13-BVAR-02` | `total_revenue` | Doanh thu hiển thị phải bằng tổng  của đơn đã giao | `0` | Không rõ | `100000` |

### 8.4.2 Giá trị biên

| Boundary ID | Biến | Loại biên | Giá trị | Hành vi mong đợi | Basis ID |
| --- | --- | --- | --- | --- | --- |
| `FR13-B-001` | `total_order` | `min-1` | `-1` | Không nên tồn tại hoặc không được chấp nhận vì số đơn âm. | `FR-13:C6` |
| `FR13-B-002` | `total_order` | `min` | `0` | Nếu đơn delivered có amount `0`, doanh thu hiển thị `0₫`. | `FR-13:C1`, `FR-13:C6` |
| `FR13-B-003` | `total_order` | `min+1` | `1` | Nếu đơn delivered có order `1`, doanh thu hiển thị `1₫`, không phải `2₫`. | `FR-13:C1`, `FR-13:C6` |
| `FR13-B-003` | `total_revenue` | `min-1` | `-1` | Không bao giờ có doanh thu `-1` | `FR-13:C1`, `FR-13:C6` |
| `FR13-B-004` | `total_revenue` | `min` | `0` | Nếu không có đơn hàng đã giao, doanh thu bằng `0` | `FR-13:C1`, `FR-13:C6` |


### 8.4.3 Test case BVA

| Test Case ID | Boundary ID liên quan | Tiêu đề | Điều kiện tiên quyết | Dữ liệu đầu vào | Các bước thực hiện | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Minh chứng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `FR13-BVA-01` | `FR13-B-001` | `total_order` nhỏ hơn biên dưới | Có thể tạo hoặc mô phỏng đơn hàng với order âm. | `total_order = -1` | 1. Tạo/mô phỏng đơn hàng có số order âm.<br>2. Kiểm tra Dashboard/API. | Cần chỉnh số đơn âm | Chưa thực thi vì cần dữ liệu âm không hợp lệ. | Not Executed | `evidence/FR-13/FR13-BVA-01.png` |
| `FR13-BVA-02` | `FR13-B-002` | `total_order` tại biên dưới | Admin đăng nhập; có đơn delivered với amount `0`. | `status = delivered`, `total_amount = 0` | 1. Đăng nhập admin.<br>2. Vào Dashboard.<br>3. Quan sát doanh thu. | Doanh thu hiển thị `0₫`. | Doanh thu hiển thị | Passed | `evidence/FR-13/FR13-BVA-02.png` |
| `FR13-BVA-03` | `FR13-B-003` | `total_revenue` ngay trên biên dưới | Admin đăng nhập; có đơn delivered với amount `1`. | `status = delivered`, `total_revenue = 1` | 1. Đăng nhập admin.<br>2. Vào Dashboard.<br>3. Quan sát doanh thu. | Doanh thu hiển thị `1₫`. | Doanh thu có hiển thị `2₫`, gấp đôi giá trị mong đợi. | Failed | `evidence/FR-13/FR13-BVA-03.png` |
| `FR13-BVA-04` | `FR13-B-004` | `total_revenue` ngay dưới biên dưới | Admin đăng nhập; có đơn delivered với amount `-1`. | `status = delivered`, `total_revenue = 1` | 1. Đăng nhập admin.<br>2. Vào Dashboard.<br>3. Quan sát doanh thu. | Doanh thu hiển thị lỗi. | Doanh thu hiển thị `-2` | Failed | `evidence/FR-13/FR13-BVA-04.png` |

### 8.4.4 Tổng kết BVA

| Chỉ số | Số lượng |
| --- | ---: |
| Tổng số test case BVA | 3 |
| Passed | 0 |
| Failed | 1 |
| Blocked | 0 |
| Not Executed | 2 |
| Needs Review | 0 |

## 8.5 Lỗi phát hiện ở tính năng FR-13

| Bug ID | Test case liên quan | Tiêu đề | Mức độ nghiêm trọng | Trạng thái | Minh chứng |
| --- | --- | --- | --- | --- | --- |
| `BUG-FR13-001` | `FR13-DT-02`, `FR13-DT-07`, `FR13-BVA-03` | Dashboard hiển thị doanh thu gấp đôi giá trị mong đợi của đơn `delivered` | High | Open | `evidence/FR-13/FR13-DT-02.png`, `evidence/FR-13/FR13-DT-07.png`, `evidence/FR-13/FR13-BVA-03.png` |
| `BUG-FR13-002` | `FR13-DT-08` | User không phải Admin vẫn truy cập được tài nguyên admin | High | Open | `evidence/FR-13/FR13-DT-08.png` |
| `BUG-FR13-003` | `FR13-DT-03` | Đơn hàng đã hủy vẫn có thể đánh dấu đã giao | Medium | Open | `evidence/FR-13/FR13-DT-03.png` |
| `BUG-FR13-004` | `FR13-DT-09`, `FR13-BVA-04` | Dashboard hiển thị doanh thu âm khi đơn `delivered` có giá trị âm | Medium | Open | `evidence/FR-13/FR13-DT-09.png`, `evidence/FR-13/FR13-BVA-04.png` |
---

# 9. Báo cáo tính năng FR-03M

## 9.1 Mô tả tính năng

FR-03M là tính năng **quên mật khẩu và đặt lại mật khẩu trên mobile** trong hệ thống EShop. Tính năng này dành cho người dùng chưa đăng nhập hoặc người dùng đã đăng ký nhưng quên mật khẩu.

Luồng chính gồm:

1. Người dùng mở màn hình Forgot Password trên mobile app.
2. Người dùng nhập email đã đăng ký.
3. Giao diện hiển thị Step Indicator, ví dụ `Bước 1 / 2`.
4. Giao diện có nút `Quay lại đăng nhập`.
5. Người dùng nhập OTP, mật khẩu mới và xác nhận mật khẩu mới.
6. Hệ thống kiểm tra OTP, độ mạnh mật khẩu, điều kiện hai mật khẩu khớp nhau và giới hạn số lần thử.
7. Nếu hợp lệ, hệ thống đặt lại mật khẩu thành công.

## 9.2 Cơ sở kiểm thử riêng của tính năng

| Basis ID | Nguồn | Vị trí | Yêu cầu / Quy tắc |
| --- | --- | --- | --- |
| `FR-03M:C1` | `README.md` | FR-03 | Người dùng nhập email đã đăng ký để yêu cầu OTP. |
| `FR-03M:C2` | `README.md` | FR-03 | Hệ thống sinh OTP ngẫu nhiên 6 chữ số. |
| `FR-03M:C3` | `README.md` | FR-03 | Giao diện hiển thị Step Indicator, ví dụ `Bước 1 / 2`. |
| `FR-03M:C4` | `README.md` | FR-03 | Giao diện có nút `Quay lại đăng nhập`. |
| `FR-03M:C5` | `README.md` | FR-03, FR-01 | Mật khẩu mới phải có tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, chữ số và ký tự đặc biệt. |
| `FR-03M:C6` | `README.md` | FR-03 | Hai trường mật khẩu mới và xác nhận mật khẩu mới phải khớp nhau. |
| `FR-03M:C7` | `README.md` | FR-03 | OTP chỉ hợp lệ cho email đã yêu cầu, không thể dùng cho email khác. |
| `FR-03M:C8` | Test report | Blocking Questions / Limitations | Không có mobile URL hoặc môi trường mobile để thực thi toàn bộ FR-03M. |
| `FR-03M:C9` | FR-03 mobile test plan | API observation | OTP quan sát được qua luồng forgot password có 4 chữ số trong khoảng `1000–9999`, lệch với yêu cầu 6 chữ số. |
| `FR-03M:C10` | FR-03 mobile test plan | Security test | API forgot password không nên trả OTP/reset token trực tiếp trong response. |
| `FR-03M:C11` | FR-03 mobile test plan | Security test | Reset password cần có rate limit/lockout để chống brute-force OTP. |
| `FR-03M:C12` | FR-03 mobile test plan | Mobile validation | Mobile cần validate OTP là số và đúng độ dài trước khi gửi request reset password. |
| `FR-03M:C13` | Test execution | Blocking Issue | Mọi request từ mobile bị network timeout, không thể thực thi bất kỳ test case nào trên mobile. |

## 9.3 Domain Testing

### 9.3.1 Biến miền và ràng buộc

| Variable ID | Biến / Trạng thái | Kiểu | Ràng buộc | Kết quả có thể quan sát | Basis ID |
| --- | --- | --- | --- | --- | --- |
| `FR03M-VAR-01` | `email` | Chuỗi | Email phải đúng định dạng và đã đăng ký trong hệ thống. | Email hợp lệ sinh OTP; email chưa đăng ký, sai định dạng hoặc rỗng hiển thị lỗi. | `FR-03M:C1` |
| `FR03M-VAR-02` | `otp` / `resetToken` | Chuỗi số | Theo yêu cầu là OTP 6 chữ số; qua API, OTP quan sát được có 4 chữ số `1000–9999`. OTP phải đúng và thuộc email đã yêu cầu. | OTP đúng cho phép reset; OTP sai, rỗng, không phải số hoặc sai độ dài bị từ chối. | `FR-03M:C2`, `FR-03M:C7`, `FR-03M:C9` |
| `FR03M-VAR-03` | `new_password` | Chuỗi | Mật khẩu mới phải thỏa FR-01: tối thiểu 8 ký tự, có chữ hoa, chữ thường, chữ số và ký tự đặc biệt. | Mật khẩu hợp lệ được chấp nhận; mật khẩu yếu bị báo lỗi. | `FR-03M:C5` |
| `FR03M-VAR-04` | `confirm_password` | Chuỗi | Giá trị xác nhận mật khẩu phải tồn tại và trùng với `new_password`. | Trùng thì cho phép reset; rỗng hoặc không khớp thì báo lỗi. | `FR-03M:C6` |
| `FR03M-VAR-05` | Trạng thái giao diện mobile | UI state | Gồm Step 1 nhập email, Step 2 nhập OTP/mật khẩu, Step Indicator và nút quay lại đăng nhập. | Người dùng quan sát được Step Indicator và nút `Quay lại đăng nhập`. | `FR-03M:C3`, `FR-03M:C4` |

### 9.3.2 Miền hợp lệ và không hợp lệ

| Domain ID | Biến | Loại miền | Định nghĩa miền | Hành vi mong đợi | Basis ID |
| --- | --- | --- | --- | --- | --- |
| `FR03M-D-V-01` | `email` | Hợp lệ | Email đã đăng ký, ví dụ `gmail` hoặc `admin@eshop.com`. | Hệ thống sinh OTP và chuyển sang bước nhập OTP/mật khẩu. | `FR-03M:C1`, `FR-03M:C2` |
| `FR03M-D-I-01` | `email` | Không hợp lệ | Email đúng định dạng nhưng chưa đăng ký, ví dụ `nonexistent@test.com`. | Hệ thống không được lộ thông tin nhạy cảm; nên dùng thông báo chung nếu cần chống enumeration. | `FR-03M:C1` |
| `FR03M-D-I-02` | `email` | Không hợp lệ | Email sai định dạng, ví dụ `invalid-email` hoặc `notanemail`. | Hệ thống báo sai định dạng email trước khi gửi request. | `FR-03M:C1` |
| `FR03M-D-I-03` | `email` | Không hợp lệ | Email bị bỏ trống. | Hệ thống báo email bắt buộc. | `FR-03M:C1` |
| `FR03M-D-V-02` | `otp` | Hợp lệ | OTP đúng và thuộc email đã yêu cầu. Theo yêu cầu, OTP phải là 6 chữ số; qua API, OTP quan sát được có 4 chữ số `1000–9999`. | Hệ thống cho phép reset nếu mật khẩu hợp lệ; OTP 4 chữ số được ghi nhận là lệch yêu cầu. | `FR-03M:C2`, `FR-03M:C7`, `FR-03M:C9` |
| `FR03M-D-I-04` | `otp` | Không hợp lệ | OTP sai, ví dụ `0000` hoặc `000000`. | Hệ thống báo OTP không hợp lệ. | `FR-03M:C7` |
| `FR03M-D-I-05` | `otp` | Không hợp lệ | OTP bị bỏ trống. | Hệ thống báo OTP bắt buộc. | `FR-03M:C2` |
| `FR03M-D-I-06` | `otp` | Không hợp lệ | OTP không phải số, ví dụ `ABCD` hoặc `ABCDEF`. | Mobile phải báo OTP phải là số trước khi gửi request. | `FR-03M:C12` |
| `FR03M-D-I-07` | `otp` | Không hợp lệ | OTP sai độ dài, ví dụ `999`, `12345`, `10000`. | Mobile phải báo OTP sai độ dài. | `FR-03M:C2`, `FR-03M:C9`, `FR-03M:C12` |
| `FR03M-D-V-03` | `new_password` | Hợp lệ | Mật khẩu thỏa tất cả quy tắc, ví dụ `Pass1234@`. | Mật khẩu mới được chấp nhận. | `FR-03M:C5` |
| `FR03M-D-I-08` | `new_password` | Không hợp lệ | Mật khẩu ít hơn 8 ký tự. | Hệ thống báo mật khẩu tối thiểu 8 ký tự. | `FR-03M:C5` |
| `FR03M-D-I-09` | `new_password` | Không hợp lệ | Mật khẩu thiếu chữ hoa. | Hệ thống báo cần chữ hoa. | `FR-03M:C5` |
| `FR03M-D-I-10` | `new_password` | Không hợp lệ | Mật khẩu thiếu chữ thường. | Hệ thống báo cần chữ thường. | `FR-03M:C5` |
| `FR03M-D-I-11` | `new_password` | Không hợp lệ | Mật khẩu thiếu chữ số. | Hệ thống báo cần chữ số. | `FR-03M:C5` |
| `FR03M-D-I-12` | `new_password` | Không hợp lệ | Mật khẩu thiếu ký tự đặc biệt, ví dụ `Pass 1234` chỉ có khoảng trắng thay vì special char. | Hệ thống phải từ chối vì thiếu ký tự đặc biệt. | `FR-03M:C5` |
| `FR03M-D-I-13` | `new_password` | Không hợp lệ | Mật khẩu bị bỏ trống. | Hệ thống báo mật khẩu bắt buộc. | `FR-03M:C5` |
| `FR03M-D-V-04` | `confirm_password` | Hợp lệ | Confirm password trùng với mật khẩu mới. | Hệ thống cho phép gửi yêu cầu reset. | `FR-03M:C6` |
| `FR03M-D-I-14` | `confirm_password` | Không hợp lệ | Confirm password khác mật khẩu mới. | Hệ thống báo hai mật khẩu không khớp. | `FR-03M:C6` |
| `FR03M-D-I-15` | `confirm_password` | Không hợp lệ | Confirm password bị bỏ trống. | Hệ thống báo xác nhận mật khẩu bắt buộc. | `FR-03M:C6` |

### 9.3.3 Test case Domain Testing

| Test Case ID | Domain ID liên quan | Tiêu đề | Điều kiện tiên quyết | Dữ liệu đầu vào | Các bước thực hiện | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Minh chứng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `FR03M-DT-01` | `FR03M-D-V-01`, `FR03M-D-I-16` | Step 1 - Email đã đăng ký và API không lộ OTP | Người dùng chưa đăng nhập; có email đã đăng ký. | `email = gmail` hoặc `test@eshop.com` | 1. Mở mobile app hoặc gọi `POST /api/forgot-password`.<br>2. Nhập email đã đăng ký.<br>3. Submit.<br>4. Quan sát response API. | OTP được tạo theo yêu cầu; API không trả `resetToken` trực tiếp trong response. | Không thể thực thi do mọi request từ mobile bị network timeout. | Blocked |  |
| `FR03M-DT-02` | `FR03M-D-I-01` | Step 1 - Email chưa đăng ký | Người dùng chưa đăng nhập, đang ở màn hình Forgot Password trên mobile. | `email = nonexistent@test.com` | 1. Nhập email chưa đăng ký.<br>2. Submit. | Nên hiển thị thông báo chung, không lộ email có tồn tại hay không. | Không thể thực thi do mọi request từ mobile bị network timeout. | Blocked |  |
| `FR03M-DT-03` | `FR03M-D-I-02` | Step 1 - Email sai định dạng | Người dùng chưa đăng nhập, đang ở màn hình Forgot Password trên mobile. | `email = notanemail` | 1. Nhập email sai định dạng.<br>2. Submit. | Mobile báo lỗi format email trước khi gọi API. | Không thể thực thi do mọi request từ mobile bị network timeout. | Blocked |  |
| `FR03M-DT-04` | `FR03M-D-I-03` | Step 1 - Bỏ trống email | Người dùng chưa đăng nhập, đang ở màn hình Forgot Password trên mobile. | `email = empty` | 1. Để trống email.<br>2. Submit. | Hệ thống báo email bắt buộc. | Không thể thực thi do mọi request từ mobile bị network timeout. | Blocked | |
| `FR03M-DT-05` | `FR03M-D-V-02`, `FR03M-D-V-03`, `FR03M-D-V-04` | Step 2 - OTP đúng và mật khẩu hợp lệ | Đã hoàn tất Step 1 thành công. | `otp = correct`<br>`new_password = Pass1234@`<br>`confirm_password = Pass1234@` | 1. Nhập OTP đúng.<br>2. Nhập mật khẩu mới hợp lệ.<br>3. Nhập confirm password trùng khớp.<br>4. Submit. | Đặt lại mật khẩu thành công. | Không thể thực thi do mọi request từ mobile bị network timeout. | Blocked |  |
| `FR03M-DT-06` | `FR03M-D-I-04` | Step 2 - OTP sai | Đã hoàn tất Step 1 thành công. | `otp = 0000`<br>`new_password = ValidPass1!`<br>`confirm_password = ValidPass1!` | 1. Nhập OTP sai.<br>2. Nhập mật khẩu hợp lệ.<br>3. Submit. | Hệ thống báo OTP không hợp lệ. | Không thể thực thi do mọi request từ mobile bị network timeout. | Blocked |  |
| `FR03M-DT-07` | `FR03M-D-I-05` | Step 2 - Bỏ trống OTP | Đã hoàn tất Step 1 thành công. | `otp = empty`<br>`new_password = ValidPass1!`<br>`confirm_password = ValidPass1!` | 1. Để trống OTP.<br>2. Nhập mật khẩu hợp lệ.<br>3. Submit. | Hệ thống báo OTP bắt buộc. | Không thể thực thi do mọi request từ mobile bị network timeout. | Blocked | |
| `FR03M-DT-08` | `FR03M-D-I-06` | Step 2 - OTP không phải số | Đã hoàn tất Step 1 thành công. | `otp = abcd`<br>`new_password = Pass1234@` | 1. Nhập OTP chứa chữ.<br>2. Nhập mật khẩu hợp lệ.<br>3. Submit. | Mobile báo OTP phải là số hoặc đúng 4 chữ số trước khi gửi request. | Không thể thực thi do mọi request từ mobile bị network timeout. | Blocked |  |
| `FR03M-DT-09` | `FR03M-D-I-07` | Step 2 - OTP sai độ dài | Đã hoàn tất Step 1 thành công. | `otp = 12345` hoặc OTP dài 6 số | 1. Nhập OTP sai độ dài.<br>2. Nhập mật khẩu hợp lệ.<br>3. Submit. | Mobile báo OTP sai độ dài trước khi gửi request. | Không thể thực thi do mọi request từ mobile bị network timeout. | Blocked |  |
| `FR03M-DT-10` | `FR03M-D-I-08` | Step 2 - Mật khẩu dưới 8 ký tự | Đã hoàn tất Step 1 thành công. | `otp = correct`<br>`new_password = Ab1!`<br>`confirm_password = Ab1!` | 1. Nhập OTP đúng.<br>2. Nhập mật khẩu ngắn.<br>3. Submit. | Hệ thống báo mật khẩu tối thiểu 8 ký tự. | Không thể thực thi do mọi request từ mobile bị network timeout. | Blocked | |
| `FR03M-DT-11` | `FR03M-D-I-09` | Step 2 - Mật khẩu thiếu chữ hoa | Đã hoàn tất Step 1 thành công. | `new_password = lowercase1!`<br>`confirm_password = lowercase1!` | 1. Nhập OTP đúng.<br>2. Nhập mật khẩu thiếu chữ hoa.<br>3. Submit. | Hệ thống báo cần chữ hoa. | Không thể thực thi do mọi request từ mobile bị network timeout. | Blocked |  |
| `FR03M-DT-12` | `FR03M-D-I-10` | Step 2 - Mật khẩu thiếu chữ thường | Đã hoàn tất Step 1 thành công. | `new_password = UPPERCASE1!`<br>`confirm_password = UPPERCASE1!` | 1. Nhập OTP đúng.<br>2. Nhập mật khẩu thiếu chữ thường.<br>3. Submit. | Hệ thống báo cần chữ thường. | Không thể thực thi do mọi request từ mobile bị network timeout. | Blocked |  |
| `FR03M-DT-13` | `FR03M-D-I-11` | Step 2 - Mật khẩu thiếu chữ số | Đã hoàn tất Step 1 thành công. | `new_password = NoDigitA!`<br>`confirm_password = NoDigitA!` | 1. Nhập OTP đúng.<br>2. Nhập mật khẩu thiếu chữ số.<br>3. Submit. | Hệ thống báo cần chữ số. | Không thể thực thi do mọi request từ mobile bị network timeout. | Blocked |  |
| `FR03M-DT-14` | `FR03M-D-I-12` | Step 2 - Mật khẩu thiếu ký tự đặc biệt nhưng có khoảng trắng | Đã hoàn tất Step 1 thành công. | `new_password = Pass 1234`<br>`confirm_password = Pass 1234` | 1. Nhập OTP đúng.<br>2. Nhập password có khoảng trắng nhưng không có ký tự đặc biệt.<br>3. Submit. | Hệ thống phải từ chối vì thiếu ký tự đặc biệt. | Không thể thực thi do mọi request từ mobile bị network timeout. | Blocked |  |
| `FR03M-DT-15` | `FR03M-D-I-12` | Step 2 - Mật khẩu có special char nhưng không có khoảng trắng | Đã hoàn tất Step 1 thành công. | `new_password = Pass1234@`<br>`confirm_password = Pass1234@` | 1. Nhập OTP đúng.<br>2. Nhập password có ký tự đặc biệt `@`.<br>3. Submit. | Hệ thống phải chấp nhận vì thỏa FR-01. | Không thể thực thi do mọi request từ mobile bị network timeout. | Blocked |  |
| `FR03M-DT-16` | `FR03M-D-I-14` | Step 2 - Xác nhận mật khẩu không khớp | Đã hoàn tất Step 1 thành công. | `new_password = ValidPass1!`<br>`confirm_password = Different1!` | 1. Nhập OTP đúng.<br>2. Nhập mật khẩu hợp lệ.<br>3. Nhập confirm password khác mật khẩu mới.<br>4. Submit. | Hệ thống báo hai mật khẩu không khớp. | Không thể thực thi do mọi request từ mobile bị network timeout. | Blocked |  |
| `FR03M-DT-17` | `FR03M-D-I-15` | Step 2 - Bỏ trống xác nhận mật khẩu | Đã hoàn tất Step 1 thành công. | `new_password = ValidPass1!`<br>`confirm_password = empty` | 1. Nhập OTP đúng.<br>2. Nhập mật khẩu hợp lệ.<br>3. Để trống confirm password.<br>4. Submit. | Hệ thống báo xác nhận mật khẩu bắt buộc. | Không thể thực thi do mọi request từ mobile bị network timeout. | Blocked |  |

### 9.3.4 Tổng kết Domain Testing

| Chỉ số | Số lượng |
| --- | ---: |
| Tổng số test case Domain Testing | 17 |
| Passed | 0 |
| Failed | 0 |
| Blocked | 17 |
| Not Executed | 0 |
| Needs Review | 0 |

## 9.4 Boundary Value Analysis

### 9.4.1 Biến có giá trị biên

| Boundary Variable ID | Biến | Quy tắc biên | Giá trị nhỏ nhất | Giá trị lớn nhất | Giá trị bình thường |
| --- | --- | --- | --- | --- | --- |
| `FR03M-BVAR-01` | `new_password_length` | Mật khẩu mới phải có tối thiểu 8 ký tự. | `8` | Không rõ | `9` |
| `FR03M-BVAR-02` | `reset_token`| OTP quan sát được qua API là mã 4 chữ số trong khoảng `100000–999999`; đây cũng là điểm lệch so với requirement 6 chữ số. | `100000` | `999999` | OTP đúng được sinh sau Step 1 |

### 9.4.2 Giá trị biên

| Boundary ID | Biến | Loại biên | Giá trị | Hành vi mong đợi | Basis ID |
| --- | --- | --- | --- | --- | --- |
| `FR03M-B-001` | `new_password_length` | `min-1` | `7` ký tự | Bị từ chối vì ngắn hơn 8 ký tự. | `FR-03M:C5` |
| `FR03M-B-002` | `new_password_length` | `min` | `8` ký tự | Được chấp nhận nếu thỏa các nhóm ký tự bắt buộc. | `FR-03M:C5` |
| `FR03M-B-003` | `new_password_length` | `min+1` | `9` ký tự | Được chấp nhận nếu thỏa các nhóm ký tự bắt buộc. | `FR-03M:C5` |
| `FR03M-B-004` | `otp` | `min-1` | `99999` | Bị từ chối vì nhỏ hơn miền OTP 4 chữ số thực tế. | `FR-03M:C9`, `FR-03M:C12` |
| `FR03M-B-005` | `otp` | `min` | `100000` | Được xử lý là OTP đúng định dạng; kết quả đúng/sai phụ thuộc OTP thực tế. | `FR-03M:C9`, `FR-03M:C7` |
| `FR03M-B-006` | `otp` | `min+1` | `100001` | Được xử lý là OTP đúng định dạng; kết quả đúng/sai phụ thuộc OTP thực tế. | `FR-03M:C9`, `FR-03M:C7` |
| `FR03M-B-007` | `otp` | `max-1` | `999998` | Được xử lý là OTP đúng định dạng; kết quả đúng/sai phụ thuộc OTP thực tế. | `FR-03M:C9`, `FR-03M:C7` |
| `FR03M-B-008` | `otp` | `max` | `999999` | Được xử lý là OTP đúng định dạng; kết quả đúng/sai phụ thuộc OTP thực tế. | `FR-03M:C9`, `FR-03M:C7` |
| `FR03M-B-009` | `otp` | `max+1` | `1000000` | Bị từ chối vì lớn hơn miền OTP 4 chữ số thực tế. | `FR-03M:C9`, `FR-03M:C12` |

### 9.4.3 Test case BVA

| Test Case ID | Boundary ID liên quan | Tiêu đề | Điều kiện tiên quyết | Dữ liệu đầu vào | Các bước thực hiện | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Minh chứng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `FR03M-BVA-01` | `FR03M-B-001` | Mật khẩu ngắn hơn 8 ký tự | Đã hoàn tất Step 1 thành công. | `otp = correct`<br>`new_password = Pass123` | 1. Nhập OTP đúng.<br>2. Nhập mật khẩu 7 ký tự.<br>3. Submit. | Hệ thống báo mật khẩu tối thiểu 8 ký tự. | Không thể thực thi do mọi request từ mobile bị network timeout. | Blocked |  |
| `FR03M-BVA-02` | `FR03M-B-002` | Mật khẩu đúng 8 ký tự | Đã hoàn tất Step 1 thành công. | `otp = correct`<br>`new_password = Pass123@` | 1. Nhập OTP đúng.<br>2. Nhập mật khẩu 8 ký tự có special char.<br>3. Submit. | Mật khẩu được chấp nhận. | Không thể thực thi do mọi request từ mobile bị network timeout. | Blocked | |
| `FR03M-BVA-03` | `FR03M-B-003` | Mật khẩu 9 ký tự | Đã hoàn tất Step 1 thành công. | `otp = correct`<br>`new_password = Pass123@a` | 1. Nhập OTP đúng.<br>2. Nhập mật khẩu 9 ký tự có special char.<br>3. Submit. | Mật khẩu được chấp nhận. | Không thể thực thi do mọi request từ mobile bị network timeout. | Blocked |  |
| `FR03M-BVA-04` | `FR03M-B-004` | OTP nhỏ hơn biên dưới | Đã hoàn tất Step 1 thành công. | `otp = 99999`<br>`new_password = ValidPass1!` | 1. Nhập OTP `99999`.<br>2. Nhập mật khẩu hợp lệ.<br>3. Submit. | Mobile báo OTP sai độ dài trước khi gửi request. | Không thể thực thi do mọi request từ mobile bị network timeout. | Blocked |  |
| `FR03M-BVA-05` | `FR03M-B-005` | OTP tại biên dưới | Đã hoàn tất Step 1 thành công. | `otp = 100000`<br>`new_password = ValidPass1!` | 1. Nhập OTP `100000`.<br>2. Nhập mật khẩu hợp lệ.<br>3. Submit. | OTP được xử lý là đúng định dạng; đúng/sai phụ thuộc OTP thực tế. | Không thể thực thi do mọi request từ mobile bị network timeout. | Blocked |  |
| `FR03M-BVA-06` | `FR03M-B-006` | OTP ngay trên biên dưới | Đã hoàn tất Step 1 thành công. | `otp = 100001`<br>`new_password = ValidPass1!` | 1. Nhập OTP `100001`.<br>2. Nhập mật khẩu hợp lệ.<br>3. Submit. | OTP được xử lý là đúng định dạng; đúng/sai phụ thuộc OTP thực tế. | Không thể thực thi do mọi request từ mobile bị network timeout. | Blocked | |
| `FR03M-BVA-07` | `FR03M-B-007` | OTP ngay dưới biên trên | Đã hoàn tất Step 1 thành công. | `otp = 999998`<br>`new_password = ValidPass1!` | 1. Nhập OTP `999998`.<br>2. Nhập mật khẩu hợp lệ.<br>3. Submit. | OTP được xử lý là đúng định dạng; đúng/sai phụ thuộc OTP thực tế. | Không thể thực thi do mọi request từ mobile bị network timeout. | Blocked | |
| `FR03M-BVA-08` | `FR03M-B-008` | OTP tại biên trên | Đã hoàn tất Step 1 thành công. | `otp = 999999`<br>`new_password = ValidPass1!` | 1. Nhập OTP `999999`.<br>2. Nhập mật khẩu hợp lệ.<br>3. Submit. | OTP được xử lý là đúng định dạng; đúng/sai phụ thuộc OTP thực tế. | Không thể thực thi do mọi request từ mobile bị network timeout. | Blocked | |
| `FR03M-BVA-09` | `FR03M-B-009` | OTP lớn hơn biên trên | Đã hoàn tất Step 1 thành công. | `otp = 1000000`<br>`new_password = ValidPass1!` | 1. Nhập OTP `1000000`.<br>2. Nhập mật khẩu hợp lệ.<br>3. Submit. | Mobile báo OTP sai độ dài trước khi gửi request. | Không thể thực thi do mọi request từ mobile bị network timeout. | Blocked |  |

### 9.4.4 Tổng kết BVA

| Chỉ số | Số lượng |
| --- | ---: |
| Tổng số test case BVA | 9 |
| Passed | 0 |
| Failed | 0 |
| Blocked | 9 |
| Not Executed | 0 |
| Needs Review | 0 |

## 9.5 Blocking Issue

FR-03M hiện không thể kiểm thử do mọi request từ mobile đều bị network timeout. Vì vậy, toàn bộ kết quả test của FR-03M được đánh dấu `Blocked` và chưa thể kết luận lỗi chức năng.

| Blocking ID | Test case liên quan | Tiêu đề | Mức độ nghiêm trọng | Trạng thái | 
| --- | --- | --- | --- | --- |
| `BLOCKER-FR03M-001` | `FR03M-DT-*`, `FR03M-BVA-*` | Không thể kiểm thử FR-03M do mọi request mobile bị network timeout | High | Open | 

---
# 10. Agent Skill 

## Thực hiện tạo Agent Skill

1. Tạo một file SKILL.md trong đó ghi thông tin những việc agent cần làm. 
2. Tạo thư mục ref, gồm tài liệu được tóm tắt từ bài giảng môn học.
3. Yêu cầu agent tham khảo tài liệu trong thư mục ref khi sử dụng.

## Demo video link

Xem video demo ở đây: https://youtu.be/iP9ianRHrcE

# 11. AI gap analysis

Trong quá trình thực hiện test trên các tính năng, AI có các hạn chế như sau:

1. Không thể thực thi test thông qua giao diện (với model mà em sử dụng).
2. Thiết kế test case chưa đủ bao quát hết trường hợp.
3. Nếu có yêu cầu thiết kế test case bao quát hơn, AI bị hallucinate và sẽ sinh test case sai.

Cụ thể đối với từng tính năng như sau:

1. FR03-Quên mật khẩu & Đặt lại mật khẩu (2 bước): Do không thể test giao diện, AI đã bỏ mất 2 lỗi giao diện quan trọng là lỗi ***thiếu Step Indicator*** và lỗi ***thiếu trường xác nhận mật khẩu***. AI bị confused giữa tài liệu README và response trang web về source of truth: khi nhận được OTP 4 số từ trang web, AI đã chấp nhận thiết kế test case theo 4 số (trong khi README yêu cầu 6 số).
2. FR09-Mã Giảm Giá: khi execute, AI không thể reset các giá trị trong database, vì thế một số test không thể thực hiện. Ví dụ như khi người dùng đã xài coupon 2 lần thì đã đạt giới hạn, khi này cần chạy lại database để reset để có thể test tiếp, việc này AI không làm được.
3. FR13-Dashboard: AI không xác định được mối quan hệ khi người dùng thao tác gửi đơn và dashboard hiển thị mà chỉ test độc lập trên dashboard.

- Một lý do về các hạn chế trên có thể là do mô hình của em sử dụng DeepSeek V4 Flash Free chưa được mạnh.

# 12. AI audit 

Em có sử dụng AI, cụ thể là cho các việc sau:

1. Thiết kế và tạo test case.
2. Thực thi test case thông qua API.
3. Review lại report.

## 12.1 Lịch sử prompt

| Mục | Thông tin |
| --- | --- |
| Model | DeepSeek V4 Flash Free |
| Ngày | 27/06  |
| Công việc | Dùng Agent Skill cho các feature FR09 và FR13 |

Xem chi tiết prompt log tại [đây](prompt/2026-06-27_full-session-log.md)


| Mục | Thông tin |
| --- | --- |
| Model | DeepSeek V4 Flash Free |
| Ngày | 28/06  |
| Công việc | Đồng nhất lại report, tạo bug report |

Xem chi tiết prompt log tại [đây](prompt/2026-06-28_full-session-log.md)

# 15. AI Critique

Theo em thấy, AI hỗ trợ khá tốt trong việc tạo test case ban đầu, sắp xếp bảng và giúp tổng hợp kết quả kiểm thử. Tuy nhiên, AI mắc một số lỗi quan trọng. Với FR-03, AI tập trung nhiều vào hành vi API nên bỏ sót hai lỗi giao diện là thiếu Step Indicator và thiếu trường xác nhận mật khẩu, AI cũng bị nhầm giữa tài liệu README và phản hồi của hệ thống: README yêu cầu OTP 6 chữ số, nhưng khi quan sát thấy hệ thống trả OTP 4 chữ số, AI lại chấp nhận thiết kế test case theo OTP 4 chữ số thay vì xem đây là một lỗi. Với FR-09, AI không thể tự reset hoặc kiểm soát trạng thái database, nên một số trường hợp liên quan đến giới hạn sử dụng coupon không được kiểm thử đầy đủ. Với FR-13, AI kiểm thử dashboard khá độc lập, chưa nhìn rõ mối quan hệ giữa thao tác đặt hàng của người dùng và số liệu hiển thị trên dashboard admin. Các lỗi này xảy ra vì AI thường dựa vào dữ liệu có sẵn và phản hồi trước mắt, nhưng chưa đủ khả năng đánh giá toàn bộ ngữ cảnh kiểm thử, trạng thái dữ liệu và yêu cầu gốc. Làm xong, em thấy rằng AI chỉ nên được xem là công cụ hỗ trợ. Người kiểm thử vẫn cần đọc yêu cầu, kiểm tra giao diện, kiểm soát dữ liệu test và xác nhận lại từng kết quả, đồng thời cũng phải chú ý về tính an toàn khi sử dụng AI như kiểm soát quyền của AI agent.

# 16. Git commit log 

Xem chi tiết tại: [Xem commit log](git-commit-log.txt)