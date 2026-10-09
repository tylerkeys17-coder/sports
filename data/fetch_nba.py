import os
import sqlite3
import requests
from pathlib import Path


API_KEY = os.getenv("SPORTS_API_KEY")

BASE_URL = "https://v1.basketball.api-sports.io"

DATABASE_PATH = (
    Path(__file__).parent / "sports.db"
)


def get_connection():
    return sqlite3.connect(DATABASE_PATH)


def fetch_games(date):

    if not API_KEY:
        raise ValueError(
            "SPORTS_API_KEY is not configured."
        )

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


def save_games(data):

    connection = get_connection()
    cursor = connection.cursor()

    games = data.get("response", [])

    for game in games:

        game_id = game["id"]
        date = game["date"]

        home_team = game["teams"]["home"]["name"]
        away_team = game["teams"]["away"]["name"]

        home_score = game["scores"]["home"]["total"]
        away_score = game["scores"]["away"]["total"]

        cursor.execute(
            """
            INSERT OR REPLACE INTO games (
                id,
                date,
                home_team,
                away_team,
                home_score,
                away_score
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                game_id,
                date,
                home_team,
                away_team,
                home_score,
                away_score
            )
        )

    connection.commit()
    connection.close()

    print(f"Saved {len(games)} games.")


def main():
    from datetime import datetime, timedelta, timezone

    today = datetime.now(timezone.utc).date()

    total_saved = 0

    for offset in range(7):
        date = (today - timedelta(days=offset)).strftime("%Y-%m-%d")

        data = fetch_games(date)
        games = data.get("response", [])

        print(f"{date}: API returned {len(games)} games")

        save_games(data)
        total_saved += len(games)

    print(f"Finished. API returned {total_saved} games across 7 days.")


if __name__ == "__main__":
    main()

 


if __name__ == "__main__":
    main()
