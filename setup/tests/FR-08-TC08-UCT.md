|ID|Objective|Input|Steps|Expected|Actual|Verdict|
|-|-|-|-|-|-|-|
|FR-08-TC08|Preserve cart when payment gateway fails|Authenticated user with cart items and simulated payment failure|1. Log in as a valid user.<br>2. Add items to cart and open Checkout.<br>3. Submit checkout request with payment details that trigger a simulated gateway failure.|1. Backend returns a failure response (4xx/5xx) with an appropriate message.<br>2. Cart remains unchanged after failure.<br>3. User can retry or return to cart.| |Blocked|
