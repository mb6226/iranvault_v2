from app.data.binance_candle_loader import load_candles

from app.ml.dataset_builder import (
    build_dataset,
)

candles = load_candles(
    symbol="BTCUSDT",
    interval="1h",
    limit=500,
)

dataset = build_dataset(
    candles,
)

print(
    "ROWS =",
    len(dataset),
)

print()

print(
    dataset[0]
)

print()

print(
    dataset[-1]
)
