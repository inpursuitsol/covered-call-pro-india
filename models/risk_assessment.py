from dataclasses import dataclass


@dataclass(frozen=True)
class RiskAssessment:

    assignment_risk: float

    volatility_risk: float

    liquidity_risk: float

    overall_risk: float