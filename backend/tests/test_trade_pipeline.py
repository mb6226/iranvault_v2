from app.domain.signal import Signal

from app.risk.trade_plan_builder import (
    build_trade_plan,
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

plan = build_trade_plan(
    signal=signal,
    account_balance=100000,
    risk_percent=1.0,
)

print(plan)
