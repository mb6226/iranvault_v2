from app.data.binance_candle_loader import load_candles_large
from app.ml.dataset_builder import build_dataset

for threshold in [
    500,
    750,
    1000,
    1250,
    1500,
    2000,
]:
    candles = load_candles_large(
        symbol="BTCUSDT",
        interval="1h",
        total_limit=10000,
    )

    dataset = build_dataset(
        candles,
        movement_threshold=threshold,
    )

    print(
        "THRESHOLD =",
        threshold,
        "ROWS =",
        len(dataset),
    )
