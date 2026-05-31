from datetime import datetime

from app.backtest.backtest_engine import (
    BacktestEngine,
)

from app.broker.paper_broker import (
    PaperBroker,
)

from app.domain.candle import Candle

from app.portfolio.portfolio import (
    Portfolio,
)

from app.strategies import trend_bos_strategy


portfolio = Portfolio(
    initial_balance=100000.0,
    cash_balance=100000.0,
)

broker = PaperBroker(
    portfolio=portfolio,
)

candles = []

price = 100.0

for _ in range(25):

    candles.append(
        Candle(
            symbol="BTCUSD",
            timeframe="M1",
            timestamp=datetime.utcnow(),
            open=price,
            high=price + 2,
            low=price - 1,
            close=price + 1,
            volume=1000,
        )
    )

    price += 1

candles.append(
    Candle(
        symbol="BTCUSD",
        timeframe="M1",
        timestamp=datetime.utcnow(),
        open=price,
        high=price + 10,
        low=price - 1,
        close=price + 5,
        volume=1000,
    )
)

signals, trade_plans, positions = (
    BacktestEngine().run(
        candles=candles,
        strategy=trend_bos_strategy,
        broker=broker,
        account_balance=100000.0,
        risk_percent=1.0,
    )
)

print("SIGNALS =", len(signals))
print("TRADE_PLANS =", len(trade_plans))
print("POSITIONS =", len(positions))
print("PORTFOLIO_POSITIONS =", len(portfolio.positions))

if signals:
    print(signals[0])

if trade_plans:
    print(trade_plans[0])
