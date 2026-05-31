from app.domain.candle import Candle

from app.market_structure.trend import detect_trend


def detect_choch(
    candles: list[Candle],
    lookback: int = 10,
) -> str:

    if len(candles) < lookback + 5:
        return "NO_CHOCH"

    trend = detect_trend(
        candles[:-1],
        lookback=lookback,
    )

    previous = candles[-(lookback + 1):-1]

    last_candle = candles[-1]

    highest_high = max(
        candle.high
        for candle in previous
    )

    lowest_low = min(
        candle.low
        for candle in previous
    )

    if (
        trend == "UPTREND"
        and last_candle.low < lowest_low
    ):
        return "CHOCH_DOWN"

    if (
        trend == "DOWNTREND"
        and last_candle.high > highest_high
    ):
        return "CHOCH_UP"

    return "NO_CHOCH"
