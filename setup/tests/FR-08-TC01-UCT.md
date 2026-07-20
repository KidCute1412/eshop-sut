|ID|Objective|Input|Steps|Expected|Actual|Verdict|
|-|-|-|-|-|-|-|
|FR-08-TC01|Block checkout for unauthenticated users|User is not logged in and cart may contain items in client state|1. Open the application without authenticating.<br>2. Navigate to the Checkout page or submit a checkout request.<br>3. Observe the response or redirect behavior.|1. Access to Checkout is blocked.<br>2. User is redirected to Login or receives HTTP 401/403.<br>3. No order is created and cart remains unchanged.|An error occured: "Lỗi khi thanh toán: Unauthorized" and no order is made. |Passed|

