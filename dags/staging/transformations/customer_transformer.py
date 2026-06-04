import pandas as pd

from sqlalchemy import create_engine
from sqlalchemy import text

ENGINE = create_engine(
    "postgresql+psycopg2://postgres:postgres@postgres-datawarehouse:5432/worldtrade_dw"
)


def transform_customers():

    eu_df = pd.read_sql(
        "SELECT * FROM raw.eu_customers",
        ENGINE
    )

    us_df = pd.read_sql(
        "SELECT * FROM raw.us_customers",
        ENGINE
    )

    asia_df = pd.read_sql(
        "SELECT * FROM raw.asia_customers",
        ENGINE
    )

    # ---------------------------------------------------
    # REGION TAGGING
    # ---------------------------------------------------

    eu_df["source_region"] = "EU"
    us_df["source_region"] = "US"
    asia_df["source_region"] = "ASIA"

    # ---------------------------------------------------
    # CONCAT
    # ---------------------------------------------------

    customers_df = pd.concat(
        [
            eu_df,
            us_df,
            asia_df
        ],
        ignore_index=True
    )

    # ---------------------------------------------------
    # EMAIL CLEANING
    # ---------------------------------------------------

    customers_df["email"] = (
        customers_df["email"]
        .astype(str)
        .str.lower()
        .str.strip()
    )

    # ---------------------------------------------------
    # COUNTRY STANDARDIZATION
    # ---------------------------------------------------

    customers_df["country"] = (
        customers_df["country"]
        .replace(
            {
                "US": "United States",
                "USA": "United States",
                "U.S.A": "United States"
            }
        )
    )

    # ---------------------------------------------------
    # REMOVE NULL EMAILS
    # ---------------------------------------------------

    customers_df = customers_df.dropna(
        subset=["email"]
    )

    # ---------------------------------------------------
    # REMOVE DUPLICATES
    # ---------------------------------------------------

    customers_df = customers_df.drop_duplicates(
        subset=["email"]
    )

    # ---------------------------------------------------
    # LOAD TO STAGING
    # ---------------------------------------------------

    with ENGINE.begin() as connection:
        connection.execute(text("CREATE SCHEMA IF NOT EXISTS staging;"))

    # 'replace' va automatiquement faire un DROP TABLE IF EXISTS 
    # puis un CREATE TABLE avant d'insérer les données.
    customers_df.to_sql(
        name="stg_customers",
        con=ENGINE,
        schema="staging",
        if_exists="replace", 
        index=False
    )

    print(
        f"Loaded staging.stg_customers "
        f"({len(customers_df)} rows)"
    )