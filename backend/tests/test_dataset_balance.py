from app.data.binance_candle_loader import load_candles

from app.ml.dataset_builder import (
    build_dataset,
)

candles = load_candles(
    symbol="BTCUSDT",
    interval="1h",
    limit=500,
)

dataset = build_dataset(candles)

up = sum(
    row["target"]
    for row in dataset
)

down = len(dataset) - up

print("ROWS =", len(dataset))
print("UP =", up)
print("DOWN =", down)

print(
    "UP_PERCENT =",
    round(
        up / len(dataset) * 100,
        2,
    ),
)
