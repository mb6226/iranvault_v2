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
    movement_threshold=1000,
)

print("TOTAL_CANDLES =", len(candles))
print("TOTAL_ROWS =", len(dataset))

print(
    "FILTER_RATE =",
    round(
        len(dataset) / len(candles) * 100,
        2,
    ),
    "%",
)
