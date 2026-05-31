from datetime import datetime

from app.backtest.backtest_engine import (
    BacktestEngine,
)

from app.broker.paper_broker import (
    PaperBroker,
)

from app.domain.candle import Candle
from app.domain.signal import Signal

from app.portfolio.portfolio import (
    Portfolio,
)


class DummyStrategy:

    def generate_signal(
        self,
        candles,
    ):

        return Signal(
            symbol="BTCUSD",
            strategy="DUMMY",
            side="BUY",
            entry_price=100.0,
            stop_loss=95.0,
            take_profit=120.0,
            confidence=0.8,
        )


portfolio = Portfolio(
    initial_balance=100000.0,
    cash_balance=100000.0,
)

broker = PaperBroker(
    portfolio=portfolio,
)

candles = [
    Candle(
        symbol="BTCUSD",
        timeframe="M1",
        timestamp=datetime.utcnow(),
        open=100,
        high=110,
        low=90,
        close=105,
        volume=1000,
    )
]

signals, trade_plans, positions = (
    BacktestEngine().run(
        candles=candles,
        strategy=DummyStrategy(),
        broker=broker,
        account_balance=100000.0,
        risk_percent=1.0,
    )
)

position = positions[0]

broker.update_position_price(
    position,
    110.0,
)

trade = broker.close_position(
    position,
    110.0,
)

print(
    "OPEN_POSITIONS =",
    len(portfolio.positions),
)

print(
    "TRADES =",
    len(portfolio.trades),
)

print(
    "REALIZED_PNL =",
    trade.pnl,
)
