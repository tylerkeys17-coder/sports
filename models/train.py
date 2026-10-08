import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error


DATA_FILE = "data/historical/player_stats.csv"


def load_data():

    df = pd.read_csv(DATA_FILE)

    return df


def train_model():

    df = load_data()

    features = [
        "minutes",
        "rebounds",
        "assists",
        "three_pointers",
        "usage_rate",
        "home"
    ]

    target = "points"

    X = df[features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=200,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    error = mean_absolute_error(
        y_test,
        predictions
    )

    print("MODEL TRAINED")
    print("----------------")
    print(f"Mean absolute error: {error:.2f}")

    return model


if __name__ == "__main__":
    train_model()