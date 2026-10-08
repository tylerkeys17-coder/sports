def predict_points(recent_points):
    if not recent_points:
        return 0

    projection = sum(recent_points) / len(recent_points)

    return round(projection, 2)


player_points = [31, 24, 29, 34, 22]

prediction = predict_points(player_points)

print(f"Projected points: {prediction}")