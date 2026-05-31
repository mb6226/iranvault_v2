from app.application.close_position import (
    ClosePositionUseCase,
)

from app.domain.position import (
    Position,
)

position = Position(
    symbol="BTCUSD",
    side="BUY",
    quantity=1.0,
    entry_price=100000.0,
    current_price=102000.0,
    stop_loss=98000.0,
    take_profit=106000.0,
    unrealized_pnl=2000.0,
)

trade = ClosePositionUseCase().execute(
    position=position,
    exit_price=102000.0,
)

print(trade)

print(
    "REALIZED_PNL =",
    trade.pnl,
)
