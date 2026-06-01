from app.data.binance_candle_loader import load_candles_large
from app.ml.predictor import predict_signal

candles = load_candles_large(
    symbol="BTCUSDT",
    interval="1h",
    total_limit=300,
)

signal = predict_signal(candles)

print(signal)
