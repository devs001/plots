import requests
import json
from operator import itemgetter
url='https://hacker-news.firebaseio.com/v0/topstories.json'
try:
    r=requests.get(url)
except Exception:
    print("check internet conection or url")
else:
    print("status code:",r.status_code)
sn_ids=r.json()
sn_dicts=[]
for sn_id in sn_ids[:30]:
   print(sn_id)
   url_id='https://hacker-news.firebaseio.com/v0/item/'+str(sn_id)+'.json'
   req=requests.get(url_id)
   req_read=req.json()
   sn_dict={
       'title':req_read['title'],
       'link':'http://news.ycombinator.com/item?id='+str(sn_id),
       'comments':req_read.get('descendants',0)
   }
   sn_dicts.append(sn_dict)
sn_dicts=sorted(sn_dicts,key=itemgetter('comments'),reverse=True)
for sn in sn_dicts:
    print('title:',sn['title'])
    print("disscion_link:",sn['link'])
    print("Comments::",sn['comments'])
