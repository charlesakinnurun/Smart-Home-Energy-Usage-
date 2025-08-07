import pandas as pd

# Load the Cleaned Data
df = pd.read_csv("datasets/smart_home_cleaned.csv")

# Convert "timestamp" object to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])
 
# How does average appliance usage duration change throughout the day
df["hour"] = df["timestamp"].dt.hour
print("Average appliance usage duration throughout the day")
print(df.groupby("hour")["usage_duration_minutes"].mean().sort_index())