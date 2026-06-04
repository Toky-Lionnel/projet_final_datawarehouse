def clean_orders(df):

    # ---------------------------------------------
    # CLEAN CURRENCY
    # ---------------------------------------------

    df["currency"] = (
        df["currency"]
        .astype(str)
        .str.upper()
        .str.strip()
    )

    # ---------------------------------------------
    # CONVERT DATES
    # ---------------------------------------------

    df["order_date"] = (
        df["order_date"]
        .astype("datetime64[ns]")
    )

    # ---------------------------------------------
    # REMOVE INVALID AMOUNTS
    # ---------------------------------------------

    df = df[df["total_amount_usd"] > 0]

    return df