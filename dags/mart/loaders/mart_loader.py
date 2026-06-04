from sqlalchemy import text


def load_mart_table(
    dataframe,
    table_name,
    engine
):

    with engine.begin() as connection:

        connection.execute(
            text(
                """
                CREATE SCHEMA IF NOT EXISTS mart
                """
            )
        )

    dataframe.to_sql(
        name=table_name,
        con=engine,
        schema="mart",
        if_exists="replace",
        index=False
    )

    print(
        f"Loaded mart.{table_name}"
    )