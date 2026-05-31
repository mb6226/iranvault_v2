from datetime import datetime, UTC

from app.domain.trade import Trade
from app.portfolio.portfolio import Portfolio

portfolio = Portfolio(
    initial_balance=100000.0,
    cash_balance=100000.0,
)

portfolio.add_trade(
    Trade(
        symbol="BTCUSD",
        side="BUY",
        quantity=1.0,
        entry_price=100,
        exit_price=120,
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
        entry_price=100,
        exit_price=90,
        pnl=-1000.0,
        opened_at=datetime.now(UTC),
        closed_at=datetime.now(UTC),
    )
)

equity = portfolio.initial_balance

curve = []

for trade in portfolio.trades:
    equity += trade.pnl
    curve.append(equity)

print(curve)
