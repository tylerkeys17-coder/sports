from statistics import mean


def project_points(recent_games):

    if not recent_games:
        raise ValueError("No games supplied.")

    points = [
        game["points"]
        for game in recent_games
    ]

    return round(mean(points), 2)


def calculate_edge(
    projection,
    line,
    model_probability,
    market_probability
):

    edge = model_probability - market_probability

    return {
        "projection": projection,
        "line": line,
        "model_probability": round(model_probability, 4),
        "market_probability": round(market_probability, 4),
        "edge": round(edge, 4)
    }