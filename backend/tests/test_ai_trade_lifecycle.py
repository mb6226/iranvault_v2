from app.backtest.backtest_engine import (
    BacktestEngine,
)

from app.broker.paper_broker import (
    PaperBroker,
)

from app.portfolio.portfolio import (
    Portfolio,
)

from app.data.binance_candle_loader import (
    load_candles_large,
)

from app.strategies import ml_strategy

candles = load_candles_large(
    symbol="BTCUSDT",
    interval="1h",
    total_limit=300,
)

portfolio = Portfolio(
    initial_balance=100000.0,
    cash_balance=100000.0,
)

broker = PaperBroker(
    portfolio=portfolio,
)

engine = BacktestEngine()

signals, trade_plans, positions = (
    engine.run(
        candles=candles,
        strategy=ml_strategy,
        broker=broker,
        account_balance=100000,
        risk_percent=1.0,
    )
)

position = positions[0]

print("OPEN_POSITION")
print(position)

exit_price = position.take_profit

trade = broker.close_position(
    position=position,
    exit_price=exit_price,
)

print()
print("TRADE")
print(trade)

print()
print("PORTFOLIO_TRADES =",
      portfolio.total_trades())

print(
    "REALIZED_PNL =",
    round(
        portfolio.total_realized_pnl(),
        2,
    ),
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
