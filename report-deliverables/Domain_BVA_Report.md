FR-05: Product listing and search

Boundary Value Analysis is generally not applicable here, as only 1 equivalence class has any meaningful order operations (<= or >=) for the inputs.
For Domain Testing and Equivalence Partitioning, a total of 8 equivalence classes (ECs) are made:
- The search query input has 4 valid classes and an invalid class, making up 5 classes. For valid classes, they are: Standard matching search term (ex: "Keyboard"), Non-matching search term (ex: "zzzzz"), Unicode matching search term (ex: "Bàn phím"), Empty or blank search term (ex: ""). For invalid classes, it is: Script injection (ex: "&lt;script>alert(1)&lt;/script>")
- The outputs here are related to the list of products shown when the search query is active, we can partition them into 3 classes: an empty list, a full list of all products and a list of only matching products.