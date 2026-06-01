from datetime import datetime, UTC

from app.domain.candle import Candle

from app.market_structure.swing import (
    swing_low,
    swing_high,
)

candles = []

for i in range(20):

    candles.append(
        Candle(
            symbol="BTCUSD",
            timeframe="M1",
            timestamp=datetime.now(UTC),
            open=100 + i,
            high=110 + i,
            low=90 + i,
            close=105 + i,
            volume=1000,
        )
    )

print(
    "SWING_LOW =",
    swing_low(candles),
)

print(
    "SWING_HIGH =",
    swing_high(candles),
)
