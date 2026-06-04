import pandas as pd

from mart.loaders.mart_loader import (
    load_mart_table
)


def build_dim_customer(engine):

    df = pd.read_sql(
        """
        SELECT DISTINCT
            customer_id,
            first_name,
            last_name,
            email,
            country,
            city,
            source_region
        FROM staging.stg_customers
        """,
        engine
    )

    df["customer_key"] = range(
        1,
        len(df) + 1
    )

    df["customer_name"] = (
        df["first_name"]
        + " "
        + df["last_name"]
    )

    load_mart_table(
        dataframe=df,
        table_name="dim_customer",
        engine=engine
    )