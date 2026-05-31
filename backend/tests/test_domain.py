from datetime import datetime, UTC

from app.domain.candle import Candle
from app.domain.signal import Signal
from app.domain.position import Position
from app.domain.trade import Trade


def main():

    candle = Candle(
        symbol="BTCUSD",
        timeframe="M1",
        timestamp=datetime.now(UTC),
        open=100,
        high=110,
        low=90,
        close=105,
        volume=1000,
    )

    signal = Signal(
        symbol="BTCUSD",
        strategy="TEST",
        side="BUY",
        entry_price=100,
        stop_loss=95,
        take_profit=120,
        confidence=0.75,
    )

    position = Position(
        symbol="BTCUSD",
        side="BUY",
        quantity=1,
        entry_price=100,
        current_price=105,
    )

    trade = Trade(
        symbol="BTCUSD",
        side="BUY",
        quantity=1,
        entry_price=100,
        exit_price=110,
        pnl=10,
        opened_at=datetime.now(UTC),
        closed_at=datetime.now(UTC),
    )

    print(candle)
    print(signal)
    print(position)
    print(trade)


if __name__ == "__main__":
    main()
