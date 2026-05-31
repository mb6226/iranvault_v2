from app.domain.position import Position

from app.application.update_position_price import (
    UpdatePositionPriceUseCase,
)

position = Position(
    symbol="BTCUSD",
    side="BUY",
    quantity=1.0,
    entry_price=100000.0,
    current_price=100000.0,
    unrealized_pnl=0.0,
)

UpdatePositionPriceUseCase().execute(
    position=position,
    new_price=102000.0,
)

print(position)

print(
    "UPNL =",
    position.unrealized_pnl,
)
