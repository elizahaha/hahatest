#coding=utf-8

'''
Created on 2019��4��14��

@author: Administrator
'''
import requests
import json

host='https://httpbin.org/'

endpoint ='post'

url=host+endpoint

data = {
    "info":[{"code":1,"sex":"男","id":1900,"name":"巧吧软件测试"}],
    "code":1,
    "name":"巧吧软件测试","sex":"女",
    "data":[{"code":1,"sex":"男","id":1900,"name":"巧吧软件测试"}],
    "id":1900
    }

#r=requests.post(url,data=json.dumps(data))
r=requests.post(url,json=data)


# print(r.headers)#响应头
# 
print(r.text)

resp =r.json()

#resp2=resp.dumps(dict,encoding="UTF-8",ensure_ascii=False)

print(resp["json"])#输出内容是unicode编码，考虑一下怎么才能正常输出中文呢

#print(resp2["json"])

