from app.data.binance_candle_loader import load_candles
from app.strategies import trend_bos_strategy

candles = load_candles(
    symbol="BTCUSDT",
    interval="1h",
    limit=500,
)

count = 0

for i in range(50, len(candles)):

    signal = trend_bos_strategy.generate_signal(
        candles[:i]
    )

    if signal is None:
        continue

    count += 1

    print()
    print(signal)

    if count >= 10:
        break
