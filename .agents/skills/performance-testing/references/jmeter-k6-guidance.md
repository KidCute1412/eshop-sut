# JMeter and k6 Guidance

Prefer JMeter because HW05 names it as the default. Use k6 only when intentionally chosen and explain
equivalent report outputs.

## JMeter Plan Components

- Test Plan named `{StudentID}_{ScenarioType}_{YYYYMMDD}`.
- CSV Data Set Config for workflow rows.
- HTTP Request Defaults:
  - Protocol: `http`.
  - Server: `localhost`.
  - Port: `3000`.
- Header Manager:
  - `Content-Type: application/json`.
  - `Authorization: Bearer ${token}` after login.
- HTTP samplers for the five-step workflow.
- JSON Extractor after login: `$.token`.
- Assertions:
  - HTTP response code `200` for expected-success workflow steps.
  - Key response text/JSON where practical, such as login token and checkout `orderId`.
- Timer for think time.
- Distinct listener/report view per scenario.

## Suggested Listener Mapping

- Load: Summary Report.
- Stress: Aggregate Report.
- Spike: View Results Tree for debug visibility plus raw log.

## Non-GUI Commands

```powershell
jmeter -n -t reports/HW5/plans/23127539_Load_YYYYMMDD.jmx -l reports/HW5/results/load/load.jtl -e -o reports/HW5/results/load/html
jmeter -n -t reports/HW5/plans/23127539_Stress_YYYYMMDD.jmx -l reports/HW5/results/stress/stress.jtl -e -o reports/HW5/results/stress/html
jmeter -n -t reports/HW5/plans/23127539_Spike_YYYYMMDD.jmx -l reports/HW5/results/spike/spike.jtl -e -o reports/HW5/results/spike/html
```

Delete/archive old HTML folders before rerun; JMeter refuses to write into non-empty report folders.

