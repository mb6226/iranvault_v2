from app.domain.candle import Candle


def detect_trend(
    candles: list[Candle],
    lookback: int = 20,
) -> str:

    if len(candles) < lookback:
        return "UNKNOWN"

    recent = candles[-lookback:]

    first_close = recent[0].close
    last_close = recent[-1].close

    if last_close > first_close:
        return "UPTREND"

    if last_close < first_close:
        return "DOWNTREND"

    return "RANGE"
