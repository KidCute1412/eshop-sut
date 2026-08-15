# CI Workflow Debugging Notes

## Current Status
- **Workflow**: Newman API Tests
- **Branch**: 23127296-NguyenThanhLuan
- **Last Commit**: faa9ad1
- **Status**: FAILING at "Verify backend is running" step

## Error Summary
Workflow fails at step "Verify backend is running" - backend server does not start properly in GitHub Actions Ubuntu environment.

## What Works Locally
- Backend starts successfully on Windows
- Newman runs successfully with 5 iterations, 20 assertions, 0 failures
- All Postman files are valid JSON

## What Fails in CI
- Backend server does not respond to health check after 15 attempts (45 seconds)
- The server.js process may be crashing silently

## Possible Root Causes

### 1. SQLite3 Native Module Issue
- `sqlite3` npm package requires native compilation
- Ubuntu CI may lack build tools or wrong architecture
- Current fix attempts: `npm install sqlite3 --build-from-source || true`

### 2. Database.js Initialization Issue
- `database.js` runs `initDatabase()` on every server start
- Uses `db.serialize()` with multiple `DROP TABLE IF EXISTS`
- May cause race conditions or file lock issues

### 3. Server Startup Timing
- Current wait: 8 seconds initial + 15 retries × 3 seconds = 53 seconds total
- May not be enough for cold start with npm install

### 4. Working Directory Issue
- `working-directory: ./backend` may not persist across steps
- Server started in step may not be accessible in verify step

## Attempted Fixes
1. Increased wait times (8s + 15×3s)
2. Added server.log capture
3. Added `npm install sqlite3 --build-from-source || true`

## Recommended Next Steps

### Option A: Simplify Backend Start
```yaml
- name: Start backend and run tests
  run: |
    cd backend
    node server.js &
    SERVER_PID=$!
    sleep 10
    curl -f http://localhost:3000/api/products || exit 1
    # ... run newman ...
    kill $SERVER_PID
```

### Option B: Use Docker
```yaml
jobs:
  api-test:
    runs-on: ubuntu-latest
    container:
      image: node:20
    steps:
      - uses: actions/checkout@v4
      - run: cd backend && npm install && node server.js &
      - run: sleep 10 && newman run ...
```

### Option C: Mock/Skip Backend for CI
- Create mock server for CI
- Or run backend tests separately

## Files Involved
- `.github/workflows/newman-api-test.yml` - CI workflow
- `backend/server.js` - Express server (port 3000)
- `backend/database.js` - SQLite initialization
- `mini_exercise_api/mini-products.postman_collection.json` - Newman collection

## Debugging Commands (for next agent)
```bash
# Check workflow status
curl -s "https://api.github.com/repos/KidCute1412/eshop-sut/actions/runs?branch=23127296-NguyenThanhLuan&per_page=1"

# Test backend locally
cd backend && npm install && node server.js

# Run Newman locally
newman run mini_exercise_api/mini-products.postman_collection.json --environment mini_exercise_api/mini-local.postman_environment.json --iteration-data mini_exercise_api/mini-products.data.json
```

## MSSV
23127296
