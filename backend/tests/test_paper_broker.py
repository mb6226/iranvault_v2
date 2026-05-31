from app.broker.paper_broker import (
    PaperBroker,
)

from app.domain.trade_plan import (
    TradePlan,
)

from app.portfolio.portfolio import (
    Portfolio,
)

portfolio = Portfolio(
    initial_balance=100000.0,
    cash_balance=100000.0,
)

broker = PaperBroker(
    portfolio=portfolio,
)

trade_plan = TradePlan(
    symbol="BTCUSD",
    side="BUY",
    entry_price=100000.0,
    stop_loss=98000.0,
    take_profit=106000.0,
    risk_percent=1.0,
    position_size=1.0,
)

position = broker.open_position(
    trade_plan
)

broker.update_position_price(
    position,
    102000.0,
)

trade = broker.close_position(
    position,
    102000.0,
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
    "PNL =",
    trade.pnl,
)
