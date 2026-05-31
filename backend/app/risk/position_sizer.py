def calculate_position_size(
    account_balance: float,
    risk_percent: float,
    entry_price: float,
    stop_loss_price: float,
) -> float:

    if account_balance <= 0:
        raise ValueError(
            "account_balance must be positive"
        )

    if risk_percent <= 0:
        raise ValueError(
            "risk_percent must be positive"
        )

    stop_distance = abs(
        entry_price - stop_loss_price
    )

    if stop_distance == 0:
        raise ValueError(
            "stop distance cannot be zero"
        )

    risk_amount = (
        account_balance
        * risk_percent
        / 100.0
    )

    position_size = (
        risk_amount
        / stop_distance
    )

    return round(
        position_size,
        8,
    )
