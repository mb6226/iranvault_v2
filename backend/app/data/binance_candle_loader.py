from datetime import datetime

from app.domain.candle import Candle

from app.data.binance_spot_client import (
    get_klines,
)


def load_candles(
    symbol: str,
    interval: str,
    limit: int = 100,
) -> list[Candle]:

    rows = get_klines(
        symbol=symbol,
        interval=interval,
        limit=limit,
    )

    candles: list[Candle] = []

    for row in rows:

        candles.append(
            Candle(
                symbol=symbol,
                timeframe=interval,
                timestamp=datetime.fromtimestamp(
                    row[0] / 1000
                ),
                open=float(row[1]),
                high=float(row[2]),
                low=float(row[3]),
                close=float(row[4]),
                volume=float(row[5]),
            )
        )

    return candles
