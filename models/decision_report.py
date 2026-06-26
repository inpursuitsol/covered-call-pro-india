from dataclasses import dataclass
from datetime import datetime

from models.market_snapshot import MarketSnapshot
from models.trade_opportunity import TradeOpportunity


@dataclass(frozen=True)
class DecisionReport:

    snapshot: MarketSnapshot

    recommendation: TradeOpportunity

    alternatives: list[TradeOpportunity]

    rejected: list[str]

    confidence: float

    generated_at: datetime