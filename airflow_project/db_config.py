import os
from dotenv import load_dotenv
from sqlalchemy import create_engine , text
from urllib.parse import quote_plus

# Load .env file
load_dotenv()


def config_db():

    username = "ashwin_dev"
    password = "admin@123"
    host = "localhost"
    port = "5432"
    database = "doctor_ka"

    # Encode password safely (handles @, #, etc.)
    password = quote_plus(password)

    DB_URL = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"


    # Create engine
    engine = create_engine(DB_URL)

    try:
        # Connect to database
        with engine.connect() as conn:
            # Run test query
            result = conn.execute(text("SELECT version();"))
            for row in result:
                print("Connected successfully!")
                print("PostgreSQL Version:", row[0])

    except Exception as e:
        print("Connection failed!")
        print(e)
        
    return engine

#config_db()
