import pandas as pd

# Load the DataFrame 
df = pd.read_csv("datasets/smart_home_cleaned.csv")

# Average energy consumption per hour for each home
print("Average energy consumption per hour for each home (top 5):")
print(df.groupby("home_id")["energy_consumption_kWh"].mean().sort_values(ascending=False))