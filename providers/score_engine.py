"""
=========================================================
ATHENA Score Engine
CoveredCall Pro India
=========================================================
"""


class ScoreEngine:

    def calculate(

        self,

        premium_score,

        vix_score,

        distance_score,

        liquidity_score,

        expiry_score

    ):

        score = (

            premium_score * 0.35 +

            vix_score * 0.20 +

            distance_score * 0.20 +

            liquidity_score * 0.15 +

            expiry_score * 0.10

        )

        return round(score)


score_engine = ScoreEngine()