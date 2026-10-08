import csv
from pathlib import Path


DATA_FILE = Path(__file__).parent / "historical" / "player_stats.csv"


def load_player_data():
    with open(DATA_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        data = []

        for row in reader:
            row["minutes"] = float(row["minutes"])
            row["points"] = float(row["points"])
            row["rebounds"] = float(row["rebounds"])
            row["assists"] = float(row["assists"])
            row["three_pointers"] = float(row["three_pointers"])
            row["usage_rate"] = float(row["usage_rate"])
            row["home"] = int(row["home"])

            data.append(row)

        return data


if __name__ == "__main__":
    games = load_player_data()

    print(f"Loaded {len(games)} games")

    for game in games:
        print(game)