from dataclasses import dataclass
from datetime import datetime, date


@dataclass(frozen=True)
class MarketSnapshot:
    spot: float
    vix: float
    expiry: date
    days_to_expiry: int
    opportunity_score: int
    market_mood: str
    risk_level: str
    expected_income: float
    last_updated: datetime