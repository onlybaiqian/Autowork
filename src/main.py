#-*- coding:utf-8 -*-
import sys
sys.path.append("./.")
from src.xuliemail import send_mail
import os
import unittest
import time
from runlib import HTMLTestRunner


#########--------发送最新的测试报告----------###
def new_report(testreoprt):
    lists = os.listdir(testreoprt)
    lists.sort(key=lambda fn: os.path.getatime(testreoprt + "\\" + fn))
    file_new = os.path.join(testreoprt,lists[-1])
    print(file_new)
    return file_new

if __name__ == '__main__':
    os.chdir("\\vanxulie\\")
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = "report\\" + now + "Report.html"
    fp = open(filename, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title='自动化测试报告',
                                           description='用例执行情况：')
    discover = unittest.defaultTestLoader.discover('runcase\\test_sina\\',pattern='test_*.py',top_level_dir=None)
    print(discover)
    runner.run(discover)
    fp.close()
    file_path = new_report('./report')
    send_mail(file_path)
