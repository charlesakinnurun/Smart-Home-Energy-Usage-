import pandas as pd

# Load the DataFramw
df = pd.read_csv("datasets/smart_home.csv")

# Print the head and info of the DataFrame
print(df.head())
print(df.info())

# Convert the "timestamp" column to datetime objects
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Convert the categorical columns to "category" data type for memory efficiency
categorical_cols = ["occupancy_status","appliance","season","day_of_week"]
for col in categorical_cols:
    df[col] = df[col].astype("category")

# Check for and remove duplicate rows
duplicates_before = df.duplicated().sum()
df.drop_duplicates(inplace=True)
duplicates_after = df.duplicated().sum()

# Print the info of the cleaned dataframe to see the changes
print("DataFrame Info after cleaning")
print(df.info())

# Print the number of duplicates found and removed
print(f"Number of duplicates found: {duplicates_before}")
print(f"Number of duplicates after removal: {duplicates_after}")

# Save the cleaned data to a new CSV file
df.to_csv("datasets/smart_home_cleaned.csv",index=False)
print("Cleaned data saved")