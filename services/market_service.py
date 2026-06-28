"""
=========================================================
Market Service
CoveredCall Pro India
=========================================================
"""

from datetime import datetime

from providers.market_provider import market_provider
from services.expiry_service import expiry_service


class MarketService:

    def get_snapshot(self):

        nifty = market_provider.get_nifty()

        vix = market_provider.get_vix()

        expiry = expiry_service.get_next_expiry()

        today = datetime.now().date()

        days_to_expiry = max(
            (expiry - today).days,
            0
        )

        return {

            "nifty": nifty,

            "change_percent": 0.0,

            "vix": vix,

            "expiry": expiry,

            "days_to_expiry": days_to_expiry,

            "market_status": "LIVE",

            "opportunity_score": 89,

            "expected_income": 18450,

            "risk": "LOW",

            "last_updated": datetime.now().strftime("%d %b %Y %I:%M:%S %p")

        }


market_service = MarketService()