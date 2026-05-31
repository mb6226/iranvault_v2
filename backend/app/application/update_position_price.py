from app.domain.position import Position


class UpdatePositionPriceUseCase:

    def execute(
        self,
        position: Position,
        new_price: float,
    ) -> Position:

        position.current_price = new_price

        if position.side == "BUY":
            position.unrealized_pnl = (
                new_price
                - position.entry_price
            ) * position.quantity

        else:
            position.unrealized_pnl = (
                position.entry_price
                - new_price
            ) * position.quantity

        return position
