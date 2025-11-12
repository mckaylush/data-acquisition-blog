import requests
import zipfile
import io
import pandas as pd
import os

# Choose a year & month to download
YEAR = 2023
MONTH = 1   # January

os.makedirs("data/bts_raw", exist_ok=True)

url = f"https://transtats.bts.gov/PREZIP/On_Time_Reporting_Carrier_On_Time_Performance_1987_present_{YEAR}_{MONTH}.zip"

print(f"Downloading BTS data from: {url}")
response = requests.get(url)

if response.status_code != 200:
    print("Download failed:", response.status_code)
    exit()

# Extract ZIP to memory
z = zipfile.ZipFile(io.BytesIO(response.content))
csv_name = z.namelist()[0]

print("Extracting:", csv_name)
z.extract(csv_name, "data/bts_raw")

print("Saved:", f"data/bts_raw/{csv_name}")
