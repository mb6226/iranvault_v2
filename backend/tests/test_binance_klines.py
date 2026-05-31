from app.data.binance_spot_client import (
    get_klines,
)

candles = get_klines(
    symbol="BTCUSDT",
    interval="1h",
    limit=5,
)

print(
    "CANDLES =",
    len(candles),
)

print(
    candles[0]
)
