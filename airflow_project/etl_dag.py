from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id='ashwin_doctor_db',
    default_args=default_args,
    description='Simple ETL DAG',
    schedule_interval='*/1 * * * *',
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    run_etl = BashOperator(
        task_id='run_etl',
        bash_command='bash /run/media/ashwin_dev/New_volume/ashwin/airflow_project/wrapper_script.sh'
    )
