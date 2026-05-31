from datetime import datetime, UTC

from app.domain.candle import Candle
from app.market_structure.choch import detect_choch


candles = []

price = 100.0

for _ in range(20):
    candles.append(
        Candle(
            symbol="BTCUSD",
            timeframe="M1",
            timestamp=datetime.now(UTC),
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
        timestamp=datetime.now(UTC),
        open=120,
        high=121,
        low=50,
        close=60,
        volume=100,
    )
)

print(
    detect_choch(
        candles
    )
)
