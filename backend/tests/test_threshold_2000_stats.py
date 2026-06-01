from app.data.binance_candle_loader import (
    load_candles_large,
)
from app.ml.dataset_builder import (
    build_dataset,
)

candles = load_candles_large(
    symbol="BTCUSDT",
    interval="1h",
    total_limit=10000,
)

dataset = build_dataset(
    candles,
    movement_threshold=2000,
)

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
