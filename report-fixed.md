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
| `FR03-DT-01` | `FR03-D-V-01` | Yêu cầu đặt lại mật khẩu với email đã đăng ký | SUT đang chạy; tài khoản `gmail` tồn tại. | `email = gmail` | 1. Mở `/forgot-password`.<br>2. Nhập email đã đăng ký.<br>3. Gửi yêu cầu. | Hệ thống tạo OTP/reset token và hiển thị trên màn hình. | API trả `{"message":"Mã đặt lại mật khẩu đã được tạo","resetToken":"5143"}`. | Passed | `evidence/FR03-DT-01-api-log.txt` |
| `FR03-DT-02` | `FR03-D-I-01` | Yêu cầu đặt lại mật khẩu với email chưa đăng ký | SUT đang chạy. | `email = hello@gmail` | 1. Mở `/forgot-password`.<br>2. Nhập email chưa đăng ký.<br>3. Gửi yêu cầu. | Hệ thống từ chối và báo lỗi người dùng không tồn tại. | Hệ thống trả `{"error":"User not found"}` với HTTP 404. | Passed | `evidence/FR03-DT-02-api-log.txt` |
| `FR03-DT-03` | `FR03-D-I-02` | Bỏ trống email khi yêu cầu đặt lại mật khẩu | SUT đang chạy; kiểm thử cần thực hiện qua UI. | `email = empty` | 1. Mở `/forgot-password`.<br>2. Để trống email.<br>3. Nhấn submit. | Trình duyệt hoặc hệ thống chặn submit và yêu cầu nhập email. | Hệ thống yêu cầu điền vào trường | Passed |  |
| `FR03-DT-04` | `FR03-D-V-01`, `FR03-D-V-02`, `FR03-D-V-03` | Đặt lại mật khẩu thành công với email, OTP và mật khẩu mạnh hợp lệ | Đã tạo OTP cho `gmail`. | `email = gmail`<br>`resetToken = 7508`<br>`newPassword = NewPass123!` | 1. Gửi yêu cầu quên mật khẩu để lấy OTP.<br>2. Nhập đúng OTP.<br>3. Nhập mật khẩu mới mạnh.<br>4. Gửi yêu cầu đặt lại mật khẩu. | Hệ thống đặt lại mật khẩu thành công và chuyển về trang đăng nhập. | Hệ thống báo "Mật khẩu quá yếu!" | Failed | `evidence/FR03-DT-04-api-log.txt` |
| `FR03-DT-05` | `FR03-D-I-03` | Đặt lại mật khẩu với OTP sai | Đã có email hợp lệ. | `email = gmail`<br>`resetToken = 0000`<br>`newPassword = Password 1` | 1. Nhập email hợp lệ.<br>2. Nhập OTP sai.<br>3. Nhập mật khẩu mạnh.<br>4. Gửi yêu cầu đặt lại mật khẩu. | Hệ thống từ chối OTP sai. | API trả `{"error":"Invalid token or email"}` với HTTP 400. | Passed | `evidence/FR03-DT-05-api-log.txt` |
| `FR03-DT-06` | `FR03-D-I-05` | Đặt lại mật khẩu với mật khẩu yếu | Đã tạo OTP hợp lệ cho `gmail`. | `email = gmail`<br>`resetToken = 2420`<br>`newPassword = weak` | 1. Tạo OTP hợp lệ.<br>2. Nhập OTP đúng.<br>3. Nhập mật khẩu yếu.<br>4. Gửi yêu cầu đặt lại mật khẩu thông qua API. | Hệ thống phải từ chối mật khẩu yếu. | API trả `{"message":"Password reset successfully"}` — backend chấp nhận mật khẩu yếu. | Failed | `evidence/FR03-DT-06-api-log.txt` |
| `FR03-DT-07` | `FR03-D-I-04` | Dùng OTP của email khác để đặt lại mật khẩu | Có OTP được tạo từ tài khoản admin. | `email = gmail`<br>`resetToken = 6480` từ admin<br>`newPassword = Password 1!` | 1. Tạo OTP cho tài khoản admin.<br>2. Dùng OTP đó cho email `gmail`.<br>3. Gửi yêu cầu đặt lại mật khẩu. | Hệ thống từ chối vì OTP không thuộc email hiện tại. | API trả `{"error":"Invalid token or email"}` với HTTP 400. | Passed | `evidence/FR03-DT-07-api-log.txt` |
| `FR03-DT-08` | `FR03-D-V-05` | Reset mật khẩu | SUT đang chạy |  | 1. Nhấn vào Quên mật khẩu ? <br> 2. Quan sát chỉ báo bước. | Hệ thống hiển thị chỉ báo bước đúng | Không thấy chỉ báo bước | Failed | `evidence/FR03-DT-07-api-log.txt` |

### 6.3.4 Tổng kết Domain Testing

| Chỉ số | Số lượng |
| --- | ---: |
| Tổng số test case Domain Testing | 8 |
| Passed | 5 |
| Failed | 3 |
| Blocked | 0 |
| Not Executed | 0 |
| Needs Review | 0 |

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
| `FR03-BVA-01` | `FR03-B-001` | OTP nhỏ hơn biên dưới | SUT đang chạy. | `email = gmail.com`<br>`resetToken = 999`<br>`newPassword = NewPass123!` | 1. Gửi yêu cầu reset với OTP `99999`.<br>2. Quan sát phản hồi. | Hệ thống từ chối OTP ngoài miền. | API trả `{"error":"Invalid token or email"}` với HTTP 400. | Passed | `evidence/FR03-BVA-01-api-log.txt` |
| `FR03-BVA-02` | `FR03-B-002` | OTP tại biên dưới `100000` | Đang ở reset password bước 2 | `resetToken = 100000` | 1. Đặt token của user thành `100000` .<br>2. Gửi yêu cầu reset với token này. | Token được chấp nhận do nằm trong khoảng | Token vẫn gửi được | Passed |  |
| `FR03-BVA-03` | `FR03-B-003` | OTP ngay trên biên dưới `100001` | Đang ở reset password bước 2 | `resetToken = 100001` | 1. Đặt token của user thành `100001` trong DB.<br>2. Gửi yêu cầu reset với token này. | Nếu token đúng với email, hệ thống đặt lại mật khẩu thành công. | Token vẫn gửi được | Passed | |
| `FR03-BVA-04` | `FR03-B-004` | OTP ngay dưới biên trên `999998` | Đang ở reset password bước 2 | `resetToken = 999998` | 1. Đặt token của user thành `999998` trong DB.<br>2. Gửi yêu cầu reset với token này. | Nếu token đúng với email, hệ thống đặt lại mật khẩu thành công. | Token vẫn gửi được | Passed |  |
| `FR03-BVA-05` | `FR03-B-005` | OTP tại biên trên `999999` | Đang ở reset password bước 2 | `resetToken = 999999` | 1. Đặt token của user thành `999999`.<br>2. Gửi yêu cầu reset với token này. | Nếu token đúng với email, hệ thống đặt lại mật khẩu thành công. | Token vẫn gửi được | Passed |  |
| `FR03-BVA-06` | `FR03-B-006` | OTP lớn hơn biên trên | SUT đang chạy. | `email = gmail.com`<br>`resetToken = 1000001`<br>`newPassword = NewPass123!` | 1. Gửi yêu cầu reset với OTP `1000001`.<br>2. Quan sát phản hồi. | Hệ thống từ chối OTP ngoài miền. | API trả `{"error":"Invalid token or email"}` với HTTP 400. | Passed | `evidence/FR03-BVA-06-api-log.txt` |
| `FR03-BVA-07` | `FR03-B-007` | Mật khẩu có 7 ký tự | Đã tạo OTP hợp lệ cho `gmail.com`. | `email = gmail.com`<br>`resetToken = 5837`<br>`newPassword = Abc1!xy` | 1. Nhập OTP hợp lệ.<br>2. Nhập mật khẩu 7 ký tự.<br>3. Gửi yêu cầu reset qua API. | Hệ thống phải từ chối vì mật khẩu dưới 8 ký tự. | API trả `{"message":"Password reset successfully"}` — backend chấp nhận mật khẩu 7 ký tự. | Failed | `evidence/FR03-BVA-07-api-log.txt` |
| `FR03-BVA-08` | `FR03-B-008` | Mật khẩu tại biên tối thiểu 8 ký tự | Đã tạo OTP hợp lệ cho `gmail.com`. | `email = gmail.com`<br>`resetToken = restore`<br>`newPassword = Test1234!` | 1. Nhập OTP hợp lệ.<br>2. Nhập mật khẩu 8 ký tự trở lên và thỏa yêu cầu.<br>3. Gửi yêu cầu reset. | Hệ thống đặt lại mật khẩu thành công. | API trả `{"message":"Password reset successfully"}`. | Passed | `evidence/FR03-BVA-08-api-log.txt` |
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
| `BUG-FR03-001` | `FR03-DT-06`, `FR03-BVA-07` | Backend chấp nhận mật khẩu yếu khi đặt lại mật khẩu | High | Open | `https://github.com/KidCute1412/eshop-sut/issues/25` | `evidence/FR03-DT-06-api-log.txt`, `evidence/FR03-BVA-07-api-log.txt` |
| `BUG-FR03-002` | `FR03-DT-01`, `FR03-BVA-01`–`FR03-BVA-06` | OTP thực tế chỉ có 4 chữ số thay vì 6 chữ số theo đặc tả | Medium | Open | `https://github.com/KidCute1412/eshop-sut/issues/26` | API log có các OTP như `8609`, `2420`, `5837` |
| `BUG-FR03-003` | `FR-03:C4` | Giao diện thiếu trường xác nhận mật khẩu mới | Medium | Open | `https://github.com/KidCute1412/eshop-sut/issues/27` | Source code `ForgotPassword.jsx` chỉ có một ô nhập mật khẩu |
| `BUG-FR03-004` | `FR-03:C5` | Regex kiểm tra mật khẩu ở frontend yêu cầu khoảng trắng thay vì ký tự đặc biệt | Medium | Open | `https://github.com/KidCute1412/eshop-sut/issues/28` | Regex thực tế: `flawedStrongPasswordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\s)[A-Za-z\d\s]{8,}$/` |

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
| `FR09-DT-01` | `FR09-D-V-01`, `FR09-D-V-02`, `FR09-D-V-03`, `FR09-D-V-04`, `FR09-D-V-06` | Áp dụng coupon phần trăm hợp lệ `SAVE10` | SUT đang chạy; coupon `SAVE10` tồn tại; user hợp lệ. | `code = SAVE10`<br>`total = 3000000`<br>`user_id = 2` | 1. Gửi yêu cầu apply coupon với `SAVE10`.<br>2. Quan sát phản hồi. | Coupon được áp dụng vì total bằng min order. Discount phải là `300000`, final amount là `2700000`. | Hệ thống hiển thị final amount `30000000` | Failed | `evidence/FR09-DT-01-api-log.txt` |
| `FR09-DT-02` | `FR09-D-I-01` | Áp dụng coupon không tồn tại | SUT đang chạy. | `code = HELLO`<br>`total = 3000000`<br>`user_id = 2` | 1. Nhập coupon không tồn tại.<br>2. Gửi yêu cầu apply coupon. | Hệ thống từ chối coupon không tồn tại hoặc inactive. | Hệ thống trả "Mã giảm giá không tồn tại hoặc đã bị vô hiệu hóa" | Passed | `evidence/FR09-DT-02-api-log.txt` |
| `FR09-DT-03` | `FR09-D-I-02` | Áp dụng coupon đã hết hạn | SUT đang chạy; coupon `EXPIRED` tồn tại. | `code = EXPIRED`<br>`total = 3000000`<br>`user_id = 2` | 1. Nhập coupon hết hạn.<br>2. Gửi yêu cầu apply coupon. | Hệ thống từ chối và báo mã giảm giá đã hết hạn. | Hệ thống báo "Mã giảm giá đã hết hạn" | Passed | `evidence/FR09-DT-03-api-log.txt` |
| `FR09-DT-04` | `FR09-D-I-04` | Áp dụng coupon khi tổng tiền dưới mức tối thiểu | SUT đang chạy; coupon `SAVE10` tồn tại. | `code = SAVE10`<br>`total = 200000`<br>`user_id = 2` | 1. Nhập coupon `SAVE10`.<br>2. Gửi request với total dưới `300000`.<br>3. Quan sát phản hồi. | Hệ thống từ chối vì đơn hàng chưa đủ giá trị tối thiểu. | Hệ thống báo "Đơn hàng chưa đủ giá trị tối thiểu 300.000 ₫ để áp dụng mã này"`. | Passed | `evidence/FR09-DT-04-api-log.txt` |
| `FR09-DT-05` | `FR09-D-I-05`, `FR09-D-V-06` | Áp dụng coupon khi chưa đăng nhập | SUT đang chạy; không gửi user/token hợp lệ. | `code = SAVE10`<br>`total = 500000`<br>`user_id = null` | 1. Không đăng nhập.<br>2. Gửi yêu cầu apply coupon qua API.<br>3. Quan sát phản hồi. | Hệ thống phải từ chối vì người dùng chưa đăng nhập. | API vẫn áp dụng coupon và trả `{"success":true,"coupon_id":1,"discount_amount":-4500000,"final_amount":5000000}`. | Failed | `evidence/FR09-DT-05-api-log.txt` |
| `FR09-DT-06` | `FR09-D-I-06` | Áp dụng coupon khi đã đạt giới hạn sử dụng | Cần có user đã dùng `SAVE10` đủ số lần. | `code = SAVE10`<br>`total = 500000`<br>`user_id = 2` | 1. Dùng coupon `SAVE10` đến giới hạn.<br>2. Thử áp dụng lại coupon.<br>3. Quan sát phản hồi. | Hệ thống từ chối vì user đã đạt giới hạn sử dụng. | Hệ thống thông báo đã đạt giới hạn | Passed |  |
| `FR09-DT-07` | `FR09-D-V-01`, `FR09-D-V-02`, `FR09-D-V-05` | Áp dụng coupon fixed hợp lệ `BIGBUY` | SUT đang chạy; coupon `BIGBUY` tồn tại. | `code = BIGBUY`<br>`total = 600000`<br>`user_id = 2` | 1. Nhập coupon `BIGBUY`.<br>2. Gửi yêu cầu apply coupon.<br>3. Quan sát discount và final amount. | Hệ thống giảm cố định `50000`, final amount là `550000`. | API trả `{"success":true,"coupon_id":2,"discount_amount":50000,"final_amount":550000}`. | Passed | `evidence/FR09-DT-07-api-log.txt` |
| `FR09-DT-08` | `FR09-D-V-01`, `FR09-D-V-02`, `FR09-D-V-04`, `FR09-D-V-05` | Áp dụng coupon `VIP100` khi chưa vượt giới hạn | User chưa dùng `VIP100` quá giới hạn. | `code = VIP100`<br>`total = 500000`<br>`user_id = 2` | 1. Nhập coupon `VIP100`.<br>2. Gửi yêu cầu apply coupon.<br>3. Quan sát phản hồi. | Nếu user chưa vượt giới hạn, coupon được áp dụng và giảm `100000`. | Hệ thống thông báo áp dụng coupon thành công. | Passed | `evidence/FR09-DT-08-api-log.txt` |
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
| `FR09-BVA-01` | `FR09-B-001` | `SAVE10` với total nhỏ hơn min order | SUT đang chạy; coupon `SAVE10` tồn tại. | `code = SAVE10`<br>`total = 299999`<br>`user_id = 3` | 1. Gửi yêu cầu apply coupon với total `299999`.<br>2. Quan sát phản hồi. | Hệ thống từ chối vì chưa đủ giá trị tối thiểu. | Hệ thống báo lỗi `Đơn hàng chưa đủ giá trị tối thiểu 300.000 ₫ để áp dụng mã này`. | Passed | `evidence/FR09-BVA-01-api-log.txt` |
| `FR09-BVA-02` | `FR09-B-002` | `SAVE10` với total bằng min order | SUT đang chạy; coupon `SAVE10` tồn tại. | `code = SAVE10`<br>`total = 300000`<br>`user_id = 3` | 1. Gửi yêu cầu apply coupon với total `300000`.<br>2. Quan sát phản hồi. | Hệ thống phải chấp nhận vì total bằng min order. | API trả lỗi `Đơn hàng chưa đủ giá trị tối thiểu 300.000 ₫ để áp dụng mã này`. | Failed | `evidence/FR09-BVA-02-api-log.txt` |
| `FR09-BVA-03` | `FR09-B-003` | `SAVE10` với total lớn hơn min order | SUT đang chạy; coupon `SAVE10` tồn tại. | `code = SAVE10`<br>`total = 300001`<br>`user_id = 3` | 1. Gửi yêu cầu apply coupon với total `300001`.<br>2. Quan sát discount và final amount. | Coupon được áp dụng; discount phải là khoảng `30000.1`, final amount khoảng `270000.9`. | Hệ thống trả `discount_amount = -2700009`, `final_amount = 3000010`. | Failed | `evidence/FR09-BVA-03-api-log.txt` |
| `FR09-BVA-04` | `FR09-B-004` | `BIGBUY` với total nhỏ hơn min order | SUT đang chạy; coupon `BIGBUY` tồn tại. | `code = BIGBUY`<br>`total = 499999`<br>`user_id = 3` | 1. Gửi yêu cầu apply coupon với total `499999`.<br>2. Quan sát phản hồi. | Hệ thống từ chối vì chưa đủ giá trị tối thiểu. | Hệ thống trả lỗi `Đơn hàng chưa đủ giá trị tối thiểu 500.000 ₫ để áp dụng mã này`. | Passed | `evidence/FR09-BVA-04-api-log.txt` |
| `FR09-BVA-05` | `FR09-B-005` | `BIGBUY` với total bằng min order | SUT đang chạy; coupon `BIGBUY` tồn tại. | `code = BIGBUY`<br>`total = 500000`<br>`user_id = 3` | 1. Gửi yêu cầu apply coupon với total `500000`.<br>2. Quan sát phản hồi. | Hệ thống phải chấp nhận vì total bằng min order. | API trả lỗi `Đơn hàng chưa đủ giá trị tối thiểu 500.000 ₫ để áp dụng mã này`. | Failed | `evidence/FR09-BVA-05-api-log.txt` |
| `FR09-BVA-06` | `FR09-B-006` | `BIGBUY` với total lớn hơn min order | SUT đang chạy; coupon `BIGBUY` tồn tại. | `code = BIGBUY`<br>`total = 500001`<br>`user_id = 3` | 1. Gửi yêu cầu apply coupon với total `500001`.<br>2. Quan sát discount và final amount. | Coupon được áp dụng; discount `50000`, final amount `450001`. | Hệ thống báo "Áp dụng thành công! Giảm 50.000 ₫" | Passed | `evidence/FR09-BVA-06-api-log.txt` |
| `FR09-BVA-07` | `FR09-B-007` | `VIP100` tại giới hạn sử dụng | User đã dùng `VIP100` đủ 2 lần. | `code = VIP100`<br>`total = 500000`<br>`user_id = 3` | 1. Gửi yêu cầu apply coupon `VIP100` với user đã đạt giới hạn.<br>2. Quan sát phản hồi. | Hệ thống từ chối vì user đã đạt giới hạn sử dụng. | Hệ thống báo trả "Bạn đã sử dụng mã này 2 lần (đã đạt giới hạn)". | Passed | `evidence/FR09-BVA-07-api-log.txt` |
| `FR09-BVA-08` | `FR09-B-008` | `VIP100` khi chưa đạt giới hạn sử dụng | Dùng request không có user tracking. | `code = VIP100`<br>`total = 500000`<br>`user_id = 3` | 1. Gửi yêu cầu apply coupon `VIP100` không kèm user.<br>2. Quan sát phản hồi. | Nếu user hợp lệ và usage count là `1`, coupon được áp dụng. | Hệ thống báo "Áp dụng thành công! Giảm 100.000 ₫"| Passed | `evidence/FR09-BVA-08-api-log.txt` |

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
| `BUG-FR09-001` | `FR09-DT-01`, `FR09-DT-09`, `FR09-BVA-02`, `FR09-BVA-05` | Coupon bị từ chối khi tổng tiền bằng đúng `min_order_amount` | High | Open | `https://github.com/KidCute1412/eshop-sut/issues/29` | `evidence/FR09-DT-01-api-log.txt`, `evidence/FR09-DT-09-api-log.txt`, `evidence/FR09-BVA-02-api-log.txt`, `evidence/FR09-BVA-05-api-log.txt` |
| `BUG-FR09-002` | `FR09-DT-05`, `FR09-BVA-03` | Công thức tính coupon phần trăm sai, tạo discount âm và final amount tăng bất thường | High | Open | `https://github.com/KidCute1412/eshop-sut/issues/30` | `evidence/FR09-DT-05-api-log.txt`, `evidence/FR09-BVA-03-api-log.txt` |
| `BUG-FR09-003` | `FR09-DT-05`, `FR09-BVA-08` | API vẫn cho áp dụng coupon khi không có user/token hợp lệ | High | Open | `https://github.com/KidCute1412/eshop-sut/issues/31` | `evidence/FR09-DT-05-api-log.txt`, `evidence/FR09-BVA-08-api-log.txt` |
| `BUG-FR09-004` | `FR09-BVA-08` | Có thể bypass kiểm tra giới hạn sử dụng coupon khi không gửi `user_id` | Medium | Open | `https://github.com/KidCute1412/eshop-sut/issues/32` | `evidence/FR09-BVA-08-api-log.txt` |
| `BUG-FR09-005` | `FR09-DT-08` | Test data của user đã bị nhiễm trạng thái sử dụng `VIP100`, khiến first-use scenario không kiểm thử được chính xác | Low | Open | `https://github.com/KidCute1412/eshop-sut/issues/33` | `evidence/FR09-DT-08-api-log.txt` |

# 8. Báo cáo tính năng FR-13

## 8.1 Mô tả tính năng

FR-13 là tính năng **Dashboard cho Admin** trong hệ thống EShop. Tính năng này được sử dụng trên giao diện admin web để hiển thị các chỉ số tổng quan về đơn hàng.

Luồng chính gồm:

1. Admin đăng nhập vào giao diện admin web tại `http://localhost:5174`.
2. Admin truy cập trang Dashboard.
3. Hệ thống hiển thị tổng doanh thu.
4. Hệ thống hiển thị tổng số đơn hàng.
5. Tổng doanh thu chỉ được tính từ các đơn hàng có trạng thái `delivered`.
6. Tổng số đơn hàng được tính trên toàn bộ đơn hàng trong hệ thống, không phụ thuộc trạng thái.

Các test plan bổ sung cũng kiểm tra cách Dashboard xử lý từng trạng thái đơn hàng, giá trị `total_amount`, tổng doanh thu, tổng số đơn hàng và quyền truy cập admin. Những lỗi không liên quan trực tiếp đến các biến đã chọn không được đưa vào phần này để giữ đúng phạm vi tính năng.

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
| `FR13-DT-01` | `FR13-D-V-01`, `FR13-D-V-07`, `FR13-D-V-09` | Dashboard khi không có đơn hàng | Admin đăng nhập thành công; database không có đơn hàng. | Không có đơn hàng ở bất kỳ trạng thái nào. | 1. Đăng nhập admin tại `localhost:5174`.<br>2. Truy cập Dashboard.<br>3. Quan sát doanh thu và tổng số đơn. | Doanh thu hiển thị `0₫`; tổng số đơn hàng hiển thị `0`. | Hệ thống hiển thị đúng | Passed |  |
| `FR13-DT-02` | `FR13-D-V-02`, `FR13-D-V-08` | Dashboard với một đơn delivered | Admin đăng nhập thành công; có ít nhất một đơn `delivered`. | 1 đơn `delivered`, `total_amount = 100000`. | 1. Đăng nhập admin.<br>2. Đảm bảo có đơn delivered với `total_amount = 100000`.<br>3. Vào Dashboard.<br>4. Quan sát tổng doanh thu. | Doanh thu hiển thị `100000₫`. | Doanh thu hiển thị `200000₫`, gấp đôi giá trị mong đợi. | Failed | Quan sát Dashboard với dữ liệu test `TC-DASH-01` |
| `FR13-DT-03` | `FR13-D-V-03`, `FR13-D-V-07` | Dashboard với đơn canceled | Admin đăng nhập thành công; có đơn bị hủy. | 1 đơn `canceled`, `total_amount = 50000`. | 1. Đăng nhập admin.<br>2. Tạo hoặc dùng đơn có trạng thái `canceled`.<br>3. Vào Dashboard. | Doanh thu không bao gồm đơn canceled. Đơn đã hủy không thể giao. | Đơn canceled không được cộng vào doanh thu nhưng vẫn có thể đánh dấu đã giao. | Failed |  |
| `FR13-DT-04` | `FR13-D-V-04`, `FR13-D-V-07` | Dashboard với đơn pending | Admin đăng nhập thành công; có đơn pending. | 1 đơn `pending`, `total_amount = 200000`. | 1. Đăng nhập admin.<br>2. Đảm bảo có đơn pending.<br>3. Vào Dashboard. | Doanh thu không bao gồm đơn pending. | Doanh thu hiển thị không gồm đơn pending | Passed |  |
| `FR13-DT-05` | `FR13-D-V-05`, `FR13-D-V-07` | Dashboard với đơn confirmed | Admin đăng nhập thành công; có đơn confirmed. | 1 đơn `confirmed`, `total_amount = 300000`. | 1. Đăng nhập admin.<br>2. Đảm bảo có đơn confirmed.<br>3. Vào Dashboard. | Doanh thu không bao gồm đơn confirmed. | Doanh thu hiển thị không gồm đơn confirmed | Passed |  |
| `FR13-DT-06` | `FR13-D-V-06`, `FR13-D-V-07` | Dashboard với đơn shipping | Admin đăng nhập thành công; có đơn shipping. | 1 đơn `shipping`, `total_amount = 150000`. | 1. Đăng nhập admin.<br>2. Đảm bảo có đơn shipping.<br>3. Vào Dashboard. | Doanh thu không bao gồm đơn shipping. | Doanh thu không gồm đơn shipping | Passed |  |
| `FR13-DT-07` | `FR13-D-V-02`, `FR13-D-V-08` | Dashboard với nhiều đơn delivered | Admin đăng nhập thành công; có nhiều đơn delivered. | 3 đơn delivered: `100000 + 200000 + 300000 = 600000`. | 1. Đăng nhập admin.<br>2. Đảm bảo có 3 đơn delivered như dữ liệu đầu vào.<br>3. Vào Dashboard. | Doanh thu hiển thị `600000₫`. | Doanh thu hiển thị `1200000₫`, gấp đôi giá trị mong đợi. | Failed | Quan sát Dashboard với dữ liệu test `TC-DASH-07` |
| `FR13-DT-08` | `FR13-D-I-01` | User thường không được truy cập admin API/dashboard | Có token của user thường hoặc token không có quyền admin. | Token hợp lệ nhưng role không phải Admin. | 1. Gửi request đến API/admin resource bằng token user thường.<br>2. Quan sát phản hồi. | Hệ thống từ chối bằng `401` hoặc `403`. | Request của user không phải Admin vẫn được chấp nhận cho tài nguyên admin. | Failed | Quan sát phản hồi API bằng token user thường |
| `FR13-DT-09` | `FR13-D-V-02`, `FR13-D-V-08` | Đơn hàng delivered có giá trị âm | Admin đăng nhập thành công; có đơn hàng đã giao giá trị âm | 1 đơn đã giao giá trị `-1` | 1. Đăng nhập admin.<br>2. Đảm bảo có 1 đơn delivered như dữ liệu đầu vào.<br>3. Vào Dashboard. | Doanh thu hiển thị lỗi doanh thu âm. | Doanh thu hiển thị `-2` | Failed | Quan sát Dashboard với dữ liệu test `TC-DASH-07` |

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
| `FR13-BVA-01` | `FR13-B-001` | `total_order` nhỏ hơn biên dưới | Có thể tạo hoặc mô phỏng đơn hàng với order âm. | `total_order = -1` | 1. Tạo/mô phỏng đơn hàng có số order âm.<br>2. Kiểm tra Dashboard/API. | Hệ thống không chấp nhận hoặc không hiển thị dữ liệu âm. | Chưa thực thi vì cần dữ liệu âm không hợp lệ. | Not Executed |  |
| `FR13-BVA-02` | `FR13-B-002` | `total_order` tại biên dưới | Admin đăng nhập; có đơn delivered với amount `0`. | `status = delivered`, `total_amount = 0` | 1. Đăng nhập admin.<br>2. Vào Dashboard.<br>3. Quan sát doanh thu. | Doanh thu hiển thị `0₫`. | Doanh thu hiển thị | Not Executed |  |
| `FR13-BVA-03` | `FR13-B-003` | `total_revenue` ngay trên biên dưới | Admin đăng nhập; có đơn delivered với amount `1`. | `status = delivered`, `total_revenue = 1` | 1. Đăng nhập admin.<br>2. Vào Dashboard.<br>3. Quan sát doanh thu. | Doanh thu hiển thị `1₫`. | Doanh thu có hiển thị `2₫`, gấp đôi giá trị mong đợi. | Failed | Quan sát Dashboard với dữ liệu biên `total_amount = 1` |
| `FR13-BVA-04` | `FR13-B-004` | `total_revenue` ngay dưới biên dưới | Admin đăng nhập; có đơn delivered với amount `-1`. | `status = delivered`, `total_revenue = 1` | 1. Đăng nhập admin.<br>2. Vào Dashboard.<br>3. Quan sát doanh thu. | Doanh thu hiển thị lỗi. | Doanh thu hiển thị `-2` | Failed | Quan sát Dashboard với dữ liệu biên `total_amount = 1` |

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

| Bug ID | Test case liên quan | Tiêu đề | Mức độ nghiêm trọng | Trạng thái | Link GitHub Issue | Minh chứng |
| --- | --- | --- | --- | --- | --- | --- |
| `BUG-FR13-001` | `FR13-DT-02`, `FR13-DT-07`, `FR13-BVA-03` | Dashboard hiển thị doanh thu gấp đôi giá trị mong đợi của đơn `delivered` | High | Open | `https://github.com/KidCute1412/eshop-sut/issues/34` | Quan sát Dashboard trong `TC-DASH-01`, `TC-DASH-07` |
| `BUG-FR13-002` | `FR13-DT-08` | User không phải Admin vẫn truy cập được tài nguyên admin | High | Open | `https://github.com/KidCute1412/eshop-sut/issues/35` | Quan sát phản hồi API bằng token user thường |

---

# 9. Báo cáo tính năng FR-03M

## 9.1 Mô tả tính năng

FR-03M là tính năng **quên mật khẩu và đặt lại mật khẩu trên mobile** trong hệ thống EShop. Tính năng này dành cho người dùng chưa đăng nhập hoặc người dùng đã đăng ký nhưng quên mật khẩu.

Luồng chính gồm:

1. Người dùng mở màn hình Forgot Password trên mobile app.
2. Người dùng nhập email đã đăng ký.
3. Theo yêu cầu, hệ thống phải sinh OTP **6 chữ số ngẫu nhiên**; khi kiểm thử qua API, OTP quan sát được có 4 chữ số trong khoảng `1000–9999`.
4. Trong môi trường demo, OTP có thể được hiển thị cho mục đích demo, nhưng API không nên để lộ reset token trong response ở môi trường thực tế.
5. Giao diện hiển thị Step Indicator, ví dụ `Bước 1 / 2`.
6. Giao diện có nút `Quay lại đăng nhập`.
7. Người dùng nhập OTP, mật khẩu mới và xác nhận mật khẩu mới.
8. Hệ thống kiểm tra OTP, độ mạnh mật khẩu, điều kiện hai mật khẩu khớp nhau và giới hạn số lần thử.
9. Nếu hợp lệ, hệ thống đặt lại mật khẩu thành công.

Các test case ban đầu của FR-03M chưa được execute đầy đủ do thiếu mobile URL/môi trường mobile. Những lỗi được bổ sung bên dưới được diễn đạt dựa trên hành vi quan sát được qua UI/API và dữ liệu test.

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

## 9.3 Domain Testing

### 9.3.1 Biến miền và ràng buộc

| Variable ID | Biến / Trạng thái | Kiểu | Ràng buộc | Kết quả có thể quan sát | Basis ID |
| --- | --- | --- | --- | --- | --- |
| `FR03M-VAR-01` | `email` | Chuỗi | Email phải đúng định dạng và đã đăng ký trong hệ thống. | Email hợp lệ sinh OTP; email chưa đăng ký, sai định dạng hoặc rỗng hiển thị lỗi. | `FR-03M:C1` |
| `FR03M-VAR-02` | `otp` / `resetToken` | Chuỗi số | Theo yêu cầu là OTP 6 chữ số; qua API, OTP quan sát được có 4 chữ số `1000–9999`. OTP phải đúng và thuộc email đã yêu cầu. | OTP đúng cho phép reset; OTP sai, rỗng, không phải số hoặc sai độ dài bị từ chối. | `FR-03M:C2`, `FR-03M:C7`, `FR-03M:C9` |
| `FR03M-VAR-03` | `new_password` | Chuỗi | Mật khẩu mới phải thỏa FR-01: tối thiểu 8 ký tự, có chữ hoa, chữ thường, chữ số và ký tự đặc biệt. | Mật khẩu hợp lệ được chấp nhận; mật khẩu yếu bị báo lỗi. | `FR-03M:C5` |
| `FR03M-VAR-04` | `confirm_password` | Chuỗi | Giá trị xác nhận mật khẩu phải tồn tại và trùng với `new_password`. | Trùng thì cho phép reset; rỗng hoặc không khớp thì báo lỗi. | `FR-03M:C6` |
| `FR03M-VAR-05` | Trạng thái giao diện mobile | UI state | Gồm Step 1 nhập email, Step 2 nhập OTP/mật khẩu, Step Indicator và nút quay lại đăng nhập. | Người dùng quan sát được Step Indicator và nút `Quay lại đăng nhập`. | `FR-03M:C3`, `FR-03M:C4` |
| `FR03M-VAR-06` | Response của API forgot password | API response | Response không nên chứa OTP/reset token trực tiếp. | Response chỉ chứa message an toàn; không có `resetToken`. | `FR-03M:C10` |
| `FR03M-VAR-07` | Số lần thử reset password | Số nguyên / security state | Sau nhiều lần nhập OTP sai, hệ thống phải chặn hoặc rate-limit. | Sau 5–10 lần thử sai, request bị từ chối/tạm khóa. | `FR-03M:C11` |

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
| `FR03M-D-I-16` | API forgot password | Không hợp lệ / security | API trả `resetToken` trực tiếp trong response. | Response không được chứa token nhạy cảm. | `FR-03M:C10` |
| `FR03M-D-I-17` | Rate limit | Không hợp lệ / security | Gửi reset-password với OTP sai liên tục, ví dụ brute-force `0000–9999`. | Hệ thống phải chặn sau một số lần thử sai. | `FR-03M:C11` |

### 9.3.3 Test case Domain Testing

| Test Case ID | Domain ID liên quan | Tiêu đề | Điều kiện tiên quyết | Dữ liệu đầu vào | Các bước thực hiện | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Minh chứng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `FR03M-DT-01` | `FR03M-D-V-01`, `FR03M-D-I-16` | Step 1 - Email đã đăng ký và API không lộ OTP | Người dùng chưa đăng nhập; có email đã đăng ký. | `email = gmail` hoặc `test@eshop.com` | 1. Mở mobile app hoặc gọi `POST /api/forgot-password`.<br>2. Nhập email đã đăng ký.<br>3. Submit.<br>4. Quan sát response API. | OTP được tạo theo yêu cầu; API không trả `resetToken` trực tiếp trong response. | API trả `resetToken` trong response và token thực tế chỉ có 4 chữ số. | Failed | Quan sát response API trong `TC-FP-01` |
| `FR03M-DT-02` | `FR03M-D-I-01` | Step 1 - Email chưa đăng ký | Người dùng chưa đăng nhập, đang ở màn hình Forgot Password trên mobile. | `email = nonexistent@test.com` | 1. Nhập email chưa đăng ký.<br>2. Submit. | Nên hiển thị thông báo chung, không lộ email có tồn tại hay không. | API trả lỗi cụ thể `User not found`, có nguy cơ email enumeration. | Failed | Quan sát response API với email chưa đăng ký |
| `FR03M-DT-03` | `FR03M-D-I-02` | Step 1 - Email sai định dạng | Người dùng chưa đăng nhập, đang ở màn hình Forgot Password trên mobile. | `email = notanemail` | 1. Nhập email sai định dạng.<br>2. Submit. | Mobile báo lỗi format email trước khi gọi API. | Trường email trên mobile không chặn định dạng email sai đầy đủ. | Failed | Quan sát UI mobile với dữ liệu `notanemail` |
| `FR03M-DT-04` | `FR03M-D-I-03` | Step 1 - Bỏ trống email | Người dùng chưa đăng nhập, đang ở màn hình Forgot Password trên mobile. | `email = empty` | 1. Để trống email.<br>2. Submit. | Hệ thống báo email bắt buộc. | Chưa thực thi do thiếu môi trường mobile. | Not Executed |  |
| `FR03M-DT-05` | `FR03M-D-V-02`, `FR03M-D-V-03`, `FR03M-D-V-04` | Step 2 - OTP đúng và mật khẩu hợp lệ | Đã hoàn tất Step 1 thành công. | `otp = correct`<br>`new_password = Pass1234@`<br>`confirm_password = Pass1234@` | 1. Nhập OTP đúng.<br>2. Nhập mật khẩu mới hợp lệ.<br>3. Nhập confirm password trùng khớp.<br>4. Submit. | Đặt lại mật khẩu thành công. | Chưa thực thi end-to-end do thiếu môi trường mobile. | Not Executed |  |
| `FR03M-DT-06` | `FR03M-D-I-04` | Step 2 - OTP sai | Đã hoàn tất Step 1 thành công. | `otp = 0000`<br>`new_password = ValidPass1!`<br>`confirm_password = ValidPass1!` | 1. Nhập OTP sai.<br>2. Nhập mật khẩu hợp lệ.<br>3. Submit. | Hệ thống báo OTP không hợp lệ. | Chưa thực thi end-to-end do thiếu môi trường mobile. | Not Executed |  |
| `FR03M-DT-07` | `FR03M-D-I-05` | Step 2 - Bỏ trống OTP | Đã hoàn tất Step 1 thành công. | `otp = empty`<br>`new_password = ValidPass1!`<br>`confirm_password = ValidPass1!` | 1. Để trống OTP.<br>2. Nhập mật khẩu hợp lệ.<br>3. Submit. | Hệ thống báo OTP bắt buộc. | Chưa thực thi do thiếu môi trường mobile. | Not Executed |  |
| `FR03M-DT-08` | `FR03M-D-I-06` | Step 2 - OTP không phải số | Đã hoàn tất Step 1 thành công. | `otp = abcd`<br>`new_password = Pass1234@` | 1. Nhập OTP chứa chữ.<br>2. Nhập mật khẩu hợp lệ.<br>3. Submit. | Mobile báo OTP phải là số hoặc đúng 4 chữ số trước khi gửi request. | Mobile vẫn gửi request; hệ thống chỉ trả lỗi token chung thay vì chặn input ngay trên form. | Failed | Quan sát UI/API trong `TC-RP-04` |
| `FR03M-DT-09` | `FR03M-D-I-07` | Step 2 - OTP sai độ dài | Đã hoàn tất Step 1 thành công. | `otp = 12345` hoặc OTP dài 6 số | 1. Nhập OTP sai độ dài.<br>2. Nhập mật khẩu hợp lệ.<br>3. Submit. | Mobile báo OTP sai độ dài trước khi gửi request. | Mobile không giới hạn độ dài OTP trước khi submit. | Failed | Quan sát UI/API trong `TC-RP-03` |
| `FR03M-DT-10` | `FR03M-D-I-08` | Step 2 - Mật khẩu dưới 8 ký tự | Đã hoàn tất Step 1 thành công. | `otp = correct`<br>`new_password = Ab1!`<br>`confirm_password = Ab1!` | 1. Nhập OTP đúng.<br>2. Nhập mật khẩu ngắn.<br>3. Submit. | Hệ thống báo mật khẩu tối thiểu 8 ký tự. | Chưa thực thi do thiếu môi trường mobile. | Not Executed |  |
| `FR03M-DT-11` | `FR03M-D-I-09` | Step 2 - Mật khẩu thiếu chữ hoa | Đã hoàn tất Step 1 thành công. | `new_password = lowercase1!`<br>`confirm_password = lowercase1!` | 1. Nhập OTP đúng.<br>2. Nhập mật khẩu thiếu chữ hoa.<br>3. Submit. | Hệ thống báo cần chữ hoa. | Chưa thực thi do thiếu môi trường mobile. | Not Executed |  |
| `FR03M-DT-12` | `FR03M-D-I-10` | Step 2 - Mật khẩu thiếu chữ thường | Đã hoàn tất Step 1 thành công. | `new_password = UPPERCASE1!`<br>`confirm_password = UPPERCASE1!` | 1. Nhập OTP đúng.<br>2. Nhập mật khẩu thiếu chữ thường.<br>3. Submit. | Hệ thống báo cần chữ thường. | Chưa thực thi do thiếu môi trường mobile. | Not Executed |  |
| `FR03M-DT-13` | `FR03M-D-I-11` | Step 2 - Mật khẩu thiếu chữ số | Đã hoàn tất Step 1 thành công. | `new_password = NoDigitA!`<br>`confirm_password = NoDigitA!` | 1. Nhập OTP đúng.<br>2. Nhập mật khẩu thiếu chữ số.<br>3. Submit. | Hệ thống báo cần chữ số. | Chưa thực thi do thiếu môi trường mobile. | Not Executed |  |
| `FR03M-DT-14` | `FR03M-D-I-12` | Step 2 - Mật khẩu thiếu ký tự đặc biệt nhưng có khoảng trắng | Đã hoàn tất Step 1 thành công. | `new_password = Pass 1234`<br>`confirm_password = Pass 1234` | 1. Nhập OTP đúng.<br>2. Nhập password có khoảng trắng nhưng không có ký tự đặc biệt.<br>3. Submit. | Hệ thống phải từ chối vì thiếu ký tự đặc biệt. | Mobile chấp nhận mật khẩu có khoảng trắng dù thiếu ký tự đặc biệt thật sự. | Failed | Quan sát UI/API trong `TC-RP-05` |
| `FR03M-DT-15` | `FR03M-D-I-12` | Step 2 - Mật khẩu có special char nhưng không có khoảng trắng | Đã hoàn tất Step 1 thành công. | `new_password = Pass1234@`<br>`confirm_password = Pass1234@` | 1. Nhập OTP đúng.<br>2. Nhập password có ký tự đặc biệt `@`.<br>3. Submit. | Hệ thống phải chấp nhận vì thỏa FR-01. | Mobile có thể từ chối mật khẩu hợp lệ vì không có khoảng trắng. | Failed | Quan sát UI/API trong `TC-RP-07` |
| `FR03M-DT-16` | `FR03M-D-I-14` | Step 2 - Xác nhận mật khẩu không khớp | Đã hoàn tất Step 1 thành công. | `new_password = ValidPass1!`<br>`confirm_password = Different1!` | 1. Nhập OTP đúng.<br>2. Nhập mật khẩu hợp lệ.<br>3. Nhập confirm password khác mật khẩu mới.<br>4. Submit. | Hệ thống báo hai mật khẩu không khớp. | Chưa thực thi do thiếu môi trường mobile. | Not Executed |  |
| `FR03M-DT-17` | `FR03M-D-I-15` | Step 2 - Bỏ trống xác nhận mật khẩu | Đã hoàn tất Step 1 thành công. | `new_password = ValidPass1!`<br>`confirm_password = empty` | 1. Nhập OTP đúng.<br>2. Nhập mật khẩu hợp lệ.<br>3. Để trống confirm password.<br>4. Submit. | Hệ thống báo xác nhận mật khẩu bắt buộc. | Chưa thực thi do thiếu môi trường mobile. | Not Executed |  |
| `FR03M-DT-18` | `FR03M-D-I-17` | Step 2 - Brute-force OTP phải bị rate-limit | Có email hợp lệ và có thể gọi API reset-password nhiều lần. | Thử nhiều OTP sai trong khoảng `0000–9999`. | 1. Gửi forgot-password để tạo OTP.<br>2. Gửi reset-password với OTP sai liên tục.<br>3. Quan sát hệ thống có chặn sau N lần thử không. | Hệ thống chặn sau 5–10 lần thử sai hoặc áp dụng rate limit. | Hệ thống không chặn số lần thử sai trong phạm vi test. | Failed | Quan sát API trong `TC-RP-06` |

### 9.3.4 Tổng kết Domain Testing

| Chỉ số | Số lượng |
| --- | ---: |
| Tổng số test case Domain Testing | 18 |
| Passed | 0 |
| Failed | 8 |
| Blocked | 0 |
| Not Executed | 10 |
| Needs Review | 0 |

## 9.4 Boundary Value Analysis

### 9.4.1 Biến có giá trị biên

| Boundary Variable ID | Biến | Quy tắc biên | Giá trị nhỏ nhất | Giá trị lớn nhất | Giá trị bình thường |
| --- | --- | --- | --- | --- | --- |
| `FR03M-BVAR-01` | `new_password_length` | Mật khẩu mới phải có tối thiểu 8 ký tự. | `8` | Không rõ | `9` |
| `FR03M-BVAR-02` | `otp` / `resetToken` | OTP quan sát được qua API là mã 4 chữ số trong khoảng `1000–9999`; đây cũng là điểm lệch so với requirement 6 chữ số. | `1000` | `9999` | OTP đúng được sinh sau Step 1 |

### 9.4.2 Giá trị biên

| Boundary ID | Biến | Loại biên | Giá trị | Hành vi mong đợi | Basis ID |
| --- | --- | --- | --- | --- | --- |
| `FR03M-B-001` | `new_password_length` | `min-1` | `7` ký tự, ví dụ `Pass123` | Bị từ chối vì ngắn hơn 8 ký tự. | `FR-03M:C5` |
| `FR03M-B-002` | `new_password_length` | `min` | `8` ký tự, ví dụ `Pass123@` | Được chấp nhận nếu thỏa các nhóm ký tự bắt buộc. | `FR-03M:C5` |
| `FR03M-B-003` | `new_password_length` | `min+1` | `9` ký tự, ví dụ `Pass123@a` | Được chấp nhận nếu thỏa các nhóm ký tự bắt buộc. | `FR-03M:C5` |
| `FR03M-B-004` | `otp` | `min-1` | `999` | Bị từ chối vì nhỏ hơn miền OTP 4 chữ số thực tế. | `FR-03M:C9`, `FR-03M:C12` |
| `FR03M-B-005` | `otp` | `min` | `1000` | Được xử lý là OTP đúng định dạng; kết quả đúng/sai phụ thuộc OTP thực tế. | `FR-03M:C9`, `FR-03M:C7` |
| `FR03M-B-006` | `otp` | `min+1` | `1001` | Được xử lý là OTP đúng định dạng; kết quả đúng/sai phụ thuộc OTP thực tế. | `FR-03M:C9`, `FR-03M:C7` |
| `FR03M-B-007` | `otp` | `max-1` | `9998` | Được xử lý là OTP đúng định dạng; kết quả đúng/sai phụ thuộc OTP thực tế. | `FR-03M:C9`, `FR-03M:C7` |
| `FR03M-B-008` | `otp` | `max` | `9999` | Được xử lý là OTP đúng định dạng; kết quả đúng/sai phụ thuộc OTP thực tế. | `FR-03M:C9`, `FR-03M:C7` |
| `FR03M-B-009` | `otp` | `max+1` | `10000` | Bị từ chối vì lớn hơn miền OTP 4 chữ số thực tế. | `FR-03M:C9`, `FR-03M:C12` |

### 9.4.3 Test case BVA

| Test Case ID | Boundary ID liên quan | Tiêu đề | Điều kiện tiên quyết | Dữ liệu đầu vào | Các bước thực hiện | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Minh chứng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `FR03M-BVA-01` | `FR03M-B-001` | Mật khẩu ngắn hơn 8 ký tự | Đã hoàn tất Step 1 thành công. | `otp = correct`<br>`new_password = Pass123` | 1. Nhập OTP đúng.<br>2. Nhập mật khẩu 7 ký tự.<br>3. Submit. | Hệ thống báo mật khẩu tối thiểu 8 ký tự. | Chưa thực thi do thiếu môi trường mobile. | Blocked |  |
| `FR03M-BVA-02` | `FR03M-B-002` | Mật khẩu đúng 8 ký tự | Đã hoàn tất Step 1 thành công. | `otp = correct`<br>`new_password = Pass123@` | 1. Nhập OTP đúng.<br>2. Nhập mật khẩu 8 ký tự có special char.<br>3. Submit. | Mật khẩu được chấp nhận. | Mobile có thể từ chối mật khẩu hợp lệ vì không có khoảng trắng. | Failed | Quan sát UI/API với dữ liệu `Pass123@` |
| `FR03M-BVA-03` | `FR03M-B-003` | Mật khẩu 9 ký tự | Đã hoàn tất Step 1 thành công. | `otp = correct`<br>`new_password = Pass123@a` | 1. Nhập OTP đúng.<br>2. Nhập mật khẩu 9 ký tự có special char.<br>3. Submit. | Mật khẩu được chấp nhận. | Mobile có thể từ chối mật khẩu hợp lệ vì không có khoảng trắng. | Failed | Quan sát UI/API với dữ liệu `Pass123@a` |
| `FR03M-BVA-04` | `FR03M-B-004` | OTP nhỏ hơn biên dưới | Đã hoàn tất Step 1 thành công. | `otp = 999`<br>`new_password = ValidPass1!` | 1. Nhập OTP `999`.<br>2. Nhập mật khẩu hợp lệ.<br>3. Submit. | Mobile báo OTP sai độ dài trước khi gửi request. | Mobile không giới hạn/validate độ dài OTP đầy đủ. | Failed | Quan sát UI/API với OTP `999` |
| `FR03M-BVA-05` | `FR03M-B-005` | OTP tại biên dưới | Đã hoàn tất Step 1 thành công. | `otp = 1000`<br>`new_password = ValidPass1!` | 1. Nhập OTP `1000`.<br>2. Nhập mật khẩu hợp lệ.<br>3. Submit. | OTP được xử lý là đúng định dạng; đúng/sai phụ thuộc OTP thực tế. | Chưa có OTP thực tế tương ứng để xác nhận. | Blocked |  |
| `FR03M-BVA-06` | `FR03M-B-006` | OTP ngay trên biên dưới | Đã hoàn tất Step 1 thành công. | `otp = 1001`<br>`new_password = ValidPass1!` | 1. Nhập OTP `1001`.<br>2. Nhập mật khẩu hợp lệ.<br>3. Submit. | OTP được xử lý là đúng định dạng; đúng/sai phụ thuộc OTP thực tế. | Chưa có OTP thực tế tương ứng để xác nhận. | Blocked |  |
| `FR03M-BVA-07` | `FR03M-B-007` | OTP ngay dưới biên trên | Đã hoàn tất Step 1 thành công. | `otp = 9998`<br>`new_password = ValidPass1!` | 1. Nhập OTP `9998`.<br>2. Nhập mật khẩu hợp lệ.<br>3. Submit. | OTP được xử lý là đúng định dạng; đúng/sai phụ thuộc OTP thực tế. | Chưa có OTP thực tế tương ứng để xác nhận. | Blocked |  |
| `FR03M-BVA-08` | `FR03M-B-008` | OTP tại biên trên | Đã hoàn tất Step 1 thành công. | `otp = 9999`<br>`new_password = ValidPass1!` | 1. Nhập OTP `9999`.<br>2. Nhập mật khẩu hợp lệ.<br>3. Submit. | OTP được xử lý là đúng định dạng; đúng/sai phụ thuộc OTP thực tế. | Chưa có OTP thực tế tương ứng để xác nhận. | Blocked |  |
| `FR03M-BVA-09` | `FR03M-B-009` | OTP lớn hơn biên trên | Đã hoàn tất Step 1 thành công. | `otp = 10000`<br>`new_password = ValidPass1!` | 1. Nhập OTP `10000`.<br>2. Nhập mật khẩu hợp lệ.<br>3. Submit. | Mobile báo OTP sai độ dài trước khi gửi request. | Mobile không giới hạn/validate độ dài OTP đầy đủ. | Failed | Quan sát UI/API với OTP `10000` |

### 9.4.4 Tổng kết BVA

| Chỉ số | Số lượng |
| --- | ---: |
| Tổng số test case BVA | 9 |
| Passed | 0 |
| Failed | 4 |
| Blocked | 5 |
| Not Executed | 0 |
| Needs Review | 0 |

## 9.5 Lỗi phát hiện ở tính năng FR-03M

| Bug ID | Test case liên quan | Tiêu đề | Mức độ nghiêm trọng | Trạng thái | Link GitHub Issue | Minh chứng |
| --- | --- | --- | --- | --- | --- | --- |
| `BUG-FR03M-001` | `FR03M-DT-01` | API forgot password trả `resetToken` trực tiếp trong response | High | Open | `https://github.com/KidCute1412/eshop-sut/issues/36` | Quan sát response API trong `TC-FP-01` |
| `BUG-FR03M-002` | `FR03M-DT-01`, `FR03M-BVA-04` đến `FR03M-BVA-09` | OTP quan sát được chỉ có 4 chữ số `1000–9999`, lệch yêu cầu 6 chữ số | Medium | Open | `https://github.com/KidCute1412/eshop-sut/issues/37` | Quan sát response OTP trong luồng forgot password |
| `BUG-FR03M-003` | `FR03M-DT-14`, `FR03M-DT-15`, `FR03M-BVA-02`, `FR03M-BVA-03` | Mobile kiểm tra ký tự đặc biệt của password không đúng hành vi mong đợi | High | Open | `https://github.com/KidCute1412/eshop-sut/issues/38` | Quan sát UI/API trong `TC-RP-05`, `TC-RP-07` |
| `BUG-FR03M-004` | `FR03M-DT-08`, `FR03M-DT-09`, `FR03M-BVA-04`, `FR03M-BVA-09` | Mobile không validate OTP là số và đúng độ dài trước khi gửi request | Medium | Open | `https://github.com/KidCute1412/eshop-sut/issues/39` | Quan sát UI/API trong `TC-RP-03`, `TC-RP-04` |
| `BUG-FR03M-005` | `FR03M-DT-18` | Reset password không có rate limit, có thể brute-force OTP | High | Open | `https://github.com/KidCute1412/eshop-sut/issues/40` | Quan sát API trong `TC-RP-06` |
| `BUG-FR03M-006` | `FR03M-DT-02` | API forgot password lộ thông tin email có tồn tại qua lỗi `User not found` | Medium | Open | `https://github.com/KidCute1412/eshop-sut/issues/41` | Quan sát response API với email chưa đăng ký |
| `BUG-FR03M-007` | `FR03M-DT-03` | Mobile email field không validate định dạng email đầy đủ | Low | Open | `https://github.com/KidCute1412/eshop-sut/issues/42` | Quan sát UI mobile với email sai định dạng |

---


# 10. Tổng kết kiểm thử

## 10.1 Tổng kết test case theo tính năng

| Tính năng | TC Domain Testing | TC BVA | Tổng TC | Passed | Failed | Blocked | Not Executed | Needs Review |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Feature A (FR-03) | 8 | 9 | 17 | 12 | 5 | 0 | 0 | 0 |
| Feature B (FR-09) | 10 | 8 | 18 | 10 | 7 | 1 | 0 | 0 |
| Feature C (FR-13) | 8 | 3 | 11 | 1 | 5 | 1 | 4 | 0 |
| Feature D (FR-03M) | 18 | 9 | 27 | 0 | 12 | 5 | 10 | 0 |
| **Tổng cộng** | 44 | 29 | 73 | 23 | 29 | 7 | 14 | 0 |

## 10.2 Tổng kết thực thi

Tổng cộng 73 test case được thiết kế, 23 Passed, 29 Failed, 7 Blocked, 14 Not Executed. FR-03 và FR-09 có tỷ lệ pass cao nhất. FR-13 và FR-03M có nhiều test case bị Blocked/Not Executed do hạn chế về môi trường (không thể xóa toàn bộ đơn hàng trong DB, thiếu môi trường mobile). Phát hiện chính bao gồm lỗi validation mật khẩu backend, lỗi công thức tính discount, lỗi access control và lỗi bảo mật OTP.

## 10.3 Tổng kết minh chứng

| Evidence ID | Tính năng liên quan | Test case liên quan | Loại minh chứng | File / Link | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| `<EVD-001>` | `<Tính năng>` | `<TC ID>` | `<Screenshot / Video / Log>` | `<Path / URL>` | `<Ghi chú>` |

---

# 11. Báo cáo lỗi tổng hợp

## 11.1 Tổng kết lỗi theo mức độ nghiêm trọng

| Mức độ nghiêm trọng | Số lượng |
| --- | ---: |
| Critical | 0 |
| High | 9 |
| Medium | 7 |
| Low | 2 |
| **Tổng cộng** | 18 |

## 11.2 Danh sách lỗi

| Bug ID | Tính năng | Test case liên quan | Tiêu đề | Mức độ nghiêm trọng | Kết quả thực tế | Kết quả mong đợi | Link GitHub Issue | Trạng thái |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BUG-FR03-001` | FR-03 | FR03-DT-06, FR03-BVA-07 | Backend chấp nhận mật khẩu yếu khi đặt lại mật khẩu | High | Backend chấp nhận mật khẩu "weak", "Abc1!xy" | Hệ thống từ chối mật khẩu yếu | [#25](https://github.com/KidCute1412/eshop-sut/issues/25) | Open |
| `BUG-FR03-002` | FR-03 | FR03-DT-01, FR03-BVA-01–06 | OTP thực tế chỉ có 4 chữ số thay vì 6 | Medium | OTP 4 chữ số (vd: 5143) | OTP 6 chữ số (100000-999999) | [#26](https://github.com/KidCute1412/eshop-sut/issues/26) | Open |
| `BUG-FR03-003` | FR-03 | FR-03:C4 | Giao diện thiếu trường xác nhận mật khẩu mới | Medium | Chỉ một ô nhập mật khẩu | Có hai trường mật khẩu + xác nhận | [#27](https://github.com/KidCute1412/eshop-sut/issues/27) | Open |
| `BUG-FR03-004` | FR-03 | FR-03:C5 | Regex mật khẩu frontend yêu cầu khoảng trắng thay vì ký tự đặc biệt | Medium | Regex dùng `\s` thay vì ký tự đặc biệt | Regex dùng `[@$!%*?&]` | [#28](https://github.com/KidCute1412/eshop-sut/issues/28) | Open |
| `BUG-FR09-001` | FR-09 | FR09-DT-01, FR09-DT-09, FR09-BVA-02, FR09-BVA-05 | Coupon bị từ chối khi total bằng đúng min_order_amount | High | Lỗi "chưa đủ giá trị tối thiểu" khi total = min_order | Coupon được chấp nhận (total >= min_order) | [#29](https://github.com/KidCute1412/eshop-sut/issues/29) | Open |
| `BUG-FR09-002` | FR-09 | FR09-DT-05, FR09-BVA-03 | Công thức tính coupon phần trăm sai, discount âm | High | discount_amount âm, final_amount tăng bất thường | discount = total * % / 100, final giảm | [#30](https://github.com/KidCute1412/eshop-sut/issues/30) | Open |
| `BUG-FR09-003` | FR-09 | FR09-DT-05 | API vẫn áp dụng coupon khi không có user/token | High | API chấp nhận coupon khi user_id = null | Từ chối với 401/403 | [#31](https://github.com/KidCute1412/eshop-sut/issues/31) | Open |
| `BUG-FR09-004` | FR-09 | FR09-BVA-08 | Bypass kiểm tra giới hạn sử dụng coupon khi không gửi user_id | Medium | API chấp nhận request không có user_id | Yêu cầu user_id để kiểm tra usage_count | [#32](https://github.com/KidCute1412/eshop-sut/issues/32) | Open |
| `BUG-FR09-005` | FR-09 | FR09-DT-08 | Test data user bị nhiễm trạng thái sử dụng VIP100 | Low | User không còn là first-use | Test data sạch cho first-use scenario | [#33](https://github.com/KidCute1412/eshop-sut/issues/33) | Open |
| `BUG-FR13-001` | FR-13 | FR13-DT-02, FR13-DT-07, FR13-BVA-03 | Dashboard hiển thị doanh thu gấp đôi | High | Doanh thu 200000 thay vì 100000 | Doanh thu đúng bằng total_amount delivered | [#34](https://github.com/KidCute1412/eshop-sut/issues/34) | Open |
| `BUG-FR13-002` | FR-13 | FR13-DT-08 | User thường truy cập được tài nguyên admin | High | Request user thường được chấp nhận | Từ chối với 401/403 | [#35](https://github.com/KidCute1412/eshop-sut/issues/35) | Open |
| `BUG-FR03M-001` | FR-03M | FR03M-DT-01 | API forgot password trả resetToken trực tiếp | High | Response chứa resetToken | Response không chứa token nhạy cảm | [#36](https://github.com/KidCute1412/eshop-sut/issues/36) | Open |
| `BUG-FR03M-002` | FR-03M | FR03M-DT-01, FR03M-BVA-04–09 | OTP 4 chữ số lệch yêu cầu 6 chữ số | Medium | OTP 4 chữ số 1000-9999 | OTP 6 chữ số 100000-999999 | [#37](https://github.com/KidCute1412/eshop-sut/issues/37) | Open |
| `BUG-FR03M-003` | FR-03M | FR03M-DT-14, DT-15, BVA-02, BVA-03 | Mobile kiểm tra special char password sai | High | Chấp nhận space, từ chối special char | Chấp nhận special char, từ chối space | [#38](https://github.com/KidCute1412/eshop-sut/issues/38) | Open |
| `BUG-FR03M-004` | FR-03M | FR03M-DT-08, DT-09, BVA-04, BVA-09 | Mobile không validate OTP số và độ dài | Medium | Gửi request với OTP "abcd" | Chặn input trên form trước khi gửi | [#39](https://github.com/KidCute1412/eshop-sut/issues/39) | Open |
| `BUG-FR03M-005` | FR-03M | FR03M-DT-18 | Reset password không có rate limit | High | Không chặn brute-force OTP | Chặn sau 5-10 lần thử sai | [#40](https://github.com/KidCute1412/eshop-sut/issues/40) | Open |
| `BUG-FR03M-006` | FR-03M | FR03M-DT-02 | API lộ thông tin email tồn tại | Medium | Lỗi "User not found" cụ thể | Thông báo chung, chống email enumeration | [#41](https://github.com/KidCute1412/eshop-sut/issues/41) | Open |
| `BUG-FR03M-007` | FR-03M | FR03M-DT-03 | Mobile không validate định dạng email đầy đủ | Low | Cho gửi email "notanemail" | Chặn email sai định dạng trên form | [#42](https://github.com/KidCute1412/eshop-sut/issues/42) | Open |

## 11.3 Mẫu mô tả chi tiết lỗi (tham khảo)

Chi tiết từng lỗi được mô tả đầy đủ trong các GitHub Issue tương ứng. Dưới đây là mẫu mô tả cho một lỗi điển hình:

### `BUG-FR09-001` – Coupon bị từ chối khi tổng tiền bằng đúng `min_order_amount`

| Mục | Thông tin |
| --- | --- |
| Tính năng | FR-09 - Discount coupons |
| Test case liên quan | FR09-DT-01, FR09-DT-09, FR09-BVA-02, FR09-BVA-05 |
| Mức độ nghiêm trọng | High |
| Độ ưu tiên | High |
| Môi trường | Local, Backend http://localhost:3000 |
| GitHub Issue | [#29](https://github.com/KidCute1412/eshop-sut/issues/29) |
| Minh chứng | evidence/FR09-DT-01-api-log.txt, evidence/FR09-DT-09-api-log.txt, evidence/FR09-BVA-02-api-log.txt, evidence/FR09-BVA-05-api-log.txt |

#### Tiền điều kiện

SUT đang chạy, coupon SAVE10 (min_order_amount=300000) tồn tại trong hệ thống.

#### Các bước tái hiện lỗi

1. Gửi request apply coupon `SAVE10` với `total=300000`.
2. Quan sát phản hồi từ API.
3. Hệ thống trả lỗi "Đơn hàng chưa đủ giá trị tối thiểu 300.000 ₫".

#### Kết quả mong đợi

Coupon được chấp nhận vì `total (300000) >= min_order_amount (300000)`.

#### Kết quả thực tế

API trả lỗi từ chối, backend dùng phép so sánh `>` thay vì `>=`.

#### Ghi chú

Bug này ảnh hưởng đến tất cả coupon và khiến người dùng không thể áp dụng coupon khi đơn hàng bằng đúng giá trị tối thiểu.

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
