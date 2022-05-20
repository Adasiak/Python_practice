from clearConsole import clearConsole
import requests
import json
clearConsole()
baseUrl='https://api.upcitemdb.com/prod/trial/lookup'
# parameters={'upc': '012993441012'} 
parameters={'upc': '073366118238'}
response =  requests.get(baseUrl, params=parameters) 
print(response.url)
# content = response.content 
# info= json.loads(content)
# print(type(info))
# print (info)
content=response.content
info=json. loads (content)
item=info['items']
itemInfo=item[0]
title=itemInfo['title']
brand=itemInfo['brand']
print(title)
print(brand)

