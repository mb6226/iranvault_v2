from app.application.open_position import (
    OpenPositionUseCase,
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

trade_plan = TradePlan(
    symbol="BTCUSD",
    side="BUY",
    entry_price=100000.0,
    stop_loss=98000.0,
    take_profit=106000.0,
    risk_percent=1.0,
    position_size=0.5,
)

position = OpenPositionUseCase().execute(
    portfolio=portfolio,
    trade_plan=trade_plan,
)

print(position)
