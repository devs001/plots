import requests
import pygal
import json
import seaBorn
url="https://api.github.com/search/repositories?q=language:Ruby&sort=stars"
req=requests.get(url)
req_read=req.json()
print((req_read))
lis_dicts=req_read['items']
print('no of projects avi.',len(lis_dicts))
pyg_dicts=[]
name_lis=[]
print(lis_dicts[0].keys())
for dict in lis_dicts:
    dicta={
        'value':dict['stargazers_count'],
        'label':dict['name']
        }
    name=dict['name']
    pyg_dicts.append(dicta)
    name_lis.append(name)

chart_go=pygal.Bar(x_label_rotation=45,major_label_font_size=13)
chart_go.add(" Ruby",pyg_dicts)
chart_go.x_labels=name_lis
chart_go.render_to_file('Ruby_chartver1.0.svg')

with open('Ruby_save.json','w') as Ruby_f:
    json.dump(lis_dicts,Ruby_f)