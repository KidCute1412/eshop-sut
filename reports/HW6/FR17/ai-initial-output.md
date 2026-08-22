# FR17 - Preserved Initial AI Output

The following is the preserved candidate suite produced during AI-assisted generation before human extension. Human-added rows are intentionally excluded here so the gap analysis can compare AI output against the final suite.

1. Reject GET coupons without token (Security) - expected 401: Unauthorized JSON error
2. Reject GET coupons with malformed token (Security) - expected 403: Forbidden JSON error
3. Reject GET coupons with user token (Security) - expected 403: User role cannot access admin coupon list
4. Accept GET coupons with admin token (Security) - expected 200: JSON array of coupons
5. GET coupons item schema (Schema) - expected 200: Each coupon has id, code, type, discount_value, min_order_amount, expired_at, is_active, max_uses_per_user
6. Reject POST coupon without token (Security) - expected 401: Unauthorized JSON error
7. Reject POST coupon with malformed token (Security) - expected 403: Forbidden JSON error
8. Reject POST coupon with user token (Security) - expected 403: User role cannot create admin coupon
9. Create valid percent coupon (Domain) - expected 200: message='Coupon created' and numeric id
10. Create valid fixed coupon (Domain) - expected 200: message='Coupon created' and numeric id
11. Reject missing code (Domain) - expected 400: Code is required
12. Reject empty code (Domain) - expected 400: Code is required
13. Reject whitespace-only code (Domain) - expected 400: Code is required after trimming
14. Reject duplicate code (Domain) - expected 400: Duplicate code rejected without server error
15. Reject invalid type value (Domain) - expected 400: Type must be percent or fixed
16. Reject missing type (Domain) - expected 400: Type is required
17. Reject uppercase type if enum is case-sensitive (Domain) - expected 400: Type must match documented percent/fixed values
18. Reject missing discount_value (Domain) - expected 400: discount_value is required
19. Reject discount_value 0 (Boundary) - expected 400: discount_value must be positive
20. Reject negative discount_value (Boundary) - expected 400: discount_value must be positive
21. Reject string discount_value (Domain) - expected 400: discount_value must be numeric
22. Reject percent discount over 100 (Boundary) - expected 400: Percent discount must not exceed 100
23. Reject missing expired_at (Domain) - expected 400: expired_at is required
24. Reject invalid expired_at format (Domain) - expected 400: expired_at must be valid date
25. Accept future expired_at date (Boundary) - expected 200: Coupon created
26. Reject missing min_order_amount (Domain) - expected 400: min_order_amount is required
27. Accept min_order_amount 0 (Boundary) - expected 200: Coupon created
28. Reject min_order_amount -1 (Boundary) - expected 400: min_order_amount must be >= 0
29. Reject string min_order_amount (Domain) - expected 400: min_order_amount must be numeric
30. Reject missing max_uses_per_user (Domain) - expected 400: max_uses_per_user is required
31. Accept max_uses_per_user 1 (Boundary) - expected 200: Coupon created
32. Reject max_uses_per_user 0 (Boundary) - expected 400: max_uses_per_user must be >= 1
33. Reject max_uses_per_user -1 (Boundary) - expected 400: max_uses_per_user must be >= 1
34. Reject string max_uses_per_user (Domain) - expected 400: max_uses_per_user must be numeric
35. Reject SQL injection-looking coupon code safely (Security) - expected 400: No database error/server crash
36. Reject script payload in coupon code or store safely (Security) - expected 400: Unsafe display value rejected or escaped downstream
37. Reject DELETE coupon without token (Security) - expected 401: Unauthorized JSON error
38. Reject DELETE coupon with user token (Security) - expected 403: User role cannot delete admin coupon
39. Delete existing coupon with admin token (Domain) - expected 200: message='Coupon deleted'
