# EShop API contract

| Step | Request | Required assertion |
| --- | --- | --- |
| Auth | `POST /api/login` | HTTP 200 and non-empty `token` |
| Read | `GET /api/products/:id` | HTTP 200 and product identity |
| Cart | `POST /api/cart` | HTTP 200 and success message |
| Checkout | `POST /api/checkout` | HTTP 200 and returned `orderId` |

Protected requests require `Authorization: Bearer <token>`. The local backend runs on port 3000 and recreates SQLite seed data when restarted.
