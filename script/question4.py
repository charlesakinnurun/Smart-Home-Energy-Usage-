import pandas as pd

# Load the Cleaned data
df = pd.read_csv("datasets/smart_home_cleaned.csv")

# Most frequent used appliances on weekend (Saturday or Sunday)
weekend_df = df[df["day_of_week"].isin(["Saturday","Sunday"])]
print("Most frequently used appliance on weekends")
print(weekend_df["appliance"].mode()[0])