from app.data.binance_candle_loader import load_candles

from app.ml.dataset_builder import (
    build_dataset,
)

from app.ml.csv_exporter import (
    export_dataset,
)

candles = load_candles(
    symbol="BTCUSDT",
    interval="1h",
    limit=500,
)

dataset = build_dataset(
    candles,
)

output_file = "data/ml/btcusdt_dataset.csv"

export_dataset(
    dataset,
    output_file,
)

print("ROWS =", len(dataset))
print("FILE =", output_file)
