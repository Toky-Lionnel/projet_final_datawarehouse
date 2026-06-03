Bases transactionnelles (Europe, USA, Asie)
   ├── customers, orders, products, shipments, payments, suppliers
   │
   └── Chaque commande (orders) est liée à :
        - un client (customers)
        - un produit (products)
        - un fournisseur (suppliers) via le produit
        - un shipment (expédition) via order_id
        - un payment (paiement) via order_id

API Node.js
   ├── /api/exchange-rates  → taux de change pour convertir les devises locales en USD
   ├── /api/shipments       → données d’expédition supplémentaires (complètent les bases)
   ├── /api/weather-impact  → impact météo pour expliquer les retards
   └── /api/supplier-score  → performance des fournisseurs (complète la table suppliers)

Fichiers CSV
   ├── monthly_sales.csv    → agrégats régionaux (peuvent servir à valider les faits)
   ├── suppliers.csv        → informations financières des fournisseurs (annual_volume_usd, payment_terms)
   └── shipments.csv        → détails logistiques (poids, origines/destinations détaillées)

Fichiers Excel
   ├── quarterly_targets.xlsx  → objectifs commerciaux par région/trimestre
   ├── product_catalog.xlsx    → catalogue avec stocks (jointure avec dim_product)
   └── marketing_budget.xlsx   → dépenses marketing par région/mois



| Source principale                | Source secondaire           | Clé de jointure                    | Usage                                    |
|---------------------------------|-----------------------------|------------------------------------|------------------------------------------|
| orders (EU/US/Asia)             | shipments (base)            | order_id                           | Calcul des retards, coûts logistiques    |
| orders                          | payments (base)             | order_id                           | Vérifier les paiements, impayés          |
| products (base)                 | suppliers (base)            | supplier_id                        | Connaître l’origine des produits         |
| products                        | product_catalog.xlsx        | product_name (ou id)               | Enrichir avec stock, seuil de réapprovisionnement |
| suppliers (base)                | suppliers.csv               | supplier_id (ou name)              | Ajouter volume annuel, délais de paiement |
| shipments (base)                | shipments.csv               | order_id (ou shipment_id)          | Ajouter poids, origine/destination texte |
| monthly_sales.csv               | fact_sales (DW)             | year, month, region                | Contrôle de cohérence                    |
| exchange_rates (API)            | fact_sales                  | date, currency                     | Conversion en USD                        |
| supplier_score (API)            | dim_supplier                | supplier_id                        | Score de performance                     |
| marketing_budget.xlsx           | fact_sales                  | region, month                      | Analyse ROI (coût marketing vs ventes)   |
| quarterly_targets.xlsx          | dim_date, fact_sales        | region, quarter                    | Suivi des objectifs                      |