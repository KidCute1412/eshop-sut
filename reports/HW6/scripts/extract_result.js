const fs = require("fs");

const report = JSON.parse(
  fs.readFileSync("../newman/report.json", "utf8")
);

const executions = report.run.executions;

for (const e of executions) {
  const name = e.item?.name || "";

  if (!name.startsWith("FR17-API-")) continue;

  const code = e.response?.code;

  let body = "";
  if (e.response?.stream?.data) {
    body = Buffer.from(e.response.stream.data).toString("utf8");
  }

  const failed = (e.assertions || []).some(a => a.error);

  console.log("==================================================");
  console.log(name);
  console.log("HTTP:", code);
  console.log("Result:", failed ? "FAIL" : "PASS");
  console.log("Body:", body);
}