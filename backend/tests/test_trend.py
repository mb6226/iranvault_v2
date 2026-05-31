from datetime import datetime, UTC

from app.domain.candle import Candle
from app.market_structure.trend import detect_trend


def build_uptrend():
    candles = []

    price = 100.0

    for _ in range(30):
        candles.append(
            Candle(
                symbol="BTCUSD",
                timeframe="M1",
                timestamp=datetime.now(UTC),
                open=price,
                high=price + 1,
                low=price - 1,
                close=price,
                volume=100,
            )
        )

        price += 1

    return candles


def main():
    candles = build_uptrend()

    trend = detect_trend(candles)

    print("TREND =", trend)


if __name__ == "__main__":
    main()
