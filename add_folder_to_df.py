import os
import pandas as pd
import sqlite3
from datetime import datetime

start = datetime.now()
df = pd.DataFrame()
path_folder = r"C:\Users\b.todorov\Desktop\MKI\\"
#path_database = r"C:\Users\b.todorov\Desktop\stock_control.db"

# for file in os.listdir(path):
#     if file.endswith('.xlsx') or file.endswith('.XLSX'):
#         print(file)
        
filenames = [file for file in os.listdir(path_folder) if file.endswith('.xlsx') or file.endswith('.XLSX')]

df = pd.concat([pd.read_excel(path_folder + file) for file in filenames], ignore_index=True)
df = df.drop_duplicates()
len(df)
df.to_excel('mki.xlsx')

print('done')
