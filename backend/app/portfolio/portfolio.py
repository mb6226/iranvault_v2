from dataclasses import dataclass, field

from app.domain.position import Position


@dataclass(slots=True)
class Portfolio:
    initial_balance: float

    cash_balance: float

    positions: list[Position] = field(
        default_factory=list
    )

    def add_position(
        self,
        position: Position,
    ) -> None:
        self.positions.append(position)

    def calculate_exposure(
        self,
    ) -> float:

        exposure = 0.0

        for position in self.positions:
            exposure += (
                position.quantity
                * position.current_price
            )

        return exposure

    def calculate_unrealized_pnl(
        self,
    ) -> float:

        pnl = 0.0

        for position in self.positions:
            pnl += position.unrealized_pnl

        return pnl

    def calculate_equity(
        self,
    ) -> float:

        return (
            self.cash_balance
            + self.calculate_unrealized_pnl()
        )
