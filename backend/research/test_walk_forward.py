import pandas as pd

from sklearn.ensemble import RandomForestClassifier

from app.data.binance_candle_loader import (
    load_candles_large,
)

from app.ml.dataset_builder import (
    build_dataset,
)

candles = load_candles_large(
    symbol="BTCUSDT",
    interval="1h",
    total_limit=10000,
)

dataset = build_dataset(
    candles,
    movement_threshold=1000,
)

df = pd.DataFrame(dataset)

features = [
    "close",
    "ema20",
    "ema50",
    "rsi14",
    "ema_spread",
    "price_vs_ema20",
    "candle_range",
]

start_index = 3000

wins = 0
losses = 0

for i in range(start_index, len(df)):

    train_df = df.iloc[:i]

    test_row = df.iloc[i:i+1]

    X_train = train_df[features]
    y_train = train_df["target"]

    X_test = test_row[features]
    y_test = int(
        test_row["target"].iloc[0]
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        n_jobs=-1,
    )

    model.fit(
        X_train,
        y_train,
    )

    prediction = int(
        model.predict(X_test)[0]
    )

    if prediction == y_test:
        wins += 1
    else:
        losses += 1

    if (i - start_index) % 100 == 0:
        print(
            "PROCESSED =",
            i - start_index,
        )

total = wins + losses

print()
print("WINS =", wins)
print("LOSSES =", losses)
print("TOTAL =", total)

print(
    "WIN_RATE =",
    round(
        wins / total * 100,
        2,
    ),
)
