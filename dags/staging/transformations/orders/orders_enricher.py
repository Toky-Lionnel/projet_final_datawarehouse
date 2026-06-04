import pandas as pd


def join_customers(df, engine):

    customers_df = pd.read_sql(
        """
        SELECT
            customer_id,
            first_name,
            last_name,
            email
        FROM staging.stg_customers
        """,
        engine
    )

    customers_df["customer_name"] = (
        customers_df["first_name"]
        + " "
        + customers_df["last_name"]
    )

    return df.merge(
        customers_df[
            [
                "customer_id",
                "customer_name",
                "email"
            ]
        ],
        on="customer_id",
        how="left"
    )

def join_products(df, engine):

    products_df = pd.read_sql(
        """
        SELECT
            product_id,
            product_name_x,
            supplier_id,
            category_x
        FROM staging.stg_products
        """,
        engine
    )

    return df.merge(
        products_df,
        on="product_id",
        how="left"
    )

def join_shipments(df, engine):

    shipments_df = pd.read_sql(
        """
        SELECT *
        FROM raw.csv_shipments
        """,
        engine
    )

    return df.merge(
        shipments_df,
        on="order_id",
        how="left"
    )


def join_suppliers(df, engine):

    suppliers_df = pd.read_sql(
        """
        SELECT
            supplier_id,
            supplier_name,
            overall_score AS supplier_score
        FROM staging.stg_suppliers
        """,
        engine
    )

    return df.merge(
        suppliers_df,
        on="supplier_id",
        how="left"
    )