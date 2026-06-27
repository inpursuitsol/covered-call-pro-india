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

        selected = candidates[len(candidates) // 2]

        return TradeRecommendation(
            action="SELL",
            strike=selected,
            expiry=market["expiry"],
            premium=285,
            confidence=92,
            monthly_income=18525,
            reason="Selected by ATHENA Candidate Engine",
            risk="LOW"
        )


athena_engine = AthenaEngine()