import json
import matplotlib.pyplot as plt
from pygal.maps.world import COUNTRIES

with open('population_data.json') as p_d:
    pop_data=json.load(p_d)
for dict in pop_data:
    if dict['Year']=='1983':
        country_name=dict['Country Name']
        population=dict['Value']
for country_code in sorted(COUNTRIES.keys()):
    print(country_code,COUNTRIES[country_code])
