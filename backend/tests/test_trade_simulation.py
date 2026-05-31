from app.data.binance_candle_loader import (
    load_candles,
)

from app.strategies import (
    trend_bos_strategy,
)

total_pnl = 0.0

wins = 0
losses = 0

candles = load_candles(
    symbol="BTCUSDT",
    interval="1h",
    limit=100,
)

for i in range(20, len(candles) - 1):

    window = candles[:i]

    signal = (
        trend_bos_strategy.generate_signal(
            window
        )
    )

    if signal is None:
        continue

    entry = signal.entry_price

    exit_price = candles[i].close

    if signal.side == "BUY":

        pnl = exit_price - entry

    else:

        pnl = entry - exit_price

    total_pnl += pnl

    if pnl > 0:
        wins += 1
    else:
        losses += 1

print(
    "TOTAL_PNL =",
    round(total_pnl, 2),
)

print(
    "WINS =",
    wins,
)

print(
    "LOSSES =",
    losses,
)

total_trades = wins + losses

if total_trades > 0:

    print(
        "WIN_RATE =",
        round(
            wins * 100 / total_trades,
            2,
        ),
    )
