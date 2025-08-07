import pandas as pd

# Load the Cleaned Data
df = pd.read_csv("datasets/smart_home_cleaned.csv")

# Which season has the highest average energy consumption
print("Season with highest average energy consumption:")
print(df.groupby("season")["energy_consumption_kWh"].mean().idxmax())