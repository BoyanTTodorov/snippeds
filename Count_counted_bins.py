import pandas as pd
import sqlite3
import numpy as np

def UPDATE_WH_LABELS(warehouse):
    MKI = 222380
    JTS1 = 139082
    JTS2 = 163962
    path = r"S:\Warehouse dept\Inventory control\Reporting and dashboards\Bin's Counting\Cycle Counting\DATABASE\cycle_couting.db"
    conn = sqlite3.connect(path)
    cmd = f'''select * from "{warehouse}"'''
    df = pd.read_sql(cmd, conn)
    df['Counted'] = df[['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52']].sum(axis=1, numeric_only=True)
    filt = df.Counted > 0
    df = df[filt]
    print(len(df))
    conn.close()

UPDATE_WH_LABELS("MKI")
UPDATE_WH_LABELS("JTS1")
UPDATE_WH_LABELS("JTS2")