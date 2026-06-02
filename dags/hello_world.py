from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime


# Fonction 1
def dire_bonjour():
    print("Bonjour Lionnel 👋")


# Fonction 2
def afficher_message():
    print("Mon premier DAG fonctionne !")


# Déclaration du DAG
with DAG(
    dag_id="hello_world",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["debutant"]
) as dag:

    # Tâche 1
    task1 = PythonOperator(
        task_id="dire_bonjour",
        python_callable=dire_bonjour
    )

    # Tâche 2
    task2 = PythonOperator(
        task_id="afficher_message",
        python_callable=afficher_message
    )

    # Ordre d'exécution
    task1 >> task2