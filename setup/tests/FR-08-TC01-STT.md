|ID|Objective|Input|Steps|Expected|Actual|Verdict|
|-|-|-|-|-|-|-|
|FR-08-TC01|Block checkout for unauthenticated users|No auth token; user not logged in|1. From public site, navigate to `/checkout`.<br>2. Attempt to submit payment.|1. Access to checkout is blocked; user is redirected to login or receives HTTP 401.<br>2. No order is created.|An error occured: "Lỗi khi thanh toán: Unauthorized" and no order is made. |Passed|
