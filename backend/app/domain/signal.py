from dataclasses import dataclass


@dataclass(slots=True)
class Signal:
    symbol: str

    strategy: str

    side: str

    entry_price: float

    stop_loss: float

    take_profit: float

    confidence: float
