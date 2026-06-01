from app.domain.signal import Signal

from app.ml.predictor import (
    predict_signal,
)


def generate_signal(
    candles,
):

    prediction = predict_signal(
        candles
    )

    if prediction is None:
        return None

    entry_price = candles[-1].close

    if prediction["direction"] == "BUY":

        stop_loss = (
            entry_price * 0.99
        )

        take_profit = (
            entry_price * 1.02
        )

    else:

        stop_loss = (
            entry_price * 1.01
        )

        take_profit = (
            entry_price * 0.98
        )

    return Signal(
        symbol=candles[-1].symbol,
        strategy="ML",
        side=prediction["direction"],
        entry_price=entry_price,
        stop_loss=stop_loss,
        take_profit=take_profit,
        confidence=prediction[
            "confidence"
        ],
    )
