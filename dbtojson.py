# import mysql.connector
# import json
# from decimal import Decimal
# from datetime import date, datetime

# # ==============================
# # CONFIGURATION
# # ==============================
# DB_CONFIG = {
#     "host": "localhost",
#     "user": "ashwin_dev",
#     "password": "admin@123",
#     "database": "doctor_ka",
#     "port": 3306  #  Fixed: correct port for MySQL (was 5432, which is PostgreSQL)
# }

# TABLE_NAME = "sales_data"
# OUTPUT_FILE = "data.json"

# # ==============================
# # CUSTOM JSON SERIALIZER
# # ==============================
# def json_serializer(obj):
#     """Handle non-serializable types from MySQL."""
#     if isinstance(obj, (Decimal)):
#         return float(obj)
#     if isinstance(obj, (date, datetime)):
#         return obj.isoformat()
#     raise TypeError(f"Type {type(obj)} not serializable")

# # ==============================
# # MAIN FUNCTION
# # ==============================
# def export_db_to_json():
#     conn = None    #  Fixed: initialize to None so finally block is safe
#     cursor = None  #  Fixed: initialize to None so finally block is safe

#     try:
#         conn = mysql.connector.connect(**DB_CONFIG)

#         if conn.is_connected():
#             print(" Connected to database")

#         cursor = conn.cursor(dictionary=True)

#         query = f"SELECT * FROM {TABLE_NAME}"
#         cursor.execute(query)

#         data = cursor.fetchall()
#         print(f" Fetched {len(data)} rows")

#         #  Fixed: use custom serializer to handle Decimal/datetime types
#         with open(OUTPUT_FILE, "w") as f:
#             json.dump(data, f, indent=4, default=json_serializer)

#         print(f" Data saved to {OUTPUT_FILE}")

#     except mysql.connector.Error as err:
#         print(" MySQL Error:", err)

#     except Exception as e:
#         print(" General Error:", e)

#     finally:
#         try:
#             if cursor:
#                 cursor.close()
#             if conn and conn.is_connected():
#                 conn.close()
#                 print(" Connection closed")
#         except:
#             pass

# # ==============================
# # RUN SCRIPT
# # ==============================
# if __name__ == "__main__":
#     export_db_to_json()



import os
from dotenv import load_dotenv
from sqlalchemy import create_engine , text
from urllib.parse import quote_plus
import json
from decimal import Decimal
from datetime import date ,datetime

# Load .env file
load_dotenv()

TABLE_NAME="sales_data"

OUTPUT_FILE ="output.json"


def json_serializer(obj):
    """Handle non-serializable types from MySQL."""
    if isinstance(obj, (Decimal)):
        return float(obj)
    if isinstance(obj, (date, datetime)):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")



def config_db():

    username ="ashwin_dev"
    password ="admin@123"
    host ="localhost"
    port ="5432"
    database="doctor_ka"
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
            cursor = conn.cursor(dictionary=True)

            query = f"SELECT * FROM {TABLE_NAME}"
            cursor.execute(query)
    
            data = cursor.fetchall()
            print(f" Fetched {len(data)} rows")
    
            #  Fixed: use custom serializer to handle Decimal/datetime types
            with open(OUTPUT_FILE, "w") as f:
                json.dump(data, f, indent=4, default=json_serializer)
    
            print(f" Data saved to {OUTPUT_FILE}")

    except Exception as e:
        print("Connection failed!")
        print(e)
        
    return engine


config_db()