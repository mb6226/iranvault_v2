from app.domain.position import Position

from app.portfolio.portfolio import (
    Portfolio,
)

portfolio = Portfolio(
    initial_balance=100000.0,
    cash_balance=100000.0,
)

position = Position(
    symbol="BTCUSD",
    side="BUY",
    quantity=1.0,
    entry_price=100000.0,
    current_price=101000.0,
    unrealized_pnl=1000.0,
)

portfolio.add_position(position)

print(
    "EXPOSURE =",
    portfolio.calculate_exposure(),
)

print(
    "UPNL =",
    portfolio.calculate_unrealized_pnl(),
)

print(
    "EQUITY =",
    portfolio.calculate_equity(),
)
