# Domain and boundary test design

The executable case matrix is the three external JSON files in `test-data/`; every row maps one-to-one to the test title and report result through its stable ID.

## Equivalence Partitioning (EP)

| Variable / Condition | Valid Equivalence Classes | Invalid Equivalence Classes |
| :--- | :--- | :--- |
| FR-06 product representation | EP-VAL-06-01 existing product; 02 image/alt; 03 numeric price; 04 string price; 05 description; 06 category | EP-INV-06-03 unknown product |
| FR-06 quantity/feedback | EP-VAL-06-07 positive integer; 08 immediate visual feedback | EP-INV-06-01 zero/negative; 02 fractional |
| FR-10 transitions | EP-VAL-10-01 pending→confirmed; 02/03 pending→canceled; 04 confirmed→shipping; 05/06 confirmed→canceled; 07 shipping→delivered | EP-INV-10-01 invalid pending edge; 02 invalid confirmed edge; 03/04 shipping cancellation; 05 delivered terminal; 06 canceled terminal |
| FR-12 identity and role | EP-VAL-12-01 valid admin JWT; 02 admin mutation | EP-INV-12-01 missing JWT; 02 malformed JWT; 03 valid non-admin JWT |

## Boundary Value Analysis (BVA)

| Variable | Boundary Condition | In-Point | On-Point | Off-Point | ID |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Product quantity | positive integer, minimum 1 | 2 | 1 | 0 / -1 | BVA-BND-06-01 |
| Product quantity | integer-only domain | 2 | 1 | 1.5 | BVA-BND-06-02 |
| Order state | terminal states have zero outgoing edges | pending/confirmed/shipping | delivered/canceled | any attempted successor | BVA-BND-10-01 |
| Authorization | both JWT validity and admin role required | valid admin JWT | valid non-admin JWT | absent/malformed JWT | BVA-BND-12-01 |

## Test suite mapping

| Feature | Case IDs | Inputs/actions | Expected result | Traceability source |
| :--- | :--- | :--- | :--- | :--- |
| FR-06 Product Detail | FR06-01…FR06-16 | seeded product IDs, quantity on/in/off points, add action, unknown ID | required content/format/constraints/feedback or clear not-found state | `test-data/fr06-product-detail.json` |
| FR-10 Order State Machine | FR10-01…FR10-16 | actor, arranged source state, requested successor | HTTP outcome and persisted state match the specified directed graph; UI cancel action only for pending/confirmed | `test-data/fr10-order-state-machine.json` |
| FR-12 Access Control | FR12-01…FR12-19 | endpoint/method with absent, malformed, user, or admin JWT | 401 missing, 403 invalid/non-admin, 200 valid admin; admin UI visible only to admin | `test-data/fr12-access-control.json` |

Shared preconditions are a freshly started seeded backend and both frontends at the documented URLs. Each row navigates or arranges its own state; no case depends on execution order. Assertions cover visibility/count, text/value/attributes, URL-independent UI state, HTTP status/body, and persisted API state.
