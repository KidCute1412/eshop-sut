# Boundary Value Analysis (BVA)

Tài liệu tham chiếu cho Phase 1 và Phase 4 của `SKILL.md`. Nội dung chỉ được lọc và chuẩn hóa từ `transcript_1782308627.pdf`.

Các lỗi nhận dạng rõ ràng được sửa theo ngữ cảnh: `binary value analysis` thành `Boundary Value Analysis`, `three Point pary values` thành `3-point boundary values`, và `-998` thành `-98` trong phép tính kề `-99`.

## Mục lục

1. [Phạm vi và mục tiêu](#1-phạm-vi-và-mục-tiêu)
2. [Khái niệm](#2-khái-niệm)
3. [2-point boundary values](#3-2-point-boundary-values)
4. [3-point boundary values](#4-3-point-boundary-values)
5. [Quy trình thực hiện](#5-quy-trình-thực-hiện)
6. [Nhiều biến và cô lập lỗi](#6-nhiều-biến-và-cô-lập-lỗi)
7. [Các bảng cần tạo](#7-các-bảng-cần-tạo)
8. [Ví dụ](#8-ví-dụ)
9. [Coverage và checklist](#9-coverage-và-checklist)

## 1. Phạm vi và mục tiêu

BVA là bước 4 của Domain Testing trong transcript. Kỹ thuật được áp dụng thêm cho numeric equivalence classes để chọn test values tại và ngay cạnh boundary. `[Transcript Domain Testing, 00:11:38-00:12:41]`

Mục tiêu là phát hiện lỗi thường xuất hiện tại ranh giới miền, đặc biệt:

- Sai toán tử so sánh, ví dụ `< 25` bị cài đặt thành `<= 25`.
- Sai boundary value, ví dụ `25` bị cài đặt thành `52`.

Một value xa boundary có thể cho cùng output ở cả implementation đúng và sai nên không phát hiện được các lỗi này. `[Transcript Domain Testing, 00:12:09-00:15:11]`

## 2. Khái niệm

### 2.1 Valid boundary value

Valid boundary value là giá trị nhỏ nhất hoặc lớn nhất mà chương trình có thể chấp nhận.

Với valid range `[-99,99]`:

- `-99` là valid minimum boundary.
- `99` là valid maximum boundary.

### 2.2 Adjacent value

Adjacent value là giá trị ngay dưới hoặc ngay trên boundary.

Trong ví dụ integer của transcript, adjacent values cách boundary một đơn vị:

- Quanh `-99`: `-100`, `-99`, `-98`.
- Quanh `99`: `98`, `99`, `100`.

Không tự áp dụng bước `1` cho non-integer data vì transcript chỉ minh họa integer ranges.

## 3. 2-point boundary values

Với mỗi valid boundary, chọn hai values:

1. Valid boundary value.
2. Một adjacent value phía ngoài valid range.

| Boundary type | Required values |
| --- | --- |
| Valid minimum `L` | `L` và value ngay dưới `L` |
| Valid maximum `U` | `U` và value ngay trên `U` |

`[Transcript Domain Testing, 00:14:37-00:16:28]`

## 4. 3-point boundary values

Với mỗi valid boundary, chọn ba values:

1. Value ngay dưới boundary.
2. Value tại boundary.
3. Value ngay trên boundary.

Với integer closed range `[L,U]`:

| Boundary | Required values |
| --- | --- |
| Minimum `L` | `L-1`, `L`, `L+1` |
| Maximum `U` | `U-1`, `U`, `U+1` |

3-point BVA tạo sáu selections cho một variable có hai distinct boundaries. `[Transcript Domain Testing, 00:15:12-00:17:23]`

## 5. Quy trình thực hiện

### Bước 1 - Chọn numeric equivalence class

Đọc Equivalence Class Table của Domain Testing và chọn numeric class có valid minimum/maximum boundary.

### Bước 2 - Xác định valid boundaries

Ghi valid minimum và valid maximum chính xác từ specification.

### Bước 3 - Chọn 2-point hoặc 3-point

Transcript giới thiệu cả hai variant và dùng 3-point trong ví dụ; transcript không tuyên bố một variant duy nhất là bắt buộc cho mọi bài toán.

### Bước 4 - Tính boundary values

Tạo required values theo variant. Với integer example, dùng adjacent values cách một đơn vị.

### Bước 5 - Giữ variables khác hợp lệ

Khi kiểm thử boundary của một variable, chọn valid representative values cho các variables còn lại để cô lập lỗi.

### Bước 6 - Xác định expected output

Tính hoặc lấy expected output tương ứng với từng test input từ specification.

### Bước 7 - Tạo test cases và coverage matrix

Tạo test cho mọi required boundary value, gắn boundary/variant reference và giữ BVA cases tách biệt với EP cases.

## 6. Nhiều biến và cô lập lỗi

Transcript áp dụng quy tắc one-variable-at-a-time:

1. Chọn boundary values cho variable mục tiêu.
2. Giữ variables khác ở valid representative values.
3. Lặp lại với từng variable.

Với hai integer variables A và B cùng range `[-99,99]`, 3-point BVA tạo:

- Sáu tests cho A khi B valid.
- Sáu tests cho B khi A valid.
- Tổng cộng 12 tests trong bảng BVA của ví dụ.

`[Transcript Domain Testing, 00:15:54-00:17:44]`

## 7. Các bảng cần tạo

### 7.1 Boundary Definition

`Boundary ID | Variable ID | EC ID | Boundary type | Valid boundary value | Variant | Transcript reference | Basis ID`

### 7.2 Boundary Value Selection

`Selection ID | Boundary ID | Position | Concrete value | Valid/Invalid | Other variables' valid values | Expected output | Test Case ID`

Dùng `Below`, `On`, `Above` cho 3-point. Với 2-point, dùng `On` và `Outside adjacent`.

### 7.3 BVA Coverage Matrix

`Coverage item | Boundary ID | Required values | Test Case IDs | Covered | Gap justification`

Dùng test-case format của `SKILL.md` và giữ liên kết từ test case tới boundary values được bao phủ.

## 8. Ví dụ

### 8.1 Range `[-99,99]`

| Boundary | 2-point values | 3-point values |
| --- | --- | --- |
| Minimum `-99` | `-100`, `-99` | `-100`, `-99`, `-98` |
| Maximum `99` | `99`, `100` | `98`, `99`, `100` |

Khi xét A, giữ B trong valid range; khi xét B, giữ A trong valid range.

### 8.2 Threshold `25`

Specification mẫu trong transcript:

- `input < 10`: error message.
- `10 <= input < 25`: `Hello`.
- `input >= 25`: error message.

Input `25` nằm tại boundary và expected output là error message. Nó phát hiện được cả lỗi `<25` bị viết thành `<=25` và boundary `25` bị viết thành `52`; input xa boundary như `53` không phát hiện được hai lỗi đó. `[Transcript Domain Testing, 00:12:09-00:15:11]`

### 8.3 Giá trị cực trị của kiểu dữ liệu

Ngoài representative value và six 3-point boundary values của một numeric range, transcript cho phép cân nhắc thêm:

- Minimum value mà ứng dụng cho phép nhập cho kiểu số.
- Maximum value mà ứng dụng cho phép nhập cho kiểu số.

Ví dụ với integer là minimum integer value và maximum integer value. Khi cả hai giá trị này được thêm, transcript mô tả tối đa chín selections cho một numeric class: một EP representative, sáu 3-point BVA values và hai type-extreme values. `[Transcript Domain Testing, 00:17:14-00:19:46]`

## 9. Coverage và checklist

Coverage đạt khi:

- Mỗi eligible numeric class có valid minimum và maximum boundary.
- Mỗi boundary có đủ values của selected variant.
- Với multiple variables, từng variable được kiểm tra trong khi variables khác valid.
- Mỗi concrete value có expected output và test case.
- EP representative, BVA values và optional type-extreme values không bị nhầm lẫn.

Checklist:

- [ ] Đã chọn đúng 2-point hoặc 3-point variant.
- [ ] Valid minimum/maximum lấy từ specification.
- [ ] Adjacent integer values được tính đúng.
- [ ] Variables không phải mục tiêu dùng valid values.
- [ ] Expected output tương ứng với từng concrete input.
- [ ] Coverage Matrix phủ mọi required boundary value.
