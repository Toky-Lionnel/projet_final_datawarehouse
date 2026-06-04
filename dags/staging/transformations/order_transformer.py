from sqlalchemy import create_engine

from staging.transformations.orders.orders_extractor import (
    extract_orders
)

from staging.transformations.orders.orders_cleaner import (
    clean_orders
)

from staging.transformations.orders.orders_enricher import (
    join_customers,
    join_products,
    join_suppliers
)

from staging.transformations.orders.payment_enricher import (
    join_payments
)

# from staging.transformations.orders.shipment_enricher import (
#     join_shipments
# )

# from staging.transformations.orders.currency_converter import (
#     convert_currency
# )

from staging.transformations.orders.orders_validator import (
    validate_orders
)

from staging.transformations.orders.orders_loader import (
    load_orders
)

ENGINE = create_engine(
    "postgresql+psycopg2://postgres:postgres@postgres-datawarehouse:5432/worldtrade_dw"
)


def transform_orders():

    df = extract_orders(ENGINE)

    df = clean_orders(df)

    df = join_customers(df, ENGINE)

    df = join_products(df, ENGINE)

    df = join_suppliers(df, ENGINE)

    df = join_payments(df, ENGINE)

    # df = join_shipments(df, ENGINE)

    # df = convert_currency(df, ENGINE)

    df = validate_orders(df)

    load_orders(df, ENGINE)

    print(
        f"Loaded staging.stg_orders "
        f"({len(df)} rows)"
    )