import polars as pl
from db import get_connection
import psycopg2
from extractor import extract, models, years
from transformer import transform

def load(complaints_df: pl.DataFrame):
    complaints_df = complaints_df.to_dicts()
    print(f"Total records to insert: {len(complaints_df)}")
    
    conn = None
    cursor = None
    
    try:
        conn = get_connection()
        cursor = conn.cursor()
        inserted = 0
        
        for complaint in complaints_df:
            try:
                cursor.execute("""
                    INSERT INTO complaints(odi_number, model, date_of_incident, date_complaint_filed, components,
                        summary, crash, fire, number_of_injuries, number_of_deaths)
                    VALUES (%(odi_number)s, %(model)s, %(date_of_incident)s, %(date_complaint_filed)s, %(components)s,
                        %(summary)s, %(crash)s, %(fire)s, %(number_of_injuries)s, %(number_of_deaths)s)
                    ON CONFLICT (odi_number) DO NOTHING;
                """, complaint)
                inserted += 1
                
            except psycopg2.DatabaseError as e:
                print(f"Error inserting row: {e}")
                
        print(f"Inserted {inserted} rows")
        conn.commit()
        
        
    except psycopg2.DatabaseError as e:
        print(f"Error inserting into table: {e}")
        
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    
if __name__ == '__main__':
    raw = extract(models,years)
    cleaned = transform(raw)
    load(cleaned)
        
        



    
