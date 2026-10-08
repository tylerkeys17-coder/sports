import os
import requests


API_KEY = os.getenv("SPORTS_API_KEY")

BASE_URL = "https://v1.basketball.api-sports.io"


def get_games(date):
    if not API_KEY:
        raise ValueError("SPORTS_API_KEY is not configured.")

    url = f"{BASE_URL}/games"

    headers = {
        "x-apisports-key": API_KEY
    }

    params = {
        "date": date
    }

    response = requests.get(
        url,
        headers=headers,
        params=params,
        timeout=20
    )

    response.raise_for_status()

    return response.json()


if __name__ == "__main__":
    games = get_games("2026-10-08")

    print(games)