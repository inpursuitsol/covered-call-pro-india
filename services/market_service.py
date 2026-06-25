"""
=========================================================
CoveredCall Pro India (CCPI)
Market Service
Version : 0.2 Foundation
=========================================================

Purpose:
Provides market data to the application.

Currently returns demo data.

Later this file will connect to:
- Zerodha
- NSE
- India VIX
- Option Chain
"""

from datetime import datetime


class MarketService:

    def get_snapshot(self):

        return {
            "nifty": 25640.25,
            "change_percent": 0.62,
            "vix": 14.80,
            "market_status": "Bullish",
            "opportunity_score": 89,
            "expected_income": 18450,
            "risk": "LOW",
            "last_updated": datetime.now().strftime("%d %b %Y %I:%M:%S %p")
        }


market_service = MarketService()