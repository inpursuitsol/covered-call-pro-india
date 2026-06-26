from dataclasses import dataclass


@dataclass(frozen=True)
class OptionContract:
    strike: int
    option_type: str

    premium: float

    bid: float
    ask: float

    open_interest: int
    volume: int

    implied_volatility: float