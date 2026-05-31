from app.application.open_position import (
    OpenPositionUseCase,
)

from app.application.update_position_price import (
    UpdatePositionPriceUseCase,
)

from app.application.close_position import (
    ClosePositionUseCase,
)

from app.domain.position import Position
from app.domain.trade import Trade
from app.domain.trade_plan import TradePlan

from app.portfolio.portfolio import Portfolio


class PaperBroker:

    def __init__(
        self,
        portfolio: Portfolio,
    ) -> None:

        self.portfolio = portfolio

        self._open_position = (
            OpenPositionUseCase()
        )

        self._update_position = (
            UpdatePositionPriceUseCase()
        )

        self._close_position = (
            ClosePositionUseCase()
        )

    def open_position(
        self,
        trade_plan: TradePlan,
    ) -> Position:

        return self._open_position.execute(
            portfolio=self.portfolio,
            trade_plan=trade_plan,
        )

    def update_position_price(
        self,
        position: Position,
        new_price: float,
    ) -> Position:

        return self._update_position.execute(
            position=position,
            new_price=new_price,
        )

    def close_position(
        self,
        position: Position,
        exit_price: float,
    ) -> Trade:

        trade = self._close_position.execute(
            position=position,
            exit_price=exit_price,
        )

        self.portfolio.add_trade(trade)

        if position in self.portfolio.positions:
            self.portfolio.positions.remove(
                position
            )

        return trade
