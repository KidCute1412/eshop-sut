Guidelines for equivalence partitioning

If an input condition specifies a range of value, identify one valid equivalence class and two invalid equivalence classes, for example:
- "The item count can be from 1 to 999" => one valid equivalence class (1 <= count <= 999) and 2 invalid equivalence classes (count < 1 and count > 999)

If an input condition specifies a set of input values and there is reason to believe that each is handle differently by the program, identify a valid equivalence class for each and one different invalid equivalence class, for example:
- "type of vehicle must be BUS, TRUCK, TAXI-CAB, PASSENGER or MOTOCYCLE" => 5 valid equivalence class for each and an invalid equivalence class (TRAILER)

If an input condition specifies a "must be" situation, identify one valid and one invalid equivalence class, for example:
- "first character of the identifier must be a letter" => 2 equivalence classes (the first character is a letter (valid) and isn't a letter (invalid))

If there is any other reason to believe that elements in an equivalence class are not handled in an identical manner by the program, split the equivalence class into two or more smaller equivalence classes.