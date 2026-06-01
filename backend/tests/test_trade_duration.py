from app.data.binance_candle_loader import load_candles
from app.strategies import trend_bos_strategy

candles = load_candles(
    symbol="BTCUSDT",
    interval="1h",
    limit=100,
)

for i in range(20, len(candles) - 1):

    signal = trend_bos_strategy.generate_signal(
        candles[:i]
    )

    if signal is None:
        continue

    bars = 0

    for future_candle in candles[i:]:

        bars += 1

        if signal.side == "BUY":

            if (
                future_candle.low <= signal.stop_loss
                or
                future_candle.high >= signal.take_profit
            ):
                break

        else:

            if (
                future_candle.high >= signal.stop_loss
                or
                future_candle.low <= signal.take_profit
            ):
                break

    print(
        signal.side,
        "bars=",
        bars,
    )

    if bars:
        pass

    break
