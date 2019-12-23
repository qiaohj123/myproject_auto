# -*- coding:utf-8 -*-
from rbemp_po.Common.CommonLib import *
from rbemp_po.Pages.ForwardGW_module.SpCountCreatepage import SpCountCreatepage
import unittest
from selenium import webdriver

class SpAccountCreate(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()
        self.page = SpCountCreatepage(self.dr)
        self.log = Log()

    def tearDown(self):
        self.dr.quit()

    def spaccount_create_01(self):
        self.log.info('>>> spaccount_create_01测试用例执行开始：新建sp账号——短信、彩信、富信、短富信账号各一条')
        try:
            login(self.dr)
            self.page.forward_page_spcreate()
            self.page.sp_create()
            i = 0
            while i < 4:
                style_list = (self.page.page_ele()[0], self.page.page_ele()[1], self.page.page_ele()[2])
                if i == 0:
                    self.log.info('>>> 创建短信sp账号')
                    self.page.page_ele()[3].send_keys(self.page.sp_get()[0])
                    self.page.page_ele()[4].send_keys('短信sp自动化测试账号')
                    self.page.page_ele()[5].send_keys('123456')
                    self.page.page_ele()[14].send_keys(self.page.mo_url)
                    self.page.page_ele()[15].send_keys(self.page.report_url)
                    self.page.page_ele()[16].click()
                    self.page.newcreat().click()
                    self.log.info('>>> 短信sp账号创建成功')
                if i == 1:
                    self.log.info('>>> 创建彩信sp账号')
                    self.page.page_ele_cx()[0].click()
                    self.page.page_ele_cx()[1].click()
                    self.page.page_ele_cx()[3].send_keys(self.page.sp_get()[1])
                    self.page.page_ele_cx()[4].send_keys('彩信sp自动化测试账号')
                    self.page.page_ele_cx()[5].send_keys('123456')
                    self.page.cxcommit().click()
                    self.page.newcreat().click()
                    self.log.info('>>> 彩信sp账号创建成功')
                if i == 2:
                    self.log.info('>>> 创建富信sp账号')
                    style_list[0].click()
                    style_list[2].click()
                    self.page.page_ele()[3].send_keys(self.page.sp_get()[2])
                    self.page.page_ele()[4].send_keys('富信sp自动化测试账号')
                    self.page.page_ele()[5].send_keys('123456')
                    self.page.page_ele()[14].send_keys(self.page.mo_url)
                    self.page.page_ele()[15].send_keys(self.page.report_url)
                    self.page.page_ele()[16].click()
                    self.page.newcreat().click()
                    self.log.info('>>> 富信sp账号创建成功')
                if i == 3:
                    self.log.info('>>> 创建短富信sp账号')
                    style_list[2].click()
                    self.page.page_ele()[3].send_keys(self.page.sp_get()[3])
                    self.page.page_ele()[4].send_keys('短富信sp自动化测试账号')
                    self.page.page_ele()[5].send_keys('123456')
                    self.page.page_ele()[14].send_keys(self.page.mo_url)
                    self.page.page_ele()[15].send_keys(self.page.report_url)
                    self.page.page_ele()[16].click()
                    self.page.newcreat().click()
                    self.log.info('>>> 短富信sp账号创建成功')
                i += 1
            self.log.info('>>> spaccount_create_01测试用例执行结束：新建sp账号——短信、彩信、富信、短富信账号各一条,执行成功')
        except Exception as e:
            self.log.info('>>> spaccount_create_01测试用例执行结束：新建sp账号——短信、彩信、富信、短富信账号各一条,执行失败{}'.format(e))
            screen_shot(self.dr, 'spaccount_create_01.png')
            raise e


if __name__ == '__main__':
    unittest.main()