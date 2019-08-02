#coding:utf-8

'''
Created on 2019��8��1��

@author: Administrator
'''
import xlrd
from _ast import In

class XLDateinof(object):
    
    def __init__(self,path=''):
    
        self.xl =xlrd.open_workbook(path)
        
    def get_sheetinfo_by_name(self,name):
        
        self.sheet =self.xl.sheet_by_name(name)
        
        return self.get_sheet_info()
        
    def get_sheet_info(self):
        
        infolist=[]
        
        for row in range(0,self.sheet.nrows):
            
            info =self.sheet.row_values(row)
            
            infolist.append(info)
            
        return infolist
    

if __name__=="__main__":
    
    datainfo = XLDateinof(r'D:\zsy\workspace\test_zsy_unittest\test_data\get_nothing_test_data.xlsx')
    
    alldata =datainfo.get_sheetinfo_by_name('TestData')
    
    print(alldata)
    