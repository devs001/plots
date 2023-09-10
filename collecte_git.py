import json
import pygal
import matplotlib.pyplot as plt
from operator import itemgetter
list_lan=['C','Java','JavaScript','Ruby','Go','Haskell']
star_lis=[]
listr=[]
#open C_saved top gits for suming up theri star
for stri in list_lan:
    with open(stri+'_save.json') as C_f:
        Cgit_read=json.load(C_f)
        c_star_count=0
        for dict in Cgit_read:
            c_star_count+=int(dict['stargazers_count'])
        listr.append(c_star_count)
        dicts={
             'label':stri+'_gits_stars',
             'value': c_star_count}
        star_lis.append(dicts)
#star_lis=sorted(star_lis,key=itemgetter('value'),reverse=True)
chart=pygal.Bar(x_label_rotation=45,label_font_size=13)
chart.add('popularty by top 30 star',star_lis)
chart.title='populatrity of a languge by stars '
chart.x_labels=list_lan
chart.render_to_file('gggvar2.3.svg')
plt.bar(list_lan,listr,width=.1)
plt.show()