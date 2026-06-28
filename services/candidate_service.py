"""
=========================================================
Candidate Strike Service
CoveredCall Pro India
=========================================================
"""

from models.candidate_trade import CandidateTrade

# Temporary: Use mock provider until live NSE provider is finalized
from providers.option_chain_provider import option_chain_provider

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

        calls = option_chain_provider.get_calls()

        candidates = []

        candidate_strikes = [
            base - 100,
            base,
            base + 100
        ]

        for option in calls:

            if option.strike not in candidate_strikes:
                continue

            distance = (
                (option.strike - nifty_price)
                / nifty_price
            ) * 100

            candidates.append(

                CandidateTrade(

                    option=option,

                    distance_percent=round(distance, 2),

                    premium=option.premium

                )

            )

        candidates.sort(
            key=lambda x: x.option.strike
        )

        return candidates


candidate_service = CandidateService()