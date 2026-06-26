"""
=========================================================
Strategy Service
=========================================================
"""

from models.user_profile import user_profile


class StrategyService:

    def get_strategy(self):

        return {

            "name": user_profile.strategy,

            "lots": user_profile.lots,

            "nifty_bees": user_profile.nifty_bees,

            "otm_percent": user_profile.otm_percent,

            "minimum_vix": user_profile.minimum_vix

        }


strategy_service = StrategyService()