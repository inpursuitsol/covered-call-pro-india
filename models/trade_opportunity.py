from dataclasses import dataclass

from models.candidate_trade import CandidateTrade
from models.trade_score import TradeScore
from models.income_projection import IncomeProjection
from models.risk_assessment import RiskAssessment


@dataclass(frozen=True)
class TradeOpportunity:

    candidate: CandidateTrade

    income: IncomeProjection

    risk: RiskAssessment

    score: TradeScore

    probability_otm: float

    reasons: list[str]

    warnings: list[str]