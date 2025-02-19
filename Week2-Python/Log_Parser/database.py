import psycopg2
from dotenv import load_dotenv
import os

# Load 
load_dotenv()

class Database:
    def __init__(self):
        self.db_name = os.getenv("DB_NAME")
        self.db_user = os.getenv("DB_USER")
        self.db_password = os.getenv("DB_PASSWORD")
        self.db_host = os.getenv("DB_HOST")
        self.db_port = os.getenv("DB_PORT")

    def get_db_connection(self):
        try:
            connection = psycopg2.connect(
                dbname=self.db_name,
                user=self.db_user,
                password=self.db_password,
                host=self.db_host,
                port=self.db_port
            )
            return connection
        except Exception as e:
            print(f"Error connecting to PostgreSQL database: {e}")
            return None

    def insert_log_data(self, log_data):
        #Inserting the data 
        connection = self.get_db_connection()
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
