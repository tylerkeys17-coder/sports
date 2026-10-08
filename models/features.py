def create_features(games):

    if not games:
        return {}

    points = [game["points"] for game in games]
    rebounds = [game["rebounds"] for game in games]
    assists = [game["assists"] for game in games]
    minutes = [game["minutes"] for game in games]
    usage = [game["usage_rate"] for game in games]

    features = {
        "avg_points": sum(points) / len(points),
        "avg_rebounds": sum(rebounds) / len(rebounds),
        "avg_assists": sum(assists) / len(assists),
        "avg_minutes": sum(minutes) / len(minutes),
        "avg_usage": sum(usage) / len(usage),
        "games": len(games),
    }

    return features