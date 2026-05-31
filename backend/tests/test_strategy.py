from datetime import datetime

from app.domain.candle import Candle
from app.strategies.trend_bos_strategy import generate_signal


candles = []

price = 100.0

for _ in range(30):
    candles.append(
        Candle(
            symbol="BTCUSD",
            timeframe="M1",
            timestamp=datetime.utcnow(),
            open=price,
            high=price + 1,
            low=price - 1,
            close=price,
            volume=100,
        )
    )

    price += 1


candles.append(
    Candle(
        symbol="BTCUSD",
        timeframe="M1",
        timestamp=datetime.utcnow(),
        open=200,
        high=250,
        low=199,
        close=240,
        volume=100,
    )
)

print(
    generate_signal(
        candles
    )
)
