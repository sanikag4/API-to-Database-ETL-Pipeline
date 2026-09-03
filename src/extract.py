import os
import logging
import requests

logger = logging.getLogger(__name__)

def extract_air_quality():
    url = os.getenv("API_URL", "https://air-quality.p.rapidapi.com/history/airquality")
    headers = {"X-RapidAPI-Key": os.getenv("RAPIDAPI_KEY", ""), "X-RapidAPI-Host": os.getenv("RAPIDAPI_HOST", "air-quality.p.rapidapi.com")}
    params = {"lon": os.getenv("LONGITUDE", "9.188"), "lat": os.getenv("LATITUDE", "45.464")}
    if not headers["X-RapidAPI-Key"]:
        raise ValueError("RAPIDAPI_KEY is not set. Add it to .env before running the pipeline.")
    response = requests.get(url, headers=headers, params=params, timeout=30)
    response.raise_for_status()
    payload = response.json()
    if "data" not in payload or not isinstance(payload["data"], list):
        raise ValueError("Unexpected API response: expected a data list")
    logger.info("Extracted %s records from API", len(payload["data"]))
    return payload["data"]
