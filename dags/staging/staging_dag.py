from airflow import DAG
from airflow.providers.standard.operators.python import (
    PythonOperator
)

from datetime import datetime

from staging.transformations.customer_transformer import (
    transform_customers
)

from staging.transformations.supplier_transformer import (
    transform_suppliers
)

from staging.transformations.product_transformer import (
    transform_products
)

from staging.transformations.order_transformer import (
    transform_orders
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

    suppliers_task = PythonOperator(
        task_id="transform_suppliers",
        python_callable=transform_suppliers
    )

    products_task = PythonOperator(
        task_id="transform_products",
        python_callable=transform_products
    )

    orders_task = PythonOperator(
        task_id="transform_orders",
        python_callable=transform_orders
    )

    customers_task >> products_task >> suppliers_task >> orders_task