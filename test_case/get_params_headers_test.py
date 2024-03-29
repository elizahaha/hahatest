#coding:utf-8

'''
Created on 2019��4��10��

@author: Administrator
'''

import requests
import unittest
from public import base
from public import HttpService


class GetParamsHeadersTest(unittest.TestCase):
#    '''GET有params和headers请求'''
    def setUp(self):
        
        endpoint ='get'
        
        self.url=base.get_url(endpoint)
        
    def test_params_headers(self):

        params ={"show_env":1}
        
        header={'Connection': 'keep-alive', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'User-Agent': 'python-requests/2.21.0'}
        
        DataALL ={'params':params,'headers':header}
        
#       r=requests.get(self.url,params=params,headers=header)
#          
#       resp = r.json()

#       resp = HttpService.MyHTTP().get(self.url, params)

        resp = HttpService.MyHTTP().get(self.url,**DataALL)
        
        connect = resp.get('headers').get('Host')
        
        self.assertEqual(connect,'httpbin.org')
        
#         print(r.status_code,r.reason)#获取响应状态码，获取状态码的原因
#         print header
#         print (r.request.headers)
#         print(r.headers)#响应头
#         print(r.text)#响应文本
    
    def tearDown(self):
        pass
    
if __name__=='__main__':
    
    unittest.main()







