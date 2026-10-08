def evaluate_predictions(predictions):

    if not predictions:
        return {
            "total": 0,
            "wins": 0,
            "losses": 0,
            "win_rate": 0
        }

    wins = sum(
        1 for prediction in predictions
        if prediction["result"] == "WIN"
    )

    losses = sum(
        1 for prediction in predictions
        if prediction["result"] == "LOSS"
    )

    total = wins + losses

    win_rate = (
        wins / total
        if total > 0
        else 0
    )

    return {
        "total": total,
        "wins": wins,
        "losses": losses,
        "win_rate": round(win_rate, 4)
    }


if __name__ == "__main__":

    example_predictions = [
        {"result": "WIN"},
        {"result": "WIN"},
        {"result": "LOSS"},
        {"result": "WIN"},
    ]

    results = evaluate_predictions(
        example_predictions
    )

    print(results)