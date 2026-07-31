from __future__ import annotations

from dataclasses import dataclass, field
import math
from uuid import uuid4

from .discrepancy import Discrepancy


@dataclass
class Obstruction:
    obstruction_id: str
    projections: tuple[str, ...]
    residual_score: float
    description: str
    first_seen: int
    last_seen: int
    recurrence_count: int = 1
    status: str = "unresolved"
    evidence: list[str] = field(default_factory=list)


def cycle_residual(edges: list[Discrepancy]) -> float:
    if not edges:
        return 0.0
    dimensions = len(edges[0].vector)
    total = [0.0] * dimensions
    for edge in edges:
        if len(edge.vector) != dimensions:
            raise ValueError("All discrepancy vectors must have equal dimension")
        for index, value in enumerate(edge.vector):
            total[index] += value
    return math.sqrt(sum(value * value for value in total))


def make_obstruction(
    projections: tuple[str, ...],
    score: float,
    step: int,
    evidence: list[str],
) -> Obstruction:
    description = "Persistent cycle inconsistency across: " + " -> ".join(projections)
    return Obstruction(
        obstruction_id=f"obs_{uuid4().hex[:10]}",
        projections=projections,
        residual_score=score,
        description=description,
        first_seen=step,
        last_seen=step,
        evidence=evidence,
    )
