# -*- coding:utf-8 -*-
from src import browser
from src import pyselenium
from src.xulielog import Log
import unittest



class Mytest_pc(unittest.TestCase):


    def setUp(self):
        Log().info('------*------*------*------START------*------*------*------')
        self.dr = pyselenium.PySelenium(browser.Browser)
        self.dr.max_window()
        self.dr.wait(15)

    def tearDown(self):
        self.dr.quit()
        Log().info('------*------*------*------*------End------*------*------*------')


class Mytest_wap(unittest.TestCase):

    def setUp(self):
        Log().info('------*------*------*------START------*------*------*------')
        self.dr = pyselenium.PySelenium(browser.Browser)
        self.dr.set_window(540, 960)
        self.dr.wait(15)


    def tearDown(self):
        self.dr.quit()
        Log().info('------*------*------*------*------End------*------*------*------')