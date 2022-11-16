import requests

response=requests.get('https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=c2cffc376cf841fda2e39392378a1c2e')

test=response.json()
# data=json.loads(response)
# print(test['articles'])
for i in test['articles']:
    x=["Shivam" if x==None in i["author"] else i["author"]]
    print(x)

print(x)
# print(data)