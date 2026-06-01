import pandas as pd

df = pd.read_csv(
    "data/ml/btcusdt_dataset.csv"
)

split_index = int(
    len(df) * 0.8
)

test = df.iloc[split_index:]

wins = (
    test["target"] == 0
).sum()

total = len(test)

print(
    "WIN_RATE =",
    round(
        wins / total * 100,
        2,
    ),
)
