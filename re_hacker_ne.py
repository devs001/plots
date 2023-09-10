import json
import requests
import dump_js
url='https://hacker-news.firebaseio.com/v0/topstories.json'
req=requests.get(url)
req_read=req.json()
lis_dicts=[]
for id in req_read[:32]:
    url='https://hacker-news.firebaseio.com/v0/item/'+str(id)+'.json'
    reqs=requests.get(url)
    dict=reqs.json()
    lis_dicts.append(dict)
dump_js.dumping('hacker_dicts.json',lis_dicts)
