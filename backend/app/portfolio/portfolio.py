from dataclasses import dataclass


@dataclass(slots=True)
class Portfolio:
    initial_balance: float

    cash_balance: float

    equity: float

    exposure: float

    open_positions: int
