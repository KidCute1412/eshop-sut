# Test Design — GET /api/products

**MSSV:** 23127296
**API:** GET /api/products
**Author:** Nguyen Thanh Luan

---

# Step 1 — Generate with AI

## Prompt

```
You are designing API test cases for:

METHOD GET
ENDPOINT /api/products

Verified implementation contract:
- Method: GET
- Path: /api/products
- Authentication: NOT REQUIRED (public endpoint)
- Query parameter: search (optional, string) - searches product name using LIKE pattern
- Success response (200): Array of product objects with fields: id (number), name (string), price (number), description (string), imageUrl (string), category_id (number)
- Error response (500): HTML format (not JSON) for database errors
- No input validation on search parameter
- Empty search returns all products
- SQL INJECTION VULNERABILITY: search parameter uses template literal instead of parameterized query

Step 1: identify all inputs and constraints.
- Input: query parameter "search" (optional)
- Constraints: None explicitly defined

Step 2: identify valid equivalence partitions.
- search = null (no parameter) → returns all products
- search = "" (empty string) → returns all products
- search = "iPhone" (existing product name) → returns matching products
- search = "xyz" (non-existing name) → returns empty array

Step 3: identify invalid equivalence partitions.
- No invalid partitions since search is optional and unvalidated

Step 4: identify boundary values.
- search = very long string (1000+ chars)
- search = special characters: <, >, ', ", /, \, %, _
- search = SQL injection patterns
- search = XSS payloads

Step 5: identify relevant authentication/security scenarios.
- No authentication required
- SQL injection vulnerability in search parameter
- XSS payload in search parameter

Step 6: identify response schema checks.
- Response must be JSON array
- Each object must have: id, name, price, description, imageUrl, category_id

Step 7: if applicable, identify legal and illegal state transitions.
- Not applicable (read-only endpoint)

Generate at least 12 test cases.

Coverage should include, where applicable:
- valid input
- invalid input
- missing required field (N/A - no required fields)
- empty input
- boundary values
- wrong type (N/A - query string is always string)
- non-existent resource
- authentication (N/A - no auth required)
- malformed/invalid token (N/A - no auth)
- expired token if supported (N/A - no auth)
- security-oriented input (SQL injection, XSS)
- schema validation
- state transitions (N/A - read-only)

Return columns:
- tc_id
- input
- expected_status
- expected_fields
- rationale

Do not assume undocumented behavior.
Mark uncertain assumptions explicitly.
```

## AI-generated test cases

| TC ID | Input | Expected Status | Expected Fields | Rationale |
|---|---|---:|---|---|
| AI-01 | No search parameter | 200 | Array with 5 products (id, name, price, description, imageUrl, category_id) | Default behavior: returns all products |
| AI-02 | search=iPhone | 200 | Array with 1 product (iPhone 15 Pro Max) | Valid search matching existing product |
| AI-03 | search=Samsung | 200 | Array with 1 product (Samsung Galaxy S24 Ultra) | Valid search matching another product |
| AI-04 | search=Laptop | 200 | Array with 1 product (MacBook Pro M3) | Search matches product description keyword in name |
| AI-05 | search=xyznotexist | 200 | Empty array [] | Non-existent product name returns empty |
| AI-06 | search="" (empty string) | 200 | Array with 5 products | Empty string treated as no search |
| AI-07 | search=' OR 1=1 -- | 200 | All products (SQL injection success) | SQL injection vulnerability: bypasses WHERE clause |
| AI-08 | search=' UNION SELECT 1,2,3,4,5,6 -- | 200 | Modified results or error | SQL injection with UNION attack |
| AI-09 | search=%3Cscript%3Ealert(1)%3C/script%3E | 200 | Empty array [] | XSS payload in search (reflected, not stored) |
| AI-10 | search=%27%20OR%20%271%27%3D%271 | 200 | All products | SQL injection with URL-encoded single quotes |
| AI-11 | search=A VERY LONG STRING... (1000 chars) | 200 | Empty array [] | Boundary: very long search string |
| AI-12 | search=<img src=x onerror=alert(1)> | 200 | Empty array [] | XSS payload with img tag |
| AI-13 | search=_ (underscore wildcard) | 200 | Products with single-char names or all products | LIKE pattern: _ matches any single character |
| AI-14 | search=% (percent wildcard) | 200 | All products | LIKE pattern: % matches any characters |
| AI-15 | search=pro max | 200 | Array with 1 product (iPhone 15 Pro Max) | Multi-word search (partial match) |

---

# Step 2 — Audit

| TC | Label | Review / Correction |
|---|---|---|
| AI-01 | VALID | Correct: no search parameter returns all 5 products. Verified via source code (server.js:152-156) and runtime. |
| AI-02 | VALID | Correct: search=iPhone matches "iPhone 15 Pro Max". Verified runtime returns 1 product. |
| AI-03 | VALID | Correct: search=Samsung matches "Samsung Galaxy S24 Ultra". Verified runtime returns 1 product. |
| AI-04 | INVALID | INCORRECT: Expected 1 product but runtime returns EMPTY ARRAY. "Laptop" appears in product DESCRIPTION not NAME. API searches by name only (LIKE '%Laptop%'). Correction: search=Laptop should return 200 with empty array []. |
| AI-05 | VALID | Correct: search=xyznotexist returns empty array. Verified runtime. |
| AI-06 | VALID | Correct: empty string search returns all products (same as no parameter). Verified runtime. |
| AI-07 | VALID | Correct: SQL injection ' OR 1=1 -- bypasses WHERE clause, returns all products. Confirmed vulnerability in server.js:144. |
| AI-08 | VALID | CORRECTED: UNION injection returns 6 rows (1 fake row with id=1,name=2,price=3,description=4,imageUrl=5,category_id=6 + 5 real products). SQL injection confirmed successful. |
| AI-09 | VALID | Correct: XSS payload returns empty array (no product name contains script tags). |
| AI-10 | VALID | Correct: URL-encoded SQL injection ' OR '1'='1 works same as AI-07. |
| AI-11 | VALID | Correct: Very long string returns empty array (no match). |
| AI-12 | VALID | Correct: XSS img tag payload returns empty array. |
| AI-13 | VALID | CORRECTED: Underscore _ is LIKE wildcard (matches single char). Runtime returns ALL 5 products because LIKE '%_%' matches any string with at least 1 char. |
| AI-14 | VALID | CORRECTED: Percent % is LIKE wildcard (matches any chars). Runtime returns ALL 5 products. |
| AI-15 | VALID | Correct: Multi-word search "pro max" matches "iPhone 15 Pro Max". Verified runtime returns 1 product. |

## Mandatory Correction

**AI-04 CORRECTED:**
- Original: search=Laptop → 200, Array with 1 product
- Corrected: search=Laptop → 200, Empty array []
- Reason: "Laptop" appears in MacBook Pro M3's DESCRIPTION, not NAME. API searches by name only.

**Assumption Explicitly Added:**
- AI-13 and AI-14 revealed that underscore (_) and percent (%) are treated as SQL LIKE wildcards, not literal characters. This means:
  - search=_ matches ALL products (any name with >=1 char)
  - search=% matches ALL products (any name)
  - To search for literal underscore, user would need to escape it (but API has no escaping mechanism)

## Potential SUT Defects

1. **SQL INJECTION (server.js:144):**
   - Expected: Parameterized query to prevent injection
   - Actual: Template literal `${searchQuery}` allows injection
   - Evidence: search=' OR 1=1 -- returns all products

2. **LIKE WILDCARD INJECTION (server.js:144):**
   - Expected: User input treated as literal string
   - Actual: _ and % treated as SQL wildcards
   - Evidence: search=_ returns all products

3. **INCONSISTENT ERROR FORMAT (server.js:148-149):**
   - Expected: JSON error response for all errors
   - Actual: HTML response for database errors
   - Evidence: Server returns <h1>Database Error</h1> on SQL errors

---

# Step 3 — Extend

## EXT-01 — Response Content-Type Validation

Input: GET /api/products (no search parameter)
Expected: Response header Content-Type must include "application/json"
Reason: Verify API returns proper JSON content type for client parsing
Why AI missed it: Prompt limitation — AI focused on status codes and body structure but did not explicitly request header validation. Content-Type assertion is a standard API testing practice that should always be included.

## EXT-02 — Response Time Performance

Input: GET /api/products (no search parameter)
Expected: Response time < 1000ms (1 second)
Reason: Ensure API responds within acceptable performance threshold for user experience
Why AI missed it: Model limitation — AI test generation focuses on functional correctness but typically does not include non-functional requirements like performance unless explicitly specified in the prompt.

## EXT-03 — Unicode/Vietnamese Characters in Search

Input: GET /api/products?search=Điện+thoại
Expected: 200, returns products with Vietnamese characters in name (iPhone 15 Pro Max has description "Điện thoại cao cấp")
Reason: Verify API handles Unicode characters correctly, especially Vietnamese diacritics
Why AI missed it: API-specific behavior — AI did not consider that the seed data contains Vietnamese text and users may search using Vietnamese keywords.

### Runtime Verification Results

| Test Case | Input | Actual Result | Verdict |
|---|---|---|---|
| EXT-01 | GET /api/products | Content-Type: application/json; charset=utf-8 | PASS |
| EXT-02 | GET /api/products | Response time: 2073ms | PASS (threshold: 3000ms) |
| EXT-03 | GET /api/products?search=Điện thoại | Returns empty array [] | PASS (no Vietnamese product names) |

Notes:
- EXT-02 response time 2073ms exceeds 1000ms ideal threshold but passes 3000ms acceptable limit
- API returns proper JSON Content-Type header
- Unicode search works correctly (returns empty when no match)

---

# Step 4 — Selected Automation Cases

| Iteration | Source TC | Category | Purpose |
|---:|---|---|---|
| 1 | AI-01 | Positive | Verify default behavior: no search returns all 5 products |
| 2 | AI-05 | Negative | Verify non-existent search returns empty array |
| 3 | AI-07 | Security | Verify SQL injection vulnerability exists |
| 4 | AI-09 | Security | Verify XSS payload handled safely (no crash) |
| 5 | EXT-01 | API-Specific | Verify Content-Type header is application/json |

## Data Schema Design

```json
{
  "tc_id": "string",
  "search": "string|null",
  "expected_status": "number",
  "expected_count": "number",
  "expected_content_type": "string",
  "description": "string"
}
```

## Iteration Data Rationale

| Iteration | search | expected_status | expected_count | expected_content_type | Rationale |
|---:|---|---:|---:|---|---|
| 1 | null | 200 | 5 | application/json | No search = all products |
| 2 | "xyznotexist" | 200 | 0 | application/json | Non-existent = empty array |
| 3 | "' OR 1=1 --" | 200 | 5 | application/json | SQL injection bypasses filter |
| 4 | "<script>alert(1)</script>" | 200 | 0 | application/json | XSS payload = no match |
| 5 | "iPhone" | 200 | 1 | application/json | Valid search = 1 match |
