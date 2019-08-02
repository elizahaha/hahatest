#coding:utf-8

'''


@author: Administrator
'''

# -*- coding: UTF-8 -*- 


import requests
import unittest
from public import base

from ddt import data,unpack,ddt
from get_nothing import endpoint

testcasefile='get_nothing_test_data.xlsx'

AllData =base.get_data(testcasefile,'AllData')

TestData =base.get_data(testcasefile,'TestData')

EndPoint = AllData[1][1]

RequestMethod = AllData[1][2]

DataAll = TestData[1][1]




@ddt
class GetNothingTest(unittest.TestCase):

    def setUp(self):
        
        endpoint ='get'
        
        self.url=base.get_url(endpoint)
    
    
    @data(200,400,500,201)
    
    def test_1(self,result):
        

        
        r=requests.get(self.url)
        
        status_code =r.status_code
        
        self.assertEqual(status_code,result)
        
    
    @data(('headers','Host','httpbin.org'),('headers','Accept-Encoding','gzip, deflate'))
    @unpack
#   1、unpack用法
    def test_2(self,headers,value,result):
                
        r=requests.get(self.url)
        
        resp =r.json()
        
        connect =resp[headers][value]
        
        self.assertEqual(connect,result)
        
        
        
    def tearDown(self):
        
        pass
    
    
    
    
if __name__=="__main__":
    
    unittest.main()