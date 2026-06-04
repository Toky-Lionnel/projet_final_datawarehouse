from sqlalchemy import text
from sqlalchemy import create_engine

DW_ENGINE = create_engine(
    "postgresql+psycopg2://postgres:postgres@postgres-datawarehouse:5432/worldtrade_dw"
)


def log_pipeline_event(
    pipeline_name,
    source_name,
    table_name,
    rows_loaded,
    status,
    message,
    execution_time
):

    query = text("""
        INSERT INTO audit.pipeline_logs (
            pipeline_name,
            source_name,
            table_name,
            rows_loaded,
            status,
            message,
            execution_time_seconds
        )
        VALUES (
            :pipeline_name,
            :source_name,
            :table_name,
            :rows_loaded,
            :status,
            :message,
            :execution_time
        )
    """)

    with DW_ENGINE.begin() as connection:

        connection.execute(
            query,
            {
                "pipeline_name": pipeline_name,
                "source_name": source_name,
                "table_name": table_name,
                "rows_loaded": rows_loaded,
                "status": status,
                "message": message,
                "execution_time": execution_time
            }
        )