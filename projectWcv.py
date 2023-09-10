import csv
import matplotlib.pyplot as plt
from _datetime import datetime
file_n='sitka_weather_2014.csv'
with open (file_n) as f_n:
    reader=csv.reader(f_n)
    header_row = next(reader)
    numb=17
    str=header_row[numb]
    lis=[]
    date_lis=[]
    for row in reader:
        date=datetime.strptime(row[0],'%Y-%m-%d')
        date_lis.append(date)
        lis.append(row[1])
print(len(date_lis))
fig=plt.figure(dpi=140,figsize=(10,8))
plt.plot(date_lis,lis,c='red')
plt.xlabel('number of days')
plt.ylabel(str)
fig.autofmt_xdate()
plt.title(str+' of the day in sitaka,alaska in july')
plt.tick_params(axis='both',labelsize=10,which='major')
plt.show()


