from app.domain.candle import Candle

from app.indicators.ema import ema
from app.indicators.rsi import rsi

from app.market_structure.trend import detect_trend
from app.market_structure.bos import detect_bos


def build_dataset(
    candles: list[Candle],
    prediction_horizon: int = 24,
) -> list[dict]:

    rows = []

    start = 50

    end = len(candles) - prediction_horizon

    for i in range(start, end):

        window = candles[:i]

        current_close = candles[i].close

        future_close = (
            candles[
                i + prediction_horizon
            ].close
        )

        row = {
            "close": current_close,
            "ema20": ema(window, 20),
            "ema50": ema(window, 50),
            "rsi14": rsi(window, 14),
            "trend": detect_trend(window),
            "bos": detect_bos(window),
            "future_return": (
                future_close
                - current_close
            ),
            "target": int(
                future_close
                > current_close
            ),
        }

        rows.append(row)

    return rows
