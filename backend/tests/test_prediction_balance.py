import pandas as pd

from sklearn.ensemble import RandomForestClassifier

from app.data.binance_candle_loader import load_candles_large
from app.ml.dataset_builder import build_dataset

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

split_index = int(len(df) * 0.8)

train_df = df.iloc[:split_index]
test_df = df.iloc[split_index:]

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
)

model.fit(
    train_df[features],
    train_df["target"],
)

preds = model.predict(
    test_df[features]
)

buys = int(preds.sum())
sells = len(preds) - buys

print("BUY_PREDICTIONS =", buys)
print("SELL_PREDICTIONS =", sells)

print(
    "BUY_PERCENT =",
    round(buys / len(preds) * 100, 2)
)
