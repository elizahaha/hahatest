#coding:utf-8
'''
Created on 2019��4��10��

@author: Administrator
'''


import unittest
from _ast import Pass
from public import base
from public import HttpService


class GetParams(unittest.TestCase):

    def setUp(self):

        endpoint='get'
        
        self.url=base.get_url(endpoint)
        
    def test_get_params(self):
        
        params ={"show_env":1}
        
        DataALL ={'params':params}
        
        #给服务器发送请求
        
#         r=requests.get(self.url,params=parmers)
#         
#         resp = r.json()
            
        resp = HttpService.MyHTTP().get(self.url,**DataALL)
        
#        resp1= json.dumps(resp, encoding="UTF-8", ensure_ascii=False)
        
#         print resp1
        
        connect = resp.get('headers').get('Host')
        self.assertEqual(connect,'httpbin.org')
        
#        print(connect)
#         
# 
#         print(r.status_code,r.reason)#获取响应状态码，获取状态码的原因
#         print(r.headers)#响应头
#         print(r.text)#响应文本
#         
    
    def test_get_params2(self):
#         
# 
        params ={"show_env":2}
        
        DataALL ={'params':params}
             
        #给服务器发送请求
             
#         r=requests.get(self.url,params=parmers)
#              
#         resp = r.json()

        resp = HttpService.MyHTTP().get(self.url, **DataALL)
             
        connect = resp.get('headers').get('Host')
                      
        self.assertIsInstance(connect,str)
    
    def tearDown(self):
        
        Pass
        
if __name__=='__main__':
    
    unittest.main()
