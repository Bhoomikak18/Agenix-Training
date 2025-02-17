import psycopg2
from dotenv import load_dotenv
import os

# Load 
load_dotenv()

# Fetch 
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

def get_db_connection():
    """Returns a connection object to PostgreSQL database."""
    try:
        connection = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        return connection
    except Exception as e:
        print(f"Error connecting to PostgreSQL database: {e}")
        return None

def insert_log_data(log_data):
    """Insert parsed log data into PostgreSQL database."""
    connection = get_db_connection()
    if connection is None:
        return

    cursor = connection.cursor()

    
    insert_query = """
    INSERT INTO logs (ip, timestamp, method, url, status_code, bytes, referrer, user_agent)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    """

    for log in log_data:
        cursor.execute(insert_query, (
            log['ip'],
            log['timestamp'],
            log['method'],
            log['url'],
            log['status_code'],
            log['bytes'],
            log['referrer'],
            log['user_agent']
        ))

    connection.commit()
    cursor.close()
    connection.close()
