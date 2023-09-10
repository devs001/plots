import csv
from datetime import datetime
import matplotlib.pyplot as plt
with open('death_valley_2014.csv') as dv_f:
    dv_read=csv.reader(dv_f)
    dv_hlis=[]
    dv_datelis=[]
    header_r=next(dv_read)

    for row in dv_read:
        try:
            dv_h_num=int(row[1])
            dv_date_num=datetime.strptime(row[0],'%Y-%m-%d')
        except ValueError:
            print(" date empty")
        else:
            dv_hlis.append(dv_h_num)
            dv_datelis.append(dv_date_num)

with open('sitka_weather_2014.csv') as s_f:
    s_read=csv.reader(s_f)
    s_hlis=[]
    header_r=next(s_read)
    s_datelis=[]
    for row in s_read:
        try:
            h_temp_num=int(row[1])
            s_date_num=datetime.strptime(row[0],'%Y-%m-%d')
        except ValueError:
            print(" -date empty")
        else:
            s_hlis.append(h_temp_num)
            s_datelis.append(s_date_num)
dv_hlis.pop(46)
dv_datelis.pop(46)
A_dv_hlis[0:]
#gif=plt.figure(dpi=128,figsize=(10,7))
plt.plot(s_datelis,s_hlis,c='red')
plt.plot(dv_datelis,dv_hlis,c='blue')
plt.fill_between(dv_datelis,s_hlis,dv_hlis,facecolor='blue',alpha=.5)
"""plt.xlabel("dates")
plt.ylabel("temprature")
plt.title('highest temprature compristion death vally and'
           ' stika(suothern alska')
#gif.autofmt_xdate()
#plt.tick_params(axis='both',labelsize=20,which='major')"""
plt.show()
