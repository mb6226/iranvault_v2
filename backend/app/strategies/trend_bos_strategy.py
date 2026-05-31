from app.domain.candle import Candle

from app.market_structure.trend import detect_trend
from app.market_structure.bos import detect_bos


def generate_signal(
    candles: list[Candle],
) -> str:

    trend = detect_trend(candles)

    bos = detect_bos(candles)

    if (
        trend == "UPTREND"
        and bos == "BOS_UP"
    ):
        return "BUY"

    if (
        trend == "DOWNTREND"
        and bos == "BOS_DOWN"
    ):
        return "SELL"

    return "HOLD"
