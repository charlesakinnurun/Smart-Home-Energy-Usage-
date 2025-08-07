import pandas as pd

# Load the Cleaned Data
df = pd.read_csv("datasets/smart_home_cleaned.csv")

# How does occupancy status relate to the average temperature setting
print("Average temprature setting by occupancy status")
print(df.groupby("occupancy_status")["temperature_setting_C"].mean())