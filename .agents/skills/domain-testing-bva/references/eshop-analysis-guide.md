# EShop Analysis Guide

## Frameworks and Conventions

- Backend: Node.js, Express 5, CommonJS, SQLite via `sqlite3`, JWT via `jsonwebtoken`, JSON body parsing via `body-parser`.
- User web frontend: React, Vite, Tailwind CSS, React Router, Axios.
- Admin frontend: React, Vite, Tailwind CSS, Axios.
- Mobile frontend: React Native with Expo, `fetch` APIs, local component state.
- Tests: no meaningful automated test convention is configured. Backend `npm test` is a placeholder. Web/admin expose `npm run build` and `npm run lint`.

## Default Evidence Files

- Assignment PDF: `2026.HW02.Domain Testing_En.pdf`.
- Requirements summary: `README.md`.
- API contract: `api_specification.md`.
- Setup instructions: `setup_guide.md`.
- Server script: `run_servers.sh`.
- Backend routes and business logic: `backend/server.js`.
- Database schema and seed data: `backend/database.js`.
- User web pages: `frontend-web/src/pages/`.
- User web auth/cart state: `frontend-web/src/context/`.
- Admin UI: `frontend-admin/src/App.jsx`.
- Mobile UI: `frontend-mobile/App.js`.

## Server Script Caution

Inspect `run_servers.sh` before executing it. In this project it contains `killall node` and hard-coded absolute macOS paths. Prefer documented manual startup commands when execution is truly needed.

## Authentication and Authorization

Token format is `Authorization: Bearer <token>`. Backend middleware checks token validity, but many admin/data-changing routes must be inspected for role checks rather than assumed correct.

## Database

SQLite schema is initialized by `backend/database.js`. Check actual constraints, not just requirements. Important examples:

- `coupons.code` is unique.
- `users.email` is not unique in the schema despite the registration requirement.
- Most required-field and range rules are not enforced by database constraints.

## Report Evidence Rule

Source inspection may identify implemented behavior and likely bugs, but it is not test execution. Keep `Actual Result: Not Executed`, `Status: Not Executed`, and `Evidence: None` until the application is started and the case is actually run.
