import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------------------
# Load dataset
# -----------------------------------------
df = pd.read_csv("data/final_combined.csv")

print("Dataset shape:", df.shape)
print(df.head())
print(df['source'].value_counts())

# -----------------------------------------
# Basic Summary
# -----------------------------------------
print("\nSummary statistics (delay_minutes):")
print(df["delay_minutes"].describe())

print("\nFlight counts by hour:")
print(df["hour_local"].value_counts().sort_index())

# -----------------------------------------
# Split data by source
# -----------------------------------------
opensky = df[df["source"] == "opensky"]
bts = df[df["source"] == "bts"]

print("\nRows from OpenSky:", opensky.shape[0])
print("Rows from BTS:", bts.shape[0])


# -----------------------------------------
# Plot 1: Flight activity by hour (OpenSky)
# Not as useful due to it only running for a short amount of time
# -----------------------------------------
plt.figure(figsize=(10,5))
opensky["hour_local"].value_counts().sort_index().plot(kind="bar", color="skyblue")
plt.title("Flight Activity by Hour (OpenSky Live Data)")
plt.xlabel("Hour of Day (Local Time)")
plt.ylabel("Number of Aircraft Observed")
plt.tight_layout()
plt.savefig("blog/plots/activity_by_hour_opensky.png")

plt.show()


# -----------------------------------------
# Plot 2: Average delay by hour (BTS)
# -----------------------------------------
hourly_delay = bts.groupby("hour_local")["delay_minutes"].mean()

plt.figure(figsize=(10,5))
hourly_delay.plot(kind="bar", color="salmon")
plt.title("Average Airline Delay by Hour (BTS Historical Data)")
plt.xlabel("Hour of Day (Local Time)")
plt.ylabel("Average Delay (minutes)")
plt.tight_layout()
plt.savefig("blog/plots/average_delay_bts.png")

plt.show()


# -----------------------------------------
# Plot 3: Delay distribution (BTS)
# -----------------------------------------
plt.figure(figsize=(10,5))

filtered = bts[(bts["delay_minutes"] > 0) & (bts["delay_minutes"] <= 500)]

sns.histplot(filtered["delay_minutes"], bins=50, kde=False)

plt.title("Distribution of Airline Delays (BTS) – 1 to 500 Minutes")
plt.xlabel("Delay (minutes)")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("blog/plots/delay_boxplot_bts.png")

plt.show()


# -----------------------------------------
# Plot 4: Boxplot - Delays by Hour (BTS)
# -----------------------------------------
plt.figure(figsize=(12,6))
sns.boxplot(data=bts, x="hour_local", y="delay_minutes")
plt.title("Delay Distribution by Hour (BTS)")
plt.xlabel("Hour of Day")
plt.ylabel("Delay (minutes)")
plt.tight_layout()
plt.savefig("blog/plots/delay_by_hour.png")

plt.show()


# -----------------------------------------
# Plot 5: Comparison of flight activity vs delay side-by-side
# -----------------------------------------

fig, axes = plt.subplots(1, 2, figsize=(14,5))

opensky["hour_local"].value_counts().sort_index().plot(
    kind="bar", color="skyblue", ax=axes[0]
)
axes[0].set_title("Flight Activity by Hour (OpenSky)")
axes[0].set_xlabel("Hour of Day")
axes[0].set_ylabel("Aircraft Count")

hourly_delay.plot(
    kind="bar", color="salmon", ax=axes[1]
)
axes[1].set_title("Average Delay by Hour (BTS)")
axes[1].set_xlabel("Hour of Day")
axes[1].set_ylabel("Avg Delay (minutes)")

plt.tight_layout()
plt.savefig("blog/plots/comparison.png")
plt.show()


# -----------------------------------------
# Print some findings (to help with blog writing)
# -----------------------------------------
print("\n=== QUICK INSIGHTS ===")

peak_activity_hour = opensky["hour_local"].value_counts().idxmax()
print(f"Peak airspace activity hour (OpenSky): {int(peak_activity_hour)}")

peak_delay_hour = hourly_delay.idxmax()
print(f"Worst airline delay hour (BTS): {int(peak_delay_hour)}")

print("\nAverage delay per hour:")
print(hourly_delay)
