from app.domain.candle import Candle

from app.features.feature_builder import (
    build_features,
)

from app.indicators.ema import ema
from app.indicators.rsi import rsi

from app.market_structure.trend import detect_trend
from app.market_structure.bos import detect_bos


def build_dataset(
    candles: list[Candle],
    prediction_horizon: int = 24,
    movement_threshold: float = 1000,
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

        future_return = (
            future_close
            - current_close
        )

        if abs(future_return) < movement_threshold:
            continue

        features = build_features(window)

        if features is None:
            continue

        row = {
            **features,

            "trend": detect_trend(window),

            "bos": detect_bos(window),

            "future_return": future_return,

            "target": int(
                future_return > 0
            ),
        }

        rows.append(row)

    return rows
