from datetime import datetime, UTC

from app.domain.candle import Candle

from app.strategies.trend_bos_strategy import (
    generate_signal,
)

candles = []

price = 100.0

for _ in range(25):

    candles.append(
        Candle(
            symbol="BTCUSD",
            timeframe="M1",
            timestamp=datetime.now(UTC),
            open=price,
            high=price + 2,
            low=price - 1,
            close=price + 1,
            volume=1000,
        )
    )

    price += 1

candles.append(
    Candle(
        symbol="BTCUSD",
        timeframe="M1",
        timestamp=datetime.now(UTC),
        open=price,
        high=price + 10,
        low=price - 1,
        close=price + 5,
        volume=1000,
    )
)

signal = generate_signal(candles)

print(signal)
