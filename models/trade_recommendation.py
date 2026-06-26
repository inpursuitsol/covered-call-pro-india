"""
=========================================================
Trade Recommendation Model
CoveredCall Pro India
=========================================================
"""

from dataclasses import dataclass


@dataclass
class TradeRecommendation:

    action: str

    strike: int

    expiry: str

    premium: float

    confidence: int

    monthly_income: float

    reason: str

    risk: str