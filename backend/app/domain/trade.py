from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Trade:
    symbol: str

    side: str

    quantity: float

    entry_price: float

    exit_price: float

    pnl: float

    opened_at: datetime

    closed_at: datetime
