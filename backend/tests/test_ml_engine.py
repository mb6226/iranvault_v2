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

print("SIGNALS =", len(signals))
print("TRADE_PLANS =", len(trade_plans))
print("POSITIONS =", len(positions))

if signals:
    print(signals[0])

if trade_plans:
    print(trade_plans[0])

if positions:
    print(positions[0])
