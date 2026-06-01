import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier

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

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
)

model.fit(
    X_train,
    y_train,
)

joblib.dump(
    model,
    "models/random_forest.pkl",
)

print(
    "MODEL_SAVED =",
    "models/random_forest.pkl",
)

print(
    "TRAIN_ROWS =",
    len(X_train),
)
