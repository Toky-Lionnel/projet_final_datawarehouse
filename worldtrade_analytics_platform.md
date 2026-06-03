# WorldTrade Analytics Platform

## 1. Présentation du projet

WorldTrade Analytics Platform est un projet complet de Data Engineering et Business Intelligence simulant une entreprise internationale de marketplace B2B opérant dans plusieurs régions du monde.

Le projet centralise des données provenant de plusieurs sources hétérogènes afin de construire un Data Warehouse local permettant l’analyse métier, la visualisation des données et la détection d’anomalies.

---

# 2. Objectifs du projet

Les objectifs principaux sont :

- Consolider les données de plusieurs pays
- Centraliser les ventes, clients, produits et expéditions
- Construire un Data Warehouse local avec PostgreSQL
- Orchestrer les pipelines de données avec Apache Airflow
- Alimenter des dashboards Power BI
- Détecter des anomalies métier
- Simuler une architecture Data moderne réaliste

---

# 3. Stack technologique

| Domaine | Technologie |
|---|---|
| Orchestration | Apache Airflow |
| Data Warehouse | PostgreSQL |
| API JSON | Node.js + Express |
| Visualisation | Power BI |
| Traitement de données | Python + Pandas |
| Sources de données | PostgreSQL / MySQL / CSV / Excel / JSON |
| Containerisation | Docker |
| Administration DB | pgAdmin |
| Versioning | Git |

---

# 4. Architecture globale

```text
                    +------------------+
                    |   APIs JSON      |
                    |  (Node.js)       |
                    +---------+--------+
                              |
                              v
+-----------+       +------------------+       +------------------+
| CSV Files | ----> |                  | ----> |                  |
+-----------+       |                  |       |                  |
                    |     Airflow      |       |   PostgreSQL DW  |
+-----------+       |   Orchestration  | ----> |  Data Warehouse  |
| Excel     | ----> |                  |       |                  |
+-----------+       |                  |       |                  |
                    +------------------+       +---------+--------+
                                                           |
                                                           v
                                                +------------------+
                                                |     Power BI     |
                                                +------------------+
```

---

# 5. Sources de données

## 5.1 Bases de données transactionnelles

### Europe
- PostgreSQL
- Base : worldtrade_eu

### USA
- MySQL
- Base : worldtrade_us

### Asie
- PostgreSQL
- Base : worldtrade_asia

Tables principales :

- customers
- orders
- products
- shipments
- suppliers
- payments

---

## 5.2 API JSON Node.js

L’API Node.js simule des services internes et externes.

### Endpoints

```http
GET /api/exchange-rates
```

```http
GET /api/shipments
```

```http
GET /api/weather-impact
```

```http
GET /api/supplier-score
```

### Exemple JSON

```json
{
  "USD_EUR": 0.91,
  "EUR_MGA": 4870,
  "JPY_USD": 0.0067
}
```

---

## 5.3 Fichiers CSV

Exemples :

- monthly_sales.csv
- suppliers.csv
- shipments.csv

---

## 5.4 Fichiers Excel

Exemples :

- quarterly_targets.xlsx
- product_catalog.xlsx
- marketing_budget.xlsx

---

# 6. Architecture du Data Warehouse

Le Data Warehouse principal utilise PostgreSQL.

Nom de la base :

```text
worldtrade_dw
```

---

# 7. Organisation des schémas PostgreSQL

## Schema raw

Contient les données brutes importées.

Exemples :

- raw.orders_raw
- raw.customers_raw

---

## Schema staging

Contient les données nettoyées et standardisées.

Fonctions :
- suppression des doublons
- validation des formats
- normalisation des dates
- conversion des devises

---

## Schema warehouse

Contient les tables métier optimisées.

Exemples :
- fact_sales
- fact_shipments
- dim_customer
- dim_product

---

## Schema datamart

Contient les tables dédiées à Power BI.

---

## Schema audit

Contient :
- logs ETL
- historique des pipelines
- erreurs
- monitoring

---

# 8. Modélisation dimensionnelle

## 8.1 Tables de dimensions

### dim_customer

| Champ | Description |
|---|---|
| customer_id | Identifiant client |
| country | Pays |
| segment | Segment client |

---

### dim_product

| Champ | Description |
|---|---|
| product_id | Identifiant produit |
| category | Catégorie |
| supplier | Fournisseur |

---

### dim_date

| Champ | Description |
|---|---|
| date | Date |
| month | Mois |
| quarter | Trimestre |
| year | Année |

---

## 8.2 Tables de faits

### fact_sales

| Champ | Description |
|---|---|
| customer_id | Client |
| product_id | Produit |
| revenue_usd | Revenu |
| quantity | Quantité |

---

### fact_shipments

| Champ | Description |
|---|---|
| shipment_id | Expédition |
| delay_days | Retard |
| shipping_cost | Coût |

---

# 9. Pipelines Airflow

## DAG 1 — ingestion_pipeline

Objectif :
Importer toutes les données sources.

Étapes :
1. Extraction PostgreSQL
2. Extraction MySQL
3. Appels API JSON
4. Import CSV
5. Import Excel
6. Chargement dans raw

---

## DAG 2 — cleaning_pipeline

Objectif :
Nettoyer et standardiser les données.

Étapes :
1. Suppression doublons
2. Correction des dates
3. Validation qualité
4. Conversion devises

---

## DAG 3 — warehouse_pipeline

Objectif :
Construire les dimensions et tables de faits.

Étapes :
1. Création dimensions
2. Création facts
3. Mise à jour datamarts

---

## DAG 4 — anomaly_detection

Objectif :
Détecter des anomalies métier.

Détections :
- commandes sans livraison
- marges négatives
- clients dupliqués
- TVA invalides

---

## DAG 5 — reporting_pipeline

Objectif :
Préparer les dashboards et rapports.

Étapes :
1. Refresh tables Power BI
2. Génération rapports
3. Envoi email automatique

---

# 10. Qualité des données

Des contrôles qualité sont intégrés :

```python
if null_percentage > 20:
    fail_pipeline()
```

Contrôles :
- valeurs nulles
- doublons
- devises invalides
- dates incorrectes

---

# 11. Gestion multi-devise

Devises prises en charge :

- USD
- EUR
- GBP
- JPY
- MGA

Les taux de change sont récupérés via API JSON.

---

# 12. Gestion des anomalies

Le système détecte :

- commandes sans expédition
- clients dupliqués
- ventes négatives
- anomalies de transport
- retards excessifs

---

# 13. Dashboards Power BI

## Dashboard exécutif

KPIs :
- chiffre d’affaires global
- croissance
- top pays
- ventes par région

---

## Dashboard logistique

- retards moyens
- transporteurs
- délais livraison
- coûts transport

---

## Dashboard finance

- marges
- TVA
- revenus convertis USD
- ventes par devise

---

## Dashboard qualité

- anomalies
- doublons
- erreurs détectées

---

# 14. Dockerisation

Le projet peut être exécuté entièrement avec Docker Compose.

Services :
- Airflow
- PostgreSQL
- MySQL
- Node.js API
- pgAdmin

Commande :

```bash
docker compose up
```

---

# 15. Structure recommandée du projet

```text
worldtrade-analytics/
│
├── airflow/
├── dags/
├── scripts/
├── api-node/
├── csv/
├── excel/
├── sql/
├── docker/
├── dashboards/
├── docs/
└── docker-compose.yml
```

---

# 16. Compétences démontrées

Ce projet démontre :

- Data Engineering
- ETL / ELT
- Apache Airflow
- PostgreSQL avancé
- APIs REST
- Power BI
- Modélisation dimensionnelle
- Orchestration de pipelines
- Docker
- Qualité des données
- Business Intelligence

---

# 17. Évolutions possibles

Améliorations futures :

- Machine Learning
- Détection de fraude
- Streaming Kafka
- Data Lake
- Déploiement Cloud
- Authentification API
- Monitoring avancé

---

# 18. Conclusion

WorldTrade Analytics Platform est un projet complet de Data Engineering simulant un environnement d’entreprise moderne.

Le projet combine :
- ingestion multi-sources
- orchestration
- transformation de données
- data warehouse
- business intelligence
- monitoring
- qualité des données

Il constitue un excellent projet de portfolio pour démontrer des compétences avancées en Data Engineering et BI.
