from app.application.create_trade_plan import (
    CreateTradePlanUseCase,
)

from app.broker.paper_broker import (
    PaperBroker,
)

from app.domain.candle import Candle
from app.domain.position import Position
from app.domain.signal import Signal
from app.domain.trade_plan import TradePlan


class BacktestEngine:

    def run(
        self,
        candles: list[Candle],
        strategy,
        broker: PaperBroker,
        account_balance: float,
        risk_percent: float,
    ) -> tuple[
        list[Signal],
        list[TradePlan],
        list[Position],
    ]:

        signals: list[Signal] = []

        trade_plans: list[TradePlan] = []

        positions: list[Position] = []

        signal = strategy.generate_signal(
            candles
        )

        if signal is not None:

            signals.append(signal)

            trade_plan = (
                CreateTradePlanUseCase()
                .execute(
                    signal=signal,
                    account_balance=account_balance,
                    risk_percent=risk_percent,
                )
            )

            trade_plans.append(
                trade_plan
            )

            position = (
                broker.open_position(
                    trade_plan
                )
            )

            positions.append(
                position
            )

        return (
            signals,
            trade_plans,
            positions,
        )
