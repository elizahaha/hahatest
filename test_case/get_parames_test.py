#coding:utf-8
'''
Created on 2019��4��10��

@author: Administrator
'''

import requests
import unittest
from _ast import Pass
from public import base


class GetParams(unittest.TestCase):

    def setUp(self):

        endpoint='get'
        
        self.url=base.get_url(endpoint)
        
    def test_get_params(self):
        

        parmers ={"show_env":1}
        
        #给服务器发送请求
        
        r=requests.get(self.url,params=parmers)
        
        resp = r.json()
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
    
#     def test_get_params2(self):
#         
# 
#         parmers ={"show_env":1}
#             
#         #给服务器发送请求
#             
#         r=requests.get(self.url,params=parmers)
#             
#         resp = r.json()
#             
#         connect = resp.get('headers').get('Host')
#         
#             
#         self.assertIsInstance(connect,unicode)



    
    
    
    
         
    def tearDown(self):
        Pass
        
if __name__=='__main__':
    
    unittest.main()
