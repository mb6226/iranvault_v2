from app.domain.signal import Signal
from app.risk.risk_validator import validate_signal


signal = Signal(
    symbol="BTCUSD",
    strategy="TREND_BOS",
    side="BUY",
    entry_price=100.0,
    stop_loss=95.0,
    take_profit=120.0,
    confidence=0.90,
)

result = validate_signal(
    signal=signal,
    risk_percent=1.0,
)

print(result)
