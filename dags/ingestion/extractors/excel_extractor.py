import pandas as pd

from sqlalchemy import create_engine

from ingestion.loaders.loader import (
    load_to_raw_schema
)

DW_ENGINE = create_engine(
    "postgresql+psycopg2://postgres:postgres@postgres-datawarehouse:5432/worldtrade_dw"
)

EXCEL_FILES = {
    "quarterly_targets":
        "/opt/airflow/data/excel/quarterly_targets.xlsx",

    "product_catalog":
        "/opt/airflow/data/excel/product_catalog.xlsx",

    "marketing_budget":
        "/opt/airflow/data/excel/marketing_budget.xlsx"
}


def extract_excel_data():

    for table_name, path in EXCEL_FILES.items():

        df = pd.read_excel(path)

        load_to_raw_schema(
            dataframe=df,
            table_name=f"excel_{table_name}",
            schema="raw",
            engine=DW_ENGINE,
            source_name="excel_files"
        )