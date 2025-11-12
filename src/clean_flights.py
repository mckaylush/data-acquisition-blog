import pandas as pd
import glob
from datetime import datetime

# -------------------------------------------------------
# 1. Load OpenSky live snapshot files
# -------------------------------------------------------

live_files = glob.glob("data/live_*.csv")

live_list = []

for f in live_files:
    df = pd.read_csv(f)

    # Drop rows missing timestamps
    df = df.dropna(subset=["time_position", "last_contact"])

    # Convert timestamps (UTC → local)
    df["time_position_dt"] = pd.to_datetime(
        df["time_position"], unit="s", errors="coerce"
    ).dt.tz_localize("UTC")

    df["time_position_local"] = df["time_position_dt"].dt.tz_convert("America/Denver")
    df["hour_local"] = df["time_position_local"].dt.hour

    # Calculate delay proxy
    df["delay_seconds"] = df["last_contact"] - df["time_position"]
    df["delay_minutes"] = df["delay_seconds"] / 60

    # Keep only standardized columns
    df_live = df[[
        "hour_local",
        "delay_minutes"
    ]].copy()

    df_live["source"] = "opensky"

    live_list.append(df_live)

# Combine all live snapshots
opensky_all = pd.concat(live_list, ignore_index=True) if live_list else pd.DataFrame()

print("Loaded OpenSky rows:", opensky_all.shape[0])


# -------------------------------------------------------
# 2. Load cleaned BTS dataset (from clean_bts.py)
# -------------------------------------------------------

try:
    bts = pd.read_csv("data/final_bts.csv")
    print("Loaded BTS rows:", bts.shape[0])
except:
    print("BTS file not found. Make sure to run fetch_bts.py and clean_bts.py first.")
    bts = pd.DataFrame()


# Make sure BTS has correct columns
if not bts.empty:
    bts_df = bts[["hour_local", "delay_minutes", "source"]].copy()
else:
    bts_df = pd.DataFrame(columns=["hour_local", "delay_minutes", "source"])


# -------------------------------------------------------
# 3. Combine OpenSky + BTS
# -------------------------------------------------------

combined = pd.concat([opensky_all, bts_df], ignore_index=True)

combined.to_csv("data/final_combined.csv", index=False)

print("Saved → data/final_combined.csv")
print("Final combined shape:", combined.shape)
