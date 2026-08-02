# FR-23 Mobile Source Review Evidence

This evidence records static inspection of `frontend-mobile/App.js`. It supports the source-derived checklist classification requested before real-device screenshots are available; it does not claim a physical-device observation.

| Defect | Checklist | Source finding | Source location | Runtime evidence |
|---|---|---|---|---|
| BUG-020 | CHK-GUI-038 | Product Detail image uses `resizeMode="stretch"` instead of preserving aspect ratio. | `App.js:553–559` | Pending real-device screenshot |
| BUG-021 | CHK-GUI-039 | Detail JSX renders name, price, and description but no category. | `App.js:560–562` | Pending real-device screenshot |
| BUG-022 | CHK-GUI-012, CHK-GUI-041 | Zero, negative, empty, and non-numeric input is silently converted to quantity 1. | `App.js:129–135` | Pending quantity before/after captures |
| BUG-023 | CHK-GUI-042 | Detail screen has no dedicated back control; only the shared brand invokes `goHome`. | `App.js:536–585` and header renderer | Pending real-device screenshot |
| BUG-024 | CHK-GUI-044 | Empty-product state displays technical text without a recovery CTA. | `App.js:544–550` | Pending real-device screenshot |

Real-device evidence takes precedence if the packaged runtime behaves differently from this source inspection.
