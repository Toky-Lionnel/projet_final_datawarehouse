from sqlalchemy import text


def load_orders(df, engine):

    with engine.begin() as connection:

        connection.execute(
            text(
                """
                CREATE SCHEMA IF NOT EXISTS staging
                """
            )
        )

    df.to_sql(
        name="stg_orders",
        con=engine,
        schema="staging",
        if_exists="replace",
        index=False
    )