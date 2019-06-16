#coding=utf-8

'''
Created on 2019��4��10��

@author: Administrator
'''

import requests
#import json

host='https://httpbin.org/'

endpoint ='get'

url=host+endpoint




''' 给服务器发送请求'''

r=requests.get(url)

#print (r.url)#获取URL

#print(r.status_code)#获取状态码

#print(r.reason)#获取状态码的原因

#print(r.headers)

# print(r.text)#文本形式
# 
# print(type(r.text))

# print(r.content)#二进制形式,图片文件
# 
# print(type(r.content))

#print(r.json())

#print(type(r.json()))

print (r.request.headers)#请求头

#print(r.request.url)

#print(r.request.method)

respons =r.json()

#print(type(respons))

#print(respons['headers']['Host'])#取headers中的host字段

print(eval(r.text)['headers']['Host'])


