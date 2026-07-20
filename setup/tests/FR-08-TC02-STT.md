|ID|Objective|Input|Steps|Expected|Actual|Verdict|
|-|-|-|-|-|-|-|
|FR-08-TC02|Prevent checkout with empty cart|Authenticated user with empty cart|1. Login with valid account.<br>2. Navigate to `/checkout`.<br>3. Attempt to submit payment.|UI shows "cart empty" message; backend rejects submission (400) or UI blocks submit; no order created.|The order was created anyway |Failed|
