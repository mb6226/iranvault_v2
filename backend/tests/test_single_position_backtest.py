from app.data.binance_candle_loader import load_candles

from app.strategies import trend_bos_strategy

from app.portfolio.portfolio import Portfolio

from app.domain.trade import Trade

from datetime import datetime, UTC


portfolio = Portfolio(
    initial_balance=100000.0,
    cash_balance=100000.0,
)

candles = load_candles(
    symbol="BTCUSDT",
    interval="1h",
    limit=100,
)

position_open = False

for i in range(20, len(candles) - 1):

    if position_open:
        continue

    signal = trend_bos_strategy.generate_signal(
        candles[:i]
    )

    if signal is None:
        continue

    entry_price = signal.entry_price

    trade_closed = False

    for future_candle in candles[i:]:

        if signal.side == "BUY":

            if future_candle.low <= signal.stop_loss:

                exit_price = signal.stop_loss

                pnl = exit_price - entry_price

                trade_closed = True

            elif future_candle.high >= signal.take_profit:

                exit_price = signal.take_profit

                pnl = exit_price - entry_price

                trade_closed = True

        else:

            if future_candle.high >= signal.stop_loss:

                exit_price = signal.stop_loss

                pnl = entry_price - exit_price

                trade_closed = True

            elif future_candle.low <= signal.take_profit:

                exit_price = signal.take_profit

                pnl = entry_price - exit_price

                trade_closed = True

        if trade_closed:

            portfolio.add_trade(
                Trade(
                    symbol=signal.symbol,
                    side=signal.side,
                    quantity=1.0,
                    entry_price=entry_price,
                    exit_price=exit_price,
                    pnl=pnl,
                    opened_at=datetime.now(UTC),
                    closed_at=datetime.now(UTC),
                )
            )

            break

print(
    "TRADES =",
    portfolio.total_trades(),
)

print(
    "WIN_RATE =",
    round(
        portfolio.win_rate(),
        2,
    ),
)

print(
    "PROFIT_FACTOR =",
    round(
        portfolio.profit_factor(),
        2,
    ),
)

print(
    "EXPECTANCY =",
    round(
        portfolio.expectancy(),
        2,
    ),
)

print(
    "MAX_DRAWDOWN =",
    round(
        portfolio.max_drawdown(),
        2,
    ),
)
