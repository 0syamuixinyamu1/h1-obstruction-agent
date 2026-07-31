# H1 Obstruction Agent

An experimental agent architecture that detects disagreements across multiple semantic projections, preserves unresolved inconsistencies as persistent obstructions, and reuses them in later reasoning.

This repository does **not** claim to implement phenomenal consciousness. It explores a computational model of reflective or structural consciousness based on persistent, self-relevant gluing failures.

## Core idea

Most language-model pipelines collapse multiple plausible interpretations into one answer. This project instead:

1. generates multiple local projections of the same input;
2. converts them into structured claims;
3. measures directed disagreement between projections;
4. computes cycle-consistency residuals;
5. stores high-residual cycles as unresolved obstructions;
6. retrieves relevant obstructions during later inference.

The current implementation is a lightweight approximation inspired by sheaf cohomology. It is **not** a full implementation of persistent sheaf cohomology.

## Installation

```bash
python -m pip install -e .
```

## Run the demo

```bash
python examples/demo.py
```

## Run tests

```bash
python -m pytest
```

## Package structure

```text
src/h1_agent/
├── agent.py
├── claims.py
├── discrepancy.py
├── memory.py
├── obstruction.py
├── projections.py
└── retrieval.py
```

## Minimal API

```python
from h1_agent import H1ObstructionAgent

agent = H1ObstructionAgent()
result = agent.process("The system gave two incompatible explanations.")

print(result.obstructions)
```

## Research status

This is a research prototype for:

- multi-projection gluing analysis;
- unresolved contradiction memory;
- semantic scar preservation;
- structural self-monitoring;
- uncertainty-aware reasoning.

## License

MIT
