from datetime import datetime, UTC

from app.domain.trade import Trade

from app.portfolio.portfolio import (
    Portfolio,
)

portfolio = Portfolio(
    initial_balance=100000.0,
    cash_balance=100000.0,
)

portfolio.add_trade(
    Trade(
        symbol="BTCUSD",
        side="BUY",
        quantity=1.0,
        entry_price=100000.0,
        exit_price=102000.0,
        pnl=2000.0,
        opened_at=datetime.now(UTC),
        closed_at=datetime.now(UTC),
    )
)

portfolio.add_trade(
    Trade(
        symbol="BTCUSD",
        side="BUY",
        quantity=1.0,
        entry_price=100000.0,
        exit_price=99000.0,
        pnl=-1000.0,
        opened_at=datetime.now(UTC),
        closed_at=datetime.now(UTC),
    )
)

print(
    "TOTAL_TRADES =",
    portfolio.total_trades(),
)

print(
    "REALIZED_PNL =",
    portfolio.total_realized_pnl(),
)

print(
    "WIN_RATE =",
    portfolio.win_rate(),
)
