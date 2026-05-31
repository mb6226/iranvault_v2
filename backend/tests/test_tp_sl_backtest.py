from app.data.binance_candle_loader import load_candles
from app.strategies import trend_bos_strategy

wins = 0
losses = 0

total_pnl = 0.0

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

    trade_closed = False

    for future_candle in candles[i:]:

        if signal.side == "BUY":

            if future_candle.low <= signal.stop_loss:

                pnl = (
                    signal.stop_loss
                    - signal.entry_price
                )

                losses += 1

                total_pnl += pnl

                trade_closed = True

                break

            if future_candle.high >= signal.take_profit:

                pnl = (
                    signal.take_profit
                    - signal.entry_price
                )

                wins += 1

                total_pnl += pnl

                trade_closed = True

                break

        else:

            if future_candle.high >= signal.stop_loss:

                pnl = (
                    signal.entry_price
                    - signal.stop_loss
                )

                losses += 1

                total_pnl += pnl

                trade_closed = True

                break

            if future_candle.low <= signal.take_profit:

                pnl = (
                    signal.entry_price
                    - signal.take_profit
                )

                wins += 1

                total_pnl += pnl

                trade_closed = True

                break

    if not trade_closed:
        pass

print("WINS =", wins)
print("LOSSES =", losses)

total_trades = wins + losses

print("TRADES =", total_trades)

if total_trades:

    print(
        "WIN_RATE =",
        round(
            wins * 100 / total_trades,
            2,
        ),
    )

print(
    "TOTAL_PNL =",
    round(total_pnl, 2),
)
