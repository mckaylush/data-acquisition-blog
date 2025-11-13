# How Time of Day Influences Flight Delays and Airspace Activity: A Data Story Using OpenSky and BTS Data

## Introduction

Flight delays affect millions of passengers every year, and air traffic patterns play a major role in how the aviation system operates. It is also relevant in today's world with uncertainty caused by the government shutdown and the fast approaching holiday seasons. Now is the perfect time to understand more about what affects our air travel. This project investigates an everyday question:

**How does time of day influence flight delays and overall flight activity in the United States?**

To explore this, I combined:
- **Live aircraft state data** collected throughout the day from the OpenSky Network, and  
- **Historical airline delay data** from the U.S. Bureau of Transportation Statistics (BTS).

This produced a dataset rich enough to highlight both real-time airspace behavior comapared against long-term delay patterns.

---

## Why This Project Matters

- Flight delays are one of the most common frustrations for travelers.  
- Airspace activity varies dramatically throughout the day.  
- Most public data sources only show *one* perspective — but combining live and historical data provides a fuller picture.  

Understanding delays and traffic patterns can help:
- Travelers make better choices  
- Researchers study aviation systems  
- Airlines optimize schedules  

---

## Ethical Data Collection

Both data sources used in this project are **public, ethical, and allowed** for academic use:

### **OpenSky Network**
- Open-access aircraft state information  
- No login/authentication required for state vectors  
- I followed good scraping/API etiquette (rate limiting, light querying)
- Limited to the data collected by the user

### **BTS On-Time Performance**
- Official open government data  
- Public domain  
- Large-scale, highly reliable delay dataset
- Needed for historic data  

---

## How I Gathered the Data

### **1. OpenSky Live Snapshots**
I collected multiple real-time snapshots of aircraft over the United States using: https://opensky-network.org/api/states/all

### **1. OpenSky Live Snapshots**

Each snapshot included thousands of aircraft and variables such as:

- timestamp  
- latitude / longitude  
- speed  
- altitude  

The plan for this is to collect snapshots at different times of the day to capture variation in real-time airspace activity. That way the dataset is constantly being updated and made relevant with fresh new information!

---

### **2. BTS Historical Delay Data**

The BTS On-Time Performance dataset provides millions of flight records, including:

- scheduled departure time  
- actual departure time  
- departure delay (in minutes)  
- origin and destination airport codes  

I downloaded one month of BTS flight records and cleaned the scheduled departure times into a **local hour-of-day** variable.

---

### **3. Combining Datasets**

After cleaning, both data sources were standardized into the following structure:

| hour_local | delay_minutes | source   |
|------------|----------------|----------|
| 14         | 0.52           | opensky  |
| 10         | 22.00          | bts      |

This allowed direct comparison between:

- **live aircraft activity** (OpenSky)  
- **historical flight delays** (BTS)  

---

## Summary of Methods

- Parsed UNIX timestamps from OpenSky  
- Converted all times to local time (America/Denver)  
- Processed BTS `CRSDepTime` (HHMM format) into hour-of-day  
- Created comparable delay measures for both datasets  
- Joined datasets into a single combined CSV  
- Generated visualizations in Python using matplotlib and seaborn  

---

## Exploratory Data Analysis (EDA)

### **Flight Activity by Hour (OpenSky)**

![Flight Activity by Hour (OpenSky)](plots/activity_by_hour_opensky.png)


Key Takeaways:
- This data isn't very useful at the moment, but the longer this blog exists, the more uesful it will become!  
- Live data taken 3 times a day  

---

### **Average Delay by Hour (BTS)**

![Average Delay by Hour (BTS)](plots/average_delay_bts.png)


Key Takeaways:
- There is a sharp increase of time of delays during the early hours of the day especially 3-4AM for all airlines
- After the initial spike, the amount of time drops drastically and follows a steady increase throughout the day before coming to a low around 1 or 2 AM 
- Any “rush hour” delay effects around afternoon/evening especially as other airlines are trying to leave around similar times 

---

### **Delay Distribution**

![Distribution of Airline Delays](plots/delay_by_hour.png)


Key Takeaways:
- Some of the longest delays occur in the morning around 7 or 8 AM.  
- High density of delays between 12 PM - 10 PM
- A good amount of extremely long delays could be caused by weather or other uncontrollable delays  
###### Y - axis should be 0-30 not 0 - 3000
---

### **Delay Variability by Hour (Boxplot)**

![Delay Distribution by Hour (BTS)](plots/delay_boxplot_bts.png)


Key Takeaways:
- Most of the delays are only 1-15 minutes long with very few going longer
- Highly unlikely to get an extreme delay time (100+ minutes)  

---

### **Comparing Activity vs. Delays**

![OpenSky Activity vs BTS Delays](plots/comparison.png)


Key Takeaways:
- Not super helpful at the moment, but allows for us to compare current conditions with historic   
- Will provide good evidence as to the change in air transportation  

---

## Key Findings

- The busiest hours of the day were typically in the late morning and early afternoon, around **10 AM to 2 PM** based on the OpenSky live snapshots.  
- The hours with the highest average delays were clearly **afternoon and evening periods**, especially between **3 PM and 9 PM**, where delay variability and severe disruptions increased sharply.  
- Delay patterns did **not** line up perfectly with the busiest times of day. Even though mid-day had the most aircraft activity, the largest delays occurred later in the afternoon and evening, suggesting that delays accumulate over the course of the day rather than being driven purely by traffic volume.  
- Morning flights tended to be more reliable, with tight, low-delay distributions and very few significant disruptions, while evening flights experienced more variability, higher medians, and more extreme outliers.  
- Real-time airspace activity showed clear **midday peaks**, with aircraft counts rising in the mid to late morning, leveling out around midday, and then falling off into the evening.  


---

## Limitations

- BTS data includes only U.S. domestic airline flights.  
- OpenSky snapshots represent *samples* rather than complete full-day coverage.  
- Real-time activity does not directly measure scheduled flight volume.  
- Derived OpenSky “delay” is a proxy and not an operational airline delay.  

These limitations do not undermine the analysis but provide context for interpretation.

---

## Conclusion

This project demonstrates that **time of day plays a significant role in both airspace activity and flight delays**.  
Combining public aviation datasets provides a fuller picture than relying on a single source.

Future extensions could explore:

- multi-day or seasonal patterns  
- differences by airline or airport  
- weather impacts on delays  
- comparisons between weekdays and weekends  

---

## Resources

- [OpenSky Network API](https://opensky-network.org)  
- [BTS On-Time Performance Database](https://transtats.bts.gov)  
- [Project GitHub Repository](link-to-your-repo)  

---

## Appendix: Code & Reproducibility

All scripts used in this project are located in the `/src` directory:

- `collect_flights.py`  
- `fetch_bts.py`  
- `clean_bts.py`  
- `clean_flights.py`  
- `eda_combined.py`  


