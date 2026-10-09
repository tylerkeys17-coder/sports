
import csv
import sqlite3
from pathlib import Path

# Project paths
DATA_DIR = Path(__file__).resolve().parent
DB_PATH = DATA_DIR / "sports.db"
OUTPUT_PATH = DATA_DIR / "historical" / "player_stats.csv"

if not DB_PATH.exists():

        raise FileNotFoundError(
            f"Database not found: {DB_PATH}"
        )


OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
with sqlite3.connect(DB_PATH) as conn:
    conn.row_factory = sqlite3.Row
    cursor = conn.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type = 'table'
          AND name = 'player_games'
    """)
    if cursor.fetchone() is None:
        raise RuntimeError("Table 'player_games' does not exist.")
    cursor = conn.execute("""
        SELECT *
        FROM player_games
        ORDER BY game_id, player
    """)
    rows = cursor.fetchall()
    if not rows:
        raise RuntimeError(
            "No player statistics found in the database."
        )
    with open(
        OUTPUT_PATH,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=rows[0].keys()
        )
        writer.writeheader()
        writer.writerows([dict(row) for row in rows])
print(f"Exported {len(rows)} player records.")
print(f"CSV saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    export_player_stats()

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

with sqlite3.connect(DB_PATH) as conn:
    conn.row_factory = sqlite3.Row

    cursor = conn.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type = 'table'
          AND name = 'player_games'
    """)

    if cursor.fetchone() is None:
        raise RuntimeError("Table 'player_games' does not exist.")

    cursor = conn.execute("""
        SELECT *
        FROM player_games
        ORDER BY game_id, player
    """)

    rows = cursor.fetchall()

    if not rows:
        raise RuntimeError(
            "No player statistics found in the database."
        )

    with open(
        OUTPUT_PATH,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=rows[0].keys()
        )
        writer.writeheader()
        writer.writerows([dict(row) for row in rows])

print(f"Exported {len(rows)} player records.")
print(f"CSV saved to: {OUTPUT_PATH}")
