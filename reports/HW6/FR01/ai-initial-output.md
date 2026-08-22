# FR01 - Preserved Initial AI Output

The following is the preserved candidate suite produced during AI-assisted generation before human extension. Human-added rows are intentionally excluded here so the gap analysis can compare AI output against the final suite.

1. Register with all valid fields and a unique email (Domain) - expected 200: JSON has message='User registered successfully' and numeric id
2. Reject missing name (Domain) - expected 400: Error response explains name is required
3. Reject empty name (Domain) - expected 400: Error response explains name is required
4. Reject whitespace-only name (Domain) - expected 400: Error response explains name is required after trimming
5. Accept one-character non-empty name (Boundary) - expected 200: User registered successfully
6. Accept long but valid name (Domain) - expected 200: User registered successfully
7. Store/display name safely when it contains script payload (Security) - expected 200: Registration succeeds or safely rejects; no script execution in downstream UI evidence
8. Reject missing email (Domain) - expected 400: Error response explains email is required
9. Reject empty email (Domain) - expected 400: Error response explains valid email is required
10. Reject email without at sign (Domain) - expected 400: Error response explains valid email format is required
11. Reject email without domain (Domain) - expected 400: Error response explains valid email format is required
12. Reject email without local part (Domain) - expected 400: Error response explains valid email format is required
13. Reject email with spaces (Domain) - expected 400: Error response explains valid email format is required
14. Accept plus-tag valid email (Domain) - expected 200: User registered successfully
15. Accept mixed-case valid email (Domain) - expected 200: User registered successfully
16. Reject duplicate email (Domain) - expected 400: Second registration is rejected because email must be unique
17. Reject SQL injection-looking email without server error (Security) - expected 400: No auth bypass or database error; safe JSON error
18. Reject SQL injection-looking name without server error (Security) - expected 200: Registration succeeds or safely rejects; database remains available
19. Reject missing password (Domain) - expected 400: Error response explains password is required
20. Reject empty password (Domain) - expected 400: Error response explains password is required/weak
21. Reject password length 7 (Boundary) - expected 400: Password length boundary below 8 rejected
22. Accept password length 8 with all required classes (Boundary) - expected 200: User registered successfully
23. Reject password missing uppercase (Domain) - expected 400: Password complexity rejection
24. Reject password missing lowercase (Domain) - expected 400: Password complexity rejection
25. Reject password missing digit (Domain) - expected 400: Password complexity rejection
26. Reject password missing special character (Domain) - expected 400: Password complexity rejection
27. Accept password with @ special character (Domain) - expected 200: User registered successfully
28. Accept password with dollar special character (Domain) - expected 200: User registered successfully
29. Accept password with ampersand special character (Domain) - expected 200: User registered successfully
30. Success response schema contains only message and numeric id (Schema) - expected 200: JSON object with string message and number id; no password field
31. Success response must not expose password (Security) - expected 200: Response does not contain password or password hash
32. Reject null name (Domain) - expected 400: Name validation error
33. Reject null email (Domain) - expected 400: Email validation error
34. Reject null password (Domain) - expected 400: Password validation error
35. Reject unexpected role field during registration (Domain) - expected 400: Registration rejects role injection or ignores role; created user is not admin
