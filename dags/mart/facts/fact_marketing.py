import pandas as pd

from mart.loaders.mart_loader import (
    load_mart_table
)


def build_fact_marketing(engine):

    df = pd.read_sql(
        """
        SELECT *
        FROM raw.excel_marketing_budget
        """,
        engine
    )

    load_mart_table(
        dataframe=df,
        table_name="fact_marketing",
        engine=engine
    )