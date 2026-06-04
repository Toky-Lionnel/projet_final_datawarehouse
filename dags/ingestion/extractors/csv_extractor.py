import pandas as pd

from sqlalchemy import create_engine

from ingestion.loaders.loader import (
    load_to_raw_schema
)

DW_ENGINE = create_engine(
    "postgresql+psycopg2://postgres:postgres@postgres-datawarehouse:5432/worldtrade_dw"
)

CSV_FILES = {
    "monthly_sales": "/opt/airflow/data/csv/monthly-sales.csv",
    "suppliers": "/opt/airflow/data/csv/suppliers.csv",
    "shipments": "/opt/airflow/data/csv/shipments.csv"
}


def extract_csv_data():

    for table_name, path in CSV_FILES.items():

        df = pd.read_csv(path)

        load_to_raw_schema(
            dataframe=df,
            table_name=f"csv_{table_name}",
            schema="raw",
            engine=DW_ENGINE,
            source_name="csv_files"
        )