"""
=========================================================
Candidate Strike Service
CoveredCall Pro India
=========================================================
"""

from services.strike_selector import strike_selector


class CandidateService:

    def generate(

        self,

        nifty_price,

        preferred_otm,

        vix,

        days_to_expiry

    ):

        base = strike_selector.select_strike(

            nifty_price,

            preferred_otm,

            vix,

            days_to_expiry

        )

        return [

            base - 100,

            base,

            base + 100

        ]


candidate_service = CandidateService()