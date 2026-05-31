from datetime import datetime

from app.backtest.backtest_engine import (
    BacktestEngine,
)

from app.domain.candle import Candle
from app.domain.signal import Signal


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

signals, trade_plans = (
    BacktestEngine().run(
        candles=candles,
        strategy=DummyStrategy(),
        account_balance=100000.0,
        risk_percent=1.0,
    )
)

print(
    "SIGNALS =",
    len(signals),
)

print(
    "TRADE_PLANS =",
    len(trade_plans),
)

print(
    trade_plans[0],
)
