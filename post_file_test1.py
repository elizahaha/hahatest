#coding=utf-8
'''
Created on 2019��4��14��

@author: Administrator
'''
import requests
from post_data_test import data

host='https://httpbin.org/'

endpoint ='post'

url=host+endpoint


#1、普通上传
#files={'files':open('test.txt','rb')}


#2、通过文件上传字符串
#files={'files':('test.txt','send 121212')}

#3、自定义文件名、文件类型以及请求头(请求文件名称、文件路径、文件类型、文件请求头)
#files={'files':('F:\test1.jpg',open('F:\test1.jpg','rb'),'imag/png')}

#4、传送多个文件
#files=[('field1',('test.txt','rb')),('field2',('F:\test1.jpg',open('F:\test1.jpg','rb'),'imag/png'))]

#r=requests.post(url,files=files)

#5、流式上传
with open('test.txt') as f:
    
    r=requests.post(url,data=f)



print(r.headers)#响应头
print(r.text)#响应文本