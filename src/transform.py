import logging
import pandas as pd

logger = logging.getLogger(__name__)
REQUIRED = ["timestamp_local", "aqi", "pm25", "pm10", "o3", "no2", "so2", "co"]

def transform_data(records):
    df = pd.DataFrame(records)
    missing = [c for c in REQUIRED if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    df = df.copy()
    df["timestamp_local"] = pd.to_datetime(df["timestamp_local"], errors="coerce")
    numeric = ["aqi", "pm25", "pm10", "o3", "no2", "so2", "co"]
    for col in numeric: df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=["timestamp_local", "aqi"]).drop_duplicates(subset=["timestamp_local"])
    for col in numeric[1:]: df[col] = df[col].fillna(df[col].median())
    df["pm10_pm25_ratio"] = (df["pm10"] / df["pm25"].replace(0, pd.NA)).astype("Float64")
    df["year"] = df["timestamp_local"].dt.year
    df["month"] = df["timestamp_local"].dt.month
    df["day"] = df["timestamp_local"].dt.day
    df["hour"] = df["timestamp_local"].dt.hour
    df["city_name"] = df.get("city_name", "Milan")
    df["country_code"] = df.get("country_code", "IT")
    logger.info("Transformed %s records", len(df))
    return df
