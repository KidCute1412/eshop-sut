# HW05 Video 01 - Performance-test demonstration

**Target duration:** 3 minutes 45 seconds  
**Language:** Vietnamese narration by the student  
**Purpose:** Demonstrate the real JMeter execution evidence. Keep Apache JMeter and Windows Task Manager visible in the same frame while each scenario result is shown.

This clip is the first half of the required unlisted YouTube demonstration. Together with Video 02, the total target duration is 6 minutes 15 seconds, exceeding the required six minutes.

## Before recording

- Start the local EShop backend on `http://localhost:3000`.
- Open Task Manager on the `Processes` or `Details` view and make `node.exe` visible.
- Open JMeter and load the relevant JMX plans from `deliverables/plans/`.
- Open the final Summary/Aggregate/Results Tree views already captured under `deliverables/evidence/execution/` when a live rerun would take too long.
- Do not claim a metric that is not visible in the corresponding JTL or JMeter report.

## Shot list and Vietnamese narration

| Time | Screen / action | Narration |
| --- | --- | --- |
| 0:00-0:25 | Show the repository folder, JMeter test-plan tree, and Task Manager with `node.exe`. | "Em là sinh viên 23127404. Đây là HW05 Performance Testing cho EShop backend chạy local. Em kiểm thử cùng một workflow gồm login, xem chi tiết sản phẩm, thêm vào giỏ hàng và checkout. Bên phải là Task Manager hiển thị tiến trình backend trong lúc JMeter thực thi." |
| 0:25-1:10 | Show the Load plan and Summary Report. Point to the four request labels, sample count, and error column. | "Đây là Load scenario. Plan dùng CSV data, lấy token sau login và truyền Bearer token cho các request bảo vệ. Kết quả cuối có 200 samples, 0 errors và p95 là 14 milliseconds. Các số liệu được lấy từ raw JTL, không suy ra từ ảnh chụp." |
| 1:10-1:55 | Show the Stress plan and Aggregate Report, with Task Manager still visible. | "Đây là Stress scenario với số virtual users cao hơn nhưng vẫn cùng workflow và dữ liệu kiểm thử. Kết quả có 800 samples, 0 errors và p95 là 13 milliseconds. Task Manager được đặt cùng frame để liên kết kết quả với môi trường backend local." |
| 1:55-2:35 | Show the Spike plan and View Results Tree. | "Đây là Spike scenario, dùng ramp-up ngắn để tạo tải đột ngột. View Results Tree là report view khác với hai scenario trước. Run cuối có 500 samples, 0 errors và p95 là 14 milliseconds." |
| 2:35-3:15 | Show the validated Endurance JMX, its raw JTL, and the HTML report folder. | "Đây là Endurance plan đã được kiểm tra có thể mở lại bằng JMeter. Run xác thực có 4,400 samples thành công, không có lỗi, p95 là 12 milliseconds và thời lượng 632.403 giây. Raw JTL và HTML dashboard đều được nộp để có thể kiểm tra lại." |
| 3:15-3:45 | Show the lockout evidence pair and the Issue page briefly. | "Em cũng kiểm tra runtime của lockout. Hai lần nhập sai trả HTTP 401; sau đó login đúng lại trả HTTP 403. Đây là lỗi lockout sớm đã được ghi nhận trên GitHub Issue kèm evidence. Video tiếp theo sẽ trình bày Agent Skill dùng để kiểm tra evidence và phân tích JTL." |

## Recording acceptance checklist

- [ ] Vietnamese narration is audible throughout.
- [ ] JMeter and Task Manager appear together for Load, Stress, and Spike.
- [ ] Labels and metric values are readable.
- [ ] The narration matches the final raw JTL values.
- [ ] No password, token, or unrelated personal data is visible.

