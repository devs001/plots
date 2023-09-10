from WORLD_MAPS import get_country_code
from pygal.maps.world import World
from pygal.style import RotateStyle as rs,LightColorizedStyle as lcs
import json
with open('population_data.json') as popf:
    pop_read=json.load(popf)
dict_add_class1={}
dict_add_class2={}
dict_add_class3={}
for pop_dict in pop_read:
    #to if population data is from 2010 updated
    if int(pop_dict['Year'])==2010:
        country_name=pop_dict['Country Name']
        #str is change from float so it will go to float first
        pop=int(float(pop_dict['Value']))
        #it will give us code from name thruogh name entered
        code=get_country_code(country_name)
        if code:
            # to diferent dictcnary based on population
            if int(pop) < 10000000:
                dict_add_class1[code] = pop
            elif int(pop) < 1000000000:
                dict_add_class2[code] = pop
            else:
                dict_add_class3[code] = pop
        else:
            pass

wpop_map=World(style=rs('#33FF99',base_Style=lcs))
wpop_map.title='world poplation in map in colors'
wpop_map.add('poplation less then 10000000',dict_add_class1)
wpop_map.add('poplation less then 1000000000',dict_add_class2)
wpop_map.add('poplation more then 10000000',dict_add_class3)
wpop_map.render_to_file("population_in_map_with_class shortnewcolornew13FFyee.svg")