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

from ingestion.notifications.mail_sender import (
    send_pipeline_email
)

from ingestion.extractors.api_extractor import (
    extract_api_data
)

from ingestion.extractors.csv_extractor import (
    extract_csv_data
)

from ingestion.extractors.excel_extractor import (
    extract_excel_data
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

    extract_api_task = PythonOperator(
        task_id="extract_api_data",
        python_callable=extract_api_data
    )

    extract_csv_task = PythonOperator(
        task_id="extract_csv_data",
        python_callable=extract_csv_data
    )

    extract_excel_task = PythonOperator(
        task_id="extract_excel_data",
        python_callable=extract_excel_data
    )

    send_email_task = PythonOperator(
        task_id="send_pipeline_email",
        python_callable=send_pipeline_email
    )

    [
        extract_eu_task,
        extract_us_task,
        extract_asia_task,
        extract_api_task,
        extract_csv_task,
        extract_excel_task
    ] >> send_email_task
