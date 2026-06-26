"""
=========================================================
Recommendation Model
CoveredCall Pro India
=========================================================
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class Recommendation:

    decision: str

    strike: str

    premium: float

    monthly_income: float

    annualized_yield: float

    confidence: int

    risk: str

    reasons: List[str] = field(default_factory=list)

    generated_at: str = field(
        default_factory=lambda: datetime.now().strftime("%d %b %Y %I:%M %p")
    )