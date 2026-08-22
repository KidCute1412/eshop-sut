# AI-Driven API Test Generator Flow

```mermaid
flowchart TD
    A[API specification] --> B[Normalize endpoint contract]
    B --> C[Extract parameters, auth, schema, states]
    C --> D[Generate AI draft cases by technique]
    D --> E[Human audit: VALID / INVALID / INCOMPLETE]
    E --> F[Correct invalid and incomplete cases]
    F --> G[Add five human cases per API]
    G --> H[Export Excel workbooks]
    H --> I[Generate Postman data files]
    I --> J[Run Newman locally and in CI]
    J --> K[Write bug, CI, audit, and main reports]
```

> Student action required: the Mermaid diagram is an implementation draft. For the official submission rule that requires a self-drawn diagram, redraw or confirm this design manually and export it as PNG/PDF.
