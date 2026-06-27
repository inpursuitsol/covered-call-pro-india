"""
=========================================================
Recommendation Service
CoveredCall Pro India
=========================================================
"""

from providers.athena_engine import athena_engine


class RecommendationService:

    def get_recommendation(self):

        return athena_engine.get_trade()


recommendation_service = RecommendationService()