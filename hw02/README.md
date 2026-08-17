# HW02 - Domain Testing trên hệ thống EShop

## 1. Tổng quan bài nộp

Các tính năng được chọn:

| Pool | Feature ID | Tên tính năng |
| --- | --- | --- |
| A | `FR-03` | Quên mật khẩu và đặt lại mật khẩu |
| B | `FR-09` | Mã giảm giá |
| C | `FR-13` | Dashboard Admin |
| D | `FR-03M` | Mobile - Quên mật khẩu và đặt lại mật khẩu |

## 2. Test Summary Report

### 2.1 Tổng kết chung

| Chỉ số | Số lượng |
| --- | ---: |
| Số tính năng được kiểm thử | 4 |
| Tổng số test case đã thiết kế | 74 |
| Test case đã thực thi | 47 |
| Passed | 29 |
| Failed | 18 |
| Blocked | 26 |
| Not Executed | 1 |
| Test case chưa thể hoàn tất | 27 |
| Bug đã ghi nhận | 11 |
| Blocking issue | 1 |

### 2.2 Tổng kết theo tính năng

| Feature | Tổng test case | Passed | Failed | Blocked | Not Executed | Bug / Blocker |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `FR-03` | 17 | 12 | 5 | 0 | 0 | 4 bugs |
| `FR-09` | 18 | 12 | 6 | 0 | 0 | 3 bugs |
| `FR-13` | 13 | 5 | 7 | 0 | 1 | 4 bugs |
| `FR-03M` | 26 | 0 | 0 | 26 | 0 | 1 blocker |
| **Total** | **74** | **29** | **18** | **26** | **1** | **11 bugs + 1 blocker** |

### 2.3 Demo video

| Nội dung | Link |
| --- | --- |
| Agent Skill demo | https://youtu.be/iP9ianRHrcE |

## 3. Bug Summary

| Feature | Bug ID / Blocking ID | Tóm tắt |
| --- | --- | --- |
| `FR-03` | `BUG-FR03-001` | Hệ thống chấp nhận mật khẩu yếu khi đặt lại mật khẩu. |
| `FR-03` | `BUG-FR03-002` | Hệ thống từ chối mật khẩu mạnh hợp lệ khi đặt lại mật khẩu. |
| `FR-03` | `BUG-FR03-003` | OTP hiển thị 4 chữ số thay vì 6 chữ số theo yêu cầu. |
| `FR-03` | `BUG-FR03-004` | Màn hình quên mật khẩu không hiển thị Step Indicator. |
| `FR-09` | `BUG-FR09-001` | Coupon phần trăm tính sai discount và final amount. |
| `FR-09` | `BUG-FR09-002` | Hệ thống cho áp dụng coupon khi người dùng chưa đăng nhập. |
| `FR-09` | `BUG-FR09-003` | Coupon bị từ chối khi tổng tiền bằng đúng min order. |
| `FR-13` | `BUG-FR13-001` | Dashboard hiển thị doanh thu gấp đôi giá trị mong đợi. |
| `FR-13` | `BUG-FR13-002` | User không phải Admin vẫn truy cập được tài nguyên admin. |
| `FR-13` | `BUG-FR13-003` | Đơn hàng đã hủy vẫn có thể đánh dấu đã giao. |
| `FR-13` | `BUG-FR13-004` | Dashboard hiển thị doanh thu âm khi đơn delivered có giá trị âm. |
| `FR-03M` | `BLOCKER-FR03M-001` | Không thể kiểm thử mobile do mọi request bị network timeout. |

## 4. Self-Assessment

| No. | Criteria | Grade | Self-Assessed Grade |
| ---: | --- | ---: | ---: |
| 1 | Feature A - `FR-03` (Domain + Boundary) | 25 | 25 |
| 2 | Feature B - `FR-09` (Domain + Boundary) | 25 | 25 |
| 3 | Feature C - `FR-13` (Domain + Boundary) | 25 | 25 |
| 4 | Feature D - `FR-03M` (Mobile, Domain + Boundary) | 15 | 15 |
| 5 | Agent Skills | 10 | 10 |
|  | **Total** | **100** | **100** |


