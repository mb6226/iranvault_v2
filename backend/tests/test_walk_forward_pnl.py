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

gross_profit = 0.0
gross_loss = 0.0

equity = 0.0
peak_equity = 0.0
max_drawdown = 0.0

trade_pnls = []

for i in range(start_index, len(df)):

    train_df = df.iloc[:i]

    test_row = df.iloc[i:i+1]

    X_train = train_df[features]
    y_train = train_df["target"]

    X_test = test_row[features]

    actual = int(
        test_row["target"].iloc[0]
    )

    future_return = float(
        test_row["future_return"].iloc[0]
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

    if prediction == 1:
        pnl = future_return
    else:
        pnl = -future_return

    trade_pnls.append(pnl)

    if pnl > 0:
        wins += 1
        gross_profit += pnl
    else:
        losses += 1
        gross_loss += abs(pnl)

    equity += pnl

    if equity > peak_equity:
        peak_equity = equity

    drawdown = peak_equity - equity

    if drawdown > max_drawdown:
        max_drawdown = drawdown

    if (i - start_index) % 100 == 0:
        print(
            "PROCESSED =",
            i - start_index,
        )

total = wins + losses

profit_factor = (
    gross_profit / gross_loss
    if gross_loss > 0
    else 0
)

expectancy = (
    sum(trade_pnls) / total
    if total > 0
    else 0
)

print()
print("TRADES =", total)
print("WINS =", wins)
print("LOSSES =", losses)

print(
    "WIN_RATE =",
    round(
        wins / total * 100,
        2,
    ),
)

print(
    "NET_PNL =",
    round(equity, 2),
)

print(
    "AVG_PNL =",
    round(expectancy, 2),
)

print(
    "PROFIT_FACTOR =",
    round(profit_factor, 2),
)

print(
    "MAX_DRAWDOWN =",
    round(max_drawdown, 2),
)
