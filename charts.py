import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from datetime import datetime


path = r"S:\Warehouse dept\Inventory control\Reporting and dashboards\Bin's Counting\Cycle Counting\DATABASE\cycle_couting.db"

all_warehouses = {'MKI':[222380], 'JTS1':[139082], 'JTS2':[206938]}
all_warehouses_counted = {}

def plotGraph(lbl_counted:str, lbl_notcounted:str, total_bins:int ,qty_counted:float, main_label:str):
        fig = plt.figure()
        ### Plotting arrangements ###
        labels = lbl_counted, lbl_notcounted
        sizes = [qty_counted, total_bins-qty_counted]
        explode = (0, 0.1)  # Only "explode" the 2nd slice
        fig, ax = plt.subplots()
        fig.suptitle(main_label, fontsize=16)
        ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        return fig


def get_data_from_database(warehouse):
        counted  = []

        query = f'''SELECT COUNT(Result) FROM (SELECT "1","2","3","4","5","6","7","8","9","10",
        "11","12","13","14","15","16","17","18","19","20","21","22",
        "23","24","25","26","27","28","29","30","31","32","33","34",
        "35","36","37","38","39","40","41","42","43","44","45","46",
        "47","48","49","50","51","52",
        "1"+"2"+"3"+"4"+"5"+"6"+"7"+"8"+"9"+"10"+"11"+"12"+"13"+"14"
        +"15"+"16"+"17"+"18"+"19"+"20"+"21"+"22"+"23"+"24"+"25"+"26"+
        "27"+"28"+"29"+"30"+"31"+"32"+"33"+"34"+"35"+"36"+"37"+"38"+"39"
        +"40"+"41"+"42"+"43"+"44"+"45"+"46"+"47"+"48"+"49"+"50"+"51"+"52" 
        AS Result from "{warehouse}") WHERE Result > 0;'''
        
        conn = sqlite3.connect(path)
        curs = conn.execute(query)
        counted = curs.fetchall()
        number_counted = counted[0]
        curs.close()
        conn.close()
        return number_counted

for wh in all_warehouses.keys():
        all_warehouses[wh].append(get_data_from_database(wh))

pp = PdfPages('Report_' + datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p") + '.pdf')

for wh in all_warehouses.items():
        warehouse = wh[0]
        total = wh[1][0]
        counted =wh[1][1]
        # print('Counted ' + str(counted[0]))
        # print('Not Counted ' + str(total - counted[0]))
        # print('Total ' + total)
        pp.savefig(plotGraph('Counted\n' + str(counted[0]), 'Not Counted\n' + str(total - counted[0]), total, counted[0], warehouse))
pp.close()