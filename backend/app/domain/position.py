from dataclasses import dataclass


@dataclass(slots=True)
class Position:
    symbol: str

    side: str

    quantity: float

    entry_price: float

    current_price: float

    unrealized_pnl: float = 0.0
