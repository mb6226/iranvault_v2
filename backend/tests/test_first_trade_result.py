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

    for future_candle in candles[i:]:

        if signal.side == "BUY":

            if future_candle.low <= signal.stop_loss:
                print("RESULT = LOSS")
                print(signal)
                raise SystemExit

            if future_candle.high >= signal.take_profit:
                print("RESULT = WIN")
                print(signal)
                raise SystemExit

        else:

            if future_candle.high >= signal.stop_loss:
                print("RESULT = LOSS")
                print(signal)
                raise SystemExit

            if future_candle.low <= signal.take_profit:
                print("RESULT = WIN")
                print(signal)
                raise SystemExit
