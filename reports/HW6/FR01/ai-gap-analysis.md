# FR01 - AI Gap Analysis

| Gap ID | Category | Initial AI Output | Human Correction / Runtime Finding | Why AI Missed It | Corrective Action | Related Case / Evidence / Bug |
|---|---|---|---|---|---|---|
| FR01-GAP-001 | Missed test case | AI did not include: Verify duplicate email using exact two-step setup in one run | Added as FR01-API-036 | AI listed duplicate conceptually but missed deterministic setup dependency for an executable Newman run. | Added to final test suite and Postman evidence plan | FR01-API-036 |
| FR01-GAP-002 | Missed test case | AI did not include: Reject body with only unknown properties | Added as FR01-API-037 | AI missed API contract robustness for malformed JSON shape. | Added to final test suite and Postman evidence plan | FR01-API-037 |
| FR01-GAP-003 | Missed test case | AI did not include: Reject array JSON body | Added as FR01-API-038 | AI missed wrong top-level JSON type. | Added to final test suite and Postman evidence plan | FR01-API-038 |
| FR01-GAP-004 | Missed test case | AI did not include: Reject boolean password type | Added as FR01-API-039 | AI focused on string complexity but missed non-string type partition. | Added to final test suite and Postman evidence plan | FR01-API-039 |
| FR01-GAP-005 | Missed test case | AI did not include: Check API/README confirm-password contradiction | Added as FR01-API-040 | AI initially turned UI confirm-password rule into an API oracle without noting the contract mismatch. | Added to final test suite and Postman evidence plan | FR01-API-040 |
