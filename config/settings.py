import os

SPORTS_API_KEY = os.getenv("SPORTS_API_KEY")

SPORT = "basketball_nba"

DATA_SOURCE = "sports_api"

if not SPORTS_API_KEY:
    print("WARNING: SPORTS_API_KEY is not configured.")