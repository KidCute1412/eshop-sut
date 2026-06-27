# Web: FR-13 - Dashboard (Admin Panel)

## 1. Thông tin Feature

| Thuộc tính | Giá trị |
|-----------|--------|
| Feature ID | FR-13 |
| Tên | Dashboard (Admin) |
| Actor | Admin |
| Interface | Web (frontend-admin) |
| URL | http://localhost:5174 |
| Tài khoản | Email: `admin@eshop.com` / Password: `Admin123!` |
| Mô tả | Trang tổng quan admin hiển thị thống kê doanh thu và số đơn hàng |

## 2. Kết quả Code Inspection

### 2.1 Cấu trúc code

- **File**: `frontend-admin/src/App.jsx` (922 dòng)
- Dashboard được render khi `activeTab === "dashboard"` (mặc định)
- Hiển thị 2 thẻ: **Tổng doanh thu (Delivered)** và **Tổng số đơn hàng**

### 2.2 Công thức doanh thu (App.jsx:218)

```javascript
const totalRevenue = orders.reduce((sum, o) => {
    if (o.status === "delivered") return sum + o.total_amount * 2;  // BUG: nhân 2
    return sum;
}, 0);
```

### 2.3 Bugs phát hiện qua code inspection

| # | Bug ID | Mô tả | File | Dòng | Severity |
|---|--------|-------|------|------|----------|
| 1 | DASH-BUG-01 | **Doanh thu bị nhân đôi**: `total_amount * 2` thay vì `total_amount` | App.jsx | 218 | **Cao** |
| 2 | DASH-BUG-02 | **XSS trong shipping_address**: dùng `dangerouslySetInnerHTML` với dữ liệu đơn hàng | App.jsx | ~660 | **Cao** |
| 3 | DASH-BUG-03 | **Sai state transition: canceled → delivered**: Cho phép chuyển từ hủy sang đã giao | server.js | ~518 | **Cao** |
| 4 | DASH-BUG-04 | **Sửa sản phẩm làm sai tên tất cả SP**: `fakeMassUpdatedProducts` đặt tên giống nhau cho mọi sản phẩm | App.jsx | ~165 | **Trung bình** |
| 5 | DASH-BUG-05 | **Checkbox vô dụng**: Checkbox trong bảng Users không có chức năng | App.jsx | ~800 | **Thấp** |
| 6 | DASH-BUG-06 | **Thiếu kiểm tra quyền admin**: Admin API chỉ check token, không check role | server.js | ~366 | **Cao** |

## 3. Domain Testing - Equivalence Partitioning

### 3.1 Biến phân tích

**Biến 1: order.status** (trạng thái đơn hàng)
- Tập giá trị: `pending`, `confirmed`, `shipping`, `delivered`, `canceled`

**Biến 2: order.total_amount** (số tiền đơn hàng)
- Kiểu: integer, >= 0

**Biến 3: shipping_address** (địa chỉ giao hàng)
- Kiểu: string

### 3.2 Variable and Condition Table

| Variable ID | Input/Output | Condition ID | Exact condition | Source |
|------------|-------------|-------------|----------------|--------|
| V1 | Input | C1 | `order.status` ∈ {pending, confirmed, shipping, delivered, canceled} | API spec / server.js |
| V2 | Input | C2 | `order.total_amount` >= 0 | API spec |
| V3 | Input | C3 | `shipping_address` là string bất kỳ | API spec |

### 3.3 Raw Equivalence Class Table

| EC ID | Variable ID | Condition ID | Validity | Precise class | Rationale |
|-------|------------|-------------|---------|--------------|-----------|
| EC1 | V1 | C1 | Valid | status ∈ {pending, confirmed, shipping, delivered} | Các trạng thái hợp lệ tính doanh thu (delivered mới tính) |
| EC2 | V1 | C1 | Valid | status = canceled | canceled không tính doanh thu |
| EC3 | V2 | C2 | Valid | total_amount >= 0 | Số tiền hợp lệ |
| EC4 | V2 | C2 | Invalid | total_amount < 0 | Số âm (lỗi dữ liệu) |
| EC5 | V3 | C3 | Valid | shipping_address là string bất kỳ | Địa chỉ giao hàng |
| EC6 | V3 | C3 | Valid | shipping_address chứa HTML/JS | XSS attack vector |

### 3.4 Combined Equivalence Class Table

| Combined EC ID | Covered raw EC IDs | Validity | Combined condition | Expected behavior |
|---------------|-------------------|---------|-------------------|------------------|
| CEC1 | EC1 (delivered), EC3, EC5 | Valid | status=delivered, amount>=0, địa chỉ thường | Doanh thu = total_amount (đúng), KHÔNG phải total_amount * 2 |
| CEC2 | EC2, EC3, EC5 | Valid | status=canceled, amount>=0, địa chỉ thường | Doanh thu = 0 (không tính) |
| CEC3 | EC1 (pending), EC3, EC5 | Valid | status=pending, amount>=0, địa chỉ thường | Doanh thu = 0 (chưa giao) |
| CEC4 | EC1 (confirmed), EC3, EC5 | Valid | status=confirmed, amount>=0, địa chỉ thường | Doanh thu = 0 (chưa giao) |
| CEC5 | EC1 (shipping), EC3, EC5 | Valid | status=shipping, amount>=0, địa chỉ thường | Doanh thu = 0 (đang giao) |
| CEC6 | EC3, EC6 | Valid | amount>=0, địa chỉ chứa HTML/JS | **LỖI XSS**: script có thể thực thi trong Dashboard |
| CEC7 | EC4, EC5 | Invalid | total_amount < 0 | Hệ thống không nên có đơn hàng với số tiền âm |

### 3.5 Representative Test Selection

| Selection ID | Target EC IDs | Test inputs | Expected output | Bug phát hiện |
|-------------|--------------|------------|----------------|--------------|
| TC-DASH-01 | CEC1 | 1 đơn delivered, total_amount=100000 | Dashboard hiển thị doanh thu = 100.000 | DASH-BUG-01 (thấy 200.000) |
| TC-DASH-02 | CEC2 | 1 đơn canceled, total_amount=50000 | Dashboard hiển thị doanh thu = 0 | Xác nhận canceled không tính |
| TC-DASH-03 | CEC3 | 1 đơn pending, total_amount=200000 | Dashboard hiển thị doanh thu = 0 | Xác nhận pending không tính |
| TC-DASH-04 | CEC4 | 1 đơn confirmed, total_amount=300000 | Dashboard hiển thị doanh thu = 0 | Xác nhận confirmed không tính |
| TC-DASH-05 | CEC5 | 1 đơn shipping, total_amount=150000 | Dashboard hiển thị doanh thu = 0 | Xác nhận shipping không tính |
| TC-DASH-06 | CEC6 | Tạo đơn với shipping_address = `<script>alert('XSS')</script>` | **Không thực thi script** | DASH-BUG-02 (script thực thi) |
| TC-DASH-07 | CEC1 (nhiều đơn) | 3 đơn delivered: 100k + 200k + 300k = 600k | Dashboard hiển thị doanh thu = 600.000 | DASH-BUG-01 (thấy 1.200.000) |

## 4. Boundary Value Analysis (BVA)

### 4.1 Biên cho total_amount

| Boundary ID | Variable ID | EC ID | Boundary type | Valid boundary | Variant | 
|------------|------------|-------|--------------|---------------|---------|
| B1 | V2 | EC3 | Valid minimum | 0 | 3-point |
| B2 | V2 | EC3 | Valid maximum (không giới hạn trên) | N/A | 3-point |

### 4.2 Boundary Value Selection

| Selection ID | Boundary ID | Position | Concrete value | Valid/Invalid | Expected result |
|-------------|------------|----------|---------------|--------------|----------------|
| BVA-DASH-01 | B1 | Below | -1 | Invalid | Không nên tồn tại đơn âm |
| BVA-DASH-02 | B1 | On | 0 | Valid | Doanh thu = 0 |
| BVA-DASH-03 | B1 | Above | 1 | Valid | Doanh thu = 1 (hiển thị 2 nếu bug) |

## 5. Test Case - Chi tiết

### TC-DASH-01: Kiểm tra doanh thu đơn delivered

| Bước | Mô tả | Dữ liệu |
|------|-------|---------|
| 1 | Đăng nhập admin | admin@eshop.com / Admin123! |
| 2 | Đảm bảo backend có ít nhất 1 đơn hàng delivered với total_amount = 100000 | - |
| 3 | Vào Dashboard (mặc định) | - |
| 4 | **Quan sát**: Tổng doanh thu | - |

**Expected**: Doanh thu = 100.000 ₫  
**Actual (bug)**: Doanh thu = 200.000 ₫ (do `total_amount * 2`)  
**Bug**: **DASH-BUG-01** - Doanh thu bị nhân đôi

### TC-DASH-02: Kiểm tra doanh thu đơn canceled

| Bước | Mô tả |
|------|-------|
| 1 | Đăng nhập admin |
| 2 | Tạo đơn hàng, sau đó hủy (canceled) |
| 3 | Vào Dashboard |

**Expected**: Doanh thu không bao gồm đơn canceled  
**Actual**: Đúng (canceled không được cộng)

### TC-DASH-06: Kiểm tra XSS trong shipping_address

| Bước | Mô tả |
|------|-------|
| 1 | Đăng nhập admin |
| 2 | Qua tab Quản lý Đơn hàng |
| 3 | Tạo đơn hàng với shipping_address = `<script>alert('XSS')</script>` |
| 4 | Kiểm tra bảng đơn hàng |

**Expected**: HTML/JS được escape, không thực thi  
**Actual (bug)**: Script thực thi do `dangerouslySetInnerHTML`  
**Bug**: **DASH-BUG-02** - Cross-Site Scripting (XSS)

### TC-DASH-07: Kiểm tra doanh thu nhiều đơn

| Bước | Mô tả |
|------|-------|
| 1 | Đăng nhập admin |
| 2 | Đảm bảo có 3 đơn delivered: 100k + 200k + 300k |
| 3 | Vào Dashboard |

**Expected**: Doanh thu = 600.000 ₫  
**Actual (bug)**: Doanh thu = 1.200.000 ₫ (600k × 2)  
**Bug**: **DASH-BUG-01**

## 6. Bug Details

### DASH-BUG-01: Doanh thu bị nhân đôi (Cao)

**File**: `frontend-admin/src/App.jsx:218`
```javascript
if (o.status === "delivered") return sum + o.total_amount * 2;
// Sửa: return sum + o.total_amount;
```

**Impact**: Sai số liệu doanh thu gấp đôi thực tế.

### DASH-BUG-02: XSS trong shipping_address (Cao)

**File**: `frontend-admin/src/App.jsx:~660`
```jsx
dangerouslySetInnerHTML={{ __html: o.shipping_address || "Chưa cập nhật" }}
```

**Impact**: Attacker có thể chèn script độc hại qua địa chỉ giao hàng.

### DASH-BUG-03: Sai state transition canceled → delivered (Cao)

**File**: `backend/server.js:~518`
```javascript
if (currentStatus === "canceled" && status === "delivered")
    isValidTransition = true;
```

**Impact**: Đơn đã hủy có thể đánh dấu là đã giao - sai logic nghiệp vụ.

### DASH-BUG-04: Sửa sản phẩm làm sai toàn bộ danh sách (Trung bình)

**File**: `frontend-admin/src/App.jsx:~165`
```javascript
const fakeMassUpdatedProducts = products.map((p) => ({
    ...p,
    name: productForm.name,
}));
setProducts(fakeMassUpdatedProducts);
```

**Impact**: Sau khi sửa 1 sản phẩm, tất cả sản phẩm hiển thị cùng tên.

### DASH-BUG-05: Checkbox vô dụng (Thấp)

**File**: `frontend-admin/src/App.jsx:~800`
```jsx
<input type="checkbox" /> {/* Không có onChange, không có state */}
```

**Impact**: Checkbox không có chức năng, gây nhầm lẫn.

### DASH-BUG-06: Thiếu kiểm tra quyền admin (Cao)

**File**: `backend/server.js:~366`
```javascript
// authenticateToken chỉ verify JWT, không check role
```

**Impact**: User thường có thể gọi API admin nếu biết token.

## 7. BVA Coverage Matrix

| Coverage item | Boundary ID | Required values | Test Case IDs | Covered | Gap justification |
|--------------|------------|----------------|--------------|---------|------------------|
| total_amount minimum | B1 | Below, On, Above | BVA-DASH-01, BVA-DASH-02, BVA-DASH-03 | Yes | - |
| total_amount maximum | B2 | - | - | N/A | Không có giới hạn trên |
