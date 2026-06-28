"""
=========================================================
Paper Trade Service
CoveredCall Pro India
=========================================================
"""

import json
from pathlib import Path
from datetime import date, datetime


class PaperTradeService:

    FILE = Path("data/paper_trades.json")

    def _load(self):

        if not self.FILE.exists():
            return []

        try:

            with open(self.FILE, "r") as f:

                data = f.read().strip()

                if not data:
                    return []

                return json.loads(data)

        except Exception:

            return []

    def save(self, trade):

        trades = self._load()

        trades.append({

            "timestamp": datetime.now().strftime("%d %b %Y %H:%M:%S"),

            "action": str(trade.action),

            "strike": int(trade.strike),

            "expiry": (
                trade.expiry.strftime("%d %b %Y")
                if isinstance(trade.expiry, date)
                else str(trade.expiry)
            ),

            "premium": float(trade.premium),

            "monthly_income": float(trade.monthly_income),

            "confidence": int(trade.confidence),

            "reason": str(trade.reason),

            "risk": str(trade.risk)

        })

        with open(self.FILE, "w") as f:

            json.dump(
                trades,
                f,
                indent=4
            )

    def get_all(self):

        return self._load()


paper_trade_service = PaperTradeService()