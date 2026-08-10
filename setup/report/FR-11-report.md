# FR-11 Report

| Test Case | Objective | Preconditions | Input Summary | Expected | Verdict |
| --- | --- | --- | --- | --- | --- |
| TC06 | Verify authenticated user can access order history and view order history headers | Frontend running at localhost:5173; test user exists | Login with test user, navigate to order history | Order history heading and table headers visible | |
| TC07 | Verify order row content includes order code, order date, total amount, and Vietnamese status | Frontend running at localhost:5173; user has at least one order | Login and open order history | First order row contains non-empty code/date, total amount in ₫, translated status text | |
| TC08 | Verify order status text displays in Vietnamese and status cells are visible | Frontend running at localhost:5173; user has order history entries | Login and open order history | Status cell text matches Vietnamese status values | |
| TC09 | Verify order history only shows the current user's orders | Frontend running at localhost:5173; test user has orders | Login as test user, open order history | Only rows belonging to the authenticated user are visible; no other user order IDs | |
| TC10 | Verify order history page has exactly one h1 and status styling indicates order state | Frontend running at localhost:5173; test user has orders | Login and open order history | One h1 only; status cells have non-empty computed color/background | |
