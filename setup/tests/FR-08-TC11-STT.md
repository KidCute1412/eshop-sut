|ID|Objective|Input|Steps|Expected|Actual|Verdict|
|-|-|-|-|-|-|-|
|FR-08-TC11|Inventory validation failure during processing (reject)|Authenticated user; item becomes out-of-stock during process|1. Login; ensure cart contains item with limited stock (1 unit).<br>2. Open checkout.<br>3. In parallel, decrement stock via API or purchase from another user so item is unavailable.<br>4. Submit payment.|Backend detects inventory issue during processing, returns error (409 or 400) describing unavailable item; cart remains unchanged; no order created.| |Blocked|
