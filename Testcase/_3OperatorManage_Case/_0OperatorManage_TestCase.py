# -*- coding:utf-8 -*-
from rbemp_po.Common.CommonLib import *
from rbemp_po.Pages.OperatorManage_moudle.OperatorManagepage import OperatorManagepage
import unittest
from selenium import webdriver

class OperatorManage(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()
        self.page = OperatorManagepage(self.dr)
        self.log = Log()

    def tearDown(self):
        self.dr.quit()

    def test_operator_01(self):
        self.log.info('>>> test_operator_01测试用例执行开始：新建操作员流程验证')
        try:
            login(self.dr)
            self.page.forward_page_operator()
            self.page.new_create()
            self.page.page_ele_newcarate()[0].send_keys(self.page.login_account)
            self.page.page_ele_newcarate()[1].send_keys(self.page.operator_name)
            self.page.organization()
            self.page.sex()
            self.page.birthday()
            self.page.page_ele_newcarate()[6].send_keys(self.page.phone_num)
            self.page.roles()
            self.page.commit()
            self.log.info('>>> test_operator_01测试用例执行结束：新建操作员流程验证，执行成功')
        except Exception as e:
            self.log.info('>>> test_operator_01测试用例执行结束：新建操作员流程验证，执行失败：{}'.format(e))
            screen_shot(self.dr, 'test_operator_01.png')
            raise e

if  __name__ == '__main__':
    unittest.main()