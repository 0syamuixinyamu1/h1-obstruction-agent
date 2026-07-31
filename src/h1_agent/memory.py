from __future__ import annotations

from dataclasses import dataclass, field

from .obstruction import Obstruction


@dataclass
class ObstructionMemory:
    items: list[Obstruction] = field(default_factory=list)

    def add_or_update(self, candidate: Obstruction, tolerance: float = 0.15) -> Obstruction:
        for existing in self.items:
            same_cycle = existing.projections == candidate.projections
            similar_score = abs(existing.residual_score - candidate.residual_score) <= tolerance
            if same_cycle and similar_score:
                existing.last_seen = candidate.last_seen
                existing.recurrence_count += 1
                existing.residual_score = (
                    existing.residual_score * (existing.recurrence_count - 1)
                    + candidate.residual_score
                ) / existing.recurrence_count
                existing.evidence.extend(candidate.evidence)
                return existing
        self.items.append(candidate)
        return candidate
