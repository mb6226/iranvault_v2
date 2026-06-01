from app.domain.candle import Candle


def swing_low(
    candles: list[Candle],
    lookback: int = 10,
) -> float | None:

    if len(candles) < lookback:
        return None

    return min(
        candle.low
        for candle in candles[-lookback:]
    )


def swing_high(
    candles: list[Candle],
    lookback: int = 10,
) -> float | None:

    if len(candles) < lookback:
        return None

    return max(
        candle.high
        for candle in candles[-lookback:]
    )
