from app.data.binance_candle_loader import load_candles

from app.market_structure.trend import detect_trend
from app.market_structure.bos import detect_bos

from app.indicators.ema import ema
from app.indicators.rsi import rsi

from app.strategies import trend_bos_strategy

candles = load_candles(
    symbol="BTCUSDT",
    interval="1h",
    limit=100,
)

for i in range(50, len(candles)):

    window = candles[:i]

    signal = trend_bos_strategy.generate_signal(
        window
    )

    if signal is None:
        continue

    print("SIGNAL =", signal)
    print("TREND =", detect_trend(window))
    print("BOS =", detect_bos(window))
    print("EMA20 =", round(ema(window, 20), 2))
    print("EMA50 =", round(ema(window, 50), 2))
    print("RSI14 =", round(rsi(window, 14), 2))

    break
