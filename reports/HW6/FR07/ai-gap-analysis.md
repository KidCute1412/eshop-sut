# FR07 - AI Gap Analysis

| Gap ID | Category | Initial AI Output | Human Correction / Runtime Finding | Why AI Missed It | Corrective Action | Related Case / Evidence / Bug |
|---|---|---|---|---|---|---|
| FR07-GAP-001 | Missed test case | AI did not include: Reject array body | Added as FR07-API-036 | AI missed wrong top-level JSON type. | Added to final test suite and Postman evidence plan | FR07-API-036 |
| FR07-GAP-002 | Missed test case | AI did not include: Reject extremely large quantity | Added as FR07-API-037 | AI covered boundaries near zero but missed abuse-scale values. | Added to final test suite and Postman evidence plan | FR07-API-037 |
| FR07-GAP-003 | Missed test case | AI did not include: Reject mismatched product name for valid id | Added as FR07-API-038 | AI assumed client body was authoritative and missed ID/body consistency. | Added to final test suite and Postman evidence plan | FR07-API-038 |
| FR07-GAP-004 | Missed test case | AI did not include: Reject mismatched product price for valid id | Added as FR07-API-039 | AI missed price tampering risk that affects checkout total. | Added to final test suite and Postman evidence plan | FR07-API-039 |
| FR07-GAP-005 | Missed test case | AI did not include: Verify `X-Student-Id` header is present on cart requests | Added as FR07-API-040 | AI often treats assignment evidence headers as tooling detail, not a test artifact. | Added to final test suite and Postman evidence plan | FR07-API-040 |
