|ID|Partition|Input Values|Expected Output Values|Applied Boundary Values|
|---|---|---|---|---|
|EC01|Matching search term|Search query matching an existing product name, e.g. "Macbook"|Only matching products are shown|No|
|EC02|Non-matching search term|Search query with no matching product, e.g. "zzzzz"|Empty state is shown and no product cards appear|No|
|EC03|Unsafe search input|Search input containing HTML-like text, e.g. "&lt;script>alert(1)&lt;/script>"|The input is displayed safely as text and does not break the UI. Empty state is shown and no product cards appear|No|
|EC04|Blank search input|Empty string or whitespace-only input|The full product list is shown again|No|
|EC05|Matching Unicode search term|Search query matching an existing product name with Unicode, e.g. "Bàn phím"|Only matching products are shown|No|
|EC06|Matching Products Only|Any non-empty valid search query|Only matching products are shown|No|
|EC07|Empty Product List|Any invalid search query or a valid search query with zero matching products|Empty state is shown and no product cards appear|No|
|EC08|Full Product List|Initial state or an empty search query|The full product list is shown|No|
|EC09|Initial history view|None|Empty display|No|
|EC10|Order creation|Any valid order of items of a user's account|The history appends a new order, displaying the status "Chờ xác nhận"|No|
|EC11|Order confirmation|Admin confirmation of an existing order with status "Chờ xác nhận"|The history updates the order, changing the status from "Chờ xác nhận" to "Đã xác nhận"|No|
|EC12|Order delivery|Admin delivery confirmation of an existing order with status "Đã xác nhận"|The history updates the order, changing the status from "Đã xác nhận" to "Đang giao"|No|
|EC13|Order completion|Admin completion confirmation of an existing order with status "Đang giao"|The history updates the order, changing the status from "Đang giao" to "Đã giao"|No|
|EC14|Order cancellation|Cancellation confirmation of an existing order|The history updates the order, changing the status to "Đã hủy"|No|
|EC15|Admin order cancellation|Admin cancellation confirmation of an existing order|The history updates the order, changing the status to "Đã hủy"|No|
|EC16|Foreign order creation|Any valid order of items of another user's account|The history does not append a new order|No|
|EC17|Empty history|None|Empty display|No|
|EC18|History appends a new order|Any valid order of items of a user's account|The history appends a new order, displaying the status "Chờ xác nhận"|No|
|EC19|History changes the status of an order|Any update confirmation of an existing order|The history updates the order and changes the status|No|
|EC20|History does not update|Any incomplete order of items of a user's account or any valid order of items of another user's account|The history does not update, remaining the same|No|
