import csv
from WORLD_MAPS import get_country_code
from pygal.maps.world import World
import matplotlib.pyplot as plt
with open('gdp_csv.csv') as gdp:
    gdp_read=csv.reader(gdp)
    header_remove=next(gdp_read)
    print(header_remove)
    dict_class1={}
    dict_class2={}
    dict_class3={}
    dict_class4={}
    for row in gdp_read:

        if int(row[2])==2000:
            country_name=row[0]
            gdp=int(float(row[3]))
            c_code=get_country_code(country_name)
            if c_code:
                if gdp<10000000000:
                    dict_class1[c_code]=gdp
                elif gdp<100000000000:
                    dict_class2[c_code]=gdp
                elif gdp<1000000000000:
                    dict_class3[c_code]=gdp
                else:
                    dict_class4[c_code]=gdp
print(dict_class3)
wpop_map=World()
wpop_map.title='gdp in 2000'
wpop_map.add('poplation less then 10 bn',dict_class1)
wpop_map.add('poplation less then 100bn',dict_class2)
wpop_map.add('poplation less then 1000bn',dict_class3)
wpop_map.add('poplation mire then 1000bn',dict_class4)

wpop_map.render_to_file("gdp of contry(2000).svg")