# BLOCKER-FR03M-001: Không thể kiểm thử FR-03M do network timeout trên mobile

| Mục | Thông tin |
| --- | --- |
| Tính năng | FR-03M - Mobile: Forgot password and password reset |
| Test case liên quan | FR03M-DT-*, FR03M-BVA-* |
| Mức độ nghiêm trọng | High |
| Trạng thái | Open |
| GitHub Issue | https://github.com/KidCute1412/eshop-sut/issues/50 |

## Mô tả
Không thể kiểm thử tính năng FR-03M trên mobile vì mọi request đều bị network timeout.

## Tiền điều kiện
- Mobile app đang chạy trên thiết bị thật qua Expo Go
- Backend đang chạy trên máy tính

## Các bước tái hiện
1. Mở mobile app (Expo Go) trên điện thoại
2. Truy cập tính năng Forgot Password hoặc bất kỳ màn hình nào có gọi API
3. Thực hiện request (ví dụ gửi email forgot-password)
4. Quan sát request bị network timeout
5. Lặp lại với các request khác của FR-03M và xác nhận tất cả đều timeout

## Kết quả mong đợi
Mobile có thể gửi request forgot password/reset password và nhận response từ hệ thống.

## Kết quả thực tế
Mọi request từ mobile bị network timeout, khiến toàn bộ test case FR-03M không thể thực thi.

## Ảnh hưởng
- Toàn bộ Domain Testing (18 TC) và BVA (9 TC) của FR-03M bị block
- 27/27 test case chuyển sang trạng thái Blocked

## Nguyên nhân phân tích
1. IP backend hardcode `192.168.10.13` trong `frontend-mobile/App.js:16` có thể không match IP thực của máy
2. `fetch()` không có timeout (AbortController), khiến UI treo khi request không đến được server
