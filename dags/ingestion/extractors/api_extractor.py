import pandas as pd
import requests

from sqlalchemy import create_engine

from ingestion.loaders.loader import (
    load_to_raw_schema
)

DW_ENGINE = create_engine(
    "postgresql+psycopg2://postgres:postgres@postgres-datawarehouse:5432/worldtrade_dw"
)

BASE_URL = "http://node-api:3000/api"

API_ENDPOINTS = {
    "exchange_rates": "/exchange-rates",
    "shipments": "/shipments",
    "weather_impact": "/weather-impact",
    "supplier_score": "/supplier-score"
}


def convert_json_to_dataframe(data):

    # ---------------------------------------------------
    # CASE 1 : LIST
    # ---------------------------------------------------

    if isinstance(data, list):

        return pd.DataFrame(data)

    # ---------------------------------------------------
    # CASE 2 : DICTIONARY
    # ---------------------------------------------------

    elif isinstance(data, dict):

        return pd.json_normalize(data)

    # ---------------------------------------------------
    # CASE 3 : INVALID FORMAT
    # ---------------------------------------------------

    else:

        raise Exception(
            f"Unsupported JSON format: {type(data)}"
        )


def extract_api_data():

    for table_name, endpoint in API_ENDPOINTS.items():

        url = f"{BASE_URL}{endpoint}"

        print(f"Calling API: {url}")

        response = requests.get(url)

        response.raise_for_status()

        data = response.json()

        print(f"JSON returned: {data}")

        df = convert_json_to_dataframe(data)

        print(df.head())

        load_to_raw_schema(
            dataframe=df,
            table_name=f"api_{table_name}",
            schema="raw",
            engine=DW_ENGINE,
            source_name="node_api"
        )