import json
import pygal
from pygal.style import LightenStyle as LS
with open('reposi.json') as reposi_f:
    lis_names=[]
    lis_dicts=[]
    reposi_read=json.load(reposi_f)
    for row in reposi_read:
        name=row['name']
        row_dict={
        'value':row['stargazers_count'],
        'label':str(row['description']),
        'xlink':row['html_url']
        }
        lis_dicts.append(row_dict)
        lis_names.append(name)
print(lis_dicts)
style=LS('#336699')
my_con=pygal.Config()
my_con.x_label_rotation=45
my_con.widht=10000
my_con.major_label_font_size=18
my_con.label_font_size=12
ch=pygal.Bar(my_con,style=style)
ch.title='most stated programe on github'
ch.add('addo',lis_dicts)
ch.x_labels=lis_names
ch.render_to_file('AA7.svg')



