"""
=========================================================
ATHENA Score Engine
CoveredCall Pro India
=========================================================
"""


class ScoreEngine:

    PREMIUM_WEIGHT = 35
    DISTANCE_WEIGHT = 25
    LIQUIDITY_WEIGHT = 25
    IV_WEIGHT = 15

    MAX_PREMIUM = 300
    MAX_OI = 2_000_000
    IDEAL_OTM = 2.5
    MAX_IV = 30

    def premium_score(self, candidate):

        return round(
            min(candidate.option.premium / self.MAX_PREMIUM, 1.0)
            * self.PREMIUM_WEIGHT,
            2
        )

    def distance_score(self, candidate):

        return round(
            max(
                0.0,
                1 - abs(candidate.distance_percent - self.IDEAL_OTM) / 5
            )
            * self.DISTANCE_WEIGHT,
            2
        )

    def liquidity_score(self, candidate):

        return round(
            min(candidate.option.open_interest / self.MAX_OI, 1.0)
            * self.LIQUIDITY_WEIGHT,
            2
        )

    def iv_score(self, candidate):

        return round(
            min(candidate.option.implied_volatility / self.MAX_IV, 1.0)
            * self.IV_WEIGHT,
            2
        )

    def score(self, candidate):

        return round(

            self.premium_score(candidate)
            + self.distance_score(candidate)
            + self.liquidity_score(candidate)
            + self.iv_score(candidate),

            2

        )


score_engine = ScoreEngine()