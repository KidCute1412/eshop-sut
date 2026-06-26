# HW02 – Domain Testing trên hệ thống EShop

---

## Mục lục

- [1. Thông tin sinh viên và môn học](#1-thông-tin-sinh-viên-và-môn-học)
- [2. Tổng quan bài tập](#2-tổng-quan-bài-tập)
- [3. Tổng quan hệ thống được kiểm thử](#3-tổng-quan-hệ-thống-được-kiểm-thử)
- [4. Các tính năng được chọn](#4-các-tính-năng-được-chọn)
- [5. Phạm vi và phương pháp kiểm thử](#5-phạm-vi-và-phương-pháp-kiểm-thử)
- [6. Báo cáo tính năng A](#6-báo-cáo-tính-năng-a)
- [7. Báo cáo tính năng B](#7-báo-cáo-tính-năng-b)
- [8. Báo cáo tính năng C](#8-báo-cáo-tính-năng-c)
- [9. Báo cáo tính năng D](#9-báo-cáo-tính-năng-d)
- [10. Tổng kết kiểm thử](#10-tổng-kết-kiểm-thử)
- [11. Báo cáo lỗi tổng hợp](#11-báo-cáo-lỗi-tổng-hợp)
- [12. Tài liệu minh chứng](#12-tài-liệu-minh-chứng)
- [13. Khai báo sử dụng AI](#13-khai-báo-sử-dụng-ai)
- [14. Phân tích thiếu sót của AI](#14-phân-tích-thiếu-sót-của-ai)
- [15. Nhận xét về AI](#15-nhận-xét-về-ai)
- [16. Báo cáo nhật ký sử dụng AI](#16-báo-cáo-nhật-ký-sử-dụng-ai)
- [17. Báo cáo Agent Skill](#17-báo-cáo-agent-skill)
- [18. Nhật ký Git Commit](#18-nhật-ký-git-commit)
- [19. Tự đánh giá](#19-tự-đánh-giá)
- [20. Checklist nộp bài](#20-checklist-nộp-bài)
- [21. Tài liệu tham khảo](#21-tài-liệu-tham-khảo)
- [Phụ lục A. Bảng test case đầy đủ](#phụ-lục-a-bảng-test-case-đầy-đủ)
- [Phụ lục B. Nhật ký AI đầy đủ](#phụ-lục-b-nhật-ký-ai-đầy-đủ)

---

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
| Backend runtime | `<Runtime / version>` |
| Database | `<Database / version>` |
| Nguồn dữ liệu kiểm thử | `<Seed data / dữ liệu tạo thủ công / script>` |
| Công cụ kiểm thử API | `<Postman / curl / script / công cụ khác>` |
| Công cụ kiểm thử UI | `<Manual / Playwright / Selenium / công cụ khác>` |

## 3.3 Tài khoản và vai trò kiểm thử

| Vai trò | Username / Email | Mật khẩu | Mục đích sử dụng | Ghi chú |
| --- | --- | --- | --- | --- |
| Guest | `N/A` | `N/A` | `<Mục đích>` | `<Ghi chú>` |
| Customer | `<Email>` | `<Password>` | `<Mục đích>` | `<Ghi chú>` |
| Admin | `<Email>` | `<Password>` | `<Mục đích>` | `<Ghi chú>` |

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
| `BASIS-02` | `Giao diện hệ thống` | `http://localhost:5173/` | 
| `BASIS-03` | `API` | `http://localhost:3000/` | 

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
| `Needs Review` | Kết quả cần được kiểm tra hoặc xác nhận thêm. |

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
| `FR03-D-V-01` | `email` | Hợp lệ | Email đúng định dạng và đã đăng ký, ví dụ `test@eshop.com`. | Hệ thống tạo OTP/reset token và chuyển sang bước đặt lại mật khẩu. | `FR-03:C1` |
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
| `FR03-DT-01` | `FR03-D-V-01` | Yêu cầu đặt lại mật khẩu với email đã đăng ký | SUT đang chạy; tài khoản `test@eshop.com` tồn tại. | `email = test@eshop.com` | 1. Mở `/forgot-password`.<br>2. Nhập email đã đăng ký.<br>3. Gửi yêu cầu. | Hệ thống tạo OTP/reset token và hiển thị trên màn hình. | API trả `{"message":"Mã đặt lại mật khẩu đã được tạo","resetToken":"8609"}`. | Passed | `evidence/FR03-DT-01-api-log.txt` |
| `FR03-DT-02` | `FR03-D-I-01` | Yêu cầu đặt lại mật khẩu với email chưa đăng ký | SUT đang chạy. | `email = nonexistent@test.com` | 1. Mở `/forgot-password`.<br>2. Nhập email chưa đăng ký.<br>3. Gửi yêu cầu. | Hệ thống từ chối và báo lỗi người dùng không tồn tại. | API trả `{"error":"User not found"}` với HTTP 404. | Passed | `evidence/FR03-DT-02-api-log.txt` |
| `FR03-DT-03` | `FR03-D-I-02` | Bỏ trống email khi yêu cầu đặt lại mật khẩu | SUT đang chạy; kiểm thử cần thực hiện qua UI. | `email = empty` | 1. Mở `/forgot-password`.<br>2. Để trống email.<br>3. Nhấn submit. | Trình duyệt hoặc hệ thống chặn submit và yêu cầu nhập email. | Không thể xác nhận qua API; frontend có thuộc tính `required`, cần kiểm thử UI bằng trình duyệt. | Blocked | N/A — UI-only test |
| `FR03-DT-04` | `FR03-D-V-01`, `FR03-D-V-02`, `FR03-D-V-03` | Đặt lại mật khẩu thành công với email, OTP và mật khẩu mạnh hợp lệ | Đã tạo OTP cho `test@eshop.com`. | `email = test@eshop.com`<br>`resetToken = 8609`<br>`newPassword = NewPass123!` | 1. Gửi yêu cầu quên mật khẩu để lấy OTP.<br>2. Nhập đúng OTP.<br>3. Nhập mật khẩu mới mạnh.<br>4. Gửi yêu cầu đặt lại mật khẩu. | Hệ thống đặt lại mật khẩu thành công và chuyển về trang đăng nhập. | API trả `{"message":"Password reset successfully"}` với HTTP 200. | Passed | `evidence/FR03-DT-04-api-log.txt` |
| `FR03-DT-05` | `FR03-D-I-03` | Đặt lại mật khẩu với OTP sai | Đã có email hợp lệ. | `email = test@eshop.com`<br>`resetToken = 0000`<br>`newPassword = NewPass123!` | 1. Nhập email hợp lệ.<br>2. Nhập OTP sai.<br>3. Nhập mật khẩu mạnh.<br>4. Gửi yêu cầu đặt lại mật khẩu. | Hệ thống từ chối OTP sai. | API trả `{"error":"Invalid token or email"}` với HTTP 400. | Passed | `evidence/FR03-DT-05-api-log.txt` |
| `FR03-DT-06` | `FR03-D-I-05` | Đặt lại mật khẩu với mật khẩu yếu | Đã tạo OTP hợp lệ cho `test@eshop.com`. | `email = test@eshop.com`<br>`resetToken = 2420`<br>`newPassword = weak` | 1. Tạo OTP hợp lệ.<br>2. Nhập OTP đúng.<br>3. Nhập mật khẩu yếu.<br>4. Gửi yêu cầu đặt lại mật khẩu. | Hệ thống phải từ chối mật khẩu yếu. | API trả `{"message":"Password reset successfully"}` — backend chấp nhận mật khẩu yếu. | Failed | `evidence/FR03-DT-06-api-log.txt` |
| `FR03-DT-07` | `FR03-D-I-04` | Dùng OTP của email khác để đặt lại mật khẩu | Có OTP được tạo từ tài khoản admin. | `email = test@eshop.com`<br>`resetToken = 6480` từ admin<br>`newPassword = NewPass123!` | 1. Tạo OTP cho tài khoản admin.<br>2. Dùng OTP đó cho email `test@eshop.com`.<br>3. Gửi yêu cầu đặt lại mật khẩu. | Hệ thống từ chối vì OTP không thuộc email hiện tại. | API trả `{"error":"Invalid token or email"}` với HTTP 400. | Passed | `evidence/FR03-DT-07-api-log.txt` |
| `FR03-DT-08` | `FR03-D-V-05` | Reset mật khẩu | SUT đang chạy |  | 1. Nhấn vào Quên mật khẩu ? <br> 2. Quan sát chỉ báo bước. | Hệ thống hiển thị chỉ báo bước đúng | Không thấy chỉ báo bước | Failed | `evidence/FR03-DT-07-api-log.txt` |

### 6.3.4 Tổng kết Domain Testing

| Chỉ số | Số lượng |
| --- | ---: |
| Tổng số test case Domain Testing | 8 |
| Passed | 5 |
| Failed | 2 |
| Blocked | 1 |
| Not Executed | 0 |
| Needs Review | 0 |

## 6.4 Boundary Value Analysis

### 6.4.1 Biến có giá trị biên

| Boundary Variable ID | Biến | Quy tắc biên | Giá trị nhỏ nhất | Giá trị lớn nhất | Giá trị bình thường | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| `FR03-BVAR-01` | `resetToken` | nằm trong khoảng `100000–999999`. | `100000` | `999999` | OTP hợp lệ được tạo từ bước 1 | Không có |
| `FR03-BVAR-02` | độ dài `newPassword`  | Mật khẩu phải có tối thiểu 8 ký tự. | `8 ký tự` | Không rõ | `NewPass123!` | Không có |
| `FR03-BVAR-03` | `OTP`  | nằm trong khoảng `100000–999999` | `100000` |       `999999` | Giá trị OTP được tạo ngẫu nhiên trong khoảng hợp lệ | Không có |

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
| `FR03-BVA-01` | `FR03-B-001` | OTP nhỏ hơn biên dưới | SUT đang chạy. | `email = test@eshop.com`<br>`resetToken = 999`<br>`newPassword = NewPass123!` | 1. Gửi yêu cầu reset với OTP `99999`.<br>2. Quan sát phản hồi. | Hệ thống từ chối OTP ngoài miền. | API trả `{"error":"Invalid token or email"}` với HTTP 400. | Passed | `evidence/FR03-BVA-01-api-log.txt` |
| `FR03-BVA-02` | `FR03-B-002` | OTP tại biên dưới `100000` | Đang ở reset password bước 2 | `resetToken = 100000` | 1. Đặt token của user thành `100000` .<br>2. Gửi yêu cầu reset với token này. | Token được chấp nhận do nằm trong khoảng | Token vẫn gửi được | Passed | N/A — requires DB access |
| `FR03-BVA-03` | `FR03-B-003` | OTP ngay trên biên dưới `100001` | Đang ở reset password bước 2 | `resetToken = 100001` | 1. Đặt token của user thành `100001` trong DB.<br>2. Gửi yêu cầu reset với token này. | Nếu token đúng với email, hệ thống đặt lại mật khẩu thành công. | Token vẫn gửi được | Passed | N/A — requires DB access |
| `FR03-BVA-04` | `FR03-B-004` | OTP ngay dưới biên trên `999998` | Đang ở reset password bước 2 | `resetToken = 999998` | 1. Đặt token của user thành `999998` trong DB.<br>2. Gửi yêu cầu reset với token này. | Nếu token đúng với email, hệ thống đặt lại mật khẩu thành công. | Token vẫn gửi được | Passed | N/A — requires DB access |
| `FR03-BVA-05` | `FR03-B-005` | OTP tại biên trên `999999` | Đang ở reset password bước 2 | `resetToken = 999999` | 1. Đặt token của user thành `999999`.<br>2. Gửi yêu cầu reset với token này. | Nếu token đúng với email, hệ thống đặt lại mật khẩu thành công. | Token vẫn gửi được | Passed | N/A — requires DB access |
| `FR03-BVA-06` | `FR03-B-006` | OTP lớn hơn biên trên | SUT đang chạy. | `email = test@eshop.com`<br>`resetToken = 10000`<br>`newPassword = NewPass123!` | 1. Gửi yêu cầu reset với OTP `10000`.<br>2. Quan sát phản hồi. | Hệ thống từ chối OTP ngoài miền. | API trả `{"error":"Invalid token or email"}` với HTTP 400. | Passed | `evidence/FR03-BVA-06-api-log.txt` |
| `FR03-BVA-07` | `FR03-B-007` | Mật khẩu có 7 ký tự | Đã tạo OTP hợp lệ cho `test@eshop.com`. | `email = test@eshop.com`<br>`resetToken = 5837`<br>`newPassword = Abc1!xy` | 1. Nhập OTP hợp lệ.<br>2. Nhập mật khẩu 7 ký tự.<br>3. Gửi yêu cầu reset. | Hệ thống phải từ chối vì mật khẩu dưới 8 ký tự. | API trả `{"message":"Password reset successfully"}` — backend chấp nhận mật khẩu 7 ký tự. | Failed | `evidence/FR03-BVA-07-api-log.txt` |
| `FR03-BVA-08` | `FR03-B-008` | Mật khẩu tại biên tối thiểu 8 ký tự | Đã tạo OTP hợp lệ cho `test@eshop.com`. | `email = test@eshop.com`<br>`resetToken = restore`<br>`newPassword = Test1234!` | 1. Nhập OTP hợp lệ.<br>2. Nhập mật khẩu 8 ký tự trở lên và thỏa yêu cầu.<br>3. Gửi yêu cầu reset. | Hệ thống đặt lại mật khẩu thành công. | API trả `{"message":"Password reset successfully"}`. | Passed | `evidence/FR03-BVA-08-api-log.txt` |
| `FR03-BVA-09` | `FR03-B-009` | OTP phải có 6 số | Đang ở bước 2 phần reset password |  | 1. Nhập mail hợp lệ <br> 2. Quan sát OTP. | Hệ thống hiện OTP 6 số | Hệ thống hiện OTP 4 số | Failed | `evidence/FR03-BVA-08-api-log.txt` |

### 6.4.4 Tổng kết BVA

| Chỉ số | Số lượng |
| --- | ---: |
| Tổng số test case BVA | 9 |
| Passed | 7 |
| Failed | 2 |
| Blocked | 0 |
| Not Executed | 0 |
| Needs Review | 0 |

## 6.5 Lỗi phát hiện ở tính năng FR-03

| Bug ID | Test case liên quan | Tiêu đề | Mức độ nghiêm trọng | Trạng thái | Link GitHub Issue | Minh chứng |
| --- | --- | --- | --- | --- | --- | --- |
| `BUG-FR03-001` | `FR03-DT-06`, `FR03-BVA-07` | Backend chấp nhận mật khẩu yếu khi đặt lại mật khẩu | High | Open | `<Thêm link GitHub Issue>` | `evidence/FR03-DT-06-api-log.txt`, `evidence/FR03-BVA-07-api-log.txt` |
| `BUG-FR03-002` | `FR03-DT-01`, `FR03-BVA-01`–`FR03-BVA-06` | OTP thực tế chỉ có 4 chữ số thay vì 6 chữ số theo đặc tả | Medium | Open | `<Thêm link GitHub Issue>` | API log có các OTP như `8609`, `2420`, `5837` |
| `BUG-FR03-003` | `FR-03:C4` | Giao diện thiếu trường xác nhận mật khẩu mới | Medium | Open | `<Thêm link GitHub Issue>` | Source code `ForgotPassword.jsx` chỉ có một ô nhập mật khẩu |
| `BUG-FR03-004` | `FR-03:C5` | Regex kiểm tra mật khẩu ở frontend yêu cầu khoảng trắng thay vì ký tự đặc biệt | Medium | Open | `<Thêm link GitHub Issue>` | Regex thực tế: `flawedStrongPasswordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\s)[A-Za-z\d\s]{8,}$/` |

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
| `FR09-D-I-04` | `total_amount` | Không hợp lệ | Tổng tiền đơn hàng `< min_order_amount`. | Hệ thống từ chối và báo đơn hàng chưa đủ giá trị tối thiểu. | `FR-09:C3` |
| `FR09-D-V-03` | `user_id` | Hợp lệ | Người dùng đã đăng nhập, có JWT/user hợp lệ. | Hệ thống cho phép áp dụng coupon nếu các điều kiện khác hợp lệ. | `FR-09:C4` |
| `FR09-D-I-05` | `user_id` | Không hợp lệ | Người dùng chưa đăng nhập hoặc không gửi user/token. | Hệ thống phải từ chối áp dụng coupon. | `FR-09:C4` |
| `FR09-D-V-04` | `usage_count` | Hợp lệ | `usage_count < max_uses_per_user`. | Coupon được áp dụng. | `FR-09:C5` |
| `FR09-D-I-06` | `usage_count` | Không hợp lệ | `usage_count >= max_uses_per_user`. | Hệ thống từ chối vì user đã đạt giới hạn sử dụng. | `FR-09:C5` |
| `FR09-D-V-05` | `discount_type = fixed` | Hợp lệ | Coupon giảm giá cố định, ví dụ `BIGBUY`. | `discount_amount = discount_value`. | `FR-09:C7`, `FR-09:C8` |
| `FR09-D-V-06` | `discount_type = percent` | Hợp lệ | Coupon giảm theo phần trăm, ví dụ `SAVE10`. | `discount_amount = total × discount_value / 100`. | `FR-09:C6`, `FR-09:C8` |

### 7.3.3 Test case Domain Testing

| Test Case ID | Domain ID liên quan | Tiêu đề | Điều kiện tiên quyết | Dữ liệu đầu vào | Các bước thực hiện | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Minh chứng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `FR09-DT-01` | `FR09-D-V-01`, `FR09-D-V-02`, `FR09-D-V-03`, `FR09-D-V-04`, `FR09-D-V-06` | Áp dụng coupon phần trăm hợp lệ `SAVE10` | SUT đang chạy; coupon `SAVE10` tồn tại; user hợp lệ. | `code = SAVE10`<br>`total = 300000`<br>`user_id = 2` | 1. Gửi yêu cầu apply coupon với `SAVE10`.<br>2. Quan sát phản hồi. | Coupon được áp dụng vì total bằng min order. Discount phải là `30000`, final amount là `270000`. | API trả lỗi `Đơn hàng chưa đủ giá trị tối thiểu 300.000 ₫ để áp dụng mã này`. | Failed | `evidence/FR09-DT-01-api-log.txt` |
| `FR09-DT-02` | `FR09-D-I-01` | Áp dụng coupon không tồn tại | SUT đang chạy. | `code = FAKE123`<br>`total = 500000`<br>`user_id = 2` | 1. Nhập coupon không tồn tại.<br>2. Gửi yêu cầu apply coupon. | Hệ thống từ chối coupon không tồn tại hoặc inactive. | API trả `{"error":"Mã giảm giá không tồn tại hoặc đã bị vô hiệu hóa"}` với HTTP 404. | Passed | `evidence/FR09-DT-02-api-log.txt` |
| `FR09-DT-03` | `FR09-D-I-02` | Áp dụng coupon đã hết hạn | SUT đang chạy; coupon `EXPIRED` tồn tại. | `code = EXPIRED`<br>`total = 500000`<br>`user_id = 2` | 1. Nhập coupon hết hạn.<br>2. Gửi yêu cầu apply coupon. | Hệ thống từ chối và báo mã giảm giá đã hết hạn. | API trả `{"error":"Mã giảm giá đã hết hạn"}` với HTTP 400. | Passed | `evidence/FR09-DT-03-api-log.txt` |
| `FR09-DT-04` | `FR09-D-I-04` | Áp dụng coupon khi tổng tiền dưới mức tối thiểu | SUT đang chạy; coupon `SAVE10` tồn tại. | `code = SAVE10`<br>`total = 200000`<br>`user_id = 2` | 1. Nhập coupon `SAVE10`.<br>2. Gửi request với total dưới `300000`.<br>3. Quan sát phản hồi. | Hệ thống từ chối vì đơn hàng chưa đủ giá trị tối thiểu. | API trả `{"error":"Đơn hàng chưa đủ giá trị tối thiểu 300.000 ₫ để áp dụng mã này"}`. | Passed | `evidence/FR09-DT-04-api-log.txt` |
| `FR09-DT-05` | `FR09-D-I-05`, `FR09-D-V-06` | Áp dụng coupon khi chưa đăng nhập | SUT đang chạy; không gửi user/token hợp lệ. | `code = SAVE10`<br>`total = 500000`<br>`user_id = null` | 1. Không đăng nhập.<br>2. Gửi yêu cầu apply coupon.<br>3. Quan sát phản hồi. | Hệ thống phải từ chối vì người dùng chưa đăng nhập. | API vẫn áp dụng coupon và trả `{"success":true,"coupon_id":1,"discount_amount":-4500000,"final_amount":5000000}`. | Failed | `evidence/FR09-DT-05-api-log.txt` |
| `FR09-DT-06` | `FR09-D-I-06` | Áp dụng coupon khi đã đạt giới hạn sử dụng | Cần có user đã dùng `SAVE10` đủ số lần. | `code = SAVE10`<br>`total = 500000`<br>`user_id = 2` | 1. Dùng coupon `SAVE10` đến giới hạn.<br>2. Thử áp dụng lại coupon.<br>3. Quan sát phản hồi. | Hệ thống từ chối vì user đã đạt giới hạn sử dụng. | Hệ thống thông báo đã đạt giới hạn | Passed |  |
| `FR09-DT-07` | `FR09-D-V-01`, `FR09-D-V-02`, `FR09-D-V-05` | Áp dụng coupon fixed hợp lệ `BIGBUY` | SUT đang chạy; coupon `BIGBUY` tồn tại. | `code = BIGBUY`<br>`total = 600000`<br>`user_id = 2` | 1. Nhập coupon `BIGBUY`.<br>2. Gửi yêu cầu apply coupon.<br>3. Quan sát discount và final amount. | Hệ thống giảm cố định `50000`, final amount là `550000`. | API trả `{"success":true,"coupon_id":2,"discount_amount":50000,"final_amount":550000}`. | Passed | `evidence/FR09-DT-07-api-log.txt` |
| `FR09-DT-08` | `FR09-D-V-01`, `FR09-D-V-02`, `FR09-D-V-04`, `FR09-D-V-05` | Áp dụng coupon `VIP100` khi chưa vượt giới hạn | User chưa dùng `VIP100` quá giới hạn. | `code = VIP100`<br>`total = 500000`<br>`user_id = 2` | 1. Nhập coupon `VIP100`.<br>2. Gửi yêu cầu apply coupon.<br>3. Quan sát phản hồi. | Nếu user chưa vượt giới hạn, coupon được áp dụng và giảm `100000`. | API trả lỗi `Bạn đã sử dụng mã này 2 lần (đã đạt giới hạn)`. | Failed | `evidence/FR09-DT-08-api-log.txt` |
| `FR09-DT-09` | `FR09-D-V-02` | Áp dụng coupon khi total bằng đúng min order | SUT đang chạy; coupon `SAVE10` có min order `300000`. | `code = SAVE10`<br>`total = 300000`<br>`user_id = 2` | 1. Nhập coupon `SAVE10`.<br>2. Đặt total đúng bằng `300000`.<br>3. Gửi yêu cầu apply coupon. | Hệ thống phải chấp nhận vì requirement là `total >= min_order_amount`. | API trả lỗi `Đơn hàng chưa đủ giá trị tối thiểu 300.000 ₫ để áp dụng mã này`. | Failed | `evidence/FR09-DT-09-api-log.txt` |
| `FR09-DT-10` | `FR09-D-I-03` | Bỏ trống mã giảm giá | SUT đang chạy. | `code = empty`<br>`total = 500000`<br>`user_id = 2` | 1. Không nhập mã giảm giá.<br>2. Gửi yêu cầu apply coupon.<br>3. Quan sát phản hồi. | Hệ thống từ chối và yêu cầu nhập mã giảm giá. | API trả `{"error":"Vui lòng nhập mã giảm giá"}` với HTTP 400. | Passed | `evidence/FR09-DT-10-api-log.txt` |

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
| `FR09-BVA-01` | `FR09-B-001` | `SAVE10` với total nhỏ hơn min order | SUT đang chạy; coupon `SAVE10` tồn tại. | `code = SAVE10`<br>`total = 299999`<br>`user_id = null` | 1. Gửi yêu cầu apply coupon với total `299999`.<br>2. Quan sát phản hồi. | Hệ thống từ chối vì chưa đủ giá trị tối thiểu. | API trả lỗi `Đơn hàng chưa đủ giá trị tối thiểu 300.000 ₫ để áp dụng mã này`. | Passed | `evidence/FR09-BVA-01-api-log.txt` |
| `FR09-BVA-02` | `FR09-B-002` | `SAVE10` với total bằng min order | SUT đang chạy; coupon `SAVE10` tồn tại. | `code = SAVE10`<br>`total = 300000`<br>`user_id = null` | 1. Gửi yêu cầu apply coupon với total `300000`.<br>2. Quan sát phản hồi. | Hệ thống phải chấp nhận vì total bằng min order. | API trả lỗi `Đơn hàng chưa đủ giá trị tối thiểu 300.000 ₫ để áp dụng mã này`. | Failed | `evidence/FR09-BVA-02-api-log.txt` |
| `FR09-BVA-03` | `FR09-B-003` | `SAVE10` với total lớn hơn min order | SUT đang chạy; coupon `SAVE10` tồn tại. | `code = SAVE10`<br>`total = 300001`<br>`user_id = null` | 1. Gửi yêu cầu apply coupon với total `300001`.<br>2. Quan sát discount và final amount. | Coupon được áp dụng; discount phải là khoảng `30000.1`, final amount khoảng `270000.9`. | API trả `discount_amount = -2700009`, `final_amount = 3000010`. | Failed | `evidence/FR09-BVA-03-api-log.txt` |
| `FR09-BVA-04` | `FR09-B-004` | `BIGBUY` với total nhỏ hơn min order | SUT đang chạy; coupon `BIGBUY` tồn tại. | `code = BIGBUY`<br>`total = 499999`<br>`user_id = null` | 1. Gửi yêu cầu apply coupon với total `499999`.<br>2. Quan sát phản hồi. | Hệ thống từ chối vì chưa đủ giá trị tối thiểu. | API trả lỗi `Đơn hàng chưa đủ giá trị tối thiểu 500.000 ₫ để áp dụng mã này`. | Passed | `evidence/FR09-BVA-04-api-log.txt` |
| `FR09-BVA-05` | `FR09-B-005` | `BIGBUY` với total bằng min order | SUT đang chạy; coupon `BIGBUY` tồn tại. | `code = BIGBUY`<br>`total = 500000`<br>`user_id = null` | 1. Gửi yêu cầu apply coupon với total `500000`.<br>2. Quan sát phản hồi. | Hệ thống phải chấp nhận vì total bằng min order. | API trả lỗi `Đơn hàng chưa đủ giá trị tối thiểu 500.000 ₫ để áp dụng mã này`. | Failed | `evidence/FR09-BVA-05-api-log.txt` |
| `FR09-BVA-06` | `FR09-B-006` | `BIGBUY` với total lớn hơn min order | SUT đang chạy; coupon `BIGBUY` tồn tại. | `code = BIGBUY`<br>`total = 500001`<br>`user_id = null` | 1. Gửi yêu cầu apply coupon với total `500001`.<br>2. Quan sát discount và final amount. | Coupon được áp dụng; discount `50000`, final amount `450001`. | API trả `{"success":true,"coupon_id":2,"discount_amount":50000,"final_amount":450001}`. | Passed | `evidence/FR09-BVA-06-api-log.txt` |
| `FR09-BVA-07` | `FR09-B-007` | `VIP100` tại giới hạn sử dụng | User đã dùng `VIP100` đủ 2 lần. | `code = VIP100`<br>`total = 500000`<br>`user_id = 2` | 1. Gửi yêu cầu apply coupon `VIP100` với user đã đạt giới hạn.<br>2. Quan sát phản hồi. | Hệ thống từ chối vì user đã đạt giới hạn sử dụng. | API trả `{"error":"Bạn đã sử dụng mã này 2 lần (đã đạt giới hạn)"}`. | Passed | `evidence/FR09-BVA-07-api-log.txt` |
| `FR09-BVA-08` | `FR09-B-008` | `VIP100` khi chưa đạt giới hạn sử dụng | Dùng request không có user tracking. | `code = VIP100`<br>`total = 500000`<br>`user_id = null` | 1. Gửi yêu cầu apply coupon `VIP100` không kèm user.<br>2. Quan sát phản hồi. | Nếu user hợp lệ và usage count là `1`, coupon được áp dụng. | API trả `{"success":true,"coupon_id":3,"discount_amount":100000,"final_amount":400000}`. | Passed | `evidence/FR09-BVA-08-api-log.txt` |

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

| Bug ID | Test case liên quan | Tiêu đề | Mức độ nghiêm trọng | Trạng thái | Link GitHub Issue | Minh chứng |
| --- | --- | --- | --- | --- | --- | --- |
| `BUG-FR09-001` | `FR09-DT-01`, `FR09-DT-09`, `FR09-BVA-02`, `FR09-BVA-05` | Coupon bị từ chối khi tổng tiền bằng đúng `min_order_amount` | High | Open | `<Thêm link GitHub Issue>` | `evidence/FR09-DT-01-api-log.txt`, `evidence/FR09-DT-09-api-log.txt`, `evidence/FR09-BVA-02-api-log.txt`, `evidence/FR09-BVA-05-api-log.txt` |
| `BUG-FR09-002` | `FR09-DT-05`, `FR09-BVA-03` | Công thức tính coupon phần trăm sai, tạo discount âm và final amount tăng bất thường | High | Open | `<Thêm link GitHub Issue>` | `evidence/FR09-DT-05-api-log.txt`, `evidence/FR09-BVA-03-api-log.txt` |
| `BUG-FR09-003` | `FR09-DT-05`, `FR09-BVA-08` | API vẫn cho áp dụng coupon khi không có user/token hợp lệ | High | Open | `<Thêm link GitHub Issue>` | `evidence/FR09-DT-05-api-log.txt`, `evidence/FR09-BVA-08-api-log.txt` |
| `BUG-FR09-004` | `FR09-BVA-08` | Có thể bypass kiểm tra giới hạn sử dụng coupon khi không gửi `user_id` | Medium | Open | `<Thêm link GitHub Issue>` | `evidence/FR09-BVA-08-api-log.txt` |
| `BUG-FR09-005` | `FR09-DT-08` | Test data của user đã bị nhiễm trạng thái sử dụng `VIP100`, khiến first-use scenario không kiểm thử được chính xác | Low | Open | `<Thêm link GitHub Issue>` | `evidence/FR09-DT-08-api-log.txt` |

# 8. Báo cáo tính năng C

> Thay phần này bằng tính năng bạn chọn từ Pool C. Có thể sử dụng cùng cấu trúc với tính năng A.

## 8.1 Thông tin tính năng

| Mục | Thông tin |
| --- | --- |
| Mã tính năng | `<FR-xx>` |
| Tên tính năng | `<Tên tính năng>` |
| Nhóm tính năng | `Pool C` |
| Vai trò liên quan | `<Guest / Customer / Admin>` |
| Vị trí trên UI | `<Trang / route>` |
| API endpoint liên quan | `<Danh sách endpoint>` |

## 8.2 Mô tả tính năng

`<Mô tả hành vi của tính năng bằng lời của bạn.>`

## 8.3 Cơ sở kiểm thử riêng của tính năng

| Basis ID | Nguồn | Vị trí | Yêu cầu / Quy tắc | Điểm mơ hồ hoặc ghi chú |
| --- | --- | --- | --- | --- |
| `<C-BASIS-01>` | `<Nguồn>` | `<Vị trí>` | `<Yêu cầu / quy tắc>` | `<Ghi chú>` |

## 8.4 Domain Testing

### 8.4.1 Biến miền và ràng buộc

| Variable ID | Biến / Trạng thái | Kiểu / Đơn vị | Ràng buộc / Phụ thuộc | Kết quả có thể quan sát | Basis ID |
| --- | --- | --- | --- | --- | --- |
| `<C-VAR-01>` | `<Biến>` | `<Kiểu>` | `<Ràng buộc>` | `<Kết quả>` | `<Basis ID>` |

### 8.4.2 Miền hợp lệ và không hợp lệ

| Domain ID | Biến / Quy tắc | Loại miền | Định nghĩa miền | Hành vi mong đợi | Basis ID |
| --- | --- | --- | --- | --- | --- |
| `<C-D-V-01>` | `<Biến>` | `Hợp lệ` | `<Định nghĩa>` | `<Hành vi mong đợi>` | `<Basis ID>` |
| `<C-D-I-01>` | `<Biến>` | `Không hợp lệ` | `<Định nghĩa>` | `<Hành vi mong đợi>` | `<Basis ID>` |

### 8.4.3 Test case Domain Testing

| Test Case ID | Domain ID liên quan | Tiêu đề | Tiền điều kiện | Dữ liệu đầu vào | Các bước thực hiện | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Minh chứng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `<C-DT-001>` | `<Domain IDs>` | `<Tiêu đề>` | `<Tiền điều kiện>` | `<Input>` | `<Steps>` | `<Expected>` | `<Actual>` | `<Status>` | `<Screenshot / Video / Log>` |

### 8.4.4 Tổng kết Domain Testing

| Chỉ số | Số lượng |
| --- | ---: |
| Tổng số test case Domain Testing | `<Số lượng>` |
| Passed | `<Số lượng>` |
| Failed | `<Số lượng>` |
| Blocked | `<Số lượng>` |
| Not Executed | `<Số lượng>` |
| Needs Review | `<Số lượng>` |

## 8.5 Boundary Value Analysis

### 8.5.1 Biến có giá trị biên

| Boundary Variable ID | Biến | Quy tắc biên | Giá trị nhỏ nhất | Giá trị lớn nhất | Giá trị bình thường | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| `<C-BVAR-01>` | `<Biến>` | `<Quy tắc>` | `<Min>` | `<Max>` | `<Normal>` | `<Ghi chú>` |

### 8.5.2 Giá trị biên

| Boundary ID | Biến | Loại biên | Giá trị | Hành vi mong đợi | Basis ID |
| --- | --- | --- | --- | --- | --- |
| `<C-B-001>` | `<Biến>` | `<min-1 / min / min+1 / max-1 / max / max+1>` | `<Giá trị>` | `<Mong đợi>` | `<Basis ID>` |

### 8.5.3 Test case BVA

| Test Case ID | Boundary ID liên quan | Tiêu đề | Tiền điều kiện | Dữ liệu đầu vào | Các bước thực hiện | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Minh chứng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `<C-BVA-001>` | `<Boundary IDs>` | `<Tiêu đề>` | `<Tiền điều kiện>` | `<Input>` | `<Steps>` | `<Expected>` | `<Actual>` | `<Status>` | `<Screenshot / Video / Log>` |

### 8.5.4 Tổng kết BVA

| Chỉ số | Số lượng |
| --- | ---: |
| Tổng số test case BVA | `<Số lượng>` |
| Passed | `<Số lượng>` |
| Failed | `<Số lượng>` |
| Blocked | `<Số lượng>` |
| Not Executed | `<Số lượng>` |
| Needs Review | `<Số lượng>` |

## 8.6 Lỗi phát hiện ở tính năng C

| Bug ID | Test case liên quan | Tiêu đề | Mức độ nghiêm trọng | Trạng thái | Link GitHub Issue | Minh chứng |
| --- | --- | --- | --- | --- | --- | --- |
| `<BUG-C-001>` | `<TC ID>` | `<Tiêu đề lỗi>` | `<Low / Medium / High / Critical>` | `<Open / Closed>` | `<Link>` | `<Screenshot / Video>` |

---

# 9. Báo cáo tính năng D

> Thay phần này bằng tính năng bạn chọn từ Pool D.

## 9.1 Thông tin tính năng

| Mục | Thông tin |
| --- | --- |
| Mã tính năng | `<FR-xx>` |
| Tên tính năng | `<Tên tính năng>` |
| Nhóm tính năng | `Pool D` |
| Vai trò liên quan | `<Guest / Customer / Admin>` |
| Vị trí trên UI | `<Trang / route>` |
| API endpoint liên quan | `<Danh sách endpoint>` |
| Nền tảng mobile | `<Android / iOS / Emulator / mô phỏng bằng trình duyệt>` |

## 9.2 Mô tả tính năng

`<Mô tả hành vi của tính năng bằng lời của bạn.>`

## 9.3 Cơ sở kiểm thử riêng của tính năng

| Basis ID | Nguồn | Vị trí | Yêu cầu / Quy tắc | Điểm mơ hồ hoặc ghi chú |
| --- | --- | --- | --- | --- |
| `<D-BASIS-01>` | `<Nguồn>` | `<Vị trí>` | `<Yêu cầu / quy tắc>` | `<Ghi chú>` |

## 9.4 Domain Testing

### 9.4.1 Biến miền và ràng buộc

| Variable ID | Biến / Trạng thái | Kiểu / Đơn vị | Ràng buộc / Phụ thuộc | Kết quả có thể quan sát | Basis ID |
| --- | --- | --- | --- | --- | --- |
| `<D-VAR-01>` | `<Biến>` | `<Kiểu>` | `<Ràng buộc>` | `<Kết quả>` | `<Basis ID>` |

### 9.4.2 Miền hợp lệ và không hợp lệ

| Domain ID | Biến / Quy tắc | Loại miền | Định nghĩa miền | Hành vi mong đợi | Basis ID |
| --- | --- | --- | --- | --- | --- |
| `<D-D-V-01>` | `<Biến>` | `Hợp lệ` | `<Định nghĩa>` | `<Hành vi mong đợi>` | `<Basis ID>` |
| `<D-D-I-01>` | `<Biến>` | `Không hợp lệ` | `<Định nghĩa>` | `<Hành vi mong đợi>` | `<Basis ID>` |

### 9.4.3 Test case Domain Testing

| Test Case ID | Domain ID liên quan | Tiêu đề | Tiền điều kiện | Dữ liệu đầu vào | Các bước thực hiện | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Minh chứng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `<D-DT-001>` | `<Domain IDs>` | `<Tiêu đề>` | `<Tiền điều kiện>` | `<Input>` | `<Steps>` | `<Expected>` | `<Actual>` | `<Status>` | `<Screenshot / Video / Log>` |

### 9.4.4 Tổng kết Domain Testing

| Chỉ số | Số lượng |
| --- | ---: |
| Tổng số test case Domain Testing | `<Số lượng>` |
| Passed | `<Số lượng>` |
| Failed | `<Số lượng>` |
| Blocked | `<Số lượng>` |
| Not Executed | `<Số lượng>` |
| Needs Review | `<Số lượng>` |

## 9.5 Boundary Value Analysis

### 9.5.1 Biến có giá trị biên

| Boundary Variable ID | Biến | Quy tắc biên | Giá trị nhỏ nhất | Giá trị lớn nhất | Giá trị bình thường | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| `<D-BVAR-01>` | `<Biến>` | `<Quy tắc>` | `<Min>` | `<Max>` | `<Normal>` | `<Ghi chú>` |

### 9.5.2 Giá trị biên

| Boundary ID | Biến | Loại biên | Giá trị | Hành vi mong đợi | Basis ID |
| --- | --- | --- | --- | --- | --- |
| `<D-B-001>` | `<Biến>` | `<min-1 / min / min+1 / max-1 / max / max+1>` | `<Giá trị>` | `<Mong đợi>` | `<Basis ID>` |

### 9.5.3 Test case BVA

| Test Case ID | Boundary ID liên quan | Tiêu đề | Tiền điều kiện | Dữ liệu đầu vào | Các bước thực hiện | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Minh chứng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `<D-BVA-001>` | `<Boundary IDs>` | `<Tiêu đề>` | `<Tiền điều kiện>` | `<Input>` | `<Steps>` | `<Expected>` | `<Actual>` | `<Status>` | `<Screenshot / Video / Log>` |

### 9.5.4 Tổng kết BVA

| Chỉ số | Số lượng |
| --- | ---: |
| Tổng số test case BVA | `<Số lượng>` |
| Passed | `<Số lượng>` |
| Failed | `<Số lượng>` |
| Blocked | `<Số lượng>` |
| Not Executed | `<Số lượng>` |
| Needs Review | `<Số lượng>` |

## 9.6 Lỗi phát hiện ở tính năng D

| Bug ID | Test case liên quan | Tiêu đề | Mức độ nghiêm trọng | Trạng thái | Link GitHub Issue | Minh chứng |
| --- | --- | --- | --- | --- | --- | --- |
| `<BUG-D-001>` | `<TC ID>` | `<Tiêu đề lỗi>` | `<Low / Medium / High / Critical>` | `<Open / Closed>` | `<Link>` | `<Screenshot / Video>` |

---

# 10. Tổng kết kiểm thử

## 10.1 Tổng kết test case theo tính năng

| Tính năng | TC Domain Testing | TC BVA | Tổng TC | Passed | Failed | Blocked | Not Executed | Needs Review |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Feature A | `<Số lượng>` | `<Số lượng>` | `<Số lượng>` | `<Số lượng>` | `<Số lượng>` | `<Số lượng>` | `<Số lượng>` | `<Số lượng>` |
| Feature B | `<Số lượng>` | `<Số lượng>` | `<Số lượng>` | `<Số lượng>` | `<Số lượng>` | `<Số lượng>` | `<Số lượng>` | `<Số lượng>` |
| Feature C | `<Số lượng>` | `<Số lượng>` | `<Số lượng>` | `<Số lượng>` | `<Số lượng>` | `<Số lượng>` | `<Số lượng>` | `<Số lượng>` |
| Feature D | `<Số lượng>` | `<Số lượng>` | `<Số lượng>` | `<Số lượng>` | `<Số lượng>` | `<Số lượng>` | `<Số lượng>` | `<Số lượng>` |
| **Tổng cộng** | `<Số lượng>` | `<Số lượng>` | `<Số lượng>` | `<Số lượng>` | `<Số lượng>` | `<Số lượng>` | `<Số lượng>` | `<Số lượng>` |

## 10.2 Tổng kết thực thi

`<Tóm tắt trạng thái thực thi tổng thể, các phát hiện chính và các giới hạn còn lại.>`

## 10.3 Tổng kết minh chứng

| Evidence ID | Tính năng liên quan | Test case liên quan | Loại minh chứng | File / Link | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| `<EVD-001>` | `<Tính năng>` | `<TC ID>` | `<Screenshot / Video / Log>` | `<Path / URL>` | `<Ghi chú>` |

---

# 11. Báo cáo lỗi tổng hợp

## 11.1 Tổng kết lỗi theo mức độ nghiêm trọng

| Mức độ nghiêm trọng | Số lượng |
| --- | ---: |
| Critical | `<Số lượng>` |
| High | `<Số lượng>` |
| Medium | `<Số lượng>` |
| Low | `<Số lượng>` |
| **Tổng cộng** | `<Số lượng>` |

## 11.2 Danh sách lỗi

| Bug ID | Tính năng | Test case liên quan | Tiêu đề | Mức độ nghiêm trọng | Kết quả thực tế | Kết quả mong đợi | Link GitHub Issue | Trạng thái |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `<BUG-001>` | `<Tính năng>` | `<TC ID>` | `<Tiêu đề lỗi>` | `<Severity>` | `<Actual>` | `<Expected>` | `<Link>` | `<Status>` |

## 11.3 Mẫu mô tả chi tiết lỗi

### `<BUG-001>` – `<Tiêu đề lỗi>`

| Mục | Thông tin |
| --- | --- |
| Tính năng | `<Feature ID / tên tính năng>` |
| Test case liên quan | `<Test Case ID>` |
| Mức độ nghiêm trọng | `<Low / Medium / High / Critical>` |
| Độ ưu tiên | `<Low / Medium / High>` |
| Môi trường | `<Browser / OS / URL / commit>` |
| GitHub Issue | `<Link>` |
| Minh chứng | `<Screenshot / video / log>` |

#### Tiền điều kiện

`<Tiền điều kiện>`

#### Các bước tái hiện lỗi

1. `<Bước 1>`
2. `<Bước 2>`
3. `<Bước 3>`

#### Kết quả mong đợi

`<Kết quả mong đợi>`

#### Kết quả thực tế

`<Kết quả thực tế>`

#### Ghi chú

`<Ghi chú bổ sung>`

---

# 12. Tài liệu minh chứng

## 12.1 Ảnh chụp màn hình

| Screenshot ID | Tính năng | Test case / Bug liên quan | Đường dẫn file | Mô tả |
| --- | --- | --- | --- | --- |
| `<IMG-001>` | `<Tính năng>` | `<TC / Bug ID>` | `<Path>` | `<Mô tả>` |

## 12.2 Video

| Video ID | Tính năng | Test case / Bug liên quan | URL | Mô tả |
| --- | --- | --- | --- | --- |
| `<VID-001>` | `<Tính năng>` | `<TC / Bug ID>` | `<YouTube / Drive link>` | `<Mô tả>` |

## 12.3 Script kiểm thử

| Script ID | Tính năng | Mục đích | Đường dẫn file | Cách chạy |
| --- | --- | --- | --- | --- |
| `<SCRIPT-001>` | `<Tính năng>` | `<Mục đích>` | `<Path>` | `<Command>` |

## 12.4 File hỗ trợ khác

| File | Mục đích | Vị trí |
| --- | --- | --- |
| `<Tên file>` | `<Mục đích>` | `<Path>` |

---

# 13. Khai báo sử dụng AI

## 13.1 Khai báo

Chọn một trong hai lựa chọn sau và xóa lựa chọn không sử dụng.

### Lựa chọn A — Có sử dụng AI

Tôi có sử dụng công cụ AI cho các công việc sau trong bài tập này:

- `<Công việc 1>`
- `<Công việc 2>`
- `<Công việc 3>`

Tất cả output do AI tạo ra đã được tôi review, chỉnh sửa và xác nhận trước khi đưa vào bài nộp.

### Lựa chọn B — Không sử dụng AI

Tôi không sử dụng bất kỳ sự hỗ trợ nào từ AI trong bài tập này.

## 13.2 Công cụ AI đã sử dụng

| Công cụ | Phiên bản / Model | Mục đích | Khoảng thời gian sử dụng | Ghi chú |
| --- | --- | --- | --- | --- |
| `<AI tool>` | `<Model / version>` | `<Mục đích>` | `<Khoảng thời gian>` | `<Ghi chú>` |

---

# 14. Phân tích thiếu sót của AI

## 14.1 Tổng hợp thiếu sót

| Gap ID | Tính năng | Loại thiếu sót | Vấn đề trong output của AI | Phần sinh viên chỉnh sửa | Ảnh hưởng | Test case / Bug liên quan |
| --- | --- | --- | --- | --- | --- | --- |
| `<GAP-001>` | `<Tính năng>` | `<Thiếu TC / Sai expected result / Miền chưa đầy đủ / Khác>` | `<AI đã tạo gì>` | `<Bạn đã chỉnh gì>` | `<Ảnh hưởng>` | `<TC / Bug ID>` |

## 14.2 Phân tích chi tiết thiếu sót

### `<GAP-001>` – `<Tiêu đề thiếu sót>`

| Mục | Thông tin |
| --- | --- |
| Tính năng | `<Tính năng>` |
| Kỹ thuật liên quan | `<Domain Testing / BVA / Bug Reporting>` |
| Lỗi của AI | `<Mô tả lỗi>` |
| Lý do AI bỏ sót | `<Prompt chưa đủ / giới hạn của AI / tính năng phức tạp / thiếu ngữ cảnh>` |
| Phần sinh viên chỉnh sửa | `<Mô tả phần chỉnh sửa>` |
| Bài học rút ra | `<Bạn học được gì>` |

---

# 15. Nhận xét về AI

Viết đoạn nhận xét 200–300 từ tại đây.

`<Đoạn AI Critique>`

Các ý nên đề cập:

- AI sai, thiên lệch hoặc chưa đầy đủ ở điểm nào.
- Vì sao AI không phát hiện được vấn đề đó.
- Việc review của sinh viên đã cải thiện kết quả như thế nào.
- Bài học rút ra khi cộng tác với AI trong kiểm thử phần mềm.

---

# 16. Báo cáo nhật ký sử dụng AI

## 16.1 Nhật ký tương tác với AI

| Interaction ID | Công cụ AI | Ngày và giờ | Mục đích | File prompt / Tóm tắt prompt | File output / Tóm tắt output | Ghi chú review của sinh viên |
| --- | --- | --- | --- | --- | --- | --- |
| `<AI-LOG-001>` | `<Tool>` | `<Date time>` | `<Mục đích>` | `<Prompt / đường dẫn file>` | `<Output / đường dẫn file>` | `<Ghi chú review>` |

## 16.2 Mẫu prompt log

### `<AI-LOG-001>` – `<Tiêu đề tương tác>`

| Mục | Thông tin |
| --- | --- |
| Công cụ AI | `<Tên công cụ>` |
| Model / Phiên bản | `<Model>` |
| Ngày và giờ | `<Date time>` |
| Công việc | `<Task>` |

#### Prompt

```text
<Dán prompt của bạn vào đây>
```

#### Tóm tắt output của AI

`<Tóm tắt output hoặc link đến file output đầy đủ.>`

#### Review và chỉnh sửa của sinh viên

`<Mô tả phần bạn chấp nhận, từ chối, chỉnh sửa hoặc bổ sung.>`

---

# 17. Báo cáo Agent Skill

## 17.1 Tổng quan Agent Skill

| Mục | Thông tin |
| --- | --- |
| Tên skill | `<Tên skill>` |
| Mục đích | `<Mục đích>` |
| Input | `<Định dạng input>` |
| Output | `<Định dạng output>` |
| Vị trí | `<Path>` |

## 17.2 Video minh họa skill

| Demo ID | Tính năng | Link video | Mô tả |
| --- | --- | --- | --- |
| `<DEMO-001>` | `<Tính năng>` | `<YouTube link>` | `<Mô tả>` |

## 17.3 Giới hạn của skill

- `<Giới hạn 1>`
- `<Giới hạn 2>`
- `<Giới hạn 3>`

---

# 18. Nhật ký Git Commit

## 18.1 Tổng hợp commit

| Commit Hash | Ngày | Tính năng / Bước thực hiện | Commit message | Ghi chú |
| --- | --- | --- | --- | --- |
| `<hash>` | `<Date>` | `<Tính năng / bước>` | `<Commit message>` | `<Ghi chú>` |

## 18.2 Git commit log gốc

```text
<Dán output git log tại đây>
```

Lệnh gợi ý:

```bash
git log --oneline --decorate --graph --all
```

---

# 19. Tự đánh giá

| STT | Tiêu chí | Điểm tối đa | Điểm tự đánh giá | Giải thích |
| --- | --- | ---: | ---: | --- |
| 1 | Tính năng A: Domain Testing + Boundary Value Analysis | 25 | `<Điểm>` | `<Giải thích>` |
| 2 | Tính năng B: Domain Testing + Boundary Value Analysis | 25 | `<Điểm>` | `<Giải thích>` |
| 3 | Tính năng C: Domain Testing + Boundary Value Analysis | 25 | `<Điểm>` | `<Giải thích>` |
| 4 | Tính năng D: Mobile, Domain Testing + Boundary Value Analysis | 15 | `<Điểm>` | `<Giải thích>` |
| 5 | Agent Skills | 10 | `<Điểm>` | `<Giải thích>` |
| **Tổng cộng** |  | **100** | `<Tổng điểm>` |  |

---

# 20. Checklist nộp bài

| Hạng mục | Bắt buộc | Đã hoàn thành | Vị trí / Ghi chú |
| --- | --- | --- | --- |
| Báo cáo chính dạng Markdown | Có | `<Có / Không>` | `<Path>` |
| Báo cáo chính dạng PDF | Có | `<Có / Không>` | `<Path>` |
| Báo cáo Domain Testing | Có | `<Có / Không>` | `<Section / Path>` |
| Báo cáo Boundary Value Analysis | Có | `<Có / Không>` | `<Section / Path>` |
| Báo cáo lỗi có ảnh minh chứng | Có | `<Có / Không>` | `<GitHub Issues / Path>` |
| AI Critique | Có | `<Có / Không>` | `<Section / Path>` |
| AI Audit Report | Có | `<Có / Không>` | `<Section / Path>` |
| Git commit log | Có | `<Có / Không>` | `<Path>` |
| README có self-assessment và test summary | Có | `<Có / Không>` | `<Path>` |
| Video demo | Nếu có áp dụng | `<Có / Không>` | `<Links>` |
| Tài liệu hỗ trợ khác | Nếu có áp dụng | `<Có / Không>` | `<Path>` |

---

# 21. Tài liệu tham khảo

- ISTQB Foundation Level Syllabus, phiên bản mới nhất.
- EShop SUT Repository: `https://github.com/ttbhanh/eshop-sut`
- `<Tài liệu tham khảo khác>`

---

# Phụ lục A. Bảng test case đầy đủ

Sử dụng phụ lục này nếu bảng test case trong báo cáo chính quá dài.

## A.1 Test case đầy đủ của tính năng A

`<Dán bảng test case đầy đủ hoặc link đến file.>`

## A.2 Test case đầy đủ của tính năng B

`<Dán bảng test case đầy đủ hoặc link đến file.>`

## A.3 Test case đầy đủ của tính năng C

`<Dán bảng test case đầy đủ hoặc link đến file.>`

## A.4 Test case đầy đủ của tính năng D

`<Dán bảng test case đầy đủ hoặc link đến file.>`

---

# Phụ lục B. Nhật ký AI đầy đủ

`<Dán hoặc link đến toàn bộ nhật ký tương tác với AI tại đây.>`
