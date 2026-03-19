from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()
def get_connection():
    try:
        conn = psycopg2.connect(host=os.getenv("DB_HOST"),
                                dbname=os.getenv("DB_NAME"),
                                user=os.getenv("DB_USER"),
                                password=os.getenv("DB_PASSWORD"),
                                port=os.getenv("DB_PORT"))
        return conn

    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")

# only run this code if I execute this file directly"
if __name__ == "__main__":
    conn = get_connection()
    print("=== Database connection successful ===")
    conn.close()