"""
=========================================================
Option Chain Provider
CoveredCall Pro India
=========================================================
"""

from models.option_contract import OptionContract


class OptionChainProvider:

    def get_calls(self):

        return [

            OptionContract(
                strike=24600,
                option_type="CE",
                premium=182,
                bid=181,
                ask=183,
                open_interest=2100000,
                volume=54000,
                implied_volatility=13.2
            ),

            OptionContract(
                strike=24700,
                option_type="CE",
                premium=166,
                bid=165,
                ask=167,
                open_interest=2600000,
                volume=72000,
                implied_volatility=13.5
            ),

            OptionContract(
                strike=24800,
                option_type="CE",
                premium=149,
                bid=148,
                ask=150,
                open_interest=1950000,
                volume=46000,
                implied_volatility=13.8
            )

        ]


option_chain_provider = OptionChainProvider()