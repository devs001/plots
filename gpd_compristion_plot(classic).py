import csv
import matplotlib.pyplot as plt
from WORLD_MAPS import get_country_code
with open('gdp_csv.csv') as gdp_csv:
    gdp_read=csv.reader(gdp_csv)
    header_remove=next(gdp_read)
    print(header_remove)
    alg_gdp_lis=[]
    zamb_gdp_lis=[]
    in_gdp_lis = []
    us_gdp_lis = []
    ch_gdp_lis = []
    arg_gdp_lis = []
    jp_gdp_lis = []
    aw_gdp_lis = []
    number_of_year=[]
    for row in gdp_read:
        print(row)
        if row[0]=='Algeria':
            alg_gdp_lis.append(int(float(row[3])))
            number_of_year.append(int(row[2]))
        elif row[0]=='Zimbabwe':
            zamb_gdp_lis.append(int(float(row[3])))
        elif row[0]=='India':
            in_gdp_lis.append(int(float(row[3])))
        elif row[0]=='United States':
            us_gdp_lis.append(int(float(row[3])))
        elif row[0]=='China':
            ch_gdp_lis.append(int(float(row[3])))
        elif row[0]=='Argentina':
            arg_gdp_lis.append(int(float(row[3])))
        elif row[0]=='Japan':
            jp_gdp_lis.append(int(float(row[3])))
        elif row[0]=='Arab World':
            aw_gdp_lis.append(int(float(row[3])))
for i in range(2):
    arg_gdp_lis.append(arg_gdp_lis[-1])
for i in range(8):
    aw_gdp_lis.append(aw_gdp_lis[-1])
plt.plot(number_of_year,alg_gdp_lis,linewidth=1)
plt.plot(number_of_year,zamb_gdp_lis)
plt.plot(number_of_year,in_gdp_lis)
plt.plot(number_of_year,us_gdp_lis)
#plt.plot(number_of_year,ch_gdp_lis)
plt.plot(number_of_year,arg_gdp_lis)
plt.plot(number_of_year,jp_gdp_lis)
plt.plot(number_of_year,aw_gdp_lis)
plt.axis([1960,2020,1000000000,9000000000000])
plt.tick_params(axis='both',labelsize=10,which='major')
plt.title("gdp of countryes")
plt.xlabel("number of year")
plt.show()
