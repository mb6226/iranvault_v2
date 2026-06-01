from app.data.binance_candle_loader import (
    load_candles_large,
)

candles = load_candles_large(
    symbol="BTCUSDT",
    interval="1h",
    total_limit=3000,
)

print()

print("CANDLES =", len(candles))

print(
    "FIRST =",
    candles[0].timestamp,
)

print(
    "LAST =",
    candles[-1].timestamp,
)
