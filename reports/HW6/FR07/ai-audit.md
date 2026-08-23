# FR07 - AI Audit

## Purpose

This file preserves the detailed prompt and raw AI output for FR07 - Shopping cart. The table below is the AI-generated candidate suite before human review, execution cleanup, and testcase removal. Because it is raw AI output, it may include rows that were later removed from the final `test-cases.md`.

## AI Prompt

```text
You are an AI-assisted API test designer for HW6 EShop API Testing.
Use only the assignment, README.md, api_specification.md, and setup_guide.md as source of truth.
For FR07 Shopping cart, analyse GET /api/cart and POST /api/cart for an authenticated customer.

Generate the initial AI candidate suite before human filtering. The suite must cover:
- missing, malformed, and valid JWT access to cart APIs;
- empty cart and cart item response schemas;
- add-to-cart success paths with valid product data;
- quantity, product id, product name, and price partitions;
- boundary values such as zero, negative, decimal, string, missing, and null values;
- state checks for duplicate add, repeated GET, and adding different products;
- security checks for cart isolation, identity-field injection, SQL injection-like product name, and data-driven quantity coverage.

Return the raw output as a Markdown test-case table. Keep the original AI candidate rows even if a later human reviewer removes some of them from the final executed suite. Do not add human-added cases in this initial output.
```

## Prompt Context Given To AI

| Field | Value |
|---|---|
| Feature | FR07 - Shopping cart |
| Endpoint(s) | GET /api/cart; POST /api/cart |
| Tooling target | Postman collection with Newman execution evidence |
| Required evidence rule | Every executed request must include `X-Student-Id` during real execution |
| Oracle rule | Expected behaviour must come from README.md, api_specification.md, setup_guide.md, and HW6 assignment, not from implementation source |
| Raw-output status | Preserved before human filtering and before final testcase pruning |

## Raw AI Output - Candidate Test Cases

| ID | Category | Objective | Expected Status | Expected Response / Schema |
|---|---|---|---:|---|
| FR07-API-001 | Security | Reject GET cart without token | 401 | Unauthorized JSON error |
| FR07-API-002 | Security | Reject GET cart with malformed token | 403 | Forbidden JSON error |
| FR07-API-003 | Security | Accept GET cart with valid user token | 200 | JSON array cart |
| FR07-API-004 | Schema | GET empty cart response is an array | 200 | Response is array |
| FR07-API-005 | Domain | Add valid product with quantity 1 | 200 | message='Added to cart' |
| FR07-API-006 | Domain | Add valid product with quantity 2 | 200 | message='Added to cart' |
| FR07-API-007 | Boundary | Reject quantity 0 | 400 | Quantity must be positive integer |
| FR07-API-008 | Boundary | Reject quantity -1 | 400 | Quantity must be positive integer |
| FR07-API-009 | Domain | Reject decimal quantity | 400 | Quantity must be integer |
| FR07-API-010 | Domain | Reject string quantity | 400 | Quantity must be number |
| FR07-API-011 | Domain | Reject missing quantity | 400 | Quantity is required |
| FR07-API-012 | Domain | Reject null quantity | 400 | Quantity is required |
| FR07-API-013 | Domain | Reject missing product id | 400 | Product id is required |
| FR07-API-014 | Domain | Reject null product id | 400 | Product id is required |
| FR07-API-015 | Domain | Reject string product id | 400 | Product id must be numeric |
| FR07-API-016 | Domain | Reject non-existing product id | 404 | Product not found |
| FR07-API-017 | Domain | Reject missing product name | 400 | Product name is required |
| FR07-API-018 | Domain | Reject empty product name | 400 | Product name is required |
| FR07-API-019 | Security | Store/display product name safely when script payload is submitted | 400 | Unsafe name rejected or safely stored for escaped rendering |
| FR07-API-020 | Domain | Reject missing price | 400 | Price is required |
| FR07-API-021 | Boundary | Reject price 0 | 400 | Price must be positive |
| FR07-API-022 | Boundary | Reject negative price | 400 | Price must be positive |
| FR07-API-023 | Domain | Reject string price | 400 | Price must be numeric |
| FR07-API-024 | Security | Reject POST cart without token | 401 | Unauthorized JSON error |
| FR07-API-025 | Security | Reject POST cart with malformed token | 403 | Forbidden JSON error |
| FR07-API-026 | State | Adding same product twice increases quantity, not duplicate row | 200 | Follow-up GET shows one row for id=1 with combined quantity |
| FR07-API-027 | State | Repeated GET cart does not mutate cart contents | 200 | Two consecutive GET responses preserve the same cart item count |
| FR07-API-028 | State | Adding different product creates separate row | 200 | Follow-up GET includes ids 1 and 2 |
| FR07-API-029 | Schema | POST cart success schema has message only | 200 | JSON object with string message |
| FR07-API-030 | Schema | GET cart item schema | 200 | Each item has id, name, price, quantity with correct types |
| FR07-API-031 | Security | Cart is isolated per user | 200 | User B cart does not contain User A item |
| FR07-API-032 | Security | Reject role or user_id injection in cart body | 400 | Server ignores/rejects identity fields from body |
| FR07-API-033 | Security | Reject SQL injection-looking product name safely | 400 | No database error/server crash |
| FR07-API-034 | Data-driven | Run quantity boundaries from data file | 200 | Only positive integer rows pass |
| FR07-API-035 | Domain | Reject empty object body | 400 | Validation error for required cart fields |

## Human Review Note

A human reviewer later checked these AI-generated candidates against the source of truth, execution feasibility, and assignment constraints. Some rows may have been corrected, extended, or removed in the final `test-cases.md`; this file intentionally keeps the raw AI candidate output for auditability.
