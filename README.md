# API-to-Database ETL Pipeline

A portfolio-ready data engineering project that extracts air-quality data from a REST API, transforms and validates it with Python/Pandas, and loads it into PostgreSQL. Apache Airflow orchestrates the daily pipeline with retries and logging, and Docker provides a reproducible local environment.

## Architecture
REST API → Python/Requests → Pandas → Validation → PostgreSQL

Airflow manages: Extract → Transform → Validate → Load

## Tech Stack
- Python, Requests, Pandas
- PostgreSQL
- Apache Airflow
- Docker / Docker Compose
- SQLAlchemy / psycopg2
- Pytest

## Setup
1. Copy `.env.example` to `.env`.
2. Put your RapidAPI key in `.env`.
3. Run `docker compose build`.
4. Run `docker compose up -d`.
5. Open Airflow at `http://localhost:8080` (admin/admin).
6. Enable/run `air_quality_api_to_postgres` from the DAGs page.

## Data quality
The pipeline checks required columns, removes duplicate timestamps, handles invalid numeric values, rejects an empty dataset, validates AQI 0–500, and rejects negative pollutant concentrations. Airflow retries failed tasks twice with a two-minute delay.

## Important
Do not commit `.env` or your real API key. This repository intentionally does not contain credentials.
