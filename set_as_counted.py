import pandas as pd
import sqlite3


path = r"C:\Users\b.todorov\Desktop\WOREHOUSE DATA\B06.xlsx"

df = pd.read_excel(path)

df = df['Storage Bin']

path_to_database = r"C:\Users\b.todorov\Desktop\cycle_couting.db"

conn = sqlite3.connect(path_to_database)
cur = conn.cursor()
for bin in df:
    cur.execute(f'UPDATE MKI SET "36" = 1 WHERE "Storage Bin" = "{bin}"')
    print(f'Updating Bin {bin}')
conn.commit()
cur.close()
conn.close()