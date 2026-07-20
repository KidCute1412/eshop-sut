|ID|Objective|Input|Steps|Expected|Actual|Verdict|
|-|-|-|-|-|-|-|
|FR-08-TC02|Prevent checkout with empty cart|Authenticated user with an empty server-side cart|1. Log in as a valid user.<br>2. Ensure the cart is empty.<br>3. Navigate to Checkout.<br>4. Attempt to submit the checkout form.|1. UI shows an empty-cart message and blocks payment.<br>2. Backend rejects any submit attempt with 400/409 if reached.<br>3. No order is created.|The order was created anyways. |Failed|
