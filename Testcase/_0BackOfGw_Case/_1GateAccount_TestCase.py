# -*- coding:utf-8 -*-
from rbemp_po.Common.CommonLib import *
from rbemp_po.Pages.BackEndGw_module.GateAccountpage import GateAccountpage
import unittest
from selenium import webdriver


class GateAccount(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()
        self.page = GateAccountpage(self.dr)
        self.log = Log()

    def tearDown(self):
        self.dr.quit()

    def test_gateaccount_01(self):
        self.log.info('>>> test_gateaccount_01测试用例执行开始：新建通道账户——短信类型')
        try:
            login(self.dr)
            self.page.forward_page_account()
            self.log.info('>>> 新建短信通道账户')
            self.page.newcreate()
            self.log.info('>>> 填写EMP内部账户基本信息')
            self.page.page_ele()[3].send_keys(self.page.gate_account_name)
            self.page.page_ele()[4].send_keys(self.page.gate_account)
            self.page.page_ele()[5].send_keys(self.page.password)
            self.page.page_ele()[6].send_keys(self.page.wg_ip)
            self.page.page_ele()[7].send_keys(self.page.wg_port)
            self.log.info('>>> 填写运营商接入账户基本信息')
            self.page.page_ele()[8].send_keys(self.page.cop_id)
            self.page.page_ele()[9].send_keys(self.page.cop_pwd)
            self.page.page_ele()[11].send_keys(self.page.cop_ip)
            self.page.page_ele()[12].send_keys(self.page.cop_port)
            self.log.info('>>> 选择后付费')
            self.page.charge_forward()
            self.log.info('>>> 确认新建')
            self.page.commit()
            self.log.info('>>> test_gateaccount_01测试用例执行结束：新建通道账户——短信类型，执行成功')
        except Exception as e:
            self.log.info('>>> test_gateaccount_01测试用例执行结束：新建通道账户——短信类型，执行失败{}'.format(e))
            screen_shot(self.dr, 'test_gateaccount_01.png')
            raise e

    def test_gateaccount_02(self):
        self.log.info('>>> test_gateaccount_02测试用例执行开始：新建通道账户——彩信类型')
        try:
            login(self.dr)
            self.page.forward_page_account()
            self.log.info('>>> 新建彩信通道账户')
            self.page.newcreate()
            self.page.page_ele()[0].click()
            self.page.page_ele()[1].click()
            self.log.info('>>> 填写EMP内部账户基本信息')
            self.page.page_ele()[3].send_keys(self.page.cx_gate_account_name)
            self.page.page_ele()[4].send_keys(self.page.cx_gate_account)
            self.page.page_ele()[5].send_keys(self.page.cx_password)
            self.page.page_ele()[6].send_keys(self.page.cx_wg_ip)
            self.page.page_ele()[7].send_keys(self.page.cx_wg_port)
            self.log.info('>>> 填写运营商接入账户基本信息')
            self.page.page_ele()[8].send_keys(self.page.cx_cop_id)
            self.page.page_ele()[9].send_keys(self.page.cx_cop_pwd)
            self.page.page_ele()[11].send_keys(self.page.cx_cop_ip)
            self.page.page_ele()[12].send_keys(self.page.cx_cop_port)
            self.log.info('>>> 选择后付费')
            self.page.charge_forward()
            self.log.info('>>> 确认新建')
            self.page.commit()
            self.log.info('>>> test_gateaccount_02测试用例执行结束：新建通道账户——彩信类型，执行成功')
        except Exception as e:
            self.log.info('>>> test_gateaccount_02测试用例执行结束：新建通道账户——彩信类型，执行失败{}'.format(e))
            screen_shot(self.dr, 'test_gateaccount_02.png')
            raise e

    def test_gateaccount_03(self):
        self.log.info('>>> test_gateaccount_03测试用例执行开始：新建通道账户——富信类型')
        try:
            login(self.dr)
            self.page.forward_page_account()
            self.log.info('>>> 新建富信通道账户')
            self.page.newcreate()
            self.log.info('>>> 填写EMP内部账户基本信息')
            self.page.page_ele()[3].send_keys(self.page.fx_gate_account_name)
            self.page.page_ele()[4].send_keys(self.page.fx_gate_account)
            self.page.page_ele()[5].send_keys(self.page.fx_password)
            self.page.page_ele()[6].send_keys(self.page.fx_wg_ip)
            self.page.page_ele()[7].send_keys(self.page.fx_wg_port)
            self.log.info('>>> 填写运营商接入账户基本信息')
            self.page.page_ele()[8].send_keys(self.page.fx_cop_id)
            self.page.page_ele()[9].send_keys(self.page.fx_cop_pwd)
            self.page.page_ele()[11].send_keys(self.page.fx_cop_ip)
            self.page.page_ele()[12].send_keys(self.page.fx_cop_port)
            self.log.info('>>> 选择后付费')
            self.page.charge_forward()
            self.log.info('>>> 确认新建')
            self.page.commit()
            self.log.info('>>> test_gateaccount_03测试用例执行结束：新建通道账户——彩信类型，执行成功')
        except Exception as e:
            self.log.info('>>> test_gateaccount_03测试用例执行结束：新建通道账户——彩信类型，执行失败{}'.format(e))
            screen_shot(self.dr, 'test_gateaccount_03.png')
            raise e

    def test_gateaccount_04(self):
        self.log.info('>>> test_gateaccount_04测试用例执行开始：通道账号绑定通道号码')
        try:
            login(self.dr)
            self.page.forward_page_account()
            self.log.info('>>> 绑定三网通道号码')
            self.page.bind_gate()
            self.log.info('>>> test_gateaccount_04测试用例执行结束：通道账号绑定通道号码，执行成功')
        except Exception as e:
            self.log.warning('>>> test_gateaccount_04测试用例执行结束：通道账号绑定通道号码，执行失败{}'.format(e))
            screen_shot(self.dr, 'test_gateaccount_04.png')
            raise e

if __name__ == '__main__':
    unittest.main()