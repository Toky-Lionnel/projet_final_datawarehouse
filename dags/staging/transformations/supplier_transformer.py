import pandas as pd

from sqlalchemy import create_engine
from sqlalchemy import text

ENGINE = create_engine(
    "postgresql+psycopg2://postgres:postgres@postgres-datawarehouse:5432/worldtrade_dw"
)


def load_staging_table(
    dataframe,
    table_name
):

    with ENGINE.begin() as connection:

        connection.execute(
            text(
                """
                CREATE SCHEMA IF NOT EXISTS staging
                """
            )
        )

    dataframe.to_sql(
        name=table_name,
        con=ENGINE,
        schema="staging",
        if_exists="replace",
        index=False
    )


def transform_suppliers():

    # ---------------------------------------------------
    # LOAD BASE SUPPLIERS
    # ---------------------------------------------------
    eu_df = pd.read_sql("SELECT * FROM raw.eu_suppliers", ENGINE)
    us_df = pd.read_sql("SELECT * FROM raw.us_suppliers", ENGINE)
    asia_df = pd.read_sql("SELECT * FROM raw.asia_suppliers", ENGINE)

    # ---------------------------------------------------
    # REGION TAGGING
    # ---------------------------------------------------
    eu_df["source_region"] = "EU"
    us_df["source_region"] = "US"
    asia_df["source_region"] = "ASIA"

    # ---------------------------------------------------
    # CONCAT
    # ---------------------------------------------------
    suppliers_df = pd.concat([eu_df, us_df, asia_df], ignore_index=True)

    # ---------------------------------------------------
    # CLEAN EMAILS & NAMES (Pour des jointures parfaites)
    # ---------------------------------------------------
    if "email" in suppliers_df.columns:
        suppliers_df["email"] = suppliers_df["email"].astype(str).str.lower().str.strip()
        
    # Nettoyage indispensable du nom (supprime les espaces invisibles au début/fin)
    suppliers_df["supplier_name"] = suppliers_df["supplier_name"].astype(str).str.strip()

    # ---------------------------------------------------
    # LOAD & MERGE CSV DATA
    # ---------------------------------------------------
    csv_suppliers_df = pd.read_sql("SELECT * FROM raw.csv_suppliers", ENGINE)
    csv_suppliers_df["supplier_name"] = csv_suppliers_df["supplier_name"].astype(str).str.strip()

    # On ne prend que les colonnes utiles du CSV pour éviter les conflits d'ID
    csv_features = ["supplier_name", "phone", "payment_terms", "annual_volume_usd"]
    
    suppliers_df = suppliers_df.merge(
        csv_suppliers_df[csv_features],
        on="supplier_name",
        how="left"
    )

    # ---------------------------------------------------
    # LOAD & MERGE API SCORE
    # ---------------------------------------------------
    api_score_df = pd.read_sql("SELECT * FROM raw.api_supplier_score", ENGINE)
    api_score_df["name"] = api_score_df["name"].astype(str).str.strip()

    # On cible uniquement les colonnes de scores qui nous intéressent
    api_features = ["name", "on_time_delivery_rate", "quality_score", "cost_competitiveness", "overall_score"]

    # Jointure textuelle : 'supplier_name' (DB) <=> 'name' (API)
    suppliers_df = suppliers_df.merge(
        api_score_df[api_features],
        left_on="supplier_name",
        right_on="name",
        how="left"
    ).drop(columns=["name"]) # On supprime la colonne dupliquée 'name' après la jointure

    # ---------------------------------------------------
    # FILL NULL SCORES
    # ---------------------------------------------------
    # Nettoyage des valeurs manquantes pour les nouveaux scores récupérés de l'API
    score_columns = ["on_time_delivery_rate", "quality_score", "cost_competitiveness", "overall_score"]
    for col in score_columns:
        if col in suppliers_df.columns:
            suppliers_df[col] = suppliers_df[col].fillna(0)

    # ---------------------------------------------------
    # LOAD TO STAGING
    # ---------------------------------------------------
    load_staging_table(
        dataframe=suppliers_df,
        table_name="stg_suppliers"
    )

    print(f"Loaded staging.stg_suppliers ({len(suppliers_df)} rows)")