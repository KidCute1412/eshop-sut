# Automation Script Generation Method

## Step-by-Step AI Prompting (Not One Generic Prompt)

The assignment explicitly forbids a single prompt like "write all the automation scripts for this
feature." Drive the AI through discrete steps, each with its own prompt and its own preserved
output:

1. **Scaffold** — project structure, Playwright config, base fixtures (e.g. a login fixture for
   admin features). One prompt, reused across all 3 features if the structure is shared.
2. **Convert one test-case group at a time** — group the selected 12+ cases by kind (positive /
   negative / edge, or by sub-flow) and convert one group per prompt. This keeps each AI output
   small enough to actually review line by line in Phase 5, and makes it possible to attribute a
   specific gap (a missed edge case, a fragile selector) to a specific prompt/response pair in the
   AI Audit Report.
3. **Data extraction** — a dedicated prompt asking the AI to extract every literal value used across
   the generated scripts into an external `.json`/`.csv` file and rewrite the scripts to load from
   it, rather than asking for data-driven scripts from the very first prompt (empirically, asking
   for both code and data-externalization at once tends to produce test data that's still partially
   inline).
4. **Assertion audit** — a dedicated prompt asking the AI to list, script by script, which assertion
   pattern each `expect(...)` call uses, so the human reviewer can quickly check Phase 4's
   "≥3 distinct patterns" requirement is actually met rather than assumed.

## What to Actually Give the AI as Context

For each prompt, include:

- The specific test case(s) being converted (ID, steps, expected result) — not a vague feature
  summary.
- The relevant page's real structure from `references/eshop-analysis-guide.md` (URLs, field labels,
  button text, and the "no `data-testid` anywhere" warning) so the AI's first-pass selectors are
  grounded in reality rather than guessed.
- The existing project's Playwright config / fixtures / helper functions already written, so later
  prompts build on earlier output instead of re-inventing conventions.

## Preserving Raw Output

Before applying any human fix, copy the AI's generated code into this feature's `ai-audit.md` via
`scripts/append_ai_audit.py --output-refs <path-to-the-generated-file-at-that-point>`, or paste it
inline with `--prompt-file`/verbatim in the entry if the file will be overwritten by the next
prompt. The gap analysis in Phase 5 needs a real "before" state to compare the final, human-fixed
script against — without it, "what the AI got wrong" degenerates into a vague generalization instead
of a concrete diff.
