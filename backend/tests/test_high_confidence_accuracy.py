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

split_index = int(
    len(df) * 0.8
)

X_train = X.iloc[:split_index]
y_train = y.iloc[:split_index]

X_test = X.iloc[split_index:]
y_test = y.iloc[split_index:]

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
)

model.fit(
    X_train,
    y_train,
)

probs = model.predict_proba(X_test)

selected_preds = []
selected_true = []

for i, p in enumerate(probs):

    up_prob = p[1]

    if up_prob >= 0.70:
        selected_preds.append(1)
        selected_true.append(y_test.iloc[i])

    elif up_prob <= 0.30:
        selected_preds.append(0)
        selected_true.append(y_test.iloc[i])

if len(selected_preds) == 0:
    print("NO SIGNALS")
else:
    accuracy = accuracy_score(
        selected_true,
        selected_preds,
    )

    print("SIGNALS =", len(selected_preds))
    print(
        "ACCURACY =",
        round(
            accuracy * 100,
            2,
        ),
    )
