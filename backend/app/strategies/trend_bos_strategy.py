from app.domain.candle import Candle
from app.domain.signal import Signal

from app.market_structure.trend import detect_trend
from app.market_structure.bos import detect_bos
from app.market_structure.swing import (
    swing_low,
    swing_high,
)

from app.indicators.ema import ema
from app.indicators.rsi import rsi


def generate_signal(
    candles: list[Candle],
) -> Signal | None:

    trend = detect_trend(candles)

    bos = detect_bos(candles)

    ema20 = ema(candles, 20)

    ema50 = ema(candles, 50)

    rsi14 = rsi(candles, 14)

    sl_low = swing_low(candles, 10)

    sl_high = swing_high(candles, 10)

    last_close = candles[-1].close

    if (
        trend == "UPTREND"
        and bos == "BOS_UP"
        and ema20 is not None
        and ema50 is not None
        and ema20 > ema50
        and rsi14 is not None
        and rsi14 > 55
    ):
        return Signal(
            symbol=candles[-1].symbol,
            strategy="TREND_BOS",
            side="BUY",
            entry_price=last_close,
            stop_loss=sl_low,
            take_profit=last_close + (
                (last_close - sl_low) * 2
            ),
            confidence=0.7,
        )

    if (
        trend == "DOWNTREND"
        and bos == "BOS_DOWN"
        and ema20 is not None
        and ema50 is not None
        and ema20 < ema50
        and rsi14 is not None
        and rsi14 < 45
    ):
        return Signal(
            symbol=candles[-1].symbol,
            strategy="TREND_BOS",
            side="SELL",
            entry_price=last_close,
            stop_loss=sl_high,
            take_profit=last_close - (
                (sl_high - last_close) * 2
            ),
            confidence=0.7,
        )

    return None
