# Mini Exercise — API Testing

**Sinh viên:** 23127404  
**API được chọn:** `GET /api/products/:id`  
**Mục tiêu:** Thiết kế, audit, chạy data-driven bằng Postman/Newman và CI cho API đọc chi tiết sản phẩm.

## 1. Generate with AI

### Prompt đã dùng

> Bạn là API test designer. Hãy thiết kế tối thiểu 12 test case cho `GET /api/products/:id` của eshop-sut. Request có header `X-Student-Id`; API hiện trả JSON product khi ID tồn tại, gồm `id`, `name`, `price`, `description`, `imageUrl`, `category_id`. Hãy bao phủ equivalence partitions, BVA cho path parameter `id`, schema/Content-Type/response time và các input bất thường. Trả về bảng gồm: `tc_id`, `input`, `expected status`, `expected fields`, `rationale`. Không tạo test mutation hay giả định auth nếu endpoint không yêu cầu token.

### AI output rút gọn

| TC | Input `id` | Expected status | Expected fields | Rationale |
|---|---|---:|---|---|
| AI-01 | `1` | 200 | full product schema | ID tồn tại hợp lệ. |
| AI-02 | `2` | 200 | full product schema, numeric price | Kiểm tra record khác. |
| AI-03 | ID tồn tại lớn nhất | 200 | full product schema | Biên trên dữ liệu. |
| AI-04 | `0` | 400 | error | ID không dương. |
| AI-05 | `-1` | 400 | error | Giá trị ngay dưới biên. |
| AI-06 | `999999` | 404 | error | ID không tồn tại. |
| AI-07 | `abc` | 400 | error | Không phải số. |
| AI-08 | `1.5` | 400 | error | Không phải số nguyên. |
| AI-09 | `` (empty path segment) | 404 | error | Thiếu path parameter. |
| AI-10 | `01` | 200 hoặc 400 | contract-defined | Dạng biểu diễn có leading zero. |
| AI-11 | `1 OR 1=1` | 400 | error | Input injection-like. |
| AI-12 | `1` | 200 | JSON Content-Type, timely response | Non-functional contract. |

## 2. Domain testing và BVA

| ID | Biến/điều kiện | Lớp hợp lệ | Lớp không hợp lệ |
|---|---|---|---|
| EP-VAL-01 | `id` | Integer dương, tồn tại trong bảng products | — |
| EP-INV-01 | `id` | — | Integer dương nhưng không tồn tại |
| EP-INV-02 | `id` | — | `0` hoặc integer âm |
| EP-INV-03 | `id` | — | Chuỗi không phải integer, decimal, injection-like |
| EP-ENV-01 | HTTP contract | JSON response có schema product khi product tồn tại | Sai/missing Content-Type hoặc schema |

| ID | Biên | On-point | Off-point | In-point |
|---|---|---|---|---|
| BVA-BND-01 | ID dương nhỏ nhất | `1` | `0`, `-1` | `3` |
| BVA-BND-02 | Biên tập dữ liệu hiện có | `5` (seed product) | `999999` | `2` |
| BVA-BND-03 | Kiểu integer | integer `1` | `1.5`, `abc` | `3` |

## 3. Audit (human review)

| TC | Nhãn | Nhận xét hoặc chỉnh sửa |
|---|---|---|
| AI-01 | VALID | Product ID 1 tồn tại và response thực tế là 200 JSON có đủ field. |
| AI-02 | INCOMPLETE | Case đúng hướng nhưng cần xác định type `price`; thực tế ID chẵn 2 trả `price` là string. |
| AI-03 | INCOMPLETE | “ID tồn tại lớn nhất” không ổn định nếu database thay đổi; thay bằng record seed xác định ID 3. |
| AI-04 | INVALID | SUT thực tế trả `200 {}` cho `0`, không phải 400; ghi đây là REST-contract defect. |
| AI-05 | INVALID | SUT thực tế trả `200 {}` cho `-1`, không phải 400; đây là off-point BVA cần báo lỗi. |
| AI-06 | INVALID | SUT thực tế trả `200 {}` cho 999999 thay vì 404; case được giữ lại để ghi nhận defect. |
| AI-07 | INVALID | SUT thực tế trả `200 {}` cho `abc`; đây là input validation defect. |
| AI-08 | INCOMPLETE | Cần chạy riêng trước khi kết luận status vì Express/SQLite không validate kiểu route parameter. |
| AI-09 | VALID | Empty segment không match route `/api/products/:id`, nên server sẽ 404. |
| AI-10 | INCOMPLETE | Đặc tả không quy định leading zero; không đưa vào 5 iteration ổn định. |
| AI-11 | INCOMPLETE | Endpoint SQL đang parameterized, nhưng expected status vẫn phải được xác minh bằng execution trước khi assertion. |
| AI-12 | VALID | Content-Type JSON và response-time là assertion bắt buộc trong collection. |

**Sửa case bắt buộc:** AI-06 được sửa thành hai kỳ vọng tách biệt: expected REST contract là `404` có error body; observed SUT behavior là `200 {}`. Data-driven run assert observed behavior để 5 iteration chạy xanh, còn sai lệch được báo rõ là defect, không bị coi là specification hợp lệ.

## 4. Extend — test case tự bổ sung

| TC | Input | Expected/observation | Vì sao AI bỏ sót |
|---|---|---|---|
| EXT-01 | Mọi iteration | Header `Content-Type` chứa `application/json`; response time < 2000 ms | Model thường ưu tiên status/body và bỏ qua non-functional HTTP contract. |
| EXT-02 | `id=2` | Product tồn tại nhưng `price` quan sát là string, trái với numeric price contract | AI không có execution result nên không thể phát hiện behavior phụ thuộc parity của ID. |
| EXT-03 | `id=999999` hoặc `abc` | Observed `200 {}`; expected REST contract phải là 404/400 | Model giả định REST chuẩn, không biết API thiếu validation. |

## 5. Bộ 5 iteration được chạy bằng Newman

| Data TC | Input | Assertion chạy | Traceability |
|---|---|---|---|
| PBI-01 | `1` | 200, schema product, price number, JSON, <2s | EP-VAL-01, BVA-BND-01 |
| PBI-02 | `2` | 200, schema product, observed price string, JSON, <2s | EP-VAL-01, EXT-02 |
| PBI-03 | `3` | 200, schema product, price number, JSON, <2s | EP-VAL-01, BVA-BND-01 |
| PBI-04 | `999999` | observed 200 empty JSON object, JSON, <2s | EP-INV-01, BVA-BND-02, EXT-03 |
| PBI-05 | `abc` | observed 200 empty JSON object, JSON, <2s | EP-INV-03, BVA-BND-03, EXT-03 |

## 6. Postman features đã dùng

| Feature | Đã dùng? | Ghi chú |
|---|---|---|
| Collections | Có | Collection chứa request data-driven cho endpoint đã chọn. |
| Environment variables | Có | Dùng `baseUrl` và `studentId` trong environment local. |
| Collection variables | Không | Không cần biến ở collection scope cho một request. |
| Pre-request scripts | Có | Upsert header `X-Student-Id` trước mỗi request. |
| Test scripts (assertions) | Có | Kiểm tra status, Content-Type, response time và response schema. |
| Data-driven runs (Collection Runner + data file) | Có | Năm records trong JSON tạo đúng 5 iteration. |
| Newman CLI | Có | Chạy collection headless và xuất JSON report. |
| Monitors | Không | Không thuộc phạm vi bài local/CI này. |
| Mock servers | Không | Kiểm thử provider thật, không dùng mock. |
| Workspaces | Không | Không cần evidence workspace để chạy artefact đã export. |

## 7. Kết quả execution và CI

- Lệnh Newman và file `mini-newman-report.json` là bằng chứng execution local.
- Workflow `newman-api-test.yml` cài dependencies, chạy provider, đợi readiness, chạy Newman và upload report.
- `ci-pass.png` và `ci-fail.png` sẽ được thêm sau khi push hai trạng thái lên GitHub Actions; commit cuối phải khôi phục data đúng để workflow pass.
