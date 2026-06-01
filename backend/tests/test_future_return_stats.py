import pandas as pd

df = pd.read_csv(
    "data/ml/btcusdt_dataset.csv"
)

print(
    "MIN =",
    round(
        df["future_return"].min(),
        2,
    ),
)

print(
    "MAX =",
    round(
        df["future_return"].max(),
        2,
    ),
)

print(
    "MEAN =",
    round(
        df["future_return"].mean(),
        2,
    ),
)

print(
    "STD =",
    round(
        df["future_return"].std(),
        2,
    ),
)

print(
    "UP =",
    (df["target"] == 1).sum(),
)

print(
    "DOWN =",
    (df["target"] == 0).sum(),
)
