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

        if days_until_thursday == 0:
            days_until_thursday = 7

        return today + timedelta(days=days_until_thursday)

    def get_next_expiry_display(self):

        return self.get_next_expiry().strftime("%d %b %Y")


expiry_service = ExpiryService()