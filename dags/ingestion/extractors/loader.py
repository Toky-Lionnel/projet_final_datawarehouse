import time

from sqlalchemy import text

from ingestion.logging.audit_logger import (
    log_pipeline_event
)


def load_to_raw_schema(
    dataframe,
    table_name,
    schema,
    engine,
    source_name,
    pipeline_name="raw_ingestion_pipeline"
):

    start_time = time.time()

    try:

        # ---------------------------------------------------
        # TRUNCATE TABLE
        # ---------------------------------------------------

        with engine.begin() as connection:

            truncate_query = text(
                f"TRUNCATE TABLE {schema}.{table_name} RESTART IDENTITY"
            )

            connection.execute(truncate_query)

        # ---------------------------------------------------
        # INSERT DATA
        # ---------------------------------------------------

        dataframe.to_sql(
            name=table_name,
            con=engine,
            schema=schema,
            if_exists="append",
            index=False
        )

        execution_time = round(
            time.time() - start_time,
            2
        )

        # ---------------------------------------------------
        # SUCCESS LOG
        # ---------------------------------------------------

        log_pipeline_event(
            pipeline_name=pipeline_name,
            source_name=source_name,
            table_name=table_name,
            rows_loaded=len(dataframe),
            status="SUCCESS",
            message="Table loaded successfully",
            execution_time=execution_time
        )

        print(
            f"Loaded {schema}.{table_name} "
            f"({len(dataframe)} rows)"
        )

    except Exception as error:

        execution_time = round(
            time.time() - start_time,
            2
        )

        # ---------------------------------------------------
        # ERROR LOG
        # ---------------------------------------------------

        log_pipeline_event(
            pipeline_name=pipeline_name,
            source_name=source_name,
            table_name=table_name,
            rows_loaded=0,
            status="FAILED",
            message=str(error),
            execution_time=execution_time
        )

        print(
            f"Error loading {schema}.{table_name}: {error}"
        )

        raise error