/* Execute HW06 suites against a real local SUT without retaining test state.
 * Raw Newman files are preserved.  The manifest is derived only from them.
 */
const fs = require('fs');
const path = require('path');
const os = require('os');
const {spawn, spawnSync} = require('child_process');
const sqlite3 = require('../backend/node_modules/sqlite3').verbose();

const root = path.resolve(__dirname, '..');
const backend = path.join(root, 'backend');
const dbPath = path.join(backend, 'database.sqlite');
const base = path.join(root, 'docs', 'assignments', 'HW06', 'deliverables');
const postman = path.join(base, 'postman');
const reports = path.join(base, 'newman-reports');
const evidence = path.join(base, 'evidence');
const backup = path.join(os.tmpdir(), `hw06-db-${process.pid}.sqlite`);

const read = name => JSON.parse(fs.readFileSync(path.join(postman, 'data', name), 'utf8'));
const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));
const exec = (cmd, args, options = {}) => new Promise((resolve, reject) => {
  // Newman is installed as a Windows .cmd shim. Quote each argument because
  // the workspace path contains spaces and cmd.exe otherwise splits it.
  const useShell = process.platform === 'win32' && cmd.endsWith('.cmd');
  const quoted = value => '"' + String(value).replace(/"/g, '\\"') + '"';
  const child = useShell
    ? spawn([quoted(cmd), ...args.map(quoted)].join(' '), {cwd: root, shell: true, ...options})
    : spawn(cmd, args, {cwd: root, shell: false, ...options});
  let stdout = '', stderr = '';
  child.stdout.on('data', d => stdout += d);
  child.stderr.on('data', d => stderr += d);
  child.on('error', reject);
  child.on('close', code => code === 0 ? resolve({stdout, stderr}) : reject(new Error(`${cmd} ${args.join(' ')} exited ${code}\n${stdout}\n${stderr}`)));
});
const dbRun = (sql, params = []) => new Promise((resolve, reject) => {
  const db = new sqlite3.Database(dbPath);
  db.run(sql, params, function(err) { db.close(); err ? reject(err) : resolve(this); });
});
const dbGet = (sql, params = []) => new Promise((resolve, reject) => {
  const db = new sqlite3.Database(dbPath);
  db.get(sql, params, (err, row) => { db.close(); err ? reject(err) : resolve(row); });
});

async function resetDb() {
  await exec(process.execPath, ['database.js'], {cwd: backend});
}

async function startServer() {
  const child = spawn(process.execPath, ['server.js'], {cwd: backend, shell: false, stdio: ['ignore', 'pipe', 'pipe']});
  for (let i = 0; i < 40; i++) {
    try { const res = await fetch('http://127.0.0.1:3000/api/products'); if (res.ok) return child; } catch (_) {}
    await sleep(125);
  }
  child.kill();
  throw new Error('Backend did not start.');
}
async function stopServer(child) {
  if (!child || child.exitCode !== null) return;
  child.kill();
  await new Promise(resolve => child.once('close', resolve));
}
async function fixtureLogin(row) {
  if (row.fixture_attempts !== undefined) await dbRun('UPDATE users SET login_attempts = ?, locked_until = NULL WHERE email = ?', [row.fixture_attempts, 'test@eshop.com']);
  if (row.fixture_locked_seconds) await dbRun('UPDATE users SET locked_until = ?, login_attempts = 4 WHERE email = ?', [new Date(Date.now() + row.fixture_locked_seconds * 1000).toISOString(), 'test@eshop.com']);
}
async function fixtureAdmin(rows) {
  for (const row of rows) {
    const orderId = Number(row.order_id);
    // Out-of-range/path-fuzz values deliberately exercise 404 handling and
    // must not become SQLite fixtures.
    if (!/^\d+$/.test(String(row.order_id)) || !Number.isSafeInteger(orderId) || orderId <= 0) continue;
    await dbRun('INSERT OR REPLACE INTO orders (id, user_id, total_amount, status, shipping_address) VALUES (?, ?, ?, ?, ?)', [orderId, 2, 30000000, row.initial_status, `Fixture ${row.tc_id}`]);
  }
}
async function newman(collection, dataPath, outJson, outHtml) {
  fs.mkdirSync(path.dirname(outJson), {recursive: true});
  // The stock Newman installation guarantees cli/json reporters.  HTML is
  // rendered later from this raw JSON and explicitly labelled as such.
  const args = ['run', collection, '-e', path.join(postman, 'environments', 'local.postman_environment.json'), '-d', dataPath, '-r', 'cli,json', '--reporter-json-export', outJson];
  return exec(process.platform === 'win32' ? 'newman.cmd' : 'newman', args);
}
function summarize(jsonPath, row) {
  const output = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
  const stats = output.run.stats;
  return {tc_id: row ? row.tc_id : null, json: path.relative(base, jsonPath).replaceAll('\\', '/'), requests: stats.requests.total, assertions: stats.assertions.total, failed_assertions: stats.assertions.failed, failures: output.run.failures.length};
}
async function runLogin(rows) {
  const pool = path.join(reports, 'pool-a');
  const manifest = [];
  for (const row of rows) {
    await resetDb();
    const server = await startServer();
    const dataFile = path.join(os.tmpdir(), `hw06-${row.tc_id}.json`);
    fs.writeFileSync(dataFile, JSON.stringify([row]));
    const json = path.join(pool, 'cases', `${row.tc_id}.json`);
    const html = path.join(pool, 'cases', `${row.tc_id}.html`);
    try { await fixtureLogin(row); await newman(path.join(postman, 'collections', 'pool_a_login.postman_collection.json'), dataFile, json, html); }
    finally { await stopServer(server); fs.rmSync(dataFile, {force: true}); }
    const item = summarize(json, row);
    if (row.expected_post_attempts !== undefined) item.post_login_state = await dbGet('SELECT login_attempts, locked_until FROM users WHERE email = ?', ['test@eshop.com']);
    manifest.push(item);
  }
  return manifest;
}
async function runWhole(poolName, dataFile, collection, fixture) {
  await resetDb();
  const rows = read(dataFile);
  const server = await startServer();
  const pool = path.join(reports, poolName);
  const json = path.join(pool, 'report.json');
  const html = path.join(pool, 'report.html');
  try { if (fixture) await fixture(rows); await newman(path.join(postman, 'collections', collection), path.join(postman, 'data', dataFile), json, html); }
  finally { await stopServer(server); }
  return [summarize(json, null)];
}
function rollup(items) {
  return items.reduce((a, x) => ({cases: a.cases + (x.tc_id ? 1 : 40), requests: a.requests + x.requests, assertions: a.assertions + x.assertions, failed_assertions: a.failed_assertions + x.failed_assertions, failures: a.failures + x.failures}), {cases: 0, requests: 0, assertions: 0, failed_assertions: 0, failures: 0});
}
async function main() {
  fs.mkdirSync(evidence, {recursive: true});
  fs.copyFileSync(dbPath, backup);
  try {
    const a = await runLogin(read('login_data.json'));
    const b = await runWhole('pool-b', 'checkout_data.json', 'pool_b_checkout.postman_collection.json');
    const c = await runWhole('pool-c', 'admin_orders_data.json', 'pool_c_admin_orders.postman_collection.json', fixtureAdmin);
    const manifest = {generated_at: new Date().toISOString(), student_id: '23127404', target: 'http://127.0.0.1:3000', pools: {a: {cases: a, totals: rollup(a)}, b: {cases: b, totals: rollup(b)}, c: {cases: c, totals: rollup(c)}}};
    fs.writeFileSync(path.join(evidence, 'execution-manifest.json'), JSON.stringify(manifest, null, 2) + '\n');
    if (manifest.pools.a.totals.failures || manifest.pools.b.totals.failures || manifest.pools.c.totals.failures) throw new Error('At least one Newman assertion failed; inspect raw reports before publishing.');
  } finally {
    fs.copyFileSync(backup, dbPath);
    fs.rmSync(backup, {force: true});
  }
}

main().catch(error => { console.error(error.stack || error.message); process.exitCode = 1; });
