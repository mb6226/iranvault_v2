from app.domain.signal import Signal


MAX_RISK_PERCENT = 2.0
MIN_CONFIDENCE = 0.60
MIN_REWARD_RISK = 2.0


def validate_signal(
    signal: Signal,
    risk_percent: float,
) -> bool:

    if risk_percent > MAX_RISK_PERCENT:
        raise ValueError(
            f"risk percent exceeds maximum ({MAX_RISK_PERCENT}%)"
        )

    if signal.confidence < MIN_CONFIDENCE:
        raise ValueError(
            f"confidence below minimum ({MIN_CONFIDENCE})"
        )

    risk = abs(
        signal.entry_price
        - signal.stop_loss
    )

    if risk == 0:
        raise ValueError(
            "stop loss distance cannot be zero"
        )

    reward = abs(
        signal.take_profit
        - signal.entry_price
    )

    reward_risk_ratio = reward / risk

    if reward_risk_ratio < MIN_REWARD_RISK:
        raise ValueError(
            f"reward/risk ratio too low ({reward_risk_ratio:.2f})"
        )

    return True
