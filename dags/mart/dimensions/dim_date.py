import pandas as pd

from mart.loaders.mart_loader import (
    load_mart_table
)


def build_dim_date(engine):

    orders_df = pd.read_sql(
        """
        SELECT order_date
        FROM staging.stg_orders
        """,
        engine
    )

    dates = pd.to_datetime(
        orders_df["order_date"]
    ).drop_duplicates()

    dim_date = pd.DataFrame()

    dim_date["full_date"] = dates

    dim_date["date_key"] = (
        dim_date["full_date"]
        .dt.strftime("%Y%m%d")
        .astype(int)
    )

    dim_date["year"] = (
        dim_date["full_date"].dt.year
    )

    dim_date["quarter"] = (
        dim_date["full_date"].dt.quarter
    )

    dim_date["month"] = (
        dim_date["full_date"].dt.month
    )

    dim_date["month_name"] = (
        dim_date["full_date"].dt.month_name()
    )

    dim_date["week"] = (
        dim_date["full_date"]
        .dt.isocalendar()
        .week
    )

    dim_date["day"] = (
        dim_date["full_date"].dt.day
    )

    load_mart_table(
        dataframe=dim_date,
        table_name="dim_date",
        engine=engine
    )