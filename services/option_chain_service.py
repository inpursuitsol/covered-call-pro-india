"""
=========================================================
Option Chain Service
CoveredCall Pro India
=========================================================
"""

import yfinance as yf


class OptionChainService:

    def get_chain(self):

        try:

            ticker = yf.Ticker("^NSEI")

            expiries = ticker.options

            return expiries

        except Exception:

            return []


option_chain_service = OptionChainService()