from dataclasses import dataclass


@dataclass(slots=True)
class Position:
    symbol: str

    side: str

    quantity: float

    entry_price: float

    current_price: float

    stop_loss: float

    take_profit: float

    unrealized_pnl: float = 0.0
