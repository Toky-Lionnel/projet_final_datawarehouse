def load_to_raw_schema(
    dataframe,
    table_name,
    schema,
    engine
):

    dataframe.to_sql(
        name=table_name,
        con=engine,
        schema=schema,
        if_exists="replace",
        index=False
    )

    print(f"Loaded table: {schema}.{table_name}") 