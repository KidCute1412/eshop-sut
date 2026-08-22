# FR07 - Preserved Initial AI Output

The following is the preserved candidate suite produced during AI-assisted generation before human extension. Human-added rows are intentionally excluded here so the gap analysis can compare AI output against the final suite.

1. Reject GET cart without token (Security) - expected 401: Unauthorized JSON error
2. Reject GET cart with malformed token (Security) - expected 403: Forbidden JSON error
3. Accept GET cart with valid user token (Security) - expected 200: JSON array cart
4. GET empty cart response is an array (Schema) - expected 200: Response is array
5. Add valid product with quantity 1 (Domain) - expected 200: message='Added to cart'
6. Add valid product with quantity 2 (Domain) - expected 200: message='Added to cart'
7. Reject quantity 0 (Boundary) - expected 400: Quantity must be positive integer
8. Reject quantity -1 (Boundary) - expected 400: Quantity must be positive integer
9. Reject decimal quantity (Domain) - expected 400: Quantity must be integer
10. Reject string quantity (Domain) - expected 400: Quantity must be number
11. Reject missing quantity (Domain) - expected 400: Quantity is required
12. Reject null quantity (Domain) - expected 400: Quantity is required
13. Reject missing product id (Domain) - expected 400: Product id is required
14. Reject null product id (Domain) - expected 400: Product id is required
15. Reject string product id (Domain) - expected 400: Product id must be numeric
16. Reject non-existing product id (Domain) - expected 404: Product not found
17. Reject missing product name (Domain) - expected 400: Product name is required
18. Reject empty product name (Domain) - expected 400: Product name is required
19. Store/display product name safely when script payload is submitted (Security) - expected 400: Unsafe name rejected or safely stored for escaped rendering
20. Reject missing price (Domain) - expected 400: Price is required
21. Reject price 0 (Boundary) - expected 400: Price must be positive
22. Reject negative price (Boundary) - expected 400: Price must be positive
23. Reject string price (Domain) - expected 400: Price must be numeric
24. Reject POST cart without token (Security) - expected 401: Unauthorized JSON error
25. Reject POST cart with malformed token (Security) - expected 403: Forbidden JSON error
26. Adding same product twice increases quantity, not duplicate row (State) - expected 200: Follow-up GET shows one row for id=1 with combined quantity
27. Repeated GET cart does not mutate cart contents (State) - expected 200: Two consecutive GET responses preserve the same cart item count
28. Adding different product creates separate row (State) - expected 200: Follow-up GET includes ids 1 and 2
29. POST cart success schema has message only (Schema) - expected 200: JSON object with string message
30. GET cart item schema (Schema) - expected 200: Each item has id, name, price, quantity with correct types
31. Cart is isolated per user (Security) - expected 200: User B cart does not contain User A item
32. Reject role or user_id injection in cart body (Security) - expected 400: Server ignores/rejects identity fields from body
33. Reject SQL injection-looking product name safely (Security) - expected 400: No database error/server crash
34. Run quantity boundaries from data file (Data-driven) - expected 200: Only positive integer rows pass
35. Reject empty object body (Domain) - expected 400: Validation error for required cart fields
