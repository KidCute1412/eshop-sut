# Domain Testing

Tài liệu tham chiếu cho Phase 1 và Phase 3 của `SKILL.md`. Nội dung chỉ được lọc và chuẩn hóa từ hai transcript môn Kiểm thử phần mềm do giảng viên Trần Thị Bích Hạnh trình bày.

## Mục lục

1. [Nguồn và phạm vi](#1-nguồn-và-phạm-vi)
2. [Khái niệm](#2-khái-niệm)
3. [Quy trình Domain Testing](#3-quy-trình-domain-testing)
4. [Quy tắc xác định lớp tương đương](#4-quy-tắc-xác-định-lớp-tương-đương)
5. [Kết hợp nhiều điều kiện và nhiều biến](#5-kết-hợp-nhiều-điều-kiện-và-nhiều-biến)
6. [Chọn test case đại diện](#6-chọn-test-case-đại-diện)
7. [Các bảng cần tạo](#7-các-bảng-cần-tạo)
8. [Ví dụ](#8-ví-dụ)
9. [Coverage và kiểm tra cuối](#9-coverage-và-kiểm-tra-cuối)
10. [Ưu điểm và hạn chế](#10-ưu-điểm-và-hạn-chế)

## 1. Nguồn và phạm vi

Nguồn duy nhất:

- `transcript_1782308627.pdf`: bài tổng quan Domain Testing, Equivalence Partitioning và Boundary Value Analysis.
- `transcript_1782309365.txt`: bài hướng dẫn chi tiết Equivalence Partitioning.

Trích dẫn bằng tên transcript và timestamp, ví dụ `[Transcript Domain Testing, 00:01:09-00:02:53]`.

Trong transcript, Domain Testing là phương pháp thiết kế kiểm thử chú trọng các giá trị đầu vào thuộc những miền hoặc phạm vi cụ thể. Mục tiêu là kiểm tra phần mềm hoạt động đúng và ổn định trong các phạm vi dữ liệu đó. `[Transcript Domain Testing, 00:00:01-00:01:38]`

Hai kỹ thuật chính được dùng:

1. Equivalence Partitioning (EP).
2. Boundary Value Analysis (BVA).

Tài liệu này tập trung vào quy trình Domain Testing và EP. Dùng `boundary-value-testing-reference.md` cho BVA.

## 2. Khái niệm

### 2.1 Domain và equivalence class

- **Domain** là tập các giá trị đầu vào có ý nghĩa chung hoặc thuộc cùng một loại.
- Domain của một biến bao gồm cả giá trị hợp lệ và không hợp lệ.
- Domain có thể được chia thành các miền con gọi là **equivalence classes**.
- Hai test inputs thuộc cùng equivalence class khi expected result, hành vi hoặc cách xử lý của chương trình là tương đương; kết quả cụ thể không cần bằng nhau.

Giả định của EP: nếu một giá trị đại diện trong class hoạt động đúng thì các giá trị khác trong class đó cũng có khả năng hoạt động đúng. Nhờ vậy, không cần kiểm thử mọi input có thể có. `[Transcript Domain Testing, 00:03:38-00:06:24]`

### 2.2 Valid và invalid equivalence class

| Loại | Ý nghĩa |
| --- | --- |
| Valid equivalence class | Các giá trị được hệ thống chấp nhận và xử lý như mong đợi |
| Invalid equivalence class | Các giá trị không phù hợp, không thỏa điều kiện hoặc không được hệ thống chấp nhận |

Mỗi biến có ít nhất một valid class và một invalid class. `[Transcript EP, 00:00:39-00:01:46]`

### 2.3 Tính heuristic

Việc xác định equivalence classes là quá trình heuristic: phụ thuộc vào kinh nghiệm, hiểu biết yêu cầu, hiểu biết hệ thống và kiến thức miền của tester. Nếu có lý do tin rằng các giá trị trong cùng class được xử lý khác nhau, chia class đó thành các class con. `[Transcript EP, 00:04:25-00:06:28]`

## 3. Quy trình Domain Testing

Transcript quy định bốn bước.

### Bước 1 - Xác định input và output variables

Đọc specification và liệt kê:

- Các input variables.
- Các output variables hoặc output conditions.
- Các kết quả hợp lệ và error behavior được specification nêu.

Trong ví dụ tính tổng hai số, inputs là `A`, `B`; output là tổng khi input hợp lệ hoặc thông báo lỗi khi input không hợp lệ. `[Transcript Domain Testing, 00:02:20-00:04:14]`

### Bước 2 - Xác định equivalence classes

1. Trích xuất từng condition của mỗi input/output variable.
2. Phân hoạch condition thành valid và invalid classes.
3. Chia nhỏ class nếu các giá trị có thể được xử lý khác nhau.
4. Kết hợp các condition/classes để tạo class hoàn chỉnh cho variable hoặc feature.

### Bước 3 - Chọn representative values và tạo test cases

1. Chọn ít nhất một giá trị đại diện cho mỗi class.
2. Với valid classes, tạo test sao cho một test bao phủ càng nhiều valid classes càng tốt.
3. Với invalid classes, mỗi test chỉ bao phủ một invalid class; các condition/variables khác dùng valid values.
4. Tạo bảng đầy đủ rồi gộp các test hoàn toàn giống nhau.

### Bước 4 - Phân tích giá trị biên

Với numeric ranges, áp dụng thêm BVA để chọn boundary và adjacent values. `[Transcript Domain Testing, 00:01:09-00:02:53; 00:11:38-00:12:41]`

## 4. Quy tắc xác định lớp tương đương

### 4.1 Condition là một khoảng giá trị

Với condition `L <= x <= U`, xác định ít nhất:

| Class | Điều kiện |
| --- | --- |
| Valid | `L <= x <= U` |
| Invalid below | `x < L` |
| Invalid above | `x > U` |

Ví dụ `item count` từ 1 đến 999 tạo ba classes: `[1,999]`, `<1`, `>999`. `[Transcript EP, 00:01:12-00:03:06]`

Giữ nguyên toán tử từ specification. Nếu khoảng dùng biên mở, class phải phản ánh đúng biên mở.

### 4.2 Condition là một tập giá trị

Nếu input phải thuộc một tập và có lý do tin mỗi giá trị được xử lý khác nhau:

- Mỗi allowed value là một valid class riêng.
- Các giá trị ngoài tập tạo một invalid class.

Ví dụ các loại xe `bus`, `truck`, `taxicab`, `passenger`, `motorcycle`: năm valid classes và một invalid class ngoài tập. `[Transcript EP, 00:02:29-00:04:23]`

### 4.3 Condition dạng “must be”

Tạo hai classes:

- Valid: thỏa điều kiện.
- Invalid: không thỏa điều kiện.

Ví dụ “ký tự đầu tiên của ID phải là chữ”: first character là chữ và first character không phải chữ. `[Transcript EP, 00:03:47-00:05:02]`

### 4.4 Chia nhỏ class

Nếu có lý do tin các phần trong class được xử lý khác nhau, chia class thành các class con.

Ví dụ khoảng `[-99,99]` có thể được chia thành:

- `< -99`.
- `[-99,-1]`.
- `{0}`.
- `[1,99]`.
- `> 99`.

Chỉ chia khi có lý do liên quan đến cách xử lý của chương trình. `[Transcript EP, 00:04:25-00:07:06]`

### 4.5 Input và output classes

Xác định classes cho cả input và output conditions khi specification mô tả chúng. Trong ví dụ tính tổng:

- Input class: là số hoặc không phải số; nằm trong hoặc ngoài khoảng cho phép.
- Output class: tổng của hai số hoặc thông báo lỗi.

Expected output của test case phải tương ứng với representative inputs đã chọn. `[Transcript Domain Testing, 00:06:22-00:08:13]`

## 5. Kết hợp nhiều điều kiện và nhiều biến

### 5.1 Một biến có nhiều conditions

1. Phân hoạch riêng từng condition.
2. Tạo valid class kết hợp sao cho bao phủ càng nhiều valid condition classes càng tốt.
3. Với mỗi invalid condition class, giữ các condition khác hợp lệ.
4. Mỗi invalid combined class chỉ chứa một nguyên nhân invalid.

Quy tắc này cô lập lỗi: nếu test thất bại, tester có thể biết invalid class nào liên quan. `[Transcript EP, 00:07:46-00:09:50]`

### 5.2 Nhiều input variables

1. Xác định classes cho từng variable riêng.
2. Tạo valid combination bao phủ valid classes của nhiều variables.
3. Khi kiểm thử invalid class của một variable, giữ variables khác trong valid classes.

Không kết hợp nhiều invalid classes trong cùng một test.

## 6. Chọn test case đại diện

### 6.1 Valid classes

Chọn values để một test case bao phủ càng nhiều valid equivalence classes càng tốt. Tiếp tục cho đến khi mọi valid class được phủ.

### 6.2 Invalid classes

Mỗi test case chỉ bao phủ một invalid class. Chọn valid values cho các conditions và variables còn lại. Tiếp tục cho đến khi mọi invalid class được phủ.

### 6.3 Rút gọn test cases

1. Lập bảng đầy đủ từ các representative selections.
2. So sánh toàn bộ inputs và expected output.
3. Gộp test cases hoàn toàn giống nhau.
4. Giữ traceability từ test đã gộp đến mọi class được phủ.

Trong ví dụ transcript, ba rows `EC1`, `EC5`, `EC9` tạo cùng inputs/expected output và được gộp; bảng cuối còn bảy test cases. `[Transcript Domain Testing, 00:09:27-00:12:14]`

## 7. Các bảng cần tạo

### 7.1 Variable and Condition Table

`Variable ID | Input/Output | Condition ID | Exact condition | Source/timestamp | Basis ID`

### 7.2 Raw Equivalence Class Table

`EC ID | Variable ID | Condition ID | Validity | Precise class | Different processing rationale | Basis ID`

Tạo bảng này trước khi kết hợp conditions.

### 7.3 Combined Equivalence Class Table

`Combined EC ID | Covered raw EC IDs | Validity | Combined condition | Other conditions/classes | Expected behavior | Basis ID`

Mỗi invalid combined class chỉ chứa một raw invalid EC; các raw EC khác phải valid.

### 7.4 Representative Test Selection

`Selection ID | Target EC IDs | Representative inputs | Expected output | Duplicate of | Test Case ID`

### 7.5 Domain Testing Coverage Matrix

`Coverage item/EC ID | Validity | Test Case IDs | Covered | Gap justification`

Dùng test-case format của `SKILL.md` và giữ liên kết từ test case tới các EC được bao phủ.

## 8. Ví dụ

### 8.1 Số nguyên dương nhỏ hơn 100

Conditions:

- `C1`: input phải là integer.
- `C2`: `0 < input < 100`.

Raw classes:

| EC | Condition | Validity | Class |
| --- | --- | --- | --- |
| EC1 | C1 | Valid | Integer |
| EC2 | C1 | Invalid | Not integer |
| EC3 | C2 | Valid | `0 < input < 100` |
| EC4 | C2 | Invalid | `input <= 0` |
| EC5 | C2 | Invalid | `input >= 100` |

Combined classes:

- Valid: integer và `0 < input < 100`.
- Invalid: not integer.
- Invalid: integer và `input <= 0`.
- Invalid: integer và `input >= 100`.

`[Transcript EP, 00:06:28-00:10:58]`

### 8.2 Hai variables

Specification: `3 <= x <= 7`, `5 <= y <= 9`.

- Một valid class: x và y đều trong khoảng hợp lệ.
- Bốn invalid classes: `x<3`, `x>7`, `y<5`, `y>9`.
- Khi x invalid, y hợp lệ; khi y invalid, x hợp lệ.

Tổng cộng năm combined classes. `[Transcript EP, 00:10:11-00:12:56]`

### 8.3 ID

Specification: ID có 3-15 ký tự chữ/số và hai ký tự đầu là chữ.

Conditions:

1. Chỉ gồm ký tự chữ/số.
2. Độ dài 3-15.
3. Hai ký tự đầu là chữ.

Tạo một valid combined class thỏa cả ba conditions và bốn invalid classes: sai loại ký tự, ngắn hơn 3, dài hơn 15, hoặc hai ký tự đầu không phải chữ. `[Transcript EP, 00:12:21-00:15:59]`

## 9. Coverage và kiểm tra cuối

Coverage đạt khi:

- Mỗi input/output variable và condition đã được liệt kê.
- Mỗi condition có valid và invalid classes phù hợp.
- Class được chia nhỏ khi có căn cứ về different processing.
- Mọi valid class được phủ bởi representative tests.
- Mỗi invalid class được phủ riêng; variables/conditions khác valid.
- Duplicate tests được gộp mà không mất EC traceability.
- Numeric ranges đã được chuyển sang Phase 4 BVA.

Checklist:

- [ ] Đã giữ nguyên khoảng, tập giá trị và “must be” condition từ specification.
- [ ] Đã phân hoạch từng condition trước khi kết hợp.
- [ ] Valid tests bao phủ nhiều valid classes khi có thể.
- [ ] Invalid tests chỉ chứa một invalid class.
- [ ] Representative values thực sự thuộc class mục tiêu.
- [ ] Expected output tương ứng với representative inputs.
- [ ] Coverage Matrix phủ mọi EC hoặc ghi gap.

## 10. Ưu điểm và hạn chế

Theo transcript, Domain Testing:

**Ưu điểm**

- Tìm lỗi hiệu quả với số lượng test nhỏ, tập trung vào values quan trọng.
- Quy trình phân chia classes và chọn representatives rõ ràng, dễ học và áp dụng.
- Có thể mở rộng khi có nhiều variables.

**Hạn chế**

- Không bảo đảm phát hiện mọi lỗi hoặc mọi special case.
- Có thể kém linh hoạt trong tình huống phức tạp.
- Hiệu quả phụ thuộc nhiều vào kiến thức và kinh nghiệm của tester khi xác định classes.

`[Transcript Domain Testing, 00:19:13-00:20:49]`
