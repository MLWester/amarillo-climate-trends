from datetime import datetime
from meteostat import Daily
import pandas as pd

station_id = '72363'
start = datetime(1944, 1, 1)
end = datetime(2025, 7, 14)

data = Daily(station_id, start, end).fetch()

print("✅ Data shape:", data.shape)
print(data.head())

if not data.empty:
    data.to_csv("amarillo_weather_1994_2024.csv")
    print("✅ CSV saved.")
else:
    print("⚠️ No data returned.")
