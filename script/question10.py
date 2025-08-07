import pandas as pd

# Load the Cleaned Data
df = pd.read_csv("datasets/smart_home_cleaned.csv")

# Distribution of appliance usage duration
print("Distribution (summary statistics) of appliance usage duration")
print(df["usage_duration_minutes"].describe())