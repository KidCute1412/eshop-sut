import { mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { resolve } from 'node:path';

const root = resolve('docs/assignments/HW05/deliverables');
const load = readFileSync(resolve(root, 'plans/23127404_Load_20260817.jmx'), 'utf8');
const profiles = [20, 50, 100, 150];
const output = resolve(root, 'supporting-materials/threshold-plans');
mkdirSync(output, { recursive: true });

for (const users of profiles) {
  const name = `Threshold ${users} VU`;
  const fileTag = `Threshold_${String(users).padStart(3, '0')}VU`;
  const plan = load
    .replaceAll('23127404 Load API Workflow', `23127404 ${name} API Workflow`)
    .replaceAll('Load Virtual Users', `${name} Virtual Users`)
    .replace('<intProp name="ThreadGroup.num_threads">5</intProp>', `<intProp name="ThreadGroup.num_threads">${users}</intProp>`)
    .replace('<intProp name="ThreadGroup.ramp_time">15</intProp>', '<intProp name="ThreadGroup.ramp_time">20</intProp>')
    .replace('<stringProp name="LoopController.loops">10</stringProp>', '<stringProp name="LoopController.loops">40</stringProp>')
    .replaceAll('23127404_Load_GUI_20260817.jtl', `23127404_${fileTag}_GUI_20260817.jtl`);
  writeFileSync(resolve(output, `23127404_${fileTag}_20260817.jmx`), plan, 'utf8');
}
console.log(`Created ${profiles.length} valid stepped-load threshold plans.`);
