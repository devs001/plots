import csv
from datetime import datetime
import matplotlib.pyplot as plt
with open('death_valley_2014.csv') as dv_f:
    death_vreader=csv.reader(dv_f)
    haeder_remove=next(death_vreader)
    print(haeder_remove)
    h_temp=[]
    l_temp=[]
    m_temp=[]
    date_lis=[]
    for row in death_vreader:
        #there is a empty in 47 it will produce a error
        try:
            num_h=int(row[1])
            num_l=int(row[3])
            num_m=int(row[2])
            date_num = datetime.strptime(row[0], '%Y-%m-%d')
        except ValueError:
            print(str(date_num)+"- missing data date")
        else:
            h_temp.append(num_h)
            l_temp.append(num_l)
            m_temp.append(num_m)
            date_lis.append(date_num)
fiu=plt.figure(dpi=130,figsize=(10,6))
plt.plot(date_lis,h_temp,c='red')
plt.plot(date_lis,l_temp,c='blue')
plt.plot(date_lis,m_temp,c='green')
plt.xlabel('number of days',fontsize=12)
fiu.autofmt_xdate()
plt.title("diffenct between low and high temp death vally")
plt.ylabel('tempratur',fontsize=14)
plt.fill_between(date_lis,h_temp,l_temp,facecolor='green',alpha=.5)
plt.show()
