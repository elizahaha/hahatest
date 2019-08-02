#coding=utf-8

'''
Created on 2019��4��10��

@author: Administrator
'''
import requests

host='https://httpbin.org/'

endpoint ='post'

url=host+endpoint

parmers ={"show_env":1}

data={'a':'瞧把软件测试','b':'form-data'}

r=requests.post(url,params=parmers,data=data)


resp=r.json()


#print(r.status_code,r.reason)#获取响应状态码，获取状态码的原因
print(resp['form'])
#print(r.headers)#响应头
#print(r.url)
#print(r.text)#响应文本

import unittest
from _ast import Pass
from public import base
from public import HttpService


class PostDataTest(unittest.TestCase):
    
    '''Post,data测试'''
    
    def setUp(self):
        
        endpoint='post'
        
        self.url=base.get_url(endpoint) 
    
    def test_post_data_1(self):
        
        '''from值验证'''
        parmers ={"show_env":1}

        data={'a':'瞧把软件测试','b':'form-data'}
