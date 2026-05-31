from app.risk.position_sizer import (
    calculate_position_size,
)

result = calculate_position_size(
    account_balance=100000,
    risk_percent=1.0,
    entry_price=100.0,
    stop_loss_price=95.0,
)

print(result)
