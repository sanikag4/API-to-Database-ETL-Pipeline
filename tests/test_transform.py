import pandas as pd
from src.transform import transform_data

def test_transform_removes_duplicate_timestamp():
 records=[{"timestamp_local":"2026-01-01 10:00:00","aqi":50,"pm25":10,"pm10":20,"o3":5,"no2":2,"so2":1,"co":100},{"timestamp_local":"2026-01-01 10:00:00","aqi":50,"pm25":10,"pm10":20,"o3":5,"no2":2,"so2":1,"co":100}]
 assert len(transform_data(records))==1
