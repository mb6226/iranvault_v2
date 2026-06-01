from app.data.binance_candle_loader import (
    load_candles_large,
)

from app.strategies import ml_strategy

candles = load_candles_large(
    symbol="BTCUSDT",
    interval="1h",
    total_limit=300,
)

signal = ml_strategy.generate_signal(
    candles
)

print(signal)
