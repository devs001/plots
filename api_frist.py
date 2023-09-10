import requests
import json
url='http://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)
print(r.status_code," status code machine readable")
respons_dict=r.json()
print(respons_dict.keys())
print('total repository',respons_dict['total_count'])
reposi_dicts=respons_dict['items']
print('repository avi.',len(reposi_dicts))
items_dict=reposi_dicts[3]
print("language: ",items_dict['language'])
print("name: ",items_dict['name'])
print("stargazers_count: ",items_dict['stargazers_count'])
print("watchers_count: ",items_dict['watchers_count'])
print("has_downloads: ",items_dict['has_downloads'])
star_dict={}
for reposi_info in reposi_dicts:
    stars=reposi_info['stargazers_count']
    name=reposi_info['name']
    star_dict[name]=stars
print(len(star_dict.keys()))
with open('stats_number.json','w') as star:
    json.dump(star_dict,star)
with open('reposi.json','w') as reposi:
    json.dump(reposi_dicts,reposi)
