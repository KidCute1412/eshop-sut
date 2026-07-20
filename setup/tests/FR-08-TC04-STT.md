|ID|Objective|Input|Steps|Expected|Actual|Verdict|
|-|-|-|-|-|-|-|
|FR-08-TC04|Checkout UI displays full product list and read-only total|Authenticated user with multiple cart items|1. Login.<br>2. Ensure cart has items A (qty2) and B (qty1).<br>3. Open `/checkout` UI.|UI shows full product list with item names, qty, unit prices and a read-only total equal to client-side cart sum. Total field is not editable.|2 types of products are added, the sum is correct and no price modification can be made. |Passed|
