from statistics import mean


def predict_player_stat(values):
    """
    Basic player-stat prediction.

    values = recent player performances
    """

    if not values:
        raise ValueError("No player data provided")

    projection = mean(values)

    return round(projection, 2)


def probability_over(line, projection, volatility=5):
    """
    Estimates probability of a player going over a betting line.

    This is an initial model.
    We will replace this with a trained ML model later.
    """

    difference = projection - line

    probability = 50 + (difference / volatility) * 10

    probability = max(1, min(99, probability))

    return round(probability, 2)


if __name__ == "__main__":

    recent_games = [
        31,
        24,
        29,
        34,
        22
    ]

    betting_line = 27.5

    projection = predict_player_stat(recent_games)

    probability = probability_over(
        betting_line,
        projection
    )

    print("PLAYER PROJECTION")
    print("------------------")
    print(f"Projection: {projection}")
    print(f"Betting line: {betting_line}")
    print(f"Over probability: {probability}%")