from dataclasses import dataclass


@dataclass(frozen=True)
class IncomeProjection:

    premium_per_unit: float

    lot_size: int

    lots: int

    total_income: float

    monthly_yield: float

    annualized_yield: float