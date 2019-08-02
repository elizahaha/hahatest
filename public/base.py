
from public import Config

from public import HttpService 

from public import read_excel

testcasefile='get_nothing_test_data.xlsx'

AllData =base.get_data(testcase,'AllData')

TestData =base.get_data(testcase,'TestData')

def get_url(endpoint):
    
    host=Config.url()
    
    url=host+endpoint
    
    return url
    
def get_response(url,Method,**DataALL):
    
    if Method == 'get':
        
        resp = HttpService.MyHTTP().get(url,**DataALL)
        
    elif Method == 'post':
        
        resp = HttpService.MyHTTP().post(url,**DataALL)
        
    return resp

def get_data(testfiles,sheetname):
    
#    datainfo =read_excel.XLD
    
    datainfo = read_excel.XLDateinof(r'D:\zsy\workspace\test_zsy_unittest\test_data\%s'%testfiles)
    
    alldata =datainfo.get_sheetinfo_by_name(sheetname)
    
    
    
    
    