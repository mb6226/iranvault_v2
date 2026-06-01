import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv(
    "data/ml/btcusdt_dataset.csv"
)

features = [
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

predictions = model.predict(
    X_test,
)

accuracy = accuracy_score(
    y_test,
    predictions,
)

print(
    "ACCURACY =",
    round(
        accuracy * 100,
        2,
    ),
)
