#coding:utf-8

'''
Created on 15 Apr 2019

@author: Administrator
'''

import requests

import json

from public import  Config
from post_data_test1 import data

class MyHTTP():
    
    def __init__(self):
        
        self.url=Config.url()
        
    def get(self,url,**DataALL):
        
        params =DataALL.get('params')
        
        headers = DataALL.get('headers')
        
        resp =requests.get(url,params=params,headers=headers)
        
        text=resp.json()
        
        return text
        
        