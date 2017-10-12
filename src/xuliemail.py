#-*- coding:utf-8 -*-

from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from src.xulielog import Log
import smtplib
import time


#定义发送邮件方法
def send_mail(report_file):
    #发送邮箱
    sender = "发送邮件的邮箱账户"
    #接收邮箱
    receiver = "接收邮件的账户"
    #发送邮件服务器
    smtpserver = '发送邮件的服务器'
    #发送邮箱账号和密码
    username = "发送邮箱的账户"
    password = "发送邮箱的账户和密码"


    mail_body = open(report_file,'rb').read()
    #定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mail_body,_subtype='html', _charset='utf-8')
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    msg['Subject'] = "自动化测试报告" + now
    msg['from'] = sender
    msg['to'] = receiver
    #加上时间戳，好像没什么卵用
    msg["date"] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    msg.attach(body)
    # 添加附件
    part = MIMEApplication(open(report_file, 'rb').read())
    part["Content-Type"] = "application/octet-stream"
    part.add_header('Content-Disposition', 'attachment', filename='自动化测试报告'+ now + 'report.html') # 这边的filename随便写，完全看你心情，但是后缀的格式一定要统一
    msg.attach(part)
    #登录邮箱
    smtp = smtplib.SMTP()
    #连接邮箱服务器
    smtp.connect(smtpserver)
    #用户名密码
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    Log().info('------*------*------邮件发送成功!------*------*------*------!------*------*------')

