import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv(
    "data/ml/btcusdt_dataset.csv"
)

df["trend"] = df["trend"].map(
    {
        "UPTREND": 1,
        "DOWNTREND": -1,
        "RANGE": 0,
        "UNKNOWN": 0,
    }
)

df["bos"] = df["bos"].map(
    {
        "BOS_UP": 1,
        "BOS_DOWN": -1,
        "NO_BOS": 0,
    }
)

features = [
    "close",
    "ema20",
    "ema50",
    "rsi14",
    "trend",
    "bos",
]

X = df[features]

y = df["target"]

X_train, X_test, y_train, y_test = (
    train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        shuffle=True,
    )
)

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
    "TRAIN_ROWS =",
    len(X_train),
)

print(
    "TEST_ROWS =",
    len(X_test),
)

print(
    "ACCURACY =",
    round(
        accuracy * 100,
        2,
    ),
)

print()

for name, importance in zip(
    features,
    model.feature_importances_,
):
    print(
        name,
        "=",
        round(importance, 4),
    )
