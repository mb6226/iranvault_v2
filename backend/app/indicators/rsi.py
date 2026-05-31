from app.domain.candle import Candle


def rsi(
    candles: list[Candle],
    period: int = 14,
) -> float | None:
    if period <= 0:
        raise ValueError("period must be greater than zero")

    if len(candles) < period + 1:
        return None

    closes = [c.close for c in candles]

    gains = []
    losses = []

    for i in range(1, len(closes)):
        diff = closes[i] - closes[i - 1]

        if diff > 0:
            gains.append(diff)
            losses.append(0.0)
        else:
            gains.append(0.0)
            losses.append(abs(diff))

    avg_gain = sum(gains[-period:]) / period
    avg_loss = sum(losses[-period:]) / period

    if avg_loss == 0:
        return 100.0

    rs = avg_gain / avg_loss

    return 100.0 - (100.0 / (1.0 + rs))
