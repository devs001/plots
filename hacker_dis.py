import json
import pygal
from operator import itemgetter
with open('hacker_news.json') as hn_f:
    hn_read=json.load(hn_f)
    print(hn_read[0].keys())
    py_dicts=[]
    py_name=[]
    for eli in hn_read:
        py_dict={
        'value':(eli['comments']),
        'label':eli['title'],
        'xlink':eli['link'],}
        py_name.append(eli['title'])
        py_dicts.append(py_dict)

my_conf=pygal.Config()
my_conf.x_label_rotation=45
my_conf.major_label_font_size=13
my_conf.label_font_size=23


py_dicts=sorted(py_dicts,key=itemgetter('value'),reverse=True)
chart=pygal.Bar(my_conf)
chart.x_labels=py_name
chart.add(" ",py_dicts)
chart.render_to_file("chart_of_popularty1.4.svg")


