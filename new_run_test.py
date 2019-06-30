#coding:utf-8

'''
Created on 15 Apr 2019

@author: Administrator
'''
# -*- coding: UTF-8 -*- 
'''

@author: Administrator
'''
import unittest
import os
import time
import HTMLTestRunner
import sendEmail


if __name__=="__main__":
     
#用例存放路径    
    test_dir='./test_case'    
#报告存放路径

    report_dir =os.path.join(os.getcwd(),'report')
    
    discover=unittest.defaultTestLoader.discover(test_dir,pattern='*_test.py')
    
   #2、html报告文件路径
   
    now = time.strftime("%y-%m-%d %H_%M_%S")
    
    print(now)  
     
    filename ='report'+now+'_test_report.html'
    
    report_abspath = os.path.join(report_dir,'report_'+now+'_test_report.html')  
    
    fp =open(report_abspath,'wb')
    
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title='zsy test report',
                                           description='the first report')
    
    runner.run(discover)
    
    fp.close()
    
    time.sleep(6)
#   获取最新的测试报告    
    
    new_report_addr = sendEmail.SendEmail().acquire_report_address(report_dir)
    sendEmail.SendEmail().send_email(new_report_addr)
    
#     test_report = './report'
#     rep=report(test_report)
# #     
    
    
    
    









































# #coding:utf-8
# 
# '''
# Created on 15 Apr 2019
# 
# @author: Administrator
# '''
# # -*- coding: UTF-8 -*- 
# '''
# 
# @author: Administrator
# '''
# import unittest
# import time
# import os
# import HTMLTestRunner
# import sendEmail
# 
# 
# if __name__=="__main__":
#      
#     #用例存放地址
#     test_dir='./test_case'
#     #报告存放地址
#     report_dir =os.path.join(os.getcwd(),'report')
#     
#     discover=unittest.defaultTestLoader.discover(test_dir,pattern='*_test.py')
#     
#    
#     now = time.strftime("%y-%m-%d %H_%M_%S")
#        
#     filename = 'report'+now+'_test_report.html'
#       
#     fp =open(filename,'wb')
#     
#     report_abspath = os.path.join(report_dir,'report_'+now+'_test_report.html')
#     
#     runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='zsy test report',description='the first report')
#     
#     runner.run(discover)
#     fp.close()
#     
#     time.sleep(10)
#   
#     new_report_addr = sendEmail.SendEmail().acquire_report_address(filename)
# #  
#     sendEmail.SendEmail().send_email(new_report_addr)
#     
# #     test_report = './report'
# #     rep=report(test_report)
#     
#     
#     
#     
#     