from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from ingestion.extractors.postgres_extractor import (
    extract_eu_data,
    extract_asia_data
)

from ingestion.extractors.mysql_extractor import (
    extract_us_data
)

default_args = {
    "owner": "worldtrade",
    "depends_on_past": False,
    "retries": 1
}

with DAG(
    dag_id="raw_ingestion_pipeline",
    default_args=default_args,
    description="Load raw data from source systems into PostgreSQL DW",
    schedule="@daily",
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=["worldtrade", "raw", "etl"]
) as dag:

    extract_eu_task = PythonOperator(
        task_id="extract_eu_data",
        python_callable=extract_eu_data
    )

    extract_us_task = PythonOperator(
        task_id="extract_us_data",
        python_callable=extract_us_data
    )

    extract_asia_task = PythonOperator(
        task_id="extract_asia_data",
        python_callable=extract_asia_data
    )

    [
        extract_eu_task,
        extract_us_task,
        extract_asia_task
    ]