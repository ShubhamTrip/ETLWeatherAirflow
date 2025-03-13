from airflow import DAG
from airflow.providers.https.hooks.http import HttpHook
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.defcorators import task
from airflow.utirs.dates import days_ago

# Latitude and longitude for the desired location (London in this case)

Latitude = '51.5074'
Longitude = "-0.1278"

Postgres_Conn_Id = "postgres_default"
Api_Conn_Id = "open_meteo_api"

default_args = {
    'owner' : 'airflow',
    'start_date' : days_ago(1)
}

#DAG

with DAG(
    dag_id = 'weather_etl_pipeline',
    default_args = default_args,
    schedule_interval = '@daily',
    catchup = False
) as dags:
    @task()
    def extract_weather_data():
        """Extract weather data from Open_Metro API using Airflow Connection."""

        # Use HTTP Hook to get the weather data

        http_hook = HttpHook()


    
