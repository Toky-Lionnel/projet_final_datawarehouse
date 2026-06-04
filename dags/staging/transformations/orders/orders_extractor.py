import pandas as pd


def extract_orders(engine):

    eu_df = pd.read_sql(
        "SELECT * FROM raw.eu_orders",
        engine
    )

    us_df = pd.read_sql(
        "SELECT * FROM raw.us_orders",
        engine
    )

    asia_df = pd.read_sql(
        "SELECT * FROM raw.asia_orders",
        engine
    )

    eu_df["source_region"] = "EU"
    us_df["source_region"] = "US"
    asia_df["source_region"] = "ASIA"

    return pd.concat(
        [
            eu_df,
            us_df,
            asia_df
        ],
        ignore_index=True
    )