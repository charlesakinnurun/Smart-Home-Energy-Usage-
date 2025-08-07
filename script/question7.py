import pandas as pd

# Load the Cleaned Data
df = pd.read_csv("datasets/smart_home_cleaned.csv")

# Energy consumption on holidays versus non-holidays
print("Average energy consumption on holidays(1) vs non-holidays(0)")
print(df.groupby("holiday")["energy_consumption_kWh"].mean())