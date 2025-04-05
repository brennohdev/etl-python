from etl.extract import read_csv
from etl.transform import transform_data
from etl.load import connect_to_db, insert_dataframe, close_connection

# Exctraction

df = read_csv('data/attendance.csv')
if df is None:
    exit()

# Transformation

df = transform_data(df)

# Loading

conn = connect_to_db('attendance.db')
insert_dataframe(df, conn, 'attendance')
close_connection(conn)

