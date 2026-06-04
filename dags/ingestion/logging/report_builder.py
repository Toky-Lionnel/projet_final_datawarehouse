import pandas as pd
from sqlalchemy import create_engine

DW_ENGINE = create_engine(
    "postgresql+psycopg2://postgres:postgres@postgres-datawarehouse:5432/worldtrade_dw"
)


def build_pipeline_report():

    query = """
        SELECT
            pipeline_name,
            source_name,
            table_name,
            rows_loaded,
            status,
            execution_time_seconds,
            created_at
        FROM audit.pipeline_logs
        ORDER BY created_at DESC
        LIMIT 20
    """

    df = pd.read_sql(query, DW_ENGINE)

    return df.to_html(index=False)