from airflow import DAG
from airflow.providers.standard.operators.python import (
    PythonOperator
)

from datetime import datetime

from sqlalchemy import create_engine

from mart.dimensions.dim_date import (
    build_dim_date
)

from mart.dimensions.dim_customer import (
    build_dim_customer
)

from mart.dimensions.dim_supplier import (
    build_dim_supplier
)

from mart.dimensions.dim_product import (
    build_dim_product
)

from mart.dimensions.dim_region import (
    build_dim_region
)

from mart.facts.fact_sales import (
    build_fact_sales
)

# from mart.facts.fact_shipments import (
#     build_fact_shipments
# )

from mart.facts.fact_marketing import (
    build_fact_marketing
)

from mart.facts.fact_targets import (
    build_fact_targets
)

ENGINE = create_engine(
    "postgresql+psycopg2://postgres:postgres@postgres-datawarehouse:5432/worldtrade_dw"
)


with DAG(
    dag_id="mart_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False
) as dag:

    dim_date_task = PythonOperator(
        task_id="build_dim_date",
        python_callable=lambda: build_dim_date(ENGINE)
    )

    dim_customer_task = PythonOperator(
        task_id="build_dim_customer",
        python_callable=lambda: build_dim_customer(ENGINE)
    )

    dim_supplier_task = PythonOperator(
        task_id="build_dim_supplier",
        python_callable=lambda: build_dim_supplier(ENGINE)
    )

    dim_product_task = PythonOperator(
        task_id="build_dim_product",
        python_callable=lambda: build_dim_product(ENGINE)
    )

    dim_region_task = PythonOperator(
        task_id="build_dim_region",
        python_callable=lambda: build_dim_region(ENGINE)
    )

    fact_sales_task = PythonOperator(
        task_id="build_fact_sales",
        python_callable=lambda: build_fact_sales(ENGINE)
    )

    # fact_shipments_task = PythonOperator(
    #     task_id="build_fact_shipments",
    #     python_callable=lambda: build_fact_shipments(ENGINE)
    # )

    fact_marketing_task = PythonOperator(
        task_id="build_fact_marketing",
        python_callable=lambda: build_fact_marketing(ENGINE)
    )

    fact_targets_task = PythonOperator(
        task_id="build_fact_targets",
        python_callable=lambda: build_fact_targets(ENGINE)
    )

    # -------------------------------------------------
    # DEPENDENCIES
    # -------------------------------------------------

    [
        dim_date_task,
        dim_customer_task,
        dim_supplier_task,
        dim_product_task,
        dim_region_task
    ] >> fact_sales_task

    fact_sales_task >> [
        fact_marketing_task,
        fact_targets_task
    ]