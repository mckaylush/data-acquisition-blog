import pandas as pd
import glob

# Load BTS file
files = glob.glob("data/bts_raw/*.csv")

if not files:
    print("No BTS files found. Make sure you've downloaded one with fetch_bts.py")
    exit()

df = pd.read_csv(files[0], low_memory=False)

# These are the columns we WANT:
desired_cols = [
    "FlightDate",     # date of flight
    "CRSDepTime",     # scheduled departure time (HHMM)
    "DepTime",        # actual departure time (HHMM)
    "DepDelay",       # departure delay in minutes
    "Origin",         # origin airport
    "Dest"            # destination airport
]

# Filter down to ONLY the available desired columns
available_cols = [c for c in desired_cols if c in df.columns]

df = df[available_cols]

# -------------------------
# Convert CRSDepTime to hour
# -------------------------

def convert_to_hour(x):
    """
    BTS stores time as integers like 1305 → 13:05.
    Here we extract just the hour (13).
    """
    if pd.isna(x):
        return None
    x = str(int(x)).zfill(4)
    return int(x[:2])  # first two digits

df["hour_local"] = df["CRSDepTime"].apply(convert_to_hour)

# drop rows without valid hours
df = df.dropna(subset=["hour_local"])

# rename delay for consistency
df["delay_minutes"] = df["DepDelay"]

# tag the source
df["source"] = "bts"

# keep the final columns
df_final = df[[
    "FlightDate",
    "Origin",
    "Dest",
    "hour_local",
    "delay_minutes",
    "source"
]]

# save cleaned data
df_final.to_csv("data/final_bts.csv", index=False)

print("Saved cleaned BTS → data/final_bts.csv")
print("Rows:", df_final.shape[0])
