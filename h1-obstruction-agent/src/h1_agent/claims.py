from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Claim:
    subject: str
    relation: str
    object: str
    confidence: float
    source_projection: str

    def normalized_key(self) -> tuple[str, str]:
        return (self.subject.strip().lower(), self.relation.strip().lower())


@dataclass
class LocalSection:
    projection: str
    claims: list[Claim] = field(default_factory=list)
