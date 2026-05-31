from app.domain.signal import Signal
from app.domain.trade_plan import TradePlan

from app.risk.trade_plan_builder import (
    build_trade_plan,
)


class CreateTradePlanUseCase:

    def execute(
        self,
        signal: Signal,
        account_balance: float,
        risk_percent: float,
    ) -> TradePlan:

        return build_trade_plan(
            signal=signal,
            account_balance=account_balance,
            risk_percent=risk_percent,
        )
