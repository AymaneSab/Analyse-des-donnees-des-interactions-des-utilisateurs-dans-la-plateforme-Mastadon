from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable
from datetime import datetime, timedelta
import subprocess
import sys

sys.path.insert(0, '/home/hadoop/Mastodon/Scrapping')
from Scrapper import getData

default_args = {
    'owner': 'admin',
    'start_date': datetime(2023, 10, 23),
    'email': ['aymaneestudying@gmail.com'],
    'email_on_failure': True,
    'email_on_success': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}

with DAG('Mastodon_Analysis', default_args=default_args, schedule_interval=None, description='This DAG performs Mastodon analysis.' , tags=['social-media', 'analysis']) as dag:

    def set_data_path(**kwargs):
        reduce_results_path = getData()  # Run the data collection function
        Variable.set("reduce_results_path", reduce_results_path)  # Store the reduce results data path as a variable

    # Create PythonOperator tasks : 
 
    # Scrapp and save mastodon data : 

    retrieve_and_save_mastodon_data_task = PythonOperator(

    task_id = 'retrieve_and_save_mastodon_data',
    provide_context = True,
    python_callable = set_data_path,
    dag = dag,  # Pass the 'dag' variable, not 'DAG'

    )

    # Run map reduce : 

    def run_map_reduce(**kwargs):

        data_path = Variable.get("reduce_results_path")  # Retrieve the reducer results data 

        output_path = '/Mostodon/Raw/' + datetime.now().strftime('%Y-%m-%d/%H-%M') + '_Mastodon.json'

        # Use subprocess to run Hadoop MapReduce job with the provided data path : 

        hadoop_command = f"hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar " \
                         f"-mapper /home/hadoop/Mastodon/MapReduce/mapper.py " \
                         f"-reducer /home/hadoop/Mastodon/MapReduce/reducer.py " \
                         f"-input {data_path} " \
                         f"-output {output_path}"

        subprocess.run(hadoop_command, shell = True)

    run_map_reduce_task = PythonOperator(

        task_id='run_map_reduce',
        provide_context = True,
        python_callable = run_map_reduce,
        dag = dag, 
    )

    retrieve_and_save_mastodon_data_task >> run_map_reduce_task

if __name__ == "__main__":
    dag.cli()

