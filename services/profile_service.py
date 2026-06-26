"""
=========================================================
Profile Service
=========================================================
"""

from models.user_profile import UserProfile

from services.settings_service import settings_service


class ProfileService:

    def get_profile(self):

        settings = settings_service.load()

        return UserProfile(

            name=settings["user"]["name"],

            broker=settings["user"]["broker"],

            nifty_bees=settings["portfolio"]["nifty_bees"],

            lots=settings["portfolio"]["lots"],

            preferred_otm=settings["strategy"]["preferred_otm"],

            minimum_vix=settings["strategy"]["minimum_vix"],

            target_monthly_yield=settings["strategy"]["target_monthly_yield"],

            paper_trading=settings["strategy"]["paper_trading"]

        )


profile_service = ProfileService()