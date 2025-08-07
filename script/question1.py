import pandas as pd

# Load the dataframe
df = pd.read_csv("datasets/smart_home_cleaned.csv")

# Total energy consumption for each appliance
print("Total energy consumption for each appliance")
print(df.groupby("appliance")["energy_consumption_kWh"].sum().sort_values(ascending=False))