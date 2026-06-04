import pandas as pd

from mart.loaders.mart_loader import (
    load_mart_table
)


def build_dim_product(engine):

    df = pd.read_sql(
        """
        SELECT DISTINCT
            product_id,
            product_name_x,
            category_x,
            stock_qty,
            reorder_level AS reorder_threshold,
            supplier_id,
            source_region
        FROM staging.stg_products
        """,
        engine
    )

    df["product_key"] = range(
        1,
        len(df) + 1
    )

    load_mart_table(
        dataframe=df,
        table_name="dim_product",
        engine=engine
    )