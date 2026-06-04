import pandas as pd

from mart.loaders.mart_loader import (
    load_mart_table
)


def build_dim_region(engine):

    regions = pd.DataFrame(
        {
            "region_key": [1, 2, 3],
            "region_name": [
                "EU",
                "US",
                "ASIA"
            ]
        }
    )

    load_mart_table(
        dataframe=regions,
        table_name="dim_region",
        engine=engine
    )