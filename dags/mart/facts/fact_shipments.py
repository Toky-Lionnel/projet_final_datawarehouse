import pandas as pd

from mart.loaders.mart_loader import (
    load_mart_table
)


def build_fact_shipments(engine):

    df = pd.read_sql(
        """
        SELECT
            order_id,
            shipment_id,
            shipment_status,
            shipment_delay_days,
            weather_impact
        FROM staging.stg_orders
        """,
        engine
    )

    load_mart_table(
        dataframe=df,
        table_name="fact_shipments",
        engine=engine
    )