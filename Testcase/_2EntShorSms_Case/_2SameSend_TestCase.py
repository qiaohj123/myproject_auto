# -*- coding:utf-8 -*-
from rbemp_po.Common.CommonLib import *
from rbemp_po.Pages.IntShortMsg_module.SameContentSendpage import SameContentSendpage
import unittest
from selenium import webdriver




class SameSend(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()
        self.samepage = SameContentSendpage(self.dr)
        self.log = Log()

    def tearDown(self):
        self.dr.quit()

    def test_same_send01(self):
        self.log.info('>>> test_same_send01测试用例执行开始：相同内容发送主要流程覆盖发送')
        try:
            login(self.dr)
            self.samepage.forward_page_samesend()
            self.samepage.page_ele()[0].send_keys(self.samepage.send_theme_content)
            self.samepage.page_ele()[1].send_keys(self.samepage.send_phones_content)
            self.samepage.page_ele()[2].click()
            self.log.info('>>> 上传发送文件,遍历上传各类型文件')
            upload_file(self.dr,self.samepage.file_path)
            self.log.info('>>> 批量添加手机号码')
            self.samepage.page_ele()[5].click()
            self.samepage.batch_add()
            self.log.info('>>> 通讯录选择人员')
            self.log.info('>>> 发送内容填写')
            self.samepage.page_ele()[7].send_keys(self.samepage.send_content)
            self.log.info('>>> 将编辑内容暂存草稿箱')
            self.samepage.draft_box()
            self.log.info('>>> 提交发送')
            self.samepage.send_commit()
            self.log.info('>>> test_same_send01测试用例执行结束：相同内容发送主要流程覆盖发送，执行成功')
        except Exception as e:
            self.log.info('>>> test_same_send01测试用例执行结束：相同内容发送主要流程覆盖发送，执行失败{}'.format(e))
            screen_shot(self.dr, 'test_same_send01.png')
            raise e

    def test_same_send02(self):
        self.log.info('>>> test_same_send02测试用例执行开始：超大文件发送')
        try:
            login(self.dr)
            self.samepage.forward_page_samesend()
            self.samepage.page_ele()[0].send_keys(self.samepage.send_theme_content)
            self.log.info('>>> 选择超大文件')
            self.samepage.page_ele()[6].click()
            self.samepage.large_file()
            self.log.info('>>> 发送内容填写')
            self.samepage.page_ele()[7].send_keys(self.samepage.send_content)
            self.log.info('>>> 提交发送')
            self.samepage.send_commit()
            self.log.info('>>> test_same_send02测试用例执行结束：超大文件发送，执行成功')
        except Exception as e:
            self.log.info('>>> test_same_send02测试用例执行结束：超大文件发送，执行失败{}'.format(e))
            screen_shot(self.dr, 'test_same_send02.png')
            raise e

    def test_same_send03(self):
        self.log.info('>>> test_same_send03测试用例执行开始：新建及选择测试模板进行发送')
        try:
            login(self.dr)
            self.samepage.forward_page_samesend()
            self.samepage.page_ele()[0].send_keys(self.samepage.send_theme_content)
            self.samepage.page_ele()[5].click()
            self.samepage.batch_add()
            self.log.info('>>> 选择静态发送模板')
            self.samepage.send_tmpl()
            self.log.info('>>> 提交发送')
            self.samepage.send_commit()
            self.log.info('>>> test_same_send03测试用例执行结束：新建及选择测试模板进行发送，执行成功')
        except Exception as e:
            self.log.info('>>> test_same_send03测试用例执行结束：新建及选择测试模板进行发送，执行失败{}'.format(e))
            screen_shot(self.dr, 'test_same_send03.png')
            raise e

    def test_same_send04(self):
        self.log.info('>>> test_same_send04测试用例执行开始：相同内容发送草稿箱选择及修改后发送')
        try:
            login(self.dr)
            self.samepage.forward_page_samesend()
            self.log.info('>>> 选择草稿箱内容')
            self.samepage.draft_box_get()
            self.log.info('>>> 上传发送文件,遍历上传各类型文件')
            self.samepage.page_ele()
            upload_file(self.dr, self.samepage.file_path)
            self.log.info('>>> 批量添加手机号码')
            self.samepage.page_ele()[5].click()
            self.samepage.batch_add()
            self.log.info('>>> 发送内容填写')
            self.samepage.page_ele()[7].send_keys(self.samepage.send_content)
            self.log.info('>>> 提交发送')
            self.samepage.send_commit()
            self.log.info('>>> test_same_send04测试用例执行结束：相同内容发送草稿箱选择及修改后发送，执行成功')
        except Exception as e:
            self.log.info('>>> test_same_send04测试用例执行结束：相同内容发送草稿箱选择及修改后发送，执行失败{}'.format(e))
            screen_shot(self.dr, 'test_same_send04.png')
            raise e

    def test_same_send05(self):
        self.log.info('>>> test_same_send05测试用例执行开始：相同内容发送-定时发送提交')
        try:
            login(self.dr)
            self.samepage.forward_page_samesend()
            self.samepage.page_ele()[0].send_keys(self.samepage.send_theme_content)
            self.samepage.page_ele()[1].send_keys(self.samepage.send_phones_content)
            self.samepage.page_ele()[2].click()
            self.log.info('>>> 批量添加手机号码')
            self.samepage.page_ele()[5].click()
            self.samepage.batch_add()
            self.log.info('>>> 发送内容填写')
            self.samepage.page_ele()[7].send_keys(self.samepage.send_content_time)
            self.log.info('>>> 选择定时发送时间为当前时间之后的一小时')
            timecontrl(self.dr)
            self.log.info('>>> 提交发送')
            self.samepage.send_commit()
            self.log.info('>>> test_same_send05测试用例执行结束：相同内容发送-定时发送提交，执行成功')
        except Exception as e:
            self.log.info('>>> test_same_send05测试用例执行结束：相同内容发送-定时发送提交，执行失败{}'.format(e))
            screen_shot(self.dr, 'test_same_send05.png')
            raise e


if __name__ == '__main__':
    unittest.main()