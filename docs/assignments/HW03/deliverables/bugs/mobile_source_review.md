# FR-23 Mobile Source Review Evidence

This file preserves the earlier static inspection of `frontend-mobile/App.js`. It is supporting root-cause context only; the linked Mobile captures, not this source review, establish the visible runtime observations.

| Defect | Checklist | Source finding | Source location | Runtime evidence |
|---|---|---|---|---|
| BUG-020 | CHK-GUI-038 | Product Detail image uses `resizeMode="stretch"` instead of preserving aspect ratio. | `App.js:553–559` | `cross_platform/mobile_real_device/mobile_01_product_detail.png` |
| BUG-021 | CHK-GUI-039 | Detail JSX renders name, price, and description but no category. | `App.js:560–562` | `cross_platform/mobile_real_device/mobile_01_product_detail.png` |
| BUG-022 | CHK-GUI-012, CHK-GUI-041 | Invalid input is normalized to quantity 1; the supplied runtime pair directly demonstrates the `0` variant only. | `App.js:129–135` | `cross_platform/mobile_real_device/mobile_03_invalid_quantity_before.png`; `cross_platform/mobile_real_device/mobile_04_invalid_quantity_after.png` |
| BUG-023 | CHK-GUI-042 | Detail screen has no dedicated back control; only the shared brand invokes `goHome`. | `App.js:536–585` and header renderer | `cross_platform/mobile_real_device/mobile_01_product_detail.png` |

Runtime evidence takes precedence if the packaged behavior differs from this source inspection. The current captures still require the PDF identity overlay before final submission.
