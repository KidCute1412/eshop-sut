|ID|Objective|Input|Steps|Expected|Actual|Verdict|
|-|-|-|-|-|-|-|
|FR-08-TC03|Cart state transition when adding items|Authenticated user, cart empty|1. Login.<br>2. Add product A (qty 1) to cart via API/UI.<br>3. Inspect cart state.|Cart moves from `LoggedInEmptyCart` to `LoggedInHasItems`; cart contains product A with correct qty and price.|1 iPhone Pro Max is added successfully |Passed|
