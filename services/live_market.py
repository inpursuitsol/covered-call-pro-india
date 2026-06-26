"""
=========================================================
Live Market Service
CoveredCall Pro India
=========================================================
"""

import yfinance as yf


class LiveMarket:

    # --------------------------------------------------
    # Live NIFTY Index
    # --------------------------------------------------

    def get_nifty_price(self):

        try:

            ticker = yf.Ticker("^NSEI")

            data = ticker.history(period="1d")

            price = float(round(data["Close"].iloc[-1], 2))

            return price

        except Exception:

            return None

    # --------------------------------------------------
    # Live India VIX
    # --------------------------------------------------

    def get_vix(self):

        try:

            ticker = yf.Ticker("^INDIAVIX")

            data = ticker.history(period="1d")

            vix = float(round(data["Close"].iloc[-1], 2))

            return vix

        except Exception:

            return None


live_market = LiveMarket()