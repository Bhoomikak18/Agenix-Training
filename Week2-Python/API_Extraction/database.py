import psycopg2
import os
from dotenv import load_dotenv

# Loading from .env
load_dotenv()

# Fetching the configuration values from .env
DB_CONFIG = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
}

class Database:
    def __init__(self, db_config):
        self.db_config = db_config

    def connect_db(self):
        #Connect
        try:
            conn = psycopg2.connect(**self.db_config)
            return conn
        except Exception as e:
            print("Error connecting to the database:", e)
            return None

    def create_table(self):
        #Create
        conn = self.connect_db()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS cat_facts (
                        id SERIAL PRIMARY KEY,
                        fact TEXT NOT NULL,
                        length INTEGER NOT NULL
                    );
                """)
                conn.commit()
                print("Table 'cat_facts' is ready!")
            except Exception as e:
                print("Error creating table:", e)
            finally:
                cursor.close()
                conn.close()

    def store_fact(self, fact, length):
        #Store
        conn = self.connect_db()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO cat_facts (fact, length) VALUES (%s, %s)", (fact, length))
                conn.commit()
                print("Fact saved to database!")
            except Exception as e:
                print("Error inserting data into database:", e)
            finally:
                cursor.close()
                conn.close()
