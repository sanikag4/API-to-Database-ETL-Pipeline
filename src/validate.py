import pandas as pd

def validate_data(df):
    if df.empty: raise ValueError("Validation failed: dataset is empty")
    if df["timestamp_local"].isna().any(): raise ValueError("Validation failed: null timestamps")
    if df["timestamp_local"].duplicated().any(): raise ValueError("Validation failed: duplicate timestamps")
    if ((df["aqi"] < 0) | (df["aqi"] > 500)).any(): raise ValueError("Validation failed: AQI outside 0-500")
    for col in ["pm25","pm10","o3","no2","so2","co"]:
        if (df[col] < 0).any(): raise ValueError(f"Validation failed: negative {col}")
    return True
