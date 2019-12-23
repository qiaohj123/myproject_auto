# -*- coding:utf-8 -*-
from rbemp_po.Common.CommonLib import *
from rbemp_po.Pages.IntShortMsg_module.DifferentContentSendpage import DifferentContentSendpage
import unittest
from selenium import webdriver

class DifferentSend(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()
        self.differpage = DifferentContentSendpage(self.dr)
        self.log = Log()

    def tearDown(self):
        self.dr.quit()

    def test_different_send01(self):
        self.log.info('>>> test_different_send01测试用例执行开始：不同内容-动态模板发送主要流程发送')
        try:
            login(self.dr)
            self.differpage.forward_page_differentsend()
            self.differpage.page_ele_var()[0].send_keys(self.differpage.var_theme_content)
            self.log.info('>>> 添加10个动态参数作为发送内容')
            self.differpage.insert_content()
            self.log.info('>>> 添加静态文本作为发送内容')
            self.differpage.page_ele_var()[1].send_keys(self.differpage.var_send_content)
            self.log.info('>>> 遍历上传各类格式发送文件')
            upload_file(self.dr, self.differpage.file_path)
            self.log.info('>>> 将编辑内容暂存草稿箱')
            self.differpage.draft_box()
            self.log.info('>>> 提交发送')
            self.differpage.send_commit()
            self.log.info('>>> test_different_send01测试用例执行结束：不同内容-动态模板发送主要流程发送,执行成功')
        except Exception as e:
            self.log.warning('>>> test_different_send01测试用例执行结束：不同内容-动态模板发送主要流程发送,执行失败:{}'.format(e))
            screen_shot(self.dr, 'test_different_send01.png')
            raise e

    def test_different_send02(self):
        self.log.info('>>> test_different_send02测试用例执行开始：不同内容-通过选择模板的方式进行发送')
        try:
            login(self.dr)
            self.differpage.forward_page_differentsend()
            self.differpage.page_ele_var()[0].send_keys(self.differpage.var_theme_content)
            self.log.info('>>> 选择新建动态模板')
            self.differpage.send_tmpl()
            self.log.info('>>> 遍历上传各类格式发送文件')
            upload_file(self.dr, self.differpage.file_path)
            self.log.info('>>> 提交发送')
            self.differpage.send_commit()
            self.log.info('>>> test_different_send02测试用例执行开始：不同内容-通过选择模板的方式进行发送,执行成功')
        except Exception as e:
            self.log.warning('>>> test_different_send02测试用例执行开始：不同内容-通过选择模板的方式进行发送,执行失败:{}'.format(e))
            screen_shot(self.dr, 'test_different_send02.png')
            raise e

    def test_different_send03(self):
        self.log.info('>>> test_different_send03测试用例之行开始：不同内容-通过草稿箱选择内容进行发送')
        try:
            login(self.dr)
            self.differpage.forward_page_differentsend()
            self.differpage.page_ele_var()[0].send_keys(self.differpage.var_theme_content)
            self.log.info('>>> 获取草稿箱内容')
            self.differpage.draft_box_get()
            self.log.info('>>> 遍历上传各类格式发送文件')
            upload_file(self.dr, self.differpage.file_path)
            self.log.info('>>> 提交发送')
            self.differpage.send_commit()
            self.log.info('>>> test_different_send03测试用例执行开始：不同内容-通过草稿箱选择内容进行发送,执行成功')
        except Exception as e:
            self.log.warning('>>> test_different_send03测试用例执行开始：不同内容-通过草稿箱选择内容进行发送,执行失败:{}'.format(e))
            screen_shot(self.dr, 'test_different_send03.png')
            raise e

    def test_differemt_send04(self):
        self.log.info('>>> test_differemt_send04测试用例执行开始：不同内容-定时发送')
        try:
            login(self.dr)
            self.differpage.forward_page_differentsend()
            self.differpage.page_ele_var()[0].send_keys(self.differpage.var_theme_content)
            self.log.info('>>> 添加10个动态参数作为发送内容')
            self.differpage.insert_content()
            self.log.info('>>> 添加静态文本作为发送内容')
            self.differpage.page_ele_var()[1].send_keys(self.differpage.var_send_content_time)
            self.log.info('>>> 遍历上传各类格式发送文件')
            upload_file(self.dr, self.differpage.file_path)
            self.log.info('>>> 设定定时发送时间,为当前时间后的一个小时')
            timecontrl(self.dr)
            self.log.info('>>> 提交发送')
            self.differpage.send_commit()
            self.log.info('>>> test_differemt_send04测试用例执行开始：不同内容-定时发送,执行成功')
        except Exception as e:
            self.log.warning('>>> test_differemt_send04测试用例执行开始：不同内容-定时发送,执行失败:{}'.format(e))
            screen_shot(self.dr, 'test_differemt_send04.png')
            raise e


if __name__ == '__mian__':
    unittest.main()