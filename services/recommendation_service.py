"""
=========================================================
Recommendation Service
CoveredCall Pro India
=========================================================
"""

from models.trade_recommendation import TradeRecommendation


class RecommendationService:

    def get_recommendation(self):

        return TradeRecommendation(

            action="SELL",

            strike=24800,

            expiry="26 Jun",

            premium=285,

            confidence=92,

            monthly_income=18525,

            reason="Paper Trade",

            risk="LOW"

        )


recommendation_service = RecommendationService()