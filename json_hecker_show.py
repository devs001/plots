import json
lis_news=[]
with open('hacker_dicts.json') as hacker_file:
    news_list=json.load(hacker_file)
    for news in news_list:
        dict={
            'title':news['title'],
            'score':news['score'],
            'comments':news.get('descendants',0),
            'link':news.get('url'),
            }
        lis_news.append(dict)
for dict_row in lis_news:
    print('title of news :',dict_row['title'])
    print('score :',dict_row['score'])
    print('coments :',dict_row['comments'])
    print('link for news :',dict_row['link'])
