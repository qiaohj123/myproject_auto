# -*- coding:utf-8 -*-
from rbemp_po.Common.PageObject import Elements_located
from rbemp_po.Common.CommonLib import rconf
from rbemp_po.Common.PageObject import PageObject
from selenium import webdriver

class LoginPage(PageObject):
    # 登录账号信息值
    name = "admin"
    pwd = "admin123"
    # 登录后，断言取值：admin
    login_page_assert = '//span[@title="admin"]'

    # 页面元素获取
    def page_ele(self):
        # 用户名元素
        username = self.Find_element('name','username')
        # 用户密码元素
        pwd = self.Find_element('name','password')
        # 登录按钮元素
        login_button = self.Find_element('xpth','//span[text()="登录"]')
        return username, pwd, login_button

