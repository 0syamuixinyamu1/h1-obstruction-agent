from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations

from .claims import LocalSection
from .discrepancy import Discrepancy, compare_sections
from .memory import ObstructionMemory
from .obstruction import Obstruction, cycle_residual, make_obstruction
from .projections import DEFAULT_PROJECTIONS, heuristic_project
from .retrieval import retrieve_relevant


@dataclass
class ProcessResult:
    sections: list[LocalSection]
    discrepancies: list[Discrepancy]
    obstructions: list[Obstruction]
    retrieved_memory: list[Obstruction]


class H1ObstructionAgent:
    def __init__(self, threshold: float = 0.35) -> None:
        self.threshold = threshold
        self.memory = ObstructionMemory()
        self.step = 0

    def process(self, text: str) -> ProcessResult:
        self.step += 1
        sections = [heuristic_project(text, name) for name in DEFAULT_PROJECTIONS]
        discrepancies: list[Discrepancy] = []
        edge_map: dict[tuple[str, str], Discrepancy] = {}
        for source in sections:
            for target in sections:
                if source.projection == target.projection:
                    continue
                edge = compare_sections(source, target)
                discrepancies.append(edge)
                edge_map[(source.projection, target.projection)] = edge

        detected: list[Obstruction] = []
        for a, b, c in combinations(DEFAULT_PROJECTIONS, 3):
            edges = [edge_map[(a, b)], edge_map[(b, c)], edge_map[(c, a)]]
            score = cycle_residual(edges)
            if score >= self.threshold:
                candidate = make_obstruction(
                    projections=(a, b, c, a),
                    score=score,
                    step=self.step,
                    evidence=[text],
                )
                detected.append(self.memory.add_or_update(candidate))

        relevant = retrieve_relevant(text, self.memory.items)
        return ProcessResult(
            sections=sections,
            discrepancies=discrepancies,
            obstructions=detected,
            retrieved_memory=relevant,
        )
