import sqlite3
from pathlib import Path


DATABASE_PATH = Path(__file__).parent / "sports.db"


def get_connection():
    return sqlite3.connect(DATABASE_PATH)


def create_tables():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY,
            date TEXT,
            home_team TEXT,
            away_team TEXT,
            home_score INTEGER,
            away_score INTEGER
        )
    """)

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
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            player TEXT,
            market TEXT,
            line REAL,
            projection REAL,
            probability REAL,
            edge REAL,
            prediction TEXT,
            actual REAL,
            result TEXT
        )
    """)

    connection.commit()
    connection.close()


if __name__ == "__main__":
    create_tables()
    print("Database tables created.")