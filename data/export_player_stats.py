import csv
import sqlite3
from pathlib import Path

# Project paths
DATA_DIR = Path(__file__).resolve().parent
DB_PATH = DATA_DIR / "sports.db"
OUTPUT_PATH = DATA_DIR / "historical" / "player_stats.csv"

def export_player_stats():
    if not DB_PATH.exists():
        raise FileNotFoundError(
            f"Database not found: {DB_PATH}"
        )

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row

        cursor = conn.execute(
            "SELECT name FROM sqlite_master "
            "WHERE type='table' AND name='player_games'"
        )
