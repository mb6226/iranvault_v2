from app.data.binance_candle_loader import (
    load_candles_large,
)

from app.ml.predictor import (
    predict_signal,
)

wins = 0
losses = 0

candles = load_candles_large(
    symbol="BTCUSDT",
    interval="1h",
    total_limit=3000,
)

for i in range(100, len(candles) - 24):

    signal = predict_signal(
        candles[:i]
    )

    if signal is None:
        continue

    entry_price = candles[i].close

    future_price = (
        candles[i + 24].close
    )

    if signal["direction"] == "BUY":

        result = (
            future_price
            > entry_price
        )

    else:

        result = (
            future_price
            < entry_price
        )

    if result:
        wins += 1
    else:
        losses += 1

total = wins + losses

print("WINS =", wins)
print("LOSSES =", losses)
print("TOTAL =", total)

if total:
    print(
        "WIN_RATE =",
        round(
            wins / total * 100,
            2,
        ),
    )
