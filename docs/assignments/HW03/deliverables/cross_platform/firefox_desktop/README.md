# Firefox Desktop Evidence

**Environment:** Playwright Firefox 144.0.2 on Windows NT 10.0.26200

**Execution date:** 2 August 2026

**Viewport:** 1440 × 1000

| File | Screen |
|---|---|
| `01_product_list.png` | Product List |
| `02_product_detail.png` | Product Detail |
| `03_cart.png` | Cart |
| `04_checkout.png` | Checkout |
| `05_order_history.png` | Profile / Order History |

The complete customer flow was executed successfully in Firefox. All five images are authentic Playwright captures and include the required student identity, browser/version, operating system, and URL caption. The earlier page-creation failure was traced to the restricted execution sandbox blocking Firefox tab subprocesses; rerunning the same compatible browser outside that restriction resolved the environment issue.
