import requests


BASE_URL = "https://api.binance.com"


def get_server_time():

    response = requests.get(
        f"{BASE_URL}/api/v3/time",
        timeout=10,
    )

    response.raise_for_status()

    return response.json()


def get_klines(
    symbol: str,
    interval: str,
    limit: int = 1000,
    start_time: int | None = None,
    end_time: int | None = None,
):

    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit,
    }

    if start_time is not None:
        params["startTime"] = start_time

    if end_time is not None:
        params["endTime"] = end_time

    response = requests.get(
        f"{BASE_URL}/api/v3/klines",
        params=params,
        timeout=10,
    )

    response.raise_for_status()

    return response.json()
