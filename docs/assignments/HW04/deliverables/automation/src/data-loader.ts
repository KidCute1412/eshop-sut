import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import type { TraceableCase } from "./types.js";

export function loadCases<T extends TraceableCase>(relativeUrl: string, minimum = 12): T[] {
  const file = fileURLToPath(new URL(relativeUrl, import.meta.url));
  const parsed: unknown = JSON.parse(readFileSync(file, "utf8"));

  if (!Array.isArray(parsed) || parsed.length < minimum) {
    throw new Error(`${file} must contain at least ${minimum} cases`);
  }

  const ids = new Set<string>();
  for (const row of parsed as T[]) {
    if (!row.id || !row.title || !row.priority || !Array.isArray(row.partition)) {
      throw new Error(`${file} contains a case without required traceability fields`);
    }
    if (ids.has(row.id)) throw new Error(`${file} contains duplicate case ID ${row.id}`);
    ids.add(row.id);
  }

  return parsed as T[];
}
