from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime, timedelta

# Define default arguments for the DAG
default_args = {
    'owner': 'Tukaram',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
sparkdag = DAG(
    'mysql_pyspark_sf_usecase_poc',
    default_args=default_args,
    description='Run PySpark job using SparkSubmitOperator every 5 minutes',
    schedule_interval='*/5 * * * *',  # Every 5 minutes
    start_date=datetime(2024, 9, 7),
    catchup=False,  # Prevent backfilling of missed runs
)

# Define the SparkSubmitOperator task
t1 = SparkSubmitOperator(
    task_id='spark_submit_task',
    application='/path/to/pyafsf.py',  # Update path to your PySpark script
    conn_id='connect_spark',  # Airflow connection ID for Spark cluster
    verbose=False,
    jars='/path/to/mysql-connector-java.jar,/path/to/snowflake-jdbc.jar,/path/to/snowflake-ingest-sdk.jar,/path/to/spark-snowflake.jar',
    dag=sparkdag,
)

t1
