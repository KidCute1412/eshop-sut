# BÁO CÁO KẾT QUẢ KIỂM THỬ

**Sinh viên:** 23127404  
**Bài:** PostgreSQL Database Testing Mini Lab

## 1. Tổng quan Test Run

- Môi trường: Docker Compose; PostgreSQL 17 Alpine; Node.js 22 Alpine; Jest 30;
  Supertest 7.
- Cách chạy: `run.bat` trên Windows hoặc `./run.sh` trên Linux/macOS.
- Dữ liệu: 5 users, 5 products, 200 orders và 4 coupons.
- Tổng số test đã chạy: 12.
- Kết quả baseline ngày 27/07/2026: 8 Pass, 4 Fail có chủ đích.
- Defect phải được phát hiện: `FN-01`, `SP-01`, `API-STATE-01`, `SQLI-01`.
- Bằng chứng runtime: `portable/evidence/test-run.log` và
  `portable/evidence/test-results.json`.

Runner xác nhận `LAB RESULT: PASS`: đúng bốn defect dự kiến được phát hiện và
không có failure ngoài danh sách.

## 2. Thiết kế Domain Testing và BVA

### 2.1. Equivalence Partitioning

| Variable / Condition | Valid Equivalence Classes | Invalid Equivalence Classes |
| :--- | :--- | :--- |
| Email | **EP-VAL-01:** Email chưa tồn tại | **EP-INV-01:** Email trùng UNIQUE |
| Discount percent | **EP-VAL-02:** `0..100` | **EP-INV-02:** `>100`, làm discount vượt order |
| Product stock | **EP-VAL-03:** Integer `>=0` | **EP-INV-03:** Integer `<0` |
| Checkout inventory | **EP-VAL-04:** Mọi item đủ hàng | **EP-INV-04:** Có ít nhất một item hết hàng |
| Coupon expiry | **EP-VAL-05:** Active và còn hạn | **EP-INV-05:** Đã hết hạn |
| Order transition | **EP-VAL-06:** Cạnh hợp lệ của state machine | **EP-INV-06:** Chuyển từ final state |
| Search query | **EP-VAL-07:** Chuỗi tìm kiếm thông thường | **EP-INV-07:** SQL metacharacter/payload |
| Database role | **EP-VAL-08:** `app_user` đọc products | **EP-INV-08:** `app_user` chạy DDL |

### 2.2. Boundary Value Analysis

| Variable | Boundary Condition | In-Point | On-Point | Off-Point | ID |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Discount percent | Không vượt `100%` | `50` | `100` | `101` | BVA-BND-01 |
| Product stock | Stock phải `>=0` | `5` | `0` | `-1` | BVA-BND-02 |
| Coupon minimum | Order amount phải `>=200` | `300` | `200` | `199.99` | BVA-BND-03 |

## 3. Danh sách lỗi phát hiện

### 3.1. FN-01 — `fn_calculate_discount` không giới hạn mức giảm

- Input: `type='percent'`, `value=150`, `order_amount=200`.
- Expected: discount `<=200`.
- Actual baseline: discount `300`.
- Test case: `FN-01 [EP-INV-02/BVA-BND-01]`.
- Root cause: function trả trực tiếp `order_amount * value / 100`, không dùng
  `LEAST(..., order_amount)` và không validate percent.
- Fix đề xuất: từ chối percent ngoài `0..100` hoặc cap discount tại tổng đơn.

### 3.2. SP-01 — `sp_process_checkout` phá vỡ atomicity

- Input: user 2 mua product 1 số lượng 1, sau đó product 5 đang hết hàng.
- Expected: procedure báo lỗi; stock product 1 giữ nguyên `10`; không có order
  hoặc order item dở dang.
- Actual baseline: procedure báo lỗi nhưng product 1 còn `9` và một order dở
  dang đã được commit.
- Test case: `SP-01 [EP-INV-04]`.
- Root cause: `COMMIT` được thực hiện sau từng order item.
- Fix đề xuất: bỏ commit trong loop; validate toàn bộ tồn kho trước, sau đó cập
  nhật trong một transaction duy nhất.

### 3.3. Trigger — `trg_prevent_negative_stock`

- Trạng thái: **Đạt**.
- On-point: cập nhật stock thành `0` thành công.
- Off-point: cập nhật stock thành `-1` bị từ chối với SQLSTATE `P0001` và message
  định danh trigger.
- Test cases: `TRIGGER-00`, `TRIGGER-01`.

### 3.4. API-STATE-01 — Cho phép `canceled → delivered`

- Input: order 1 đang `canceled`, admin gửi `status='delivered'`.
- Expected: HTTP `400`, trạng thái không đổi.
- Actual baseline: HTTP `200`, order bị chuyển thành `delivered`.
- Root cause: transition map khai báo sai cạnh từ final state `canceled`.
- Fix đề xuất: để danh sách transition của `canceled` và `delivered` rỗng.

### 3.5. SQLI-01 — API search nội suy trực tiếp

- Input: query `' OR '1'='1`.
- Expected: payload được coi là chuỗi literal, kết quả rỗng.
- Actual baseline: điều kiện được mở rộng và trả toàn bộ 5 products.
- Kiểm tra bổ sung: API không trả 500 và số products trước/sau vẫn là 5.
- Root cause: ghép `q` trực tiếp vào câu SQL.
- Fix đề xuất: dùng `WHERE name ILIKE $1` với parameter `%' + q + '%'`.

### 3.6. Các kiểm tra đạt khác

- UNIQUE email từ chối bản ghi trùng với SQLSTATE `23505`.
- Coupon `CP_EXPIRED` trả HTTP `400`.
- Coupon `CP_OK` tại đúng minimum `200` được chấp nhận.
- `app_user` đọc được products nhưng `DROP TABLE` bị từ chối với SQLSTATE
  `42501`.

## 4. Kết quả Hiệu năng

Truy vấn đo:

```sql
SELECT user_id, SUM(final_amount)
FROM orders
GROUP BY user_id
ORDER BY SUM(final_amount) DESC;
```

| Lần đo | Scan | Execution Time | Buffers |
| :--- | :--- | :--- | :--- |
| Trước index | Seq Scan | 0.210 ms | shared hit=2; planning hit=41 |
| Sau index | Seq Scan | 0.156 ms | shared hit=2; planning hit=12, read=1 |

Với khoảng 200 dòng và truy vấn aggregate toàn bảng, planner có thể tiếp tục
chọn Seq Scan vì hầu hết các tuple đều phải được đọc. Việc index không được sử
dụng trong trường hợp này không tự động là defect. Chênh lệch 0.054 ms rất nhỏ
và nằm trong nhiễu của một phép đo nhỏ; không thể kết luận index cải thiện hiệu
năng chỉ từ một lần chạy.

## 5. Nhật ký MCP

- MCP server: `minilab_postgres`, kết nối bằng role chỉ đọc `mcp_reader`.
- Kiểm tra kết nối ngày 27/07/2026: **Đạt**; handshake MCP protocol
  `2024-11-05`, tool `query` được liệt kê và truy vấn `information_schema`
  trả về 5 bảng public. Bằng chứng: `portable/evidence/mcp-smoke.log`.
- Prompt:

  > Liệt kê các bảng, khóa ngoại, constraints, trigger, function và stored
  > procedure trong schema public. Với mỗi đối tượng, nêu tên, bảng liên quan
  > và mục đích; kiểm chứng bằng pg_catalog hoặc information_schema.

- Tóm tắt phản hồi: **Điền từ thread Codex sau khi chạy `run` và mở lại folder.**
- Cách kiểm chứng:
  - Tables/columns: `information_schema.tables`, `information_schema.columns`.
  - Constraints/FK: `information_schema.table_constraints` và
    `key_column_usage`.
  - Trigger: `pg_trigger` kết hợp `pg_class`.
  - Function/procedure: `pg_proc` kết hợp `pg_namespace`, kiểm tra `prokind`.
- Phân biệt bằng chứng: phản hồi AI chỉ dùng để khám phá; kết luận trong báo cáo
  phải dựa trên catalog query, Jest và `EXPLAIN ANALYZE`.

## 6. Kết luận và Khuyến nghị

Baseline đáp ứng việc minh họa constraint, trigger và RBAC, nhưng có bốn lỗi
nghiêm trọng về giới hạn discount, atomicity, state transition và SQL Injection.
Ưu tiên sửa transaction checkout và SQL Injection trước, sau đó sửa state
machine và validation discount. Chạy lại cùng test suite sau sửa; tiêu chí hoàn
thành là 12/12 test pass và không thay đổi các test oracle.
