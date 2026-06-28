from dataclasses import dataclass


@dataclass
class DecisionReport:
    strike: int
    score: float
    premium: float
    distance: float
    confidence: int
    reason: str