from app.domain.candle import Candle


def detect_bos(
    candles: list[Candle],
    lookback: int = 10,
) -> str:

    if len(candles) < lookback + 1:
        return "NO_BOS"

    previous = candles[-(lookback + 1):-1]

    last_candle = candles[-1]

    highest_high = max(c.high for c in previous)

    lowest_low = min(c.low for c in previous)

    if last_candle.high > highest_high:
        return "BOS_UP"

    if last_candle.low < lowest_low:
        return "BOS_DOWN"

    return "NO_BOS"
