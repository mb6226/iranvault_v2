from app.data.binance_candle_loader import load_candles
from app.strategies import trend_bos_strategy

candles = load_candles(
    symbol="BTCUSDT",
    interval="1h",
    limit=500,
)

signals = []

for i in range(20, len(candles)):

    signal = trend_bos_strategy.generate_signal(
        candles[:i]
    )

    if signal is not None:
        signals.append(signal)

print("CANDLES =", len(candles))
print("SIGNALS =", len(signals))

buys = len(
    [s for s in signals if s.side == "BUY"]
)

sells = len(
    [s for s in signals if s.side == "SELL"]
)

print("BUYS =", buys)
print("SELLS =", sells)

if signals:

    print()
    print("FIRST_SIGNAL =", signals[0])
    print()
    print("LAST_SIGNAL =", signals[-1])
