import { readFileSync, writeFileSync } from 'node:fs';
import { resolve } from 'node:path';

const plans = resolve('docs/assignments/HW05/deliverables/plans');
const load = readFileSync(resolve(plans, '23127404_Load_20260817.jmx'), 'utf8');
const endurance = load
  .replaceAll('23127404 Load API Workflow', '23127404 Endurance API Workflow')
  .replaceAll('Load Virtual Users', 'Endurance Virtual Users')
  .replace('<stringProp name="LoopController.loops">10</stringProp>', '<stringProp name="LoopController.loops">220</stringProp>')
  .replaceAll('23127404_Load_GUI_20260817.jtl', '23127404_Endurance_GUI_VALIDATED_20260817.jtl');

writeFileSync(resolve(plans, '23127404_Endurance_20260817.jmx'), endurance, 'utf8');
console.log('Rebuilt valid Endurance JMX from the verified Load-plan structure.');
