from app.data.binance_candle_loader import load_candles
from app.strategies import trend_bos_strategy

candles = load_candles(
    symbol="BTCUSDT",
    interval="1h",
    limit=500,
)

ratios = []

for i in range(20, len(candles)):

    signal = trend_bos_strategy.generate_signal(
        candles[:i]
    )

    if signal is None:
        continue

    risk = abs(
        signal.entry_price
        - signal.stop_loss
    )

    reward = abs(
        signal.take_profit
        - signal.entry_price
    )

    ratios.append(
        reward / risk
    )

print("SIGNALS =", len(ratios))

print(
    "AVG_RR =",
    round(
        sum(ratios) / len(ratios),
        2,
    ),
)

print(
    "MIN_RR =",
    round(min(ratios), 2),
)

print(
    "MAX_RR =",
    round(max(ratios), 2),
)
