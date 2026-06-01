import joblib
import pandas as pd

from app.features.feature_builder import (
    build_features,
)


MODEL_PATH = (
    "models/random_forest.pkl"
)

FEATURES = [
    "close",
    "ema20",
    "ema50",
    "rsi14",
    "ema_spread",
    "price_vs_ema20",
    "candle_range",
]

_model = joblib.load(
    MODEL_PATH
)


def predict_signal(
    candles,
):

    features = build_features(
        candles
    )

    if features is None:
        return None

    X = pd.DataFrame(
        [{
            "close": features["close"],
            "ema20": features["ema20"],
            "ema50": features["ema50"],
            "rsi14": features["rsi14"],
            "ema_spread": features["ema_spread"],
            "price_vs_ema20": features["price_vs_ema20"],
            "candle_range": features["candle_range"],
        }]
    )

    probs = _model.predict_proba(
        X
    )[0]

    down_prob = float(
        probs[0]
    )

    up_prob = float(
        probs[1]
    )

    direction = (
        "BUY"
        if up_prob >= down_prob
        else "SELL"
    )

    confidence = max(
        up_prob,
        down_prob,
    )

    if confidence < 0.7:
        return None

    return {
        "direction": direction,
        "confidence": round(
            confidence,
            4,
        ),
        "up_probability": round(
            up_prob,
            4,
        ),
        "down_probability": round(
            down_prob,
            4,
        ),
    }
