from dataclasses import dataclass

from models.option_contract import OptionContract


@dataclass(frozen=True)
class CandidateTrade:

    option: OptionContract

    distance_percent: float

    premium: float = 0.0

    score: float = 0.0