import pandas as pd
import sqlite3

def load_data(db_path='attendance.db', table_name='attendance'):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql(f'SELECT * FROM {table_name}', conn)
    conn.close()
    return df