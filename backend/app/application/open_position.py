from app.domain.position import Position
from app.domain.trade_plan import TradePlan

from app.portfolio.portfolio import (
    Portfolio,
)


class OpenPositionUseCase:

    def execute(
        self,
        portfolio: Portfolio,
        trade_plan: TradePlan,
    ) -> Position:

        position = Position(
            symbol=trade_plan.symbol,
            side=trade_plan.side,
            quantity=trade_plan.position_size,
            entry_price=trade_plan.entry_price,
            current_price=trade_plan.entry_price,
            stop_loss=trade_plan.stop_loss,
            take_profit=trade_plan.take_profit,
            unrealized_pnl=0.0,
        )

        portfolio.add_position(position)

        return position
