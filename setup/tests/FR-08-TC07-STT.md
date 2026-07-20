|ID|Objective|Input|Steps|Expected|Actual|Verdict|
|-|-|-|-|-|-|-|
|FR-08-TC07|Submit payment with empty cart (defensive)|Authenticated user but cart emptied before submit|1. Login.<br>2. Ensure cart has items, open checkout.<br>3. Remove all items before submission (via API or UI).<br>4. Submit payment.|Backend detects empty cart at submission and rejects (400/409); no order created; user informed of empty cart.|The order was created anyway |Failed|
