import pandas as pd

# Load the Cleaned Data
df = pd.read_csv("datasets/smart_home_cleaned.csv")

# Top 5 homes with the highest total energy consumption
print("Top 5 homes with the highest total energy_consumption")
print(df.groupby("home_id")["energy_consumption_kWh"].sum().nlargest(5))