import { mkdirSync, writeFileSync } from "node:fs";
import path from "node:path";
import type { FullConfig, FullResult, Reporter, Suite } from "@playwright/test/reporter";

interface Options {
  reportDir: string;
  studentId: string;
  runTimestamp: string;
  feature: string;
  browser: string;
  automationRevision: string;
  sutRevision: string;
  executionCommand: string;
}

export default class RunMetadataReporter implements Reporter {
  private total = 0;

  constructor(private readonly options: Options) {}

  onBegin(_config: FullConfig, suite: Suite): void {
    this.total = suite.allTests().length;
    this.write({ status: "running", total: this.total });
  }

  onEnd(result: FullResult): void {
    this.write({ status: result.status, total: this.total, durationMs: result.duration });
  }

  private write(result: Record<string, unknown>): void {
    mkdirSync(this.options.reportDir, { recursive: true });
    writeFileSync(
      path.join(this.options.reportDir, "run-metadata.json"),
      `${JSON.stringify(
        {
          runBy: this.options.studentId,
          runTimestamp: this.options.runTimestamp,
          feature: this.options.feature,
          browser: this.options.browser,
          automationRevision: this.options.automationRevision,
          sutRevision: this.options.sutRevision,
          executionCommand: this.options.executionCommand,
          ...result,
        },
        null,
        2,
      )}\n`,
      "utf8",
    );
  }
}
