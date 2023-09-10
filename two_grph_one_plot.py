import matplotlib.pyplot as plt
import csv
from datetime import datetime
with open('sitka_weather_2014.csv') as w_r_2014:
    report_reader=csv.reader(w_r_2014)
    high_t=[]
    mean_t=[]
    date_t=[]
    header_removal=next(report_reader)
    print(header_removal)
    for row in report_reader:
        high_t.append(int(row[1]))
        mean_t.append(int(row[3]))
        date=datetime.strptime(row[0],'%Y-%m-%d')
        date_t.append(date)

print(high_t)
print(mean_t)
figu=plt.figure(dpi=128,figsize=(10,6))

plt.plot(date_t,mean_t,c='blue',alpha=.7)
plt.xlabel("dates and combination",fontsize=12)
plt.ylabel("mean and high temprature computristion",fontsize=1)
plt.plot(date_t,high_t,c='red',alpha=.7)
plt.fill_between(date_t,mean_t,high_t,alpha=.4,facecolor='blue')
figu.autofmt_xdate()
plt.show()