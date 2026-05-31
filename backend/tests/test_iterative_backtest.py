from app.data.binance_candle_loader import (
    load_candles,
)

from app.strategies import (
    trend_bos_strategy,
)

signals = []

candles = load_candles(
    symbol="BTCUSDT",
    interval="1h",
    limit=100,
)

for i in range(20, len(candles) + 1):

    window = candles[:i]

    signal = (
        trend_bos_strategy.generate_signal(
            window
        )
    )

    if signal is not None:
        signals.append(signal)

print(
    "TOTAL_CANDLES =",
    len(candles),
)

print(
    "SIGNALS_FOUND =",
    len(signals),
)

if signals:

    print()

    print(
        signals[-1]
    )
