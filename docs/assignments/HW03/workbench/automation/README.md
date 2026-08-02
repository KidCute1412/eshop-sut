# HW03 Runtime Test Harness

This internal harness executes the Web, Admin, API, and desktop cross-browser checks used to populate the HW03 submission. It deliberately excludes real-participant usability results and qualifying mobile-device execution.

Run `npm install` in this directory before execution. The runner expects the EShop backend, customer frontend, and admin frontend at ports 3000, 5173, and 5174. It writes raw execution results under `results/`. Submission-facing screenshots are written directly to the appropriate HW03 evidence folders.

Before execution, back up `backend/database.sqlite`. Run against a freshly seeded database and restore the original database after the run.
