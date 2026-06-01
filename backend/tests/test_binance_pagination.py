from app.data.binance_spot_client import get_klines

batch1 = get_klines(
    symbol="BTCUSDT",
    interval="1h",
    limit=1000,
)

first_open_time = batch1[0][0]

batch2 = get_klines(
    symbol="BTCUSDT",
    interval="1h",
    limit=1000,
    end_time=first_open_time - 1,
)

print("BATCH1 =", len(batch1))
print("BATCH2 =", len(batch2))

print()

print("BATCH1_FIRST =", batch1[0][0])
print("BATCH1_LAST  =", batch1[-1][0])

print()

print("BATCH2_FIRST =", batch2[0][0])
print("BATCH2_LAST  =", batch2[-1][0])
