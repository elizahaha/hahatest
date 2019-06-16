# -*- coding: UTF-8 -*- 
'''

@author: Administrator
'''
import unittest
import time
#import BSTestRunner
import HTMLTestRunner
import sendEmail


if __name__=="main":
     
    
    test_dir='./test_case'
    discover=unittest.defaultTestLoader.discover(test_dir,pattern='*_test.py')
    
   
    now = time.strftime("%y-%m-%d %H_%M_%S")   
    filename = './report/'+now+'_test_report.html'  
    fp =open(filename,'wb')
    
    runner = HTMLTestRunner(stream=fp,title='zsy test report',description='the first report')
    
    runner.run(discover)
    fp.close()
    
    time.sleep(6)
  
    new_report_addr = sendEmail.SendEmail().acquire_report_address(filename)
 
    sendEmail.SendEmail().send_email(new_report_addr)
    
#     test_report = './report'
#     rep=report(test_report)
    
    
    
    
    