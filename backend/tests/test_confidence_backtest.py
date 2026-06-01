import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv(
    "data/ml/btcusdt_dataset.csv"
)

features = [
    "close",
    "ema20",
    "ema50",
    "rsi14",
    "ema_spread",
    "price_vs_ema20",
    "candle_range",
]

X = df[features]
y = df["target"]

split_index = int(len(df) * 0.8)

X_train = X.iloc[:split_index]
y_train = y.iloc[:split_index]

X_test = X.iloc[split_index:]
y_test = y.iloc[split_index:]

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
)

model.fit(X_train, y_train)

for threshold in [0.50, 0.60, 0.70, 0.80, 0.90]:

    probs = model.predict_proba(X_test)

    preds = []
    actuals = []

    for i, p in enumerate(probs):

        confidence = max(p)

        if confidence < threshold:
            continue

        preds.append(
            1 if p[1] > p[0] else 0
        )

        actuals.append(
            y_test.iloc[i]
        )

    if not preds:
        print(
            "THRESHOLD =",
            threshold,
            "NO_SIGNALS"
        )
        continue

    accuracy = accuracy_score(
        actuals,
        preds,
    )

    print(
        "THRESHOLD =",
        threshold,
        "SIGNALS =",
        len(preds),
        "ACCURACY =",
        round(
            accuracy * 100,
            2,
        ),
    )
