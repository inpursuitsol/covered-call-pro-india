"""
=========================================================
Market Provider Interface
CoveredCall Pro India
=========================================================
"""

from services.live_market import live_market


class MarketProvider:

    def get_nifty(self):
        return live_market.get_nifty_price()

    def get_vix(self):
        return live_market.get_vix()


market_provider = MarketProvider()