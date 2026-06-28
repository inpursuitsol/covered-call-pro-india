"""
=========================================================
ATHENA Engine
CoveredCall Pro India
=========================================================
"""

from providers.score_engine import score_engine

from services.market_service import market_service
from services.profile_service import profile_service
from services.candidate_service import candidate_service

from models.trade_recommendation import TradeRecommendation


class AthenaEngine:

    def get_trade(self):

        market = market_service.get_snapshot()

        profile = profile_service.get_profile()

        candidates = candidate_service.generate(
            nifty_price=market["nifty"],
            preferred_otm=profile.preferred_otm,
            vix=market["vix"],
            days_to_expiry=market["days_to_expiry"]
        )

        if not candidates:
            return None

        scored_candidates = []

        for candidate in candidates:

            score = score_engine.score(candidate)

            scored_candidates.append((candidate, score))

        scored_candidates.sort(
            key=lambda x: x[1],
            reverse=True
        )

        best_candidate, best_score = scored_candidates[0]

        monthly_income = round(
            best_candidate.option.premium *
            profile.lots *
            50
        )

        confidence = min(
            round(best_score),
            100
        )

        return TradeRecommendation(

            action="SELL",

            strike=best_candidate.option.strike,

            expiry=market["expiry"],

            premium=best_candidate.option.premium,

            confidence=confidence,

            monthly_income=monthly_income,

            reason=(
                f"Premium ₹{best_candidate.option.premium} | "
                f"OI {best_candidate.option.open_interest:,} | "
                f"IV {best_candidate.option.implied_volatility}% | "
                f"Distance {best_candidate.distance_percent:.2f}%"
            ),

            risk="LOW"

        )


athena_engine = AthenaEngine()