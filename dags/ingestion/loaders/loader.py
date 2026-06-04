import time

from sqlalchemy import text
from sqlalchemy import inspect

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

    full_table_name = f"{schema}.{table_name}"

    try:

        inspector = inspect(engine)

        table_exists = inspector.has_table(
            table_name,
            schema=schema
        )

        # ---------------------------------------------------
        # TABLE EXISTS
        # ---------------------------------------------------

        if table_exists:

            with engine.begin() as connection:

                truncate_query = text(
                    f"""
                    TRUNCATE TABLE
                    {full_table_name}
                    RESTART IDENTITY
                    """
                )

                connection.execute(truncate_query)

            print(f"Truncated {full_table_name}")

        # ---------------------------------------------------
        # TABLE DOES NOT EXIST
        # ---------------------------------------------------

        else:

            print(f"Creating table {full_table_name}")

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
            f"Loaded {full_table_name} "
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
            f"Error loading {full_table_name}: {error}"
        )

        raise error