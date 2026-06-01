from app.data.binance_candle_loader import load_candles

from app.market_structure.trend import detect_trend
from app.market_structure.bos import detect_bos

from app.indicators.ema import ema
from app.indicators.rsi import rsi

candles = load_candles(
    symbol="BTCUSDT",
    interval="1h",
    limit=500,
)

buys = 0
sells = 0

for i in range(50, len(candles)):

    window = candles[:i]

    trend = detect_trend(window)

    bos = detect_bos(window)

    ema20 = ema(window, 20)

    ema50 = ema(window, 50)

    rsi14 = rsi(window, 14)

    if (
        trend == "UPTREND"
        and bos == "BOS_UP"
        and ema20 is not None
        and ema50 is not None
        and ema20 > ema50
        and rsi14 is not None
        and rsi14 > 55
    ):
        buys += 1

    if (
        trend == "DOWNTREND"
        and bos == "BOS_DOWN"
        and ema20 is not None
        and ema50 is not None
        and ema20 < ema50
        and rsi14 is not None
        and rsi14 < 45
    ):
        sells += 1

print("BUYS =", buys)
print("SELLS =", sells)
print("TOTAL =", buys + sells)
