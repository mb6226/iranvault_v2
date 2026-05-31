from dataclasses import dataclass


@dataclass(slots=True)
class TradePlan:
    symbol: str

    side: str

    entry_price: float

    stop_loss: float

    take_profit: float

    risk_percent: float

    position_size: float
