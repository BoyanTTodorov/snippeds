import pandas as pd
import datetime 

year = datetime.date.today().year
timestamp = pd.Timestamp(datetime.datetime(year, 12, 31))
res = timestamp.today()
days_left = int((timestamp - res).days)
print(days_left)

def days_left_in_year(month, day, year):
   day_of_year = datetime.datetime(year,month,day).timetuple().tm_yday
   end_of_year = datetime.datetime(year,12,31).timetuple().tm_yday
   return end_of_year - day_of_year