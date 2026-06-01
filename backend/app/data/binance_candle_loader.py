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


def load_candles_large(
    symbol: str,
    interval: str,
    total_limit: int = 10000,
) -> list[Candle]:

    all_rows = []

    end_time = None

    batch_limit = 1000

    while len(all_rows) < total_limit:

        batch_size = min(batch_limit, total_limit - len(all_rows))

        rows = get_klines(
            symbol=symbol,
            interval=interval,
            limit=batch_size,
            end_time=end_time,
        )

        if not rows:
            break

        # API returns rows in ascending time order. To page backwards
        # from the most recent candles, prepend older batches.
        all_rows = rows + all_rows

        # set end_time to one ms before earliest returned candle
        end_time = rows[0][0] - 1

        if len(rows) < batch_size:
            break

    # keep only the most recent `total_limit` rows
    if len(all_rows) > total_limit:
        all_rows = all_rows[-total_limit:]

    candles: list[Candle] = []

    for row in all_rows:

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
