import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from app.data.binance_candle_loader import (
    load_candles_large,
)
from app.ml.dataset_builder import (
    build_dataset,
)
from app.ml.csv_exporter import (
    export_dataset,
)

candles = load_candles_large(
    symbol="BTCUSDT",
    interval="1h",
    total_limit=10000,
)

for threshold in [
    500,
    750,
    1000,
    1250,
    1500,
    2000,
]:

    dataset = build_dataset(
        candles,
        movement_threshold=threshold,
    )

    export_dataset(
        dataset,
        "data/ml/temp.csv",
    )

    df = pd.read_csv(
        "data/ml/temp.csv"
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

    predictions = model.predict(
        X_test,
    )

    accuracy = accuracy_score(
        y_test,
        predictions,
    )

    print(
        "THRESHOLD =",
        threshold,
        "ROWS =",
        len(df),
        "ACCURACY =",
        round(
            accuracy * 100,
            2,
        ),
    )
