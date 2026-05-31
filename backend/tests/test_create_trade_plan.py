from app.domain.signal import Signal

from app.application.create_trade_plan import (
    CreateTradePlanUseCase,
)


signal = Signal(
    symbol="BTCUSD",
    strategy="TREND_BOS",
    side="BUY",
    entry_price=100.0,
    stop_loss=95.0,
    take_profit=120.0,
    confidence=0.90,
)

use_case = CreateTradePlanUseCase()

plan = use_case.execute(
    signal=signal,
    account_balance=100000,
    risk_percent=1.0,
)

print(plan)
