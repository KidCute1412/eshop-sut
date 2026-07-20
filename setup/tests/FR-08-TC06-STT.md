|ID|Objective|Input|Steps|Expected|Actual|Verdict|
|-|-|-|-|-|-|-|
|FR-08-TC06|Submit payment with expired/invalid session (authentication lost)|Previously authenticated user; session expired before submit|1. Login and open checkout.<br>2. Expire session or remove auth token.<br>3. Submit payment.|Backend rejects submission with 401/403; no order is created; cart remains unchanged.|An error occured: "Lỗi khi thanh toán: Unauthorized" and no order changes are made. |Passed|
