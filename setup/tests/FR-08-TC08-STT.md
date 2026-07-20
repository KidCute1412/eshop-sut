|ID|Objective|Input|Steps|Expected|Actual|Verdict|
|-|-|-|-|-|-|-|
|FR-08-TC08|Payment gateway failure handling (cart preserved)|Authenticated user with cart items; payment gateway returns failure|1. Login; ensure cart has items.<br>2. Submit payment; simulate gateway failure (decline or error).|Backend returns failure (4xx/5xx) with reason; cart remains unchanged; user can retry or cancel.| |Blocked|
