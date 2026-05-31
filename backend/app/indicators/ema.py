from app.domain.candle import Candle


def ema(
    candles: list[Candle],
    period: int,
) -> float | None:
    if period <= 0:
        raise ValueError("period must be greater than zero")

    if len(candles) < period:
        return None

    closes = [c.close for c in candles]

    multiplier = 2.0 / (period + 1)

    ema_value = sum(closes[:period]) / period

    for close_price in closes[period:]:
        ema_value = (
            close_price * multiplier
            + ema_value * (1.0 - multiplier)
        )

    return ema_value
