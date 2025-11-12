# data-acquisition-blog

# Flight Activity & Delay Analysis Using OpenSky and BTS Data

This repository contains a complete data acquisition and exploratory analysis project examining how **time of day influences flight delays and overall airspace activity** in the United States.  

The project combines **live aircraft state data** from the OpenSky Network with **historical airline delay data** from the U.S. Bureau of Transportation Statistics (BTS). This creates a rich dataset suitable for studying flight behavior across multiple time periods.

---

## 📌 Project Question

**How does time of day influence flight delays and flight activity in the United States?**

To answer this, the project compares:

- **Real-time aircraft activity** from OpenSky  
- **Historical airline delays (in minutes)** from BTS  

Both datasets are standardized on an hourly basis, allowing direct comparisons between activity levels and delay patterns.

---

## 📂 Repository Structure
data-acquisition-blog/

- data/
- final_bts.csv -- Cleaned BTS data
- final_flights.csv -- Cleaned OpenSky live data
- final_combined.csv -- Unified final dataset
- other.csv -- Necessary .csv files for data

- src/
- collect_flights.py -- Fetches OpenSky live snapshots
- fetch_bts.py -- Downloads BTS on-time performance ZIP
- clean_bts.py -- Cleans BTS historical data
- clean_flights.py -- Cleans + merges OpenSky + BTS
- eda_flights.py -- Exploratory data analysis script
- blog/
- blog.md # Final blog post 
- .venv/
- I created a virutal machine to work everything
- README.md # This file

---

## 🚀 Data Sources

### **1. OpenSky Network (Live Data)**
- Endpoint: `https://opensky-network.org/api/states/all`
- Data Collected:
  - latitude/longitude
  - velocity
  - timestamps (`time_position`, `last_contact`)
  - derived variables (`hour_local`, `delay_minutes`)
- Used to measure **real-time airspace activity**.

### **2. BTS On-Time Performance (Historical Delays)**
- Source: U.S. DOT Bureau of Transportation Statistics  
- URL pattern:https://transtats.bts.gov/PREZIP/On_Time_Reporting_Carrier_On_Time_Performance_1987_present_YEAR_MONTH.zip
- Contains:
- scheduled departure time (`CRSDepTime`)
- actual departure time (`DepTime`)
- departure delay (`DepDelay`)
- origin/destination airports
- Used to measure **real airline delay patterns** across hours of the day.




