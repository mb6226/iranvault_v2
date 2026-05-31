from app.data.binance_candle_loader import load_candles
from app.strategies import trend_bos_strategy

signals = []

candles = load_candles(
    symbol="BTCUSDT",
    interval="1h",
    limit=100,
)

for i in range(20, len(candles)):

    window = candles[:i]

    signal = trend_bos_strategy.generate_signal(
        window
    )

    if signal is not None:

        signals.append(
            signal
        )

print(
    "TOTAL_CANDLES =",
    len(candles),
)

print(
    "TOTAL_SIGNALS =",
    len(signals),
)

buy_count = len(
    [s for s in signals if s.side == "BUY"]
)

sell_count = len(
    [s for s in signals if s.side == "SELL"]
)

print(
    "BUY_SIGNALS =",
    buy_count,
)

print(
    "SELL_SIGNALS =",
    sell_count,
)
