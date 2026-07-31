from __future__ import annotations

from .obstruction import Obstruction


def token_overlap_score(query: str, obstruction: Obstruction) -> float:
    query_tokens = set(query.lower().split())
    memory_tokens = set(
        (obstruction.description + " " + " ".join(obstruction.evidence)).lower().split()
    )
    if not query_tokens or not memory_tokens:
        return 0.0
    return len(query_tokens & memory_tokens) / len(query_tokens | memory_tokens)


def retrieve_relevant(
    query: str,
    obstructions: list[Obstruction],
    limit: int = 5,
) -> list[Obstruction]:
    ranked = sorted(
        obstructions,
        key=lambda item: (token_overlap_score(query, item), item.residual_score),
        reverse=True,
    )
    return [item for item in ranked[:limit] if token_overlap_score(query, item) > 0.0]
