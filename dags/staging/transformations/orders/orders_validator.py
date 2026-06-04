def validate_orders(df):

    # ---------------------------------------------
    # REMOVE ORDERS WITHOUT CUSTOMERS
    # ---------------------------------------------

    df = df.dropna(
        subset=["customer_id"]
    )

    # ---------------------------------------------
    # REMOVE NEGATIVE USD
    # ---------------------------------------------

    df = df[df["amount_usd"] >= 0]

    return df