import os
import requests


API_KEY = os.getenv("SPORTS_API_KEY")

BASE_URL = "https://v1.basketball.api-sports.io"


def fetch_games(date):
    if not API_KEY:
        raise ValueError("SPORTS_API_KEY is not configured.")

    response = requests.get(
        f"{BASE_URL}/games",
        headers={
            "x-apisports-key": API_KEY
        },
        params={
            "date": date
        },
        timeout=30
    )

    response.raise_for_status()

    return response.json()


def main():
    data = fetch_games("2026-10-08")

    print("API response received.")

    print(data)


if __name__ == "__main__":
    main()