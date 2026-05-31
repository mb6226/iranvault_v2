from datetime import datetime

from app.domain.trade import Trade
from app.portfolio.portfolio import Portfolio

portfolio = Portfolio(
    initial_balance=100000.0,
    cash_balance=100000.0,
)

for pnl in [2000.0, -1000.0, 3000.0]:

    portfolio.add_trade(
        Trade(
            symbol="BTCUSD",
            side="BUY",
            quantity=1.0,
            entry_price=100,
            exit_price=100,
            pnl=pnl,
            opened_at=datetime.utcnow(),
            closed_at=datetime.utcnow(),
        )
    )

print("CURVE =", portfolio.equity_curve())

print("MAX_DRAWDOWN =", portfolio.max_drawdown())
