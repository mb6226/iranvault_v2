from app.domain.signal import Signal
from app.domain.trade_plan import TradePlan

from app.risk.position_sizer import (
    calculate_position_size,
)

from app.risk.risk_validator import (
    validate_signal,
)


def build_trade_plan(
    signal: Signal,
    account_balance: float,
    risk_percent: float,
) -> TradePlan:

    validate_signal(
        signal=signal,
        risk_percent=risk_percent,
    )

    position_size = calculate_position_size(
        account_balance=account_balance,
        risk_percent=risk_percent,
        entry_price=signal.entry_price,
        stop_loss_price=signal.stop_loss,
    )

    return TradePlan(
        symbol=signal.symbol,
        side=signal.side,
        entry_price=signal.entry_price,
        stop_loss=signal.stop_loss,
        take_profit=signal.take_profit,
        risk_percent=risk_percent,
        position_size=position_size,
    )
