from airflow import DAG
from airflow.providers.standard.operators.python import (
    PythonOperator
)

from datetime import datetime

from staging.transformations.customer_transformer import (
    transform_customers
)

with DAG(
    dag_id="staging_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False
) as dag:

    customers_task = PythonOperator(
        task_id="transform_customers",
        python_callable=transform_customers
    )