## Introduction
The file smart_home.csv contains simulated data from a smart home environment. The dataset, which has 1 million entries and 10 columns, tracks various metrics over time, including:
* **Energy consumption** for different appliances.
* **Home conditions** such as temperature setting and occupancy status.
* **Contextual information** like the season, day of the week, and whether it was a holiday.
This data could be used to analyze energy usage patterns, identify trends, and understand the relationship between environmental factors and home appliance consumption.
### Data Cleaning
```python
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
```
### Analysis
Here are 10 analytical questions that you can solve using pandas on the smart_home_cleaned.csv dataset:

1. What is the total energy consumption for each appliance?
2. What is the average energy consumption per hour for each home?
3. Which season has the highest average energy consumption?
4. What is the most frequently used appliance on weekends (Saturday and Sunday)?
6. What is the trend of energy consumption over the months? (You can extract the month from the timestamp column).
7. How does average appliance usage duration change throughout the day? (You can extract the hour from the timestamp column).
8. What is the energy consumption on holidays versus non-holidays?
9. Which top 5 homes have the highest total energy consumption?
10. How does occupancy status relate to the average temperature setting?
11. What is the distribution of appliance usage duration? (You could use a histogram for this, or just find the mean, median, and mode).
#### What is the total energy consumption for each appliance?
```python
import pandas as pd

# Load the dataframe
df = pd.read_csv("datasets/smart_home_cleaned.csv")

# Total energy consumption for each appliance
print("Total energy consumption for each appliance")
print(df.groupby("appliance")["energy_consumption_kWh"].sum().sort_values(ascending=False))
```
#### What is the average energy consumption per hour for each home?
```python
import pandas as pd

# Load the DataFrame 
df = pd.read_csv("datasets/smart_home_cleaned.csv")

# Average energy consumption per hour for each home
print("Average energy consumption per hour for each home (top 5):")
print(df.groupby("home_id")["energy_consumption_kWh"].mean().sort_values(ascending=False))
```
#### Which season has the highest average energy consumption?
```python
import pandas as pd

# Load the Cleaned Data
df = pd.read_csv("datasets/smart_home_cleaned.csv")

# Which season has the highest average energy consumption
print("Season with highest average energy consumption:")
print(df.groupby("season")["energy_consumption_kWh"].mean().idxmax())
```
#### What is the most frequently used appliance on weekends (Saturday and Sunday)?
```python
import pandas as pd

# Load the Cleaned data
df = pd.read_csv("datasets/smart_home_cleaned.csv")

# Most frequent used appliances on weekend (Saturday or Sunday)
weekend_df = df[df["day_of_week"].isin(["Saturday","Sunday"])]
print("Most frequently used appliance on weekends")
print(weekend_df["appliance"].mode()[0])
```
#### What is the trend of energy consumption over the months? (You can extract the month from the timestamp column).
```python
import pandas as pd

# Load the Cleaned Data
df = pd.read_csv("datasets/smart_home_cleaned.csv")

# Convert the "timestamp" column to datetime objects
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Trend of energy consumption over the months
df["month"] = df["timestamp"].dt.month
print("Trend of energy consumption over the months:")
print(df.groupby("month")["energy_consumption_kWh"].mean().sort_index())
```
#### How does average appliance usage duration change throughout the day? (You can extract the hour from the timestamp column).
```python
import pandas as pd

# Load the Cleaned Data
df = pd.read_csv("datasets/smart_home_cleaned.csv")

# Convert "timestamp" object to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])
 
# How does average appliance usage duration change throughout the day
df["hour"] = df["timestamp"].dt.hour
print("Average appliance usage duration throughout the day")
print(df.groupby("hour")["usage_duration_minutes"].mean().sort_index())
```
#### What is the energy consumption on holidays versus non-holidays?
```python
import pandas as pd

# Load the Cleaned Data
df = pd.read_csv("datasets/smart_home_cleaned.csv")

# Energy consumption on holidays versus non-holidays
print("Average energy consumption on holidays(1) vs non-holidays(0)")
print(df.groupby("holiday")["energy_consumption_kWh"].mean())
```
#### Which top 5 homes have the highest total energy consumption?
```python
import pandas as pd

# Load the Cleaned Data
df = pd.read_csv("datasets/smart_home_cleaned.csv")

# Top 5 homes with the highest total energy consumption
print("Top 5 homes with the highest total energy_consumption")
print(df.groupby("home_id")["energy_consumption_kWh"].sum().nlargest(5))
```
#### How does occupancy status relate to the average temperature setting?
```python
import pandas as pd

# Load the Cleaned Data
df = pd.read_csv("datasets/smart_home_cleaned.csv")

# How does occupancy status relate to the average temperature setting
print("Average temprature setting by occupancy status")
print(df.groupby("occupancy_status")["temperature_setting_C"].mean())
```
#### What is the distribution of appliance usage duration? (You could use a histogram for this, or just find the mean, median, and mode).
```python
import pandas as pd

# Load the Cleaned Data
df = pd.read_csv("datasets/smart_home_cleaned.csv")

# Distribution of appliance usage duration
print("Distribution (summary statistics) of appliance usage duration")
print(df["usage_duration_minutes"].describe())
```
