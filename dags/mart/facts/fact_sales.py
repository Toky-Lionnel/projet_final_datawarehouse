import pandas as pd

from mart.loaders.mart_loader import (
    load_mart_table
)


def build_fact_sales(engine):

    orders_df = pd.read_sql(
        """
        SELECT *
        FROM staging.stg_orders
        """,
        engine
    )

    customer_dim = pd.read_sql(
        """
        SELECT customer_key, customer_id
        FROM mart.dim_customer
        """,
        engine
    )

    product_dim = pd.read_sql(
        """
        SELECT product_key, product_id
        FROM mart.dim_product
        """,
        engine
    )

    supplier_dim = pd.read_sql(
        """
        SELECT supplier_key, supplier_id
        FROM mart.dim_supplier
        """,
        engine
    )

    region_dim = pd.read_sql(
        """
        SELECT region_key, region_name
        FROM mart.dim_region
        """,
        engine
    )

    # ---------------------------------------------
    # JOIN DIMENSIONS
    # ---------------------------------------------

    fact_df = orders_df.merge(
        customer_dim,
        on="customer_id",
        how="left"
    )

    fact_df = fact_df.merge(
        product_dim,
        on="product_id",
        how="left"
    )

    fact_df = fact_df.merge(
        supplier_dim,
        on="supplier_id",
        how="left"
    )

    fact_df = fact_df.merge(
        region_dim,
        left_on="source_region",
        right_on="region_name",
        how="left"
    )

    # ---------------------------------------------
    # DATE KEY
    # ---------------------------------------------

    fact_df["date_key"] = (
        pd.to_datetime(
            fact_df["order_date"]
        )
        .dt.strftime("%Y%m%d")
        .astype(int)
    )

    # ---------------------------------------------
    # FINAL FACT
    # ---------------------------------------------

    fact_sales = fact_df[
        [
            "order_id",
            "date_key",
            "customer_key",
            "product_key",
            "supplier_key",
            "region_key",
            "quantity",
            "total_amount_usd",
            "amount_usd",
            "supplier_score"
        ]
    ]

    load_mart_table(
        dataframe=fact_sales,
        table_name="fact_sales",
        engine=engine
    )