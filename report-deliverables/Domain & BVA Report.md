# FR-05: Product listing and search

Boundary Value Analysis is generally not applicable here, as only 1 equivalence class has any meaningful order operations (<= or >=) for the inputs.
For Domain Testing and Equivalence Partitioning, a total of 8 equivalence classes (ECs) are made:
- The search query input has 4 valid classes and an invalid class, making up 5 classes. For valid classes, they are: Standard matching search term (ex: "Keyboard"), Non-matching search term (ex: "zzzzz"), Unicode matching search term (ex: "Bàn phím"), Empty or blank search term (ex: ""). For invalid classes, it is: Script injection (ex: "&lt;script>alert(1)&lt;/script>")
- The outputs here are related to the list of products shown when the search query is active, we can partition them into 3 classes: an empty list, a full list of all products and a list of only matching products.

# FR-11: Order history view (user)

Boundary Value Analysis is completely not applicable here, as there is no equivalence class with any meaningful order operations (<= or >=) for the inputs or outputs.
For Domain Testing and Equivalence Partitioning, a total of 12 equivalence classes (ECs) are made:
- 8 classes are related to "action" inputs rather than raw input, with 7 valid classes representing valid actions the user can take to update the history and 1 invalid class relating to the addition of an order by another user.
- The other 4 classes are related to the history and its status after any input, being: empty, appending a new order, changing the status of an existing order and unchanged.

# FR-14: Category management (CRUD) 

Like in FR-05, Boundary Value Analysis is generally not applicable here, as only 1 equivalence class has any meaningful order operations (<= or >=) for the inputs.

Domain Testing and Equivalence Partitioning is straightforward:
- The name query has 2 valid classes: standard, Unicode and 1 specified invalid class: white-space query.
- The deletion of a category is listed as one unique valid class.
- For outputs, there are 3 classes in total: new category, no category or deleted category.

# FR-15: Product management (CRUD)

# FR-21: Product listing and search for Mobile
The same process in FR-05 applies here.
