from dataclasses import dataclass


@dataclass(frozen=True)
class TradeScore:

    premium: float
    distance: float
    probability: float
    liquidity: float
    expiry: float

    overall: float