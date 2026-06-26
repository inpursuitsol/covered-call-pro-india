"""
=========================================================
User Profile Model
CoveredCall Pro India
=========================================================
"""

from dataclasses import dataclass


@dataclass
class UserProfile:

    name: str

    broker: str

    nifty_bees: int

    lots: int

    preferred_otm: float

    minimum_vix: float

    target_monthly_yield: float

    paper_trading: bool