import pandas as pd

def add_weather_impact(df, engine):

    weather_df = pd.read_sql(
        """
        SELECT *
        FROM raw.api_weather_impact
        """,
        engine
    )

    return df.merge(
        weather_df,
        on="shipment_id",
        how="left"
    )