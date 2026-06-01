from app.data.binance_candle_loader import load_candles
from app.features.feature_builder import (
    build_features,
)

candles = load_candles(
    symbol="BTCUSDT",
    interval="1h",
    limit=100,
)

features = build_features(candles)

for k, v in features.items():
    print(k, "=", v)
