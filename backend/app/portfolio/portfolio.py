from dataclasses import dataclass, field

from app.domain.position import Position
from app.domain.trade import Trade


@dataclass(slots=True)
class Portfolio:
    initial_balance: float

    cash_balance: float

    positions: list[Position] = field(default_factory=list)

    trades: list[Trade] = field(default_factory=list)

    def add_position(self, position: Position) -> None:
        self.positions.append(position)

    def add_trade(self, trade: Trade) -> None:
        self.trades.append(trade)

    def calculate_exposure(self) -> float:
        return sum(
            p.quantity * p.current_price
            for p in self.positions
        )

    def calculate_unrealized_pnl(self) -> float:
        return sum(
            p.unrealized_pnl
            for p in self.positions
        )

    def calculate_equity(self) -> float:
        return (
            self.cash_balance
            + self.calculate_unrealized_pnl()
        )

    def total_realized_pnl(self) -> float:
        return sum(
            trade.pnl
            for trade in self.trades
        )

    def total_trades(self) -> int:
        return len(self.trades)

    def win_rate(self) -> float:
        total = len(self.trades)

        if total == 0:
            return 0.0

        wins = sum(
            1
            for trade in self.trades
            if trade.pnl > 0
        )

        return (wins / total) * 100.0

    def average_win(self) -> float:
        wins = [
            trade.pnl
            for trade in self.trades
            if trade.pnl > 0
        ]

        if not wins:
            return 0.0

        return sum(wins) / len(wins)

    def average_loss(self) -> float:
        losses = [
            abs(trade.pnl)
            for trade in self.trades
            if trade.pnl < 0
        ]

        if not losses:
            return 0.0

        return sum(losses) / len(losses)

    def profit_factor(self) -> float:
        gross_profit = sum(
            trade.pnl
            for trade in self.trades
            if trade.pnl > 0
        )

        gross_loss = abs(
            sum(
                trade.pnl
                for trade in self.trades
                if trade.pnl < 0
            )
        )

        if gross_loss == 0:
            return 0.0

        return gross_profit / gross_loss

    def expectancy(self) -> float:
        total = len(self.trades)

        if total == 0:
            return 0.0

        return (
            self.total_realized_pnl()
            / total
        )
