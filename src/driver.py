#-*- coding:utf-8 -*-

from selenium.webdriver import Remote
from selenium import webdriver

#启动浏览器
def is_chrome():
    driver = webdriver.Chrome()
    # host = '127.0.0.1:4444'   #运行主机：端口号
    # dc = {'browserName': 'Chrome'} #指定浏览器（'Chrome','Firefox'）
    # driver = Remote(command_executor = 'http://' + host + '/wd/hub', desired_capabilites=dc)
    return driver

def is_firefox():
    driver = webdriver.Firefox
    return  driver

def is_ie():
    driver = webdriver.Ie
    return  driver




if __name__ == '__main__':
    dr = is_chrome()
    dr.get("http://www.baidu.com")
    dr.quit()