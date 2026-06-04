import pandas as pd


def join_payments(df, engine):

    payments_df = pd.read_sql(
        """
        SELECT *
        FROM raw.eu_payments

        UNION ALL

        SELECT *
        FROM raw.us_payments

        UNION ALL

        SELECT *
        FROM raw.asia_payments
        """,
        engine
    )

    return df.merge(
        payments_df,
        on="order_id",
        how="left"
    )