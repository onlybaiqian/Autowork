#-*- coding:utf-8 -*-



import  sys
sys.path.append(".")
from src import myunit
from src.pyselenium import PySelenium
from src.urlpath import weibo_url
from src.xulielog import Log
from page.sina import temp_Weibologin
import unittest,time



class test_Weibo(myunit.Mytest_pc):
    '''测试微博登录'''
    def test_weibo_login(self):

        self.dr.open(weibo_url)
        # logging.Logger().log().info("打开浏览器")
        temp_Weibologin.Weibo_login(self.dr).login('微博账号', '微博密码')



if __name__ == "__main__":
    unittest.main()
