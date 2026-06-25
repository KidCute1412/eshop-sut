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
| Tổng số test case Domain Testing | 7 |
| Passed | 5 |
| Failed | 1 |
| Blocked | 1 |
| Not Executed | 0 |
| Needs Review | 0 |

## 6.4 Boundary Value Analysis

### 6.4.1 Biến có giá trị biên

| Boundary Variable ID | Biến | Quy tắc biên | Giá trị nhỏ nhất | Giá trị lớn nhất | Giá trị bình thường | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| `FR03-BVAR-01` | `resetToken` | OTP thực tế của backend nằm trong khoảng `1000–9999`. | `1000` | `9999` | OTP hợp lệ được tạo từ bước 1 | Đặc tả yêu cầu OTP 6 chữ số, nhưng backend tạo OTP 4 chữ số. |
| `FR03-BVAR-02` | `newPassword` length | Mật khẩu phải có tối thiểu 8 ký tự. | `8 ký tự` | Không nêu rõ | `NewPass123!` | Kiểm thử tập trung vào biên dưới của độ dài mật khẩu. |

### 6.4.2 Giá trị biên

| Boundary ID | Biến | Loại biên | Giá trị | Hành vi mong đợi | Basis ID |
| --- | --- | --- | --- | --- | --- |
| `FR03-B-001` | `resetToken` | `min-1` | `999` | Bị từ chối vì nhỏ hơn miền OTP thực tế. | `FR-03:C2`, `FR-03:C6` |
| `FR03-B-002` | `resetToken` | `min` | `1000` | Được chấp nhận nếu đúng là token đang lưu cho email. | `FR-03:C2`, `FR-03:C6` |
| `FR03-B-003` | `resetToken` | `min+1` | `1001` | Được chấp nhận nếu đúng là token đang lưu cho email. | `FR-03:C2`, `FR-03:C6` |
| `FR03-B-004` | `resetToken` | `max-1` | `9998` | Được chấp nhận nếu đúng là token đang lưu cho email. | `FR-03:C2`, `FR-03:C6` |
| `FR03-B-005` | `resetToken` | `max` | `9999` | Được chấp nhận nếu đúng là token đang lưu cho email. | `FR-03:C2`, `FR-03:C6` |
| `FR03-B-006` | `resetToken` | `max+1` | `10000` | Bị từ chối vì lớn hơn miền OTP thực tế. | `FR-03:C2`, `FR-03:C6` |
| `FR03-B-007` | `newPassword` length | `min-1` | 7 ký tự, ví dụ `Abc1!xy` | Bị từ chối vì ngắn hơn 8 ký tự. | `FR-03:C5` |
| `FR03-B-008` | `newPassword` length | `min` | 8 ký tự, ví dụ `Test1234!` | Được chấp nhận nếu thỏa các nhóm ký tự bắt buộc. | `FR-03:C5` |

### 6.4.3 Test case BVA

| Test Case ID | Boundary ID liên quan | Tiêu đề | Tiền điều kiện | Dữ liệu đầu vào | Các bước thực hiện | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Minh chứng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `FR03-BVA-01` | `FR03-B-001` | OTP nhỏ hơn biên dưới | SUT đang chạy. | `email = test@eshop.com`<br>`resetToken = 999`<br>`newPassword = NewPass123!` | 1. Gửi yêu cầu reset với OTP `999`.<br>2. Quan sát phản hồi. | Hệ thống từ chối OTP ngoài miền. | API trả `{"error":"Invalid token or email"}` với HTTP 400. | Passed | `evidence/FR03-BVA-01-api-log.txt` |
| `FR03-BVA-02` | `FR03-B-002` | OTP tại biên dưới `1000` | Cần có quyền chỉnh dữ liệu DB để ép token thành `1000`. | `resetToken = 1000` | 1. Đặt token của user thành `1000` trong DB.<br>2. Gửi yêu cầu reset với token này. | Nếu token đúng với email, hệ thống đặt lại mật khẩu thành công. | Không thể ép backend tạo token cụ thể nếu không có quyền chỉnh DB. | Blocked | N/A — requires DB access |
| `FR03-BVA-03` | `FR03-B-003` | OTP ngay trên biên dưới `1001` | Cần có quyền chỉnh dữ liệu DB để ép token thành `1001`. | `resetToken = 1001` | 1. Đặt token của user thành `1001` trong DB.<br>2. Gửi yêu cầu reset với token này. | Nếu token đúng với email, hệ thống đặt lại mật khẩu thành công. | Không thể ép backend tạo token cụ thể nếu không có quyền chỉnh DB. | Blocked | N/A — requires DB access |
| `FR03-BVA-04` | `FR03-B-004` | OTP ngay dưới biên trên `9998` | Cần có quyền chỉnh dữ liệu DB để ép token thành `9998`. | `resetToken = 9998` | 1. Đặt token của user thành `9998` trong DB.<br>2. Gửi yêu cầu reset với token này. | Nếu token đúng với email, hệ thống đặt lại mật khẩu thành công. | Không thể ép backend tạo token cụ thể nếu không có quyền chỉnh DB. | Blocked | N/A — requires DB access |
| `FR03-BVA-05` | `FR03-B-005` | OTP tại biên trên `9999` | Cần có quyền chỉnh dữ liệu DB để ép token thành `9999`. | `resetToken = 9999` | 1. Đặt token của user thành `9999` trong DB.<br>2. Gửi yêu cầu reset với token này. | Nếu token đúng với email, hệ thống đặt lại mật khẩu thành công. | Không thể ép backend tạo token cụ thể nếu không có quyền chỉnh DB. | Blocked | N/A — requires DB access |
| `FR03-BVA-06` | `FR03-B-006` | OTP lớn hơn biên trên | SUT đang chạy. | `email = test@eshop.com`<br>`resetToken = 10000`<br>`newPassword = NewPass123!` | 1. Gửi yêu cầu reset với OTP `10000`.<br>2. Quan sát phản hồi. | Hệ thống từ chối OTP ngoài miền. | API trả `{"error":"Invalid token or email"}` với HTTP 400. | Passed | `evidence/FR03-BVA-06-api-log.txt` |
| `FR03-BVA-07` | `FR03-B-007` | Mật khẩu có 7 ký tự | Đã tạo OTP hợp lệ cho `test@eshop.com`. | `email = test@eshop.com`<br>`resetToken = 5837`<br>`newPassword = Abc1!xy` | 1. Nhập OTP hợp lệ.<br>2. Nhập mật khẩu 7 ký tự.<br>3. Gửi yêu cầu reset. | Hệ thống phải từ chối vì mật khẩu dưới 8 ký tự. | API trả `{"message":"Password reset successfully"}` — backend chấp nhận mật khẩu 7 ký tự. | Failed | `evidence/FR03-BVA-07-api-log.txt` |
| `FR03-BVA-08` | `FR03-B-008` | Mật khẩu tại biên tối thiểu 8 ký tự | Đã tạo OTP hợp lệ cho `test@eshop.com`. | `email = test@eshop.com`<br>`resetToken = restore`<br>`newPassword = Test1234!` | 1. Nhập OTP hợp lệ.<br>2. Nhập mật khẩu 8 ký tự trở lên và thỏa yêu cầu.<br>3. Gửi yêu cầu reset. | Hệ thống đặt lại mật khẩu thành công. | API trả `{"message":"Password reset successfully"}`. | Passed | `evidence/FR03-BVA-08-api-log.txt` |

### 6.4.4 Tổng kết BVA

| Chỉ số | Số lượng |
| --- | ---: |
| Tổng số test case BVA | 8 |
| Passed | 3 |
| Failed | 1 |
| Blocked | 4 |
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

# 7. Báo cáo tính năng B

> Thay phần này bằng tính năng bạn chọn từ Pool B. Có thể sử dụng cùng cấu trúc với tính năng A.

## 7.1 Thông tin tính năng

| Mục | Thông tin |
| --- | --- |
| Mã tính năng | `<FR-xx>` |
| Tên tính năng | `<Tên tính năng>` |
| Nhóm tính năng | `Pool B` |
| Vai trò liên quan | `<Guest / Customer / Admin>` |
| Vị trí trên UI | `<Trang / route>` |
| API endpoint liên quan | `<Danh sách endpoint>` |

## 7.2 Mô tả tính năng

`<Mô tả hành vi của tính năng bằng lời của bạn.>`

## 7.3 Cơ sở kiểm thử riêng của tính năng

| Basis ID | Nguồn | Vị trí | Yêu cầu / Quy tắc | Điểm mơ hồ hoặc ghi chú |
| --- | --- | --- | --- | --- |
| `<B-BASIS-01>` | `<Nguồn>` | `<Vị trí>` | `<Yêu cầu / quy tắc>` | `<Ghi chú>` |

## 7.4 Domain Testing

### 7.4.1 Biến miền và ràng buộc

| Variable ID | Biến / Trạng thái | Kiểu / Đơn vị | Ràng buộc / Phụ thuộc | Kết quả có thể quan sát | Basis ID |
| --- | --- | --- | --- | --- | --- |
| `<B-VAR-01>` | `<Biến>` | `<Kiểu>` | `<Ràng buộc>` | `<Kết quả>` | `<Basis ID>` |

### 7.4.2 Miền hợp lệ và không hợp lệ

| Domain ID | Biến / Quy tắc | Loại miền | Định nghĩa miền | Hành vi mong đợi | Basis ID |
| --- | --- | --- | --- | --- | --- |
| `<B-D-V-01>` | `<Biến>` | `Hợp lệ` | `<Định nghĩa>` | `<Hành vi mong đợi>` | `<Basis ID>` |
| `<B-D-I-01>` | `<Biến>` | `Không hợp lệ` | `<Định nghĩa>` | `<Hành vi mong đợi>` | `<Basis ID>` |

### 7.4.3 Test case Domain Testing

| Test Case ID | Domain ID liên quan | Tiêu đề | Tiền điều kiện | Dữ liệu đầu vào | Các bước thực hiện | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Minh chứng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `<B-DT-001>` | `<Domain IDs>` | `<Tiêu đề>` | `<Tiền điều kiện>` | `<Input>` | `<Steps>` | `<Expected>` | `<Actual>` | `<Status>` | `<Screenshot / Video / Log>` |

### 7.4.4 Tổng kết Domain Testing

| Chỉ số | Số lượng |
| --- | ---: |
| Tổng số test case Domain Testing | `<Số lượng>` |
| Passed | `<Số lượng>` |
| Failed | `<Số lượng>` |
| Blocked | `<Số lượng>` |
| Not Executed | `<Số lượng>` |
| Needs Review | `<Số lượng>` |

## 7.5 Boundary Value Analysis

### 7.5.1 Biến có giá trị biên

| Boundary Variable ID | Biến | Quy tắc biên | Giá trị nhỏ nhất | Giá trị lớn nhất | Giá trị bình thường | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| `<B-BVAR-01>` | `<Biến>` | `<Quy tắc>` | `<Min>` | `<Max>` | `<Normal>` | `<Ghi chú>` |

### 7.5.2 Giá trị biên

| Boundary ID | Biến | Loại biên | Giá trị | Hành vi mong đợi | Basis ID |
| --- | --- | --- | --- | --- | --- |
| `<B-B-001>` | `<Biến>` | `<min-1 / min / min+1 / max-1 / max / max+1>` | `<Giá trị>` | `<Mong đợi>` | `<Basis ID>` |

### 7.5.3 Test case BVA

| Test Case ID | Boundary ID liên quan | Tiêu đề | Tiền điều kiện | Dữ liệu đầu vào | Các bước thực hiện | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Minh chứng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `<B-BVA-001>` | `<Boundary IDs>` | `<Tiêu đề>` | `<Tiền điều kiện>` | `<Input>` | `<Steps>` | `<Expected>` | `<Actual>` | `<Status>` | `<Screenshot / Video / Log>` |

### 7.5.4 Tổng kết BVA

| Chỉ số | Số lượng |
| --- | ---: |
| Tổng số test case BVA | `<Số lượng>` |
| Passed | `<Số lượng>` |
| Failed | `<Số lượng>` |
| Blocked | `<Số lượng>` |
| Not Executed | `<Số lượng>` |
| Needs Review | `<Số lượng>` |

## 7.6 Lỗi phát hiện ở tính năng B

| Bug ID | Test case liên quan | Tiêu đề | Mức độ nghiêm trọng | Trạng thái | Link GitHub Issue | Minh chứng |
| --- | --- | --- | --- | --- | --- | --- |
| `<BUG-B-001>` | `<TC ID>` | `<Tiêu đề lỗi>` | `<Low / Medium / High / Critical>` | `<Open / Closed>` | `<Link>` | `<Screenshot / Video>` |

---

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
