import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def get_connection():
    try:
        conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            host=os.getenv('SUPABASE_HOST'),
            password=os.getenv('SUPABASE_PASS')
        )
        return conn
    except psycopg2.OperationalError as e:
        print("I am unable to connect to the database")
        return None
    
if __name__ == "__main__":
    conn = get_connection()
    print("Connected!")
    if conn:
        conn.close()