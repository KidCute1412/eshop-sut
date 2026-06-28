|ID|Partition|Input Values|Expected Output Values|Applied Boundary Values|
|---|---|---|---|---|
|EC01|Matching search term|Search query matching an existing product name, e.g. "Macbook"|Only matching products are shown|No|
|EC02|Non-matching search term|Search query with no matching product, e.g. "zzzzz"|Empty state is shown and no product cards appear|No|
|EC03|Unsafe search input|Search input containing HTML-like text, e.g. "&lt;script>alert(1)&lt;/script>"|The input is displayed safely as text and does not break the UI. Empty state is shown and no product cards appear|No|
|EC04|Blank search input|Empty string or whitespace-only input|The full product list is shown again|No|
|EC05|Matching Unicode search term|Search query matching an existing product name with Unicode, e.g. "Bàn phím"|Only matching products are shown|No|
|EC06|Matching Products Only|Any non-empty valid search query|Only matching products are shown|No|
|EC07|Empty Product List|Any invalid search query or a valid search query with zero matching products|Empty state is shown and no product cards appear|No|
|EC08|Full Product List|Initial state or an empty search query|The full product list is shown|No|
