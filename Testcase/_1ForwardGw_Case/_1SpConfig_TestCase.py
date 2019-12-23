# -*- coding:utf-8 -*-
from rbemp_po.Common.CommonLib import *
from rbemp_po.Pages.ForwardGW_module.SpConfigGatepage import SpConfigGatepage
import unittest
from selenium import webdriver

class SpConfig(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()
        self.page = SpConfigGatepage(self.dr)
        self.log = Log()

    def tearDown(self):
        self.dr.quit()

    def test_spconfig_01(self):
        self.log.info('>>> test_spconfig_01测试用例执行开始：新增账户通道配置-短信SP绑定移动、联通、电信通道号码')
        try:
            login(self.dr)
            self.page.forward_page_account()
            self.page.newcreate()
            i = 1
            while i < 4:
                self.page.page_sp('短信')
                self.page.page_routstatus('启用')
                self.log.info('>>> 选择上下行路由')
                self.page.page_routstyle()
                if i == 1:
                    self.log.info('>>> 绑定移动通道号码')
                    self.page.page_gate('移动')
                elif i == 2:
                    self.log.info('>>> 绑定联通通道号码')
                    self.page.page_gate('联通')
                elif i == 3:
                    self.log.info('>>> 绑定电信通道号码')
                    self.page.page_gate('电信')
                self.page.page_ele()[4].send_keys('1')
                self.page.commit()
                i += 1
                self.page.newcreate()
            self.log.info('>>> test_spconfig_01测试用例执行结束： 新增账户通道配置-短信sp绑定移动、联通、电信通道号码，执行成功')
        except Exception as e:
            self.log.info('>>> test_spconfig_01测试用例执行结束： 新增账户通道配置-短信sp绑定移动、联通、电信通道号码，执行失败{}'.format(e))
            screen_shot(self.dr, 'test_spconfig_01.png')
            raise e


if __name__ == '__main__':
    unittest.main()