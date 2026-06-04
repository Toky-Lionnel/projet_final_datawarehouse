import pandas as pd

def join_suppliers(df, engine):

    suppliers_df = pd.read_sql(
        """
        SELECT
            supplier_id,
            supplier_name,
            supplier_score
        FROM staging.stg_suppliers
        """,
        engine
    )

    return df.merge(
        suppliers_df,
        on="supplier_id",
        how="left"
    )