#-*- coding:utf-8 -*-
from src import basepage
import time


class Weibo_login(basepage.Page):

    def input_user(self,user):

        # self.dr.clear_type('id=>loginname')

        self.dr.type('id->loginname',user)


    def input_password(self,psw):

        # self.dr.clear_type('id=>password')
        self.dr.type('name->password',psw)
        # self.driver.find_element_by_name("password").clear()
        # self.driver.find_element_by_name("password").send_keys(psw)

    def click_button(self):
        self.dr.click("xpath->//div[@id='pl_login_form']/div/div[3]/div[6]/a")
        # self.driver.find_element_by_xpath("//div[@id='pl_login_form']/div/div[3]/div[6]/a").click()


    def login(self, user, psw):
        # log.info('---执行测试----')
        '''登录公共方法'''
        self.input_user(user)
        self.input_password(psw)
        self.click_button()

