from datetime import datetime, timedelta
import sys
sys.path.append("/opt/airflow/src")
from airflow import DAG
from airflow.operators.python import PythonOperator
from src.extract import extract_air_quality
from src.transform import transform_data
from src.validate import validate_data
from src.load import load_to_postgres

def extract_task(**context): context["ti"].xcom_push(key="records", value=extract_air_quality())
def transform_task(**context): context["ti"].xcom_push(key="records", value=transform_data(context["ti"].xcom_pull(task_ids="extract", key="records")).to_json(orient="records"))
def validate_task(**context):
 import pandas as pd
 validate_data(pd.DataFrame.from_json(context["ti"].xcom_pull(task_ids="transform", key="records"), orient="records"))
def load_task(**context):
 import pandas as pd
 load_to_postgres(pd.DataFrame.from_json(context["ti"].xcom_pull(task_ids="transform", key="records"), orient="records"))

default_args={"owner":"data-engineering","retries":2,"retry_delay":timedelta(minutes=2)}
with DAG("air_quality_api_to_postgres", default_args=default_args, start_date=datetime(2026,1,1), schedule="@daily", catchup=False, tags=["etl","api","postgresql"]) as dag:
    extract=PythonOperator(task_id="extract",python_callable=extract_task)
    transform=PythonOperator(task_id="transform",python_callable=transform_task)
    validate=PythonOperator(task_id="validate",python_callable=validate_task)
    load=PythonOperator(task_id="load",python_callable=load_task)
    extract >> transform >> validate >> load
