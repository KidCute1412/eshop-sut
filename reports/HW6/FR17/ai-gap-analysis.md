# FR17 - AI Gap Analysis

| Gap ID | Category | Initial AI Output | Human Correction / Runtime Finding | Why AI Missed It | Corrective Action | Related Case / Evidence / Bug |
|---|---|---|---|---|---|---|
| FR17-GAP-001 | Missed test case | AI did not include: Reject empty object body for coupon creation | Added as FR17-API-040 | AI generated field-by-field cases but missed fully empty body shape. | Added to final test suite and Postman evidence plan | FR17-API-040 |
| FR17-GAP-002 | Missed test case | AI did not include: Reject array body for coupon creation | Added as FR17-API-041 | AI missed wrong top-level JSON type. | Added to final test suite and Postman evidence plan | FR17-API-041 |
