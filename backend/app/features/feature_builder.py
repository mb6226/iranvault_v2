from app.domain.candle import Candle

from app.indicators.ema import ema
from app.indicators.rsi import rsi


def build_features(
    candles: list[Candle],
) -> dict | None:

    ema20 = ema(candles, 20)
    ema50 = ema(candles, 50)
    rsi14 = rsi(candles, 14)

    if (
        ema20 is None
        or ema50 is None
        or rsi14 is None
    ):
        return None

    previous_rsi = rsi(candles[:-1], 14)

    rsi_slope = 0.0

    if previous_rsi is not None:
        rsi_slope = rsi14 - previous_rsi

    prev_ema20 = ema(candles[:-1], 20)

    ema20_slope = 0.0

    if prev_ema20 is not None:
        ema20_slope = ema20 - prev_ema20

    avg_volume20 = (
        sum(
            c.volume
            for c in candles[-20:]
        ) / 20
    )

    volume_ratio = (
        candles[-1].volume
        / avg_volume20
    )

    close = candles[-1].close

    high = candles[-1].high
    low = candles[-1].low

    return {
        "close": close,
        "ema20": ema20,
        "ema50": ema50,
        "rsi14": rsi14,

        "ema_spread":
        (ema20 - ema50) / close,

        "price_vs_ema20":
        (close - ema20) / close,

        "candle_range":
        (high - low) / close,
        "rsi_slope": rsi_slope,
        "ema20_slope": ema20_slope,
        "volume_ratio": volume_ratio,
    }
