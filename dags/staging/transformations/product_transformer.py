import pandas as pd

from sqlalchemy import create_engine
from sqlalchemy import text

ENGINE = create_engine(
    "postgresql+psycopg2://postgres:postgres@postgres-datawarehouse:5432/worldtrade_dw"
)


def load_staging_table(
    dataframe,
    table_name
):

    with ENGINE.begin() as connection:

        connection.execute(
            text(
                """
                CREATE SCHEMA IF NOT EXISTS staging
                """
            )
        )

    dataframe.to_sql(
        name=table_name,
        con=ENGINE,
        schema="staging",
        if_exists="replace",
        index=False
    )


def transform_products():

    # ---------------------------------------------------
    # LOAD PRODUCTS
    # ---------------------------------------------------

    eu_df = pd.read_sql(
        "SELECT * FROM raw.eu_products",
        ENGINE
    )

    us_df = pd.read_sql(
        "SELECT * FROM raw.us_products",
        ENGINE
    )

    asia_df = pd.read_sql(
        "SELECT * FROM raw.asia_products",
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

    products_df = pd.concat(
        [
            eu_df,
            us_df,
            asia_df
        ],
        ignore_index=True
    )

    # ---------------------------------------------------
    # CLEAN PRODUCT NAMES
    # ---------------------------------------------------

    products_df["product_name"] = (
        products_df["product_name"]
        .astype(str)
        .str.strip()
    )

    # ---------------------------------------------------
    # LOAD PRODUCT CATALOG
    # ---------------------------------------------------

    catalog_df = pd.read_sql(
        "SELECT * FROM raw.excel_product_catalog",
        ENGINE
    )

    # ---------------------------------------------------
    # MERGE CATALOG
    # ---------------------------------------------------

    products_df = products_df.merge(
        catalog_df,
        on="product_id",
        how="left"
    )

    # ---------------------------------------------------
    # STOCK CLEANING
    # ---------------------------------------------------

    if "stock_quantity" in products_df.columns:

        products_df["stock_quantity"] = (
            products_df["stock_quantity"]
            .fillna(0)
        )

    # ---------------------------------------------------
    # LOAD TO STAGING
    # ---------------------------------------------------

    load_staging_table(
        dataframe=products_df,
        table_name="stg_products"
    )

    print(
        f"Loaded staging.stg_products "
        f"({len(products_df)} rows)"
    )