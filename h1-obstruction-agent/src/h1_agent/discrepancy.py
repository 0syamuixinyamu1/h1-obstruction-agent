from __future__ import annotations

from dataclasses import dataclass
import math

from .claims import LocalSection


@dataclass(frozen=True)
class Discrepancy:
    source: str
    target: str
    vector: tuple[float, ...]

    @property
    def magnitude(self) -> float:
        return math.sqrt(sum(value * value for value in self.vector))


def _stable_text_score(text: str) -> float:
    total = sum((index + 1) * ord(char) for index, char in enumerate(text))
    return (total % 1000) / 1000.0


def _directed_interaction(source: str, target: str, channel: str) -> float:
    """Pair-specific term that cannot generally be reduced to target-source potentials."""
    raw = _stable_text_score(f"{channel}:{source}->{target}")
    return (raw - 0.5) * 0.8


def compare_sections(source: LocalSection, target: LocalSection) -> Discrepancy:
    """Return a deterministic directed semantic-difference vector.

    The first terms measure local differences. Pair-specific interaction terms
    deliberately permit non-zero cycle residuals, approximating incompatibility
    that cannot be removed by assigning one scalar correction per projection.
    """
    if not source.claims or not target.claims:
        raise ValueError("Each local section must contain at least one claim")

    source_claim = source.claims[0]
    target_claim = target.claims[0]

    lexical = (
        _stable_text_score(target_claim.object)
        - _stable_text_score(source_claim.object)
        + _directed_interaction(source.projection, target.projection, "lexical")
    )
    confidence = (
        target_claim.confidence
        - source_claim.confidence
        + _directed_interaction(source.projection, target.projection, "confidence")
    )
    relation = (
        _stable_text_score(target_claim.relation)
        - _stable_text_score(source_claim.relation)
        + _directed_interaction(source.projection, target.projection, "relation")
    )
    projection = _directed_interaction(source.projection, target.projection, "projection")

    return Discrepancy(
        source=source.projection,
        target=target.projection,
        vector=(lexical, confidence, relation, projection),
    )
