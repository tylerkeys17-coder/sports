
import os
import sqlite3
import requests
from pathlib import Path

API_KEY = os.getenv("SPORTS_API_KEY")
BASE_URL = "https://v1.basketball.api-sports.io"

DATABASE_PATH = Path(__file__).parent / "sports.db"


def get_connection():
    return sqlite3.connect(DATABASE_PATH)


def fetch_player_stats(game_id):
    if not API_KEY:
        raise ValueError("SPORTS_API_KEY is not configured.")

    
    response = requests.get(
        f"{BASE_URL}/games/statistics/players",
        headers={"x-apisports-key": API_KEY},
        params={"id": game_id},
        timeout=30,
    )

    response.raise_for_status()
    data = response.json()

    if data.get("errors"):
        raise ValueError(f"API error: {data['errors']}")

    return data.get("response", [])



def save_player_stats(game_id, stats):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS player_games (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            game_id INTEGER,
            player TEXT,
            team TEXT,
            opponent TEXT,
            minutes REAL,
            points REAL,
            rebounds REAL,
            assists REAL,
            three_pointers REAL,
            usage_rate REAL
        )
    """)

    cursor.execute("""
        CREATE UNIQUE INDEX IF NOT EXISTS
        idx_player_games_unique
        ON player_games (game_id, player, team)
    """)

    
    saved = 0

    # Find the two teams involved in this game
    team_ids = []
    for item in stats:
        team_info = item.get("team") or {}
        team_id = team_info.get("id")
        if team_id is not None and team_id not in team_ids:
            team_ids.append(team_id)

    for item in stats:
        player_info = item.get("player") or {}
        team_info = item.get("team") or {}
        player_name = player_info.get("name")
        team_id = team_info.get("id")

        if not player_name or team_id is None:
            continue

        opponent_id = next(
            (tid for tid in team_ids if tid != team_id),
            None,
        )

        minutes_value = item.get("minutes")
        minutes = None
        if isinstance(minutes_value, str) and ":" in minutes_value:
            parts = minutes_value.split(":")
            minutes = int(parts[0]) + int(parts[1]) / 60
        elif minutes_value not in (None, ""):
            try:
                minutes = float(minutes_value)
            except (ValueError, TypeError):
                minutes = None

        rebounds_info = item.get("rebounds") or {}
        threes_info = item.get("threepoint_goals") or {}

        rebounds = (
            rebounds_info.get("total")
            if isinstance(rebounds_info, dict)
            else rebounds_info
        )
        threes = (
            threes_info.get("total")
            if isinstance(threes_info, dict)
            else threes_info
        )

        cursor.execute("""
            INSERT INTO player_games (
                game_id, player, team, opponent,
                minutes, points, rebounds, assists,
                three_pointers, usage_rate
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(game_id, player, team) DO UPDATE SET
                opponent = excluded.opponent,
                minutes = excluded.minutes,
                points = excluded.points,
                rebounds = excluded.rebounds,
                assists = excluded.assists,
                three_pointers = excluded.three_pointers,
                usage_rate = excluded.usage_rate
        """, (
            game_id,
            player_name,
            str(team_id),
            str(opponent_id) if opponent_id is not None else None,
            minutes,
            item.get("points"),
            rebounds,
            item.get("assists"),
            threes,
            None,
        ))

        saved += 1

    connection.commit()
    connection.close()
    return saved


def main():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id FROM games
        WHERE home_score IS NOT NULL
        AND away_score IS NOT NULL
    """)

    game_ids = [row[0] for row in cursor.fetchall()]
    connection.close()

    print(f"Found {len(game_ids)} completed games.")

    total = 0

    for game_id in game_ids:
        try:
            stats = fetch_player_stats(game_id)
            saved = save_player_stats(game_id, stats)
            total += saved
            print(f"Game {game_id}: saved {saved} player records.")

        except Exception as error:
            print(f"Game {game_id} failed: {error}")

    print(f"Finished. Processed {total} player records.")


if __name__ == "__main__":
    main()
