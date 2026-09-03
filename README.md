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

## Project Structure

```text
API-to-Database-ETL-Pipeline/
│
├── dags/
│   └── air_quality_etl_dag.py
│       → Airflow DAG that orchestrates the complete ETL workflow
│
├── src/
│   ├── extract.py
│   │   → Extracts air-quality data from the REST API
│   │
│   ├── transform.py
│   │   → Cleans and transforms raw API data using Pandas
│   │
│   ├── validate.py
│   │   → Performs data-quality and validation checks
│   │
│   └── load.py
│       → Loads validated data into PostgreSQL
│
├── sql/
│   └── init.sql
│       → Creates the PostgreSQL table and indexes
│
├── tests/
│   └── test_transform.py
│       → Unit tests for transformation logic
│
├── data/
│   → Local data storage (not committed to Git)
│
├── logs/
│   → Local application/Airflow logs
│
├── Dockerfile
│   → Builds the custom Airflow environment
│
├── docker-compose.yml
│   → Runs Airflow and PostgreSQL services
│
├── requirements.txt
│   → Lists the Python dependencies
│
├── .env.example
│   → Template for API and database configuration
│
├── .gitignore
│   → Prevents secrets, logs and temporary files from being committed
│
└── README.md
    → Project documentation and setup instructions
```

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
