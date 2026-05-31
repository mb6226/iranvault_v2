from app.domain.candle import Candle


def atr(
    candles: list[Candle],
    period: int = 14,
) -> float | None:
    if period <= 0:
        raise ValueError("period must be greater than zero")

    if len(candles) < period + 1:
        return None

    true_ranges = []

    for i in range(1, len(candles)):
        current = candles[i]
        previous = candles[i - 1]

        tr = max(
            current.high - current.low,
            abs(current.high - previous.close),
            abs(current.low - previous.close),
        )

        true_ranges.append(tr)

    return sum(true_ranges[-period:]) / period
