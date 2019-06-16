#coding:utf-8

import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time



class SendEmail():
    def send_email(self, new_report):
    
        with open(new_report, 'r', encoding='utf8') as f:
            mail_body = f.read()
      
        send_addr = '2549189581@qq.com'
       
        reciver_addr = '2549189581@qq.com'
       
        mail_server = 'smtp.qq.com'
        now = time.strftime("%Y-%m-%d %H_%M_%S")

        subject = 'TEST report' + now

        username = '2549189581@qq.com'
        password = 'Zhang@19881221' 
        message = MIMEText(mail_body, 'html', 'utf8')
        message['Subject'] = Header(subject, charset='utf8')
    
        smtp = smtplib.SMTP()
        smtp.connect(mail_server)
        smtp.login(username, password)
        smtp.sendmail(send_addr, reciver_addr.split(','), message.as_string())
        smtp.quit()


    def acquire_report_address(self, reports_address):
       
        test_reports_list = os.listdir(reports_address)

        new_test_reports_list = sorted(test_reports_list)

        the_last_report = new_test_reports_list[-1]

        the_last_report_address = os.path.join(reports_address, the_last_report)
        return the_last_report_address
