# Phase 3 — SUS Scoring

**Formula:** odd items (1,3,5,7,9): score = rating − 1. Even items (2,4,6,8,10): score = 5 − rating. Sum × 2.5 = SUS score (0–100).

| Participant | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10 | SUS Score |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 (Long) | 2 | 4 | 2 | 4 | 2 | 4 | 3 | 4 | 2 | 3 | 30.0 |
| P2 (Linh) | 3 | 3 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 2 | 55.0 |
| P3 (Tiến) | 1 | 5 | 2 | 4 | 2 | 5 | 2 | 5 | 1 | 4 | 12.5 |
| P4 (Khải) | 2 | 4 | 3 | 3 | 3 | 3 | 3 | 4 | 2 | 3 | 40.0 |
| **Mean** |  |  |  |  |  |  |  |  |  |  | **34.4** |

**Benchmark reference:** SUS mean ≥ 68 = above-average usability (industry norm); < 51 = poor. Report where the mean falls once computed, and note variance across participants (a wide spread often flags an issue only some user segments hit — e.g. IT vs non-IT participants).

## Interpretation

- **Mean SUS score: 34.4** (rounded from 34.375).
- **Comparison to the 68 benchmark:** Well below it — this sits deep in the "poor" band (<51), consistent with the fact that all 4 participants failed to complete the task at all. A SUS this low after a single blocking bug is expected; it should not be read as "the whole site is unusable," only that this specific screen/flow is.
- **Notable outliers and hypothesized cause:** P3 (Tiến, 12.5) is a clear low outlier — he made the most attempts (4) and was visibly the most frustrated, which tracks with SUS items 1/6/8/9 all scoring at the extreme. P2 (Linh, 55.0) is the high outlier — she disengaged analytically after only 2 attempts ("chắc web bị lỗi") rather than emotionally, which kept her ratings closer to neutral despite also not completing the task. This suggests SUS score here is driven less by the bug itself (identical for all 4) and more by each participant's persistence/attempt count and attribution style (blaming the site vs. blaming themselves).
