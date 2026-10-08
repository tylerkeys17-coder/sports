import csv
from pathlib import Path

from database import get_connection


DATA_FILE = (
    Path(__file__).parent
    / "historical"
    / "player_stats.csv"
)


def import_player_games():

    connection = get_connection()
    cursor = connection.cursor()

    with open(
        DATA_FILE,
        "r",
        encoding="utf-8",
        newline=""
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            cursor.execute(
                """
                INSERT INTO player_games (
                    game_id,
                    player,
                    team,
                    opponent,
                    minutes,
                    points,
                    rebounds,
                    assists,
                    three_pointers,
                    usage_rate
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    None,
                    row["player"],
                    row["team"],
                    row["opponent"],
                    float(row["minutes"]),
                    float(row["points"]),
                    float(row["rebounds"]),
                    float(row["assists"]),
                    float(row["three_pointers"]),
                    float(row["usage_rate"]),
                )
            )

    connection.commit()
    connection.close()

    print("Player data imported successfully.")


if __name__ == "__main__":
    import_player_games()