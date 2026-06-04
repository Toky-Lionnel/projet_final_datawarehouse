# import pandas as pd


# def convert_currency(df, engine):

#     rates_df = pd.read_sql(
#         """
#         SELECT *
#         FROM raw.api_exchange_rates
#         """,
#         engine
#     )

#     df = df.merge(
#         rates_df,
#         on="currency",
#         how="left"
#     )

#     df["exchange_rate"] = (
#         df["exchange_rate"]
#         .fillna(1)
#     )

#     df["amount_usd"] = (
#         df["amount"]
#         * df["exchange_rate"]
#     )

#     return df