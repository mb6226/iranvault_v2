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
    limit: int = 10,
):

    response = requests.get(
        f"{BASE_URL}/api/v3/klines",
        params={
            "symbol": symbol,
            "interval": interval,
            "limit": limit,
        },
        timeout=10,
    )

    response.raise_for_status()

    return response.json()
