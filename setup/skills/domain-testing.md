In domain testing, we partition a domain into sub-domains (equivalence classes) and then test using values from each sub-domain.

There are 4 steps
1. Identify Input & Output variables
2. Identify equivalence classes for each Input & Output
- 2.1. Divide the set of possible values (domain) of the field into subsets (sub-domains – equivalence classes)
3. Find a "best representative" for each subset
4. Best representatives of ordered fields will typically be boundary values

Two tests belong to the same equivalence class if the expected result of each is the same.
Executing multiple test cases of the same equivalence class is by definition, redundant testing.

To identify equivalence classes:
- Based on input/output conditions
- VALID EQUIVALENCE CLASSES are chosen to represent valid inputs.
- INVALID EQUIVALENCE CLASSES are chosen to represent invalid inputs.
- Identifying Equivalence Classes is a heuristic process.

When selecting test cases:
- Choose at least one test case from each equivalence class
- For valid classes, choose test cases to cover as many equivalence classes as possible, until all valid classes have been covered.
- For invalid classes, choose test cases so that each covers one and only one invalid class, until all classes are covered.

Example (EC = equivalence class)
|#EC|Partition|Input A|Input B|Expected Output|
|---|---|---|---|---|
|EC1|-99 <= A <= 99|10|9|19|
|EC2|A < -99|-102|9|Invalid Input|
|EC3|A > 99|102|9|Invalid Input|
|EC4|A is not an integer|Abc|9|Invalid Input|
|EC5|-99 <= B <= 99|10|9|19|
|EC6|B < -99|10|-200|Invalid Input|
|EC7|B > 99|10|200|Invalid Input|
|EC8|B is not an integer|10|1.25|Invalid Input|
|EC9|SUM = A+B|10|9|19|
|EC10|Invalid Input|-102|9|Invalid Input|

From there, the minimum amount of test cases can be achieved
| #TC | Partitions Tested | Input 1 (A) | Input 2 (B) | Expected Output |
|---|---|---|---|---|
| TC1 | EC1. -99 <= A <= 99<br>EC5. -99 <= B <= 99<br>EC9. SUM = A+B | 10 | 9 | 19 |
| TC2 | EC2. A < -99<br>EC10. Invalid Input | -102 | 9 | Invalid Input |
| TC3 | EC3. A > 99 | 102 | 9 | Invalid Input |
| TC4 | EC4. A is not an integer | Abc | 9 | Invalid Input |
| TC5 | EC6. B < -99 | 10 | -200 | Invalid Input |
| TC6 | EC7. B > 99 | 10 | 200 | Invalid Input |
| TC7 | EC8. B is not an integer | 10 | 1.25 | Invalid Input |


Types of boundary values:
- Valid Boundary Values - The minimum or maximum valid values which the program can accepts.
- 2-Point Boundary Values - Valid Boundary Value and a value just below the minimum valid boundary or a value just above the maximum boundary value.
- 3-Point Boundary Values - Valid Boundary Value and a value just below Valid Boundary Value and A value just above Valid Boundary Value

Apply 2-Point boundary values:
| #TC | Partition Tested | Input 1 (A) | Input 2 (B) | Expected Output |
|---|---|---|---|---|
| TC1 | A < -99 | -100 | 9 | Invalid Input |
| TC2 | -99 <= A <= 99 | -99 | 9 | 90 |
| TC3 | -99 <= A <= 99 | -98 | 9 | 89 |
| TC4 | -99 <= A <= 99 | 98 | 9 | 107 |
| TC5 | -99 <= A <= 99 | 99 | 9 | 108 |
| TC6 | A > 99 | 100 | 9 | Invalid Input |
| TC7 | B < -99 | -10 | -100 | Invalid Input |
| TC8 | -99 <= B <= 99 | 10 | -99 | 89 |
| TC9 | -99 <= B <= 99 | 10 | -98 | 88 |
| TC10 | -99 <= B <= 99 | 10 | 98 | 108 |
| TC11 | -99 <= B <= 99 | 10 | 99 | 109 |
| TC12 | B > 99 | 10 | 100 | Invalid Input |

For each equivalence class partition, we'll have at most, 9 test cases to execute.
It is essential to understand that each identified equivalence class represents a specific risk that it may pose.


Strengths:
- Find highest probability errors with a relatively small set of tests. Intuitively clear approach, easy to teach and understand
- Extends well to multi-variable situations

Blind spots or weaknesses:
- Errors that are not at boundaries or in obvious special cases Also, the actual domains are often unknowable