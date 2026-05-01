import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

os.makedirs('logs', exist_ok=True)

logging.basicConfig(
    filename='logs/ingestion_db.log',
    level=logging.DEBUG,
    format='%(asctime)s-%(levelname)s-%(message)s',
    filemode='a'
)

engine = create_engine('sqlite:///inventory.db')

def ingest_db(df, table_name, engine):
    df.to_sql(
        table_name,
        con=engine,
        if_exists="replace",
        index=False,
        chunksize=1000
    )

def load_raw_data():
    start = time.time()

    for file in os.listdir('data'):
        if file.endswith('.csv'):
            try:
                file_path = os.path.join('data', file)

                df = pd.read_csv(file_path, encoding='utf-8', low_memory=False)

                table_name = file[:-4].replace(" ", "_").replace("-", "_")

                print(f"\n📂 Processing: {file}")
                print(f"Rows in CSV: {len(df)}")

                ingest_db(df, table_name, engine)

                # Verify insertion
                count = pd.read_sql(f"SELECT COUNT(*) as c FROM '{table_name}'", engine)
                print(f"✅ Rows inserted: {count['c'][0]}")

            except Exception as e:
                print(f"❌ Error in {file}: {e}")
                logging.error(f"Error processing {file}: {e}")

    end = time.time()
    print(f"\n⏱ Total time: {(end-start)/60} minutes")

if __name__ == '__main__':
    load_raw_data()

'''import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

logging.basicConfig(
    filename='logs/ingestion_db.log',
    level=logging.DEBUG,
    fromat='%(asctime)s-%(levelname)s-%(message)s',
    filemode='a'
)
engine=create_engine('sqlite:///inventry.db')

def ingest_db(df,table_name,engine):
    df.to_sql(table_name, con=engine,if_exists="replace",index=False)
def load_raw_data():
    start=time.time()
    for file in os.listdir('data'):
        if '.csv' in file:
            df=pd.read_csv('data/'+file)
            logging.info(f'ingesting{file} in db')
            ingest_db(df,file[:-4],engine)
    end=time.time()
    total_time =(end-start)/60
    logging.info("ingestion complete")
    logging.info(f"total time taken:{total_time} minutes")

if __name__=='__main__':
    load_raw_data()'''
'''import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

logging.basicConfig(
    filename='logs/ingestion_db.log',
    level=logging.DEBUG,
    fromat='%(asctime)s-%(levelname)s-%(message)s',
    filemode='a'
)
engine=create_engine('sqlite:///inventry.db')

def ingest_db(df,table_name,engine):
    df.to_sql(table_name, con=engine,if_exists="replace",index=False)
def load_raw_data():
    start=time.time()
    for file in os.listdir('data'):
        if '.csv' in file:
            df=pd.read_csv('data/'+file)
            logging.info(f'ingesting{file} in db')
            ingest_db(df,file[:-4],engine)
    end=time.time()
    total_time =(end-start)/60
    logging.info("ingestion complete")
    logging.info(f"total time taken:{total_time} minutes")

if __name__=='__main__':
    load_raw_data()(this is code I have to make a databases but whike perfermning oprationag and it execution the whole database is not getting insertered in ingestion.db file
