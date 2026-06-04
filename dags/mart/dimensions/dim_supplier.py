import pandas as pd

from mart.loaders.mart_loader import (
    load_mart_table
)


def build_dim_supplier(engine):

    df = pd.read_sql(
        """
        SELECT DISTINCT
            supplier_id,
            supplier_name,
            country,
            overall_score AS supplier_score,
            annual_volume_usd,
            payment_terms,
            source_region
        FROM staging.stg_suppliers
        """,
        engine
    )

    df["supplier_key"] = range(
        1,
        len(df) + 1
    )

    load_mart_table(
        dataframe=df,
        table_name="dim_supplier",
        engine=engine
    )