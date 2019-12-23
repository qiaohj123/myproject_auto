# -*- coding:utf-8 -*-
from rbemp_po.Common.CommonLib import *
from rbemp_po.Common.PageObject import PageObject
from rbemp_po.Pages.Loginpage import LoginPage
import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()
        self.PO = PageObject(self.dr)
        self.log = Log()

    def tearDown(self):
        self.dr.quit()

    def test_login(self):
        self.pages = LoginPage(self.dr,page_url='http://192.169.7.138:8109')
        self.log.info('>>> 测试用例执行开始：正常登录系统')
        self.pages.page_ele()[0].send_keys(self.pages.name)
        self.pages.page_ele()[1].send_keys(self.pages.pwd)
        self.pages.page_ele()[2].click()
        self.PO.Find_element('xpth',self.pages.login_page_assert)
        self.log.info('>>> 测试用例执行结束：登录系统成功')
# if __name__ == '__main__':
#     unittest.main()



