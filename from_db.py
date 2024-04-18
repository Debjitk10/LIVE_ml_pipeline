import pandas as pd
import sqlite3

conn = sqlite3.connect("laptop_data.db")

query = "SELECT * FROM LAPTOP_DATA"
df = pd.read_sql_query(query, conn)

conn.close()