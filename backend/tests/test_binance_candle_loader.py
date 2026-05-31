from app.data.binance_candle_loader import (
    load_candles,
)

candles = load_candles(
    symbol="BTCUSDT",
    interval="1h",
    limit=3,
)

print(
    "CANDLES =",
    len(candles),
)

print()

print(candles[0])
