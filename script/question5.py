import pandas as pd

# Load the Cleaned Data
df = pd.read_csv("datasets/smart_home_cleaned.csv")

# Convert the "timestamp" column to datetime objects
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Trend of energy consumption over the months
df["month"] = df["timestamp"].dt.month
print("Trend of energy consumption over the months:")
print(df.groupby("month")["energy_consumption_kWh"].mean().sort_index())