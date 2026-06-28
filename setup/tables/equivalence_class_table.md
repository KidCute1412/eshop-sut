|ID|Partition|Input Values|Expected Output Values|Applied Boundary Values|
|---|---|---|---|---|
|EC01|Standard matching search term|Search query matching an existing product name, e.g. "Macbook"|Only matching products are shown|No|
|EC02|Non-matching search term|Search query with no matching product, e.g. "zzzzz"|Empty state is shown and no product cards appear|No|
|EC03|Unsafe search input|Search input containing HTML-like text, e.g. "&lt;script>alert(1)&lt;/script>"|The input is displayed safely as text and does not break the UI. Empty state is shown and no product cards appear|No|
|EC04|Blank search input|Empty string or whitespace-only input|The full product list is shown again|Yes|
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
|EC21|Valid standard category name|A non-empty standard category name such as "Electronics"|The category is created and appears in the category list|No|
|EC22|Valid Unicode category name|A non-empty Unicode category name such as "Máy tính"|The category is created and appears in the category list|No|
|EC23|Whitespace-only category name|A value containing only spaces such as "   "|The create action is rejected with a validation error and no category is added|Yes|
|EC24|Category Deletion|Delete confirmation of a category|The corresponding category is deleted.|No|
|EC25|New Category|Any valid category name|The category is created and appears in the category list|No|
|EC26|No Category Updates|Any invalid category name|The create action is rejected with a validation error and no category is added|No
|EC27|Deleted Category|Delete confirmation of a category|The corresponding category is deleted.|No|
|EC28|Standard Name|Any valid standard name that does not reach char limit, e.g. "Test"|Product when added has matching name.|No|
|EC29|White-space Name|A name with only white-space that does not reach char limit, e.g. " "|Product cannot be added to the pool.|Yes|
|EC30|Script Injection Name|An invalid HTML scripted name that does not reach char limit, e.g. "&lt;script>alert(1)&lt;/script>"|Product cannot be added to the pool.|No|
|EC31|Overlength name|A name that reaches char limit, e.g. "a"x256|Product cannot be added to the pool.|Yes|
|EC32|Valid Link Image|A valid image link name, e.g. "https://cloudinary-marketing-res.cloudinary.com/images/w_1000,c_scale/v1679921049/Image_URL_header/Image_URL_header-png?_i=AA"|Product when added has the image shown|No|
|EC33|Non-Link Non-Script Image|An invalid non-script name, e.g "123"|Product cannot be added to the pool.|No|
|EC34|Script Injection Image|An invalid HTML scripted link, e.g. "&lt;script>alert(1)&lt;/script>"|Product cannot be added to the pool.|Product cannot be added to the pool.|No|
|EC35|Valid Price|A valid positive price point, e.g. "1"|Product when added has matching price tag.|Yes|
|EC36|Not a number Price|A NaN price point, e.g. "--"|Product cannot be added to the pool.|No|
|EC37|Negative Price|An invalid non-positive price point, e.g. "-1"|Product cannot be added to the pool.|Yes|
|EC38|Valid Description|A description with any regular text input, e.g. "description"|Product when added has matching description.|No|
|EC39|Script Injection Image|A description with a script, e.g. "&lt;script>alert(1)&lt;/script>"|Product when added has description with no script (empty).|No|
|EC40|No Category|Category is not selected|Product cannot be added to the pool.|No|
|EC41|Category Selected|A category from the spinner is selected, e.g. "Laptop"|Product when added has matching category.|No|
|EC42|Product Added|Valid name, image link, price, description and category.|Product when added has matching details.|No|
|EC43|Product List Not Changed|Having an invalid input in one of: name, image link, price, description and category.|Product cannot be added to the pool.|No|
|EC44|Product Deleted|None other than pressing "Xóa"|Product is removed safely|No|
|EC45|Product Adjusted|Valid name, image link, price, description and category after pressing "Xóa"|Product is adjusted accordingly|No|
