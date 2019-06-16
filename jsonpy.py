# coding=UTF-8

'''
Created on 2019��4��9��

@author: Administrator
'''
import requests
 
payload = {'phone': '15928658524', 'key': '6abd8629789a6da00567296f83267b81'}
 
r = requests.get("http://apis.juhe.cn/mobile/get", params=payload)

print r.text