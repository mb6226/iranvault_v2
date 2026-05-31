from datetime import datetime, UTC

from app.domain.position import Position
from app.domain.trade import Trade


class ClosePositionUseCase:

    def execute(
        self,
        position: Position,
        exit_price: float,
    ) -> Trade:

        if position.side == "BUY":
            pnl = (
                exit_price
                - position.entry_price
            ) * position.quantity
        else:
            pnl = (
                position.entry_price
                - exit_price
            ) * position.quantity

        now = datetime.now(UTC)

        return Trade(
            symbol=position.symbol,
            side=position.side,
            quantity=position.quantity,
            entry_price=position.entry_price,
            exit_price=exit_price,
            pnl=pnl,
            opened_at=now,
            closed_at=now,
        )
