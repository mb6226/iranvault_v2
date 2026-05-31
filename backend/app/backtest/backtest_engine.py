from app.domain.candle import Candle
from app.domain.signal import Signal
from app.domain.trade_plan import TradePlan

from app.application.create_trade_plan import (
    CreateTradePlanUseCase,
)


class BacktestEngine:

    def run(
        self,
        candles: list[Candle],
        strategy,
        account_balance: float,
        risk_percent: float,
    ) -> tuple[list[Signal], list[TradePlan]]:

        signals: list[Signal] = []

        trade_plans: list[TradePlan] = []

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

            trade_plans.append(trade_plan)

        return signals, trade_plans
