from datetime import datetime, UTC

from app.domain.trade import Trade

from app.portfolio.portfolio import (
    Portfolio,
)

portfolio = Portfolio(
    initial_balance=100000.0,
    cash_balance=100000.0,
)

trade = Trade(
    symbol="BTCUSD",
    side="BUY",
    quantity=1.0,
    entry_price=100000.0,
    exit_price=102000.0,
    pnl=2000.0,
    opened_at=datetime.now(UTC),
    closed_at=datetime.now(UTC),
)

portfolio.add_trade(trade)

print(
    "TRADES =",
    len(portfolio.trades),
)
