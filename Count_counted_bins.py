import pandas as pd
import sqlite3
import numpy as np

def UPDATE_WH_LABELS(warehouse):
    MKI = 222380
    JTS1 = 139082
    JTS2 = 163962

    conn = sqlite3.connect(r'C:\Users\b.todorov\Desktop\post_2022.db')
    cmd = f'''select * from "{warehouse}"'''
    df = pd.read_sql(cmd, conn)
    # df['Counted'] = df[['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52']].sum(axis=1, numeric_only=True)
    ndf = df.groupby('Physical Inventory Document').sum()
    print(ndf)


    conn.close()


UPDATE_WH_LABELS("postings")
