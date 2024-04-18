import pandas as pd
import sqlite3

df = pd.read_csv("laptop_data.csv")
df = df.drop('Unnamed: 0', axis='columns')

# Printing columns names
# print(df.columns)

# create connection to db
conn = sqlite3.connect("laptop_data.db")

# export dataframe to db
df.to_sql('LAPTOP_DATA', conn, if_exists='replace', index=False)
conn.close() 