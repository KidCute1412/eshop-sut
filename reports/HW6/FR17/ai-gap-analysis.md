# FR17 - AI Gap Analysis

| Gap ID | Category | Initial AI Output | Human Correction / Runtime Finding | Why AI Missed It | Corrective Action | Related Case / Evidence / Bug |
|---|---|---|---|---|---|---|
| FR17-GAP-001 | Missed test case | AI did not include: Reject empty object body for coupon creation | Added as FR17-API-040 | AI generated field-by-field cases but missed fully empty body shape. | Added to final test suite and Postman evidence plan | FR17-API-040 |
| FR17-GAP-002 | Missed test case | AI did not include: Reject array body for coupon creation | Added as FR17-API-041 | AI missed wrong top-level JSON type. | Added to final test suite and Postman evidence plan | FR17-API-041 |
| FR17-GAP-003 | Missed test case | AI did not include: Verify user-token cannot create then delete coupon | Added as FR17-API-042 | AI listed authorization checks separately but missed create-side-effect verification. | Added to final test suite and Postman evidence plan | FR17-API-042 |
| FR17-GAP-004 | Missed test case | AI did not include: Verify duplicate code failure is not a raw database 500 | Added as FR17-API-043 | AI missed error-message quality/security leakage. | Added to final test suite and Postman evidence plan | FR17-API-043 |
| FR17-GAP-005 | Missed test case | AI did not include: Verify `X-Student-Id` header is present on admin coupon requests | Added as FR17-API-044 | AI often treats assignment evidence headers as tooling detail, not a test artifact. | Added to final test suite and Postman evidence plan | FR17-API-044 |
