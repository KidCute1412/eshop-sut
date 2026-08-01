# HW03 — Defect Report

**Author / Evaluator:** Lê Tuấn Lộc (Student ID: 23127404; 23127404@hcmus.edu.vn)  
**Target Application:** EShop SUT (Web Frontend, Mobile Expo App, Admin Portal, Backend API)  
**Scope:** Functional Requirements FR-07 (Shopping Cart), FR-10 (Order State Machine), FR-11 (Order History), FR-18 (Admin Management), FR-23 (Mobile Product Detail)  
**Candidate Defect Count:** 13 records (BUG-001 through BUG-013), subject to final execution and evidence verification  

> **Evidence integrity gate:** The files currently referenced under `evidence_images/` and `github_issues_screenshots/` are not independently authenticated by this document. Before submission, the student must confirm that each image is a genuine capture of the running SUT or an actual accessible GitHub Issue. Replace any mock, generated, or illustrative image with authentic evidence and update the reference if its filename changes.

---

## Defect Summary

| Bug ID | Title | Severity | Target Feature | Primary Module |
| :--- | :--- | :---: | :---: | :--- |
| **BUG-001** | Web ProductDetail "Thêm vào giỏ hàng" button requires double click to add product | Medium | FR-07 / FR-23 | `frontend-web/src/pages/ProductDetail.jsx` |
| **BUG-002** | Cart accepts 0 and negative quantities without input validation | Medium | FR-07 | `frontend-web/src/pages/Cart.jsx` |
| **BUG-003** | Decimal cart quantity silently truncated to integer without user warning | Low | FR-07 | `frontend-web/src/context/CartContext.jsx` |
| **BUG-004** | Mobile Product Detail screen omits product category name display | Low | FR-23 | `frontend-mobile/App.js` |
| **BUG-005** | Querying non-existent Product ID returns technical error text without CTA navigation | Medium | FR-23 | `frontend-mobile/App.js` & `backend/server.js` |
| **BUG-006** | Web Checkout renders Total Amount inside editable numeric input field | High | FR-07 / FR-10 | `frontend-web/src/pages/Checkout.jsx` |
| **BUG-007** | Web Checkout does not call clearCart() after successful payment, leaving cart populated | Medium | FR-07 | `frontend-web/src/pages/Checkout.jsx` |
| **BUG-008** | Mobile Checkout drops last item from order payload due to cart.slice(0, -1) | Critical | FR-07 / FR-10 | `frontend-mobile/App.js` |
| **BUG-009** | Mobile Cart quantity input change handler adds 1 to entered quantity (parsed + 1) | Medium | FR-07 | `frontend-mobile/App.js` |
| **BUG-010** | Order cancellation logic allows users to cancel orders in shipping state | High | FR-10 / FR-11 | `backend/server.js` & `frontend-web` |
| **BUG-011** | Backend API and Admin UI permit illegal state transition from canceled to delivered | High | FR-10 / FR-18 | `backend/server.js` & `frontend-admin` |
| **BUG-012** | Phone number validation regex /^[1-9][0-9]{8,9}$/ rejects valid Vietnamese phone numbers | High | FR-11 | `frontend-web` & `frontend-mobile` |
| **BUG-013** | Stored XSS vulnerability in Admin shipping address table and double revenue metric bug | Critical | FR-18 | `frontend-admin/src/App.jsx` |

---

## Detailed Defect Records

### BUG-001: Web ProductDetail "Thêm vào giỏ hàng" button requires double click to add product

* **Severity:** Medium
* **FR ID:** FR-07 (Shopping Cart) / FR-23 (Product Detail)
* **Target Module:** `frontend-web/src/pages/ProductDetail.jsx`
* **Environment:** Web Desktop (Chrome / Firefox)

#### Description
On the Web Product Detail page, clicking the green "Thêm vào giỏ hàng" button for the first time fails to add the product to the user's shopping cart state. The first click only increments an internal `clickCount` component state. The user must click the button a second time to dispatch the `addToCart()` context action.

#### Steps to Reproduce
1. Launch Web application and navigate to any Product Detail page (e.g. `http://localhost:5173/product/1`).
2. Observe the initial cart item counter badge in the header navigation bar (e.g. `0`).
3. Click the "Thêm vào giỏ hàng" button **once**.
4. Inspect the header navigation bar cart badge.
5. Click the "Thêm vào giỏ hàng" button a **second time**.

#### Expected Behavior
The first button click dispatches `addToCart(product)` immediately, updating the cart state and header badge from `0` to `1` with feedback notification.

#### Actual Behavior
The first click increments internal `clickCount` state from `0` to `1` without dispatching `addToCart()`. The item is added to the cart only upon the second click.

#### Screenshot References
* **Annotated Evidence:** `evidence_images/bug_001_evidence.png`
* **GitHub Issue Screenshot:** `github_issues_screenshots/bug_001_github.png`

#### Remediation
In `frontend-web/src/pages/ProductDetail.jsx`, eliminate the `clickCount` condition check in `handleAddToCart` and directly invoke `addToCart(product)` on the button onClick handler:
```javascript
// Fix: Directly dispatch addToCart without requiring clickCount state check
const handleAddToCart = () => {
  addToCart({ ...product, quantity });
  toast.success("Đã thêm sản phẩm vào giỏ hàng!");
};
```

---

### BUG-002: Cart accepts 0 and negative quantities without input validation

* **Severity:** Medium
* **FR ID:** FR-07 (Shopping Cart)
* **Target Module:** `frontend-web/src/pages/Cart.jsx` & `frontend-web/src/context/CartContext.jsx`
* **Environment:** Web Desktop & Mobile App

#### Description
The shopping cart quantity handler allows users to input `0` or negative numeric values (e.g., `-5`) into the quantity input field. The application processes these non-positive values without input validation or rejection, resulting in zero or negative subtotal calculations and invalid cart states.

#### Steps to Reproduce
1. Add any product to the shopping cart and navigate to `/cart`.
2. Locate the quantity input field for the cart item.
3. Manually enter `0` or `-5` into the input field.
4. Trigger input blur or form submission.

#### Expected Behavior
The application validates quantity inputs, rejecting values `< 1` with a validation message "Số lượng phải lớn hơn 0" or automatically enforcing a minimum quantity of `1`.

#### Actual Behavior
The system accepts non-positive quantities, updating cart state to `0` or negative counts and calculating negative subtotals.

#### Screenshot References
* **Annotated Evidence:** `evidence_images/bug_002_evidence.png`
* **GitHub Issue Screenshot:** `github_issues_screenshots/bug_002_github.png`

#### Remediation
Update `updateQuantity` in `CartContext.jsx` to enforce a strict minimum threshold of `1`:
```javascript
const updateQuantity = (index, qty) => {
  const sanitizedQty = Math.max(1, parseInt(qty, 10) || 1);
  setCart(prev => prev.map((item, idx) => idx === index ? { ...item, quantity: sanitizedQty } : item));
};
```

---

### BUG-003: Decimal cart quantity silently truncated to integer without user warning

* **Severity:** Low
* **FR ID:** FR-07 (Shopping Cart)
* **Target Module:** `frontend-web/src/context/CartContext.jsx` & `frontend-mobile/App.js`
* **Environment:** Web & Mobile

#### Description
When a user enters a floating-point decimal quantity (e.g. `2.5`) into the quantity field, `parseInt('2.5', 10)` silently truncates the input value to integer `2` without displaying any user warning or input error message.

#### Steps to Reproduce
1. Open the shopping cart page.
2. Enter `2.5` into the quantity field of any cart item.
3. Click outside the input box to trigger change handling.

#### Expected Behavior
The interface displays a clear input validation warning "Số lượng sản phẩm phải là số nguyên dương" and prevents silent modification.

#### Actual Behavior
`parseInt('2.5', 10)` strips the decimal `.5` and updates quantity to `2` silently without notifying the user.

#### Screenshot References
* **Annotated Evidence:** `evidence_images/bug_003_evidence.png`
* **GitHub Issue Screenshot:** `github_issues_screenshots/bug_003_github.png`

#### Remediation
Enforce explicit decimal validation using `Number.isInteger()` before applying updates:
```javascript
if (!Number.isInteger(Number(val))) {
  toast.error("Số lượng sản phẩm phải là số nguyên dương!");
  return;
}
```

---

### BUG-004: Mobile Product Detail screen omits product category name display

* **Severity:** Low
* **FR ID:** FR-23 (Product Detail Mobile)
* **Target Module:** `frontend-mobile/App.js`
* **Environment:** Mobile App (React Native / Expo Go)

#### Description
The Mobile Product Detail screen displays the product image, title, price, and description, but fails to render the product category name (e.g. "Điện thoại", "Laptop"), even though `category_id` and `category_name` are present in the REST API payload.

#### Steps to Reproduce
1. Open the EShop Mobile App on Expo Go.
2. Tap "Xem chi tiết" on any product card from the main catalog.
3. Inspect the product metadata section under the title.

#### Expected Behavior
The category badge or text (e.g., "Danh mục: Thiết bị điện tử") is displayed below the product title.

#### Actual Behavior
The category name element is completely omitted from the React Native UI view.

#### Screenshot References
* **Annotated Evidence:** `evidence_images/bug_004_evidence.png`
* **GitHub Issue Screenshot:** `github_issues_screenshots/bug_004_github.png`

#### Remediation
In `frontend-mobile/App.js`, add a category subtitle tag below the product title:
```javascript
<Text style={styles.categoryBadge}>
  Danh mục: {product.category_name || "Mặc định"}
</Text>
```

---

### BUG-005: Querying non-existent Product ID returns technical error text without CTA navigation

* **Severity:** Medium
* **FR ID:** FR-23 (Product Detail Mobile)
* **Target Module:** `frontend-mobile/App.js` & `backend/server.js`
* **Environment:** Mobile App (React Native / Expo Go)

#### Description
When querying a non-existent Product ID (e.g. `/api/products/999999`), the backend API returns HTTP status 200 with an empty JSON object `{}`. The mobile application catches the empty payload and renders technical error text `"Sản phẩm không tồn tại (Lỗi trắng trang do data rỗng)"` on a blank screen without any "Quay lại trang chủ" CTA navigation button.

#### Steps to Reproduce
1. Trigger mobile product detail view with invalid ID `999999`.
2. Observe screen rendering and user control elements.

#### Expected Behavior
Backend returns HTTP 404 Not Found `{ "error": "Product not found" }`. Mobile app displays a friendly empty state component with a prominent "Quay lại Trang chủ" button.

#### Actual Behavior
Displays raw text `"Sản phẩm không tồn tại (Lỗi trắng trang do data rỗng)"` without back navigation or home CTA buttons, stranding the user.

#### Screenshot References
* **Annotated Evidence:** `evidence_images/bug_005_evidence.png`
* **GitHub Issue Screenshot:** `github_issues_screenshots/bug_005_github.png`

#### Remediation
Fix backend to return HTTP 404 and update mobile app to render a full fallback view with navigation buttons:
```javascript
// Backend server.js
if (!product) return res.status(404).json({ error: "Product not found" });

// Mobile App.js UI Fallback
if (error || !product?.id) {
  return (
    <View style={styles.errorContainer}>
      <Text style={styles.errorText}>Sản phẩm không tồn tại!</Text>
      <TouchableOpacity style={styles.btnHome} onPress={() => navigation.navigate("Home")}>
        <Text style={styles.btnText}>Quay lại Trang chủ</Text>
      </TouchableOpacity>
    </View>
  );
}
```

---

### BUG-006: Web Checkout renders Total Amount inside editable numeric input field

* **Severity:** High
* **FR ID:** FR-07 (Shopping Cart) / FR-10 (Order State Machine)
* **Target Module:** `frontend-web/src/pages/Checkout.jsx`
* **Environment:** Web Desktop (Chrome / Firefox)

#### Description
On the Web Checkout page (`/checkout`), the order total amount is rendered inside an editable `<input type="number">` field bound to local state (`editableTotal`). A malicious customer can manually edit this field, changing the total price from `500,000 ₫` to `0 ₫` or `1 ₫` before clicking "Xác Nhận Thanh Toán". The backend accepts the user-submitted total without server-side recalculation.

#### Steps to Reproduce
1. Add items to cart totaling `500,000 ₫`.
2. Navigate to Checkout page (`/checkout`).
3. Click inside the "Tổng tiền thanh toán" numeric input field.
4. Change the value to `0` or `1`.
5. Click "Xác Nhận Thanh Toán".

#### Expected Behavior
Total order amount is displayed as static formatted text (`<span>500.000 ₫</span>`). Backend recalculates order total server-side based on item prices and quantities.

#### Actual Behavior
Input field allows arbitrary user modification, and order is created with the altered total amount of `0 ₫` or `1 ₫`.

#### Screenshot References
* **Annotated Evidence:** `evidence_images/bug_006_evidence.png`
* **GitHub Issue Screenshot:** `github_issues_screenshots/bug_006_github.png`

#### Remediation
Remove `<input type="number">` element in `Checkout.jsx` and replace with read-only formatted text. Calculate total server-side in `server.js`:
```javascript
// Frontend Checkout.jsx
<div className="text-xl font-bold text-indigo-600">
  {cartTotal.toLocaleString()} ₫
</div>
```

---

### BUG-007: Web Checkout does not call clearCart() after successful payment, leaving cart populated

* **Severity:** Medium
* **FR ID:** FR-07 (Shopping Cart)
* **Target Module:** `frontend-web/src/pages/Checkout.jsx`
* **Environment:** Web Desktop (Chrome / Firefox)

#### Description
When a user completes payment on the Web Checkout page, `handleCheckout` executes order submission and redirects to `/profile`. However, it fails to invoke `clearCart()` from `CartContext`. Consequently, the purchased items remain in the user's cart state and header navigation badge.

#### Steps to Reproduce
1. Add items to cart and proceed through `/checkout`.
2. Click "Xác Nhận Thanh Toán".
3. After automatic navigation to Profile page, observe cart icon badge in the top right header.

#### Expected Behavior
Cart state is reset (`clearCart()`); cart badge updates to `0` items.

#### Actual Behavior
Cart badge retains previous items and count (e.g. `2` items) after successful payment.

#### Screenshot References
* **Annotated Evidence:** `evidence_images/bug_007_evidence.png`
* **GitHub Issue Screenshot:** `github_issues_screenshots/bug_007_github.png`

#### Remediation
Call `clearCart()` in `Checkout.jsx` prior to triggering router redirection:
```javascript
// Fix: Invoke clearCart before navigation
const handleCheckout = async () => {
  await api.post("/checkout", payload);
  clearCart();
  toast.success("Thanh toán thành công!");
  navigate("/profile");
};
```

---

### BUG-008: Mobile Checkout drops last item from order payload due to cart.slice(0, -1)

* **Severity:** Critical
* **FR ID:** FR-07 (Shopping Cart) / FR-10 (Order State Machine)
* **Target Module:** `frontend-mobile/App.js`
* **Environment:** Mobile App (React Native / Expo Go)

#### Description
In the Mobile App checkout handler (`App.js` line 391), the HTTP request body payload constructs the items array as `items: cart.length > 1 ? cart.slice(0, -1) : cart`. When a user checks out with 2 or more items in their cart, `cart.slice(0, -1)` strips the final item from the array sent to the backend. The customer pays full price, but the last item is omitted from the saved order.

#### Steps to Reproduce
1. Add 3 distinct items to cart in Mobile App (Item A, Item B, Item C).
2. Tap "Thanh toán".
3. Check created order details in Database or Admin portal.

#### Expected Behavior
The order payload contains all 3 items (Item A, Item B, Item C).

#### Actual Behavior
Order payload sent to API contains only Item A and Item B. Item C is dropped.

#### Screenshot References
* **Annotated Evidence:** `evidence_images/bug_008_evidence.png`
* **GitHub Issue Screenshot:** `github_issues_screenshots/bug_008_github.png`

#### Remediation
In `frontend-mobile/App.js`, remove `cart.slice(0, -1)` and transmit the entire `cart` array:
```javascript
// Fix: Send full cart array in request payload
body: JSON.stringify({
  items: cart,
  total_amount: finalAmount,
  coupon_id: couponResult?.coupon_id || null,
})
```

---

### BUG-009: Mobile Cart quantity input change handler adds 1 to entered quantity (parsed + 1)

* **Severity:** Medium
* **FR ID:** FR-07 (Shopping Cart)
* **Target Module:** `frontend-mobile/App.js`
* **Environment:** Mobile App (React Native / Expo Go)

#### Description
In `frontend-mobile/App.js` (line 619), the text change handler for cart item quantity sets `newCart[index].quantity = Number.isFinite(parsed) && parsed > 0 ? parsed + 1 : 1`. When a user types a new quantity into the text box (e.g. typing `2`), the code adds `1` to `parsed`, resulting in quantity `3`.

#### Steps to Reproduce
1. Open Mobile Cart with an item of quantity `1`.
2. Tap quantity `TextInput` field and replace `1` with `2`.
3. Tap outside input to register change.

#### Expected Behavior
Item quantity updates to `2`.

#### Actual Behavior
Item quantity updates to `3` (`2 + 1`).

#### Screenshot References
* **Annotated Evidence:** `evidence_images/bug_009_evidence.png`
* **GitHub Issue Screenshot:** `github_issues_screenshots/bug_009_github.png`

#### Remediation
In `frontend-mobile/App.js`, remove `+ 1` arithmetic addition from text change listener:
```javascript
// Fix: Assign parsed value directly without adding 1
newCart[index].quantity = Number.isFinite(parsed) && parsed > 0 ? parsed : 1;
```

---

### BUG-010: Order cancellation logic allows users to cancel orders in shipping state

* **Severity:** High
* **FR ID:** FR-10 (Order State Machine) / FR-11 (Order History)
* **Target Module:** `backend/server.js` & `frontend-web/src/pages/Profile.jsx`
* **Environment:** Web & Backend API

#### Description
In `backend/server.js` (`PUT /api/orders/:id/cancel`), the status check logic is written as `if (order.status === "delivered" || order.status === "canceled") return res.status(400)`. This check fails to block cancellation when order status is `shipping` (Đang giao). Consequently, users can cancel orders already in transit.

#### Steps to Reproduce
1. Admin transitions user order status to `shipping`.
2. Log in as Customer and navigate to Web Profile Order History (`/profile`).
3. Click "Hủy đơn" button on the order in `shipping` status.

#### Expected Behavior
Cancellation is blocked with error message "Không thể hủy đơn hàng đang giao".

#### Actual Behavior
Backend accepts request and updates order status to `canceled`.

#### Screenshot References
* **Annotated Evidence:** `evidence_images/bug_010_evidence.png`
* **GitHub Issue Screenshot:** `github_issues_screenshots/bug_010_github.png`

#### Remediation
Update backend status guard in `server.js` to enforce positive status whitelist:
```javascript
// Fix: Allow cancellation ONLY when order is pending or confirmed
if (order.status !== "pending" && order.status !== "confirmed") {
  return res.status(400).json({ error: "Không thể hủy đơn hàng ở trạng thái hiện tại." });
}
```

---

### BUG-011: Backend API and Admin UI permit illegal state transition from canceled to delivered

* **Severity:** High
* **FR ID:** FR-10 (Order State Machine) / FR-18 (Admin Order Management)
* **Target Module:** `backend/server.js` & `frontend-admin/src/App.jsx`
* **Environment:** Backend API & Admin Web Dashboard

#### Description
In `backend/server.js` (line 550), status transition logic explicitly contains `if (currentStatus === "canceled" && status === "delivered") isValidTransition = true;`. Additionally, `frontend-admin/src/App.jsx` renders an active "Đánh dấu Đã giao" action button for orders in `canceled` status. This violates state machine rules by allowing canceled orders to jump directly to terminal state `delivered`.

#### Steps to Reproduce
1. Open Admin Dashboard (`http://localhost:5174/`) and navigate to Orders tab.
2. Locate any order with status `canceled`.
3. Observe active green button "Đánh dấu Đã giao".
4. Click the button.

#### Expected Behavior
Canceled state is terminal; transition to `delivered` is prohibited, and no action buttons are rendered.

#### Actual Behavior
Status changes from `canceled` to `delivered` in database and UI.

#### Screenshot References
* **Annotated Evidence:** `evidence_images/bug_011_evidence.png`
* **GitHub Issue Screenshot:** `github_issues_screenshots/bug_011_github.png`

#### Remediation
Remove `canceled` -> `delivered` rule from `server.js` and hide action buttons on canceled orders in `frontend-admin`:
```javascript
// Backend server.js: Remove illegal rule
// Admin App.jsx: Hide action buttons when status is canceled
{o.status !== "delivered" && o.status !== "canceled" && (
  // Action buttons
)}
```

---

### BUG-012: Phone number validation regex /^[1-9][0-9]{8,9}$/ rejects valid Vietnamese phone numbers

* **Severity:** High
* **FR ID:** FR-11 (Order History / Profile)
* **Target Module:** `frontend-web/src/pages/Profile.jsx` & `frontend-mobile/App.js`
* **Environment:** Web Desktop & Mobile App

#### Description
In `Profile.jsx` (line 43) and `App.js` (line 287), profile phone number validation uses regex `!/^[1-9][0-9]{8,9}$/.test(phone)`. Standard Vietnamese mobile phone numbers always start with digit `0` (e.g. `0912345678`). Because the regex requires the first digit to be `[1-9]`, every valid Vietnamese mobile number is rejected with error "Số điện thoại không hợp lệ".

#### Steps to Reproduce
1. Navigate to Profile page.
2. Type `0912345678` into phone number input field.
3. Click "Cập nhật thông tin".

#### Expected Behavior
Profile updates successfully with phone number `0912345678`.

#### Actual Behavior
Triggers alert "Số điện thoại không hợp lệ. Vui lòng nhập đúng 9-10 chữ số."

#### Screenshot References
* **Annotated Evidence:** `evidence_images/bug_012_evidence.png`
* **GitHub Issue Screenshot:** `github_issues_screenshots/bug_012_github.png`

#### Remediation
Update regex pattern to support standard Vietnamese prefix `0`:
```javascript
// Fix: Validate Vietnamese phone prefix 03/05/07/08/09
const phoneRegex = /^(0[3|5|7|8|9])[0-9]{8}$/;
if (!phoneRegex.test(phone)) {
  alert("Số điện thoại không hợp lệ. Vui lòng nhập đúng 10 chữ số bắt đầu bằng số 0.");
  return;
}
```

---

### BUG-013: Stored XSS vulnerability in Admin shipping address table and double revenue metric bug

* **Severity:** Critical
* **FR ID:** FR-18 (Admin Order Management)
* **Target Module:** `frontend-admin/src/App.jsx`
* **Environment:** Admin Web Dashboard

#### Description
This issue contains two severe admin portal defects:
1. **Stored XSS Vulnerability:** In `frontend-admin/src/App.jsx` (lines 801-803), the shipping address column renders via `dangerouslySetInnerHTML={{ __html: o.shipping_address }}` without HTML escaping. If an attacker inputs `<img src=x onerror=alert(document.cookie)>` in their shipping address on the store site, arbitrary JavaScript automatically executes in the admin dashboard upon viewing orders.
2. **Dashboard Revenue Calculation Bug:** `frontend-admin/src/App.jsx` (lines 217-220) calculates total revenue as `sum + o.total_amount * 2` for delivered orders, falsely doubling the reported system revenue metric.

#### Steps to Reproduce
1. As a customer, set shipping address to `<img src=x onerror=alert('XSS_ADMIN_COOKIE:'+document.cookie)>` and place order.
2. Log into Admin Dashboard (`http://localhost:5174/`).
3. Click Orders tab and observe script execution alert.
4. Check Dashboard summary card for Total Revenue metric on delivered orders ($100k displayed as $200k).

#### Expected Behavior
1. Shipping address HTML tags are sanitized/escaped, rendering as plain text.
2. Dashboard total revenue equals exact sum of delivered order totals (`sum + o.total_amount`).

#### Actual Behavior
1. Browser executes injected JavaScript payload inside Admin DOM.
2. Revenue display reports double the actual total revenue (`total_amount * 2`).

#### Screenshot References
* **Annotated Evidence:** `evidence_images/bug_013_evidence.png`
* **GitHub Issue Screenshot:** `github_issues_screenshots/bug_013_github.png`

#### Remediation
Replace `dangerouslySetInnerHTML` with standard JSX text node rendering, and fix revenue accumulator formula:
```javascript
// Fix 1: Escape shipping address using standard JSX text rendering
<td className="p-3 font-mono text-sm">
  {o.shipping_address || "Chưa cập nhật"}
</td>

// Fix 2: Correct revenue sum calculation formula
const totalRevenue = orders.reduce((sum, o) => {
  if (o.status === "delivered") return sum + o.total_amount;
  return sum;
}, 0);
```
