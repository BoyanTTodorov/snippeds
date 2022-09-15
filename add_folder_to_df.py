import os
import pandas as pd
import sqlite3
from datetime import datetime

start = datetime.now()
df = pd.DataFrame()
path_folder = r"C:\Users\b.todorov\Desktop\POST_EXCEL\\"
path_database = r"C:\Users\b.todorov\Desktop\post_2022.db"

# for file in os.listdir(path):
#     if file.endswith('.xlsx') or file.endswith('.XLSX'):
#         print(file)
        
filenames = [file for file in os.listdir(path_folder) if file.endswith('.xlsx') or file.endswith('.XLSX')]

df = pd.concat([pd.read_excel(path_folder + file) for file in filenames], ignore_index=True)
df = df.reset_index()

conn = sqlite3.connect(path_database)
df.to_sql('postings', conn, if_exists='append', index = False)
conn.commit()
conn.close()


end = datetime.now() - start
print(end)