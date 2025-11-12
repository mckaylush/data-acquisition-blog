import requests
import pandas as pd
from datetime import datetime
import os

# --- Create data directory if it doesn't exist ---
os.makedirs("data", exist_ok=True)

# --- USA bounding box parameters ---
params = {
    "lamin": 25,     # south
    "lomin": -125,   # west
    "lamax": 49,     # north
    "lomax": -66     # east
}

url = "https://opensky-network.org/api/states/all"

def fetch_flight_data():
    response = requests.get(url, params=params)
    data = response.json()

    if "states" not in data or data["states"] is None:
        print("No flight data returned.")
        return None

    columns = [
        "icao24", "callsign", "origin_country", "time_position", "last_contact",
        "longitude", "latitude", "baro_altitude", "on_ground", "velocity",
        "heading", "vertical_rate", "sensors", "geo_altitude", "squawk",
        "spi", "position_source"
    ]

    df = pd.DataFrame(data["states"], columns=columns)
    return df

def save_with_timestamp(df):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename = f"data/flights_{timestamp}.csv"
    df.to_csv(filename, index=False)
    print(f"Saved: {filename}")

if __name__ == "__main__":
    df = fetch_flight_data()
    if df is not None:
        save_with_timestamp(df)
