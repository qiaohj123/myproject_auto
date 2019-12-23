# -*- coding:utf-8 -*-
from rbemp_po.Common.CommonLib import *
from rbemp_po.Pages.BackEndGw_module.GateWaypage import GateWaypage
import unittest
from selenium import webdriver

class GateWsy(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()
        self.page = GateWaypage(self.dr)
        self.log = Log()

    def tearDown(self):
        self.dr.quit()

    def test_gateway_01(self):
        self.log.info('>>> test_gateway_01测试用例执行开始：新建短信通道，移动、联通、电信、国外通道各一条')
        self.page.gate_nums()
        try:
            login(self.dr)
            self.page.forward_page_gate()
            i = 1
            while i < 4:
                if i == 1:
                    self.log.info('>>> 创建短信移动通道')
                    self.page.gate_style('短信')
                    self.page.operator_style('移动')
                    self.page.page_ele()[2].send_keys(self.page.gate_name_yd)
                    self.page.page_ele()[3].send_keys(self.page.read_nums()[0])
                if i == 2:
                    self.log.info('>>> 创建短信联通通道')
                    self.page.gate_style('短信')
                    self.page.operator_style('联通')
                    self.page.page_ele()[2].send_keys(self.page.gate_name_lt)
                    self.page.page_ele()[3].send_keys(self.page.read_nums()[1])
                if i == 3:
                    self.log.info('>>> 创建短信电信通道')
                    self.page.gate_style('短信')
                    self.page.operator_style('电信')
                    self.page.page_ele()[2].send_keys(self.page.gate_name_dx)
                    self.page.page_ele()[3].send_keys(self.page.read_nums()[2])
                self.page.page_ele()[4].send_keys(self.page.expend_num)
                self.page.page_ele()[5].send_keys(self.page.sign_sms)
                self.page.commit_create()
                self.page.new_create()
                i += 1
            self.log.info('>>> test_gateway_01测试用例执行结束：新建短信通道，移动、联通、电信、国外通道各一条，执行成功')
        except Exception as e:
            self.log.info('>>> test_gateway_01测试用例执行结束：新建短信通道，移动、联通、电信、国外通道各一条，执行失败{}'.format(e))
            screen_shot(self.dr, 'test_gateway_01.png')
            raise e

if __name__ == '__main__':
    unittest.main()