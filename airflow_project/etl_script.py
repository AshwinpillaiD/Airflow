import pandas as pd
from sqlalchemy import text
from db_config import config_db
import os

def fetch_data_from_db():
    query = text("SELECT * FROM sales_data")
    engine = config_db()

    try:
        with engine.connect() as conn:
            result = conn.execute(query)
            df = pd.DataFrame(result.fetchall(), columns=result.keys())

            print(df.head())
            print(f"Fetched {len(df)} rows")

            return df

    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def  writw_data_to_file(df):
	output_dir = '/run/media/ashwin_dev/New_volume/ashwin/airflow_project'
	file_name = 'etl_output.csv'
	file_path = os.path.join(output_dir,file_name)
	df.to_csv(file_path, index=False)
	print(f'data writen to {file_path}')



def etl_process():
	df = fetch_data_from_db()
	writw_data_to_file(df)

if __name__ == "__main__":
	etl_process()
