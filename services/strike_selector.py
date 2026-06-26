"""
=========================================================
Strike Selector
CoveredCall Pro India
=========================================================
"""

import math


class StrikeSelector:

    def round_to_strike(self, value):

        return int(math.ceil(value / 100) * 100)

    def select_strike(

        self,

        nifty_price,

        preferred_otm,

        vix,

        days_to_expiry

    ):

        target = nifty_price * (1 + preferred_otm / 100)

        strike = self.round_to_strike(target)

        return strike


strike_selector = StrikeSelector()