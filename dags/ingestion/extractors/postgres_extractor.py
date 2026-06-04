import pandas as pd
from sqlalchemy import create_engine

from ingestion.loaders.loader import load_to_raw_schema

SOURCE_TABLES = [
    "customers",
    "orders",
    "products",
    "shipments"
]

DW_SCHEMA = "raw"


def extract_eu_data():

    source_engine = create_engine(
        "postgresql+psycopg2://postgres:postgres@postgres-datawarehouse:5432/worldtrade_eu"
    )

    dw_engine = create_engine(
        "postgresql+psycopg2://postgres:postgres@postgres-datawarehouse:5432/worldtrade_dw"
    )

    for table in SOURCE_TABLES:

        query = f"SELECT * FROM {table}"

        df = pd.read_sql(query, source_engine)

        load_to_raw_schema(
            dataframe=df,
            table_name=f"eu_{table}",
            schema=DW_SCHEMA,
            engine=dw_engine,
            source_name="EU Database"
        )


def extract_asia_data():

    source_engine = create_engine(
        "postgresql+psycopg2://postgres:postgres@postgres-datawarehouse:5432/worldtrade_asia"
    )

    dw_engine = create_engine(
        "postgresql+psycopg2://postgres:postgres@postgres-datawarehouse:5432/worldtrade_dw"
    )

    for table in SOURCE_TABLES:

        query = f"SELECT * FROM {table}"

        df = pd.read_sql(query, source_engine)

        load_to_raw_schema(
            dataframe=df,
            table_name=f"asia_{table}",
            schema=DW_SCHEMA,
            engine=dw_engine,
            source_name="Asia Database"
        )