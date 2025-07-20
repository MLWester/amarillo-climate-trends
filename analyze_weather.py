import pandas as pd

# Load raw data
df = pd.read_csv("amarillo_weather_1994_2024.csv", parse_dates=["time"])

# Display initial info
print("\nLoaded DataFrame:")
print(df.head())

print(f"\nShape: {df.shape}")

print("\nColumn Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isna().sum())

# Define essential columns we require for analysis
essential_columns = ['tavg', 'tmin', 'tmax', 'prcp', 'snow', 'pres', 'wspd']

# Drop only rows missing any of the essential columns
clean_df = df.dropna(subset=essential_columns)

# Save cleaned file
clean_df.to_csv("amarillo_weather_cleaned.csv", index=False)

print(f"\nCleaned data saved. New shape: {clean_df.shape}")
