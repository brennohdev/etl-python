import sqlite3

def connect_to_db(db_name):
    return sqlite3.connect(db_name)

def insert_dataframe(df, conn, table_name):
    df.to_sql(table_name, conn, if_exists='replace', index=False)


def close_connection(conn):
    conn.close()