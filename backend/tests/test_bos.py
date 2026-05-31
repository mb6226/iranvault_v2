from datetime import datetime

from app.domain.candle import Candle
from app.market_structure.bos import detect_bos


candles = []

price = 100.0

for _ in range(20):
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
    detect_bos(
        candles
    )
)
