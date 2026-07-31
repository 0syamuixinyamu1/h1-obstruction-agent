from __future__ import annotations

from .claims import Claim, LocalSection

DEFAULT_PROJECTIONS = (
    "factual",
    "causal",
    "normative",
    "self_model",
    "social_model",
    "adversarial",
)


def heuristic_project(text: str, projection: str) -> LocalSection:
    """Create deterministic placeholder projections without an external LLM.

    Replace this function with an API-backed generator for real experiments.
    """
    cleaned = " ".join(text.strip().split())
    base_confidence = {
        "factual": 0.85,
        "causal": 0.60,
        "normative": 0.55,
        "self_model": 0.50,
        "social_model": 0.58,
        "adversarial": 0.42,
    }.get(projection, 0.50)

    relation = {
        "factual": "describes",
        "causal": "may_be_caused_by",
        "normative": "should_be_evaluated_as",
        "self_model": "is_interpreted_by_system_as",
        "social_model": "is_interpreted_socially_as",
        "adversarial": "may_be_misread_as",
    }.get(projection, "relates_to")

    object_text = {
        "factual": cleaned,
        "causal": f"multiple possible causes of: {cleaned}",
        "normative": f"an unresolved evaluation of: {cleaned}",
        "self_model": f"a potentially self-relevant conflict in: {cleaned}",
        "social_model": f"a socially situated interpretation of: {cleaned}",
        "adversarial": f"an underdetermined or unsupported reading of: {cleaned}",
    }.get(projection, cleaned)

    claim = Claim(
        subject="input",
        relation=relation,
        object=object_text,
        confidence=base_confidence,
        source_projection=projection,
    )
    return LocalSection(projection=projection, claims=[claim])
