import psycopg2
from db import get_connection

def create_tables():
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS complaints (
                odi_number INT PRIMARY KEY,
                model VARCHAR(20)
                date_of_incident DATE, 
                date_complaint_filed DATE,
                components VARCHAR(40),
                summary TEXT,
                crash BOOLEAN,
                fire BOOLEAN,
                number_of_injuries INT,
                number_of_deaths INT
            )
        """)
    
        conn.commit()
        print("Table 'complaints' created successfully")
    
    except psycopg2.DatabaseError as e:
        print(f"Error creating table: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        
              
if __name__ == '__main__':
    create_tables()

