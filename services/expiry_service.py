"""
=========================================================
Expiry Service
CoveredCall Pro India
=========================================================
"""

from datetime import date, timedelta


class ExpiryService:

    def get_next_expiry(self):

        today = date.today()

        days_until_thursday = (3 - today.weekday()) % 7

        expiry = today + timedelta(days=days_until_thursday)

        return expiry.strftime("%d %b %Y")


expiry_service = ExpiryService()