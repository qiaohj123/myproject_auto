# -*- coding:utf-8 -*-
from rbemp_po.Common.CommonLib import *
from rbemp_po.Pages.IntShortMsg_module.FilesManagepage import FileManagepage
import unittest
from selenium import webdriver

class FileManage(unittest.TestCase):

    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()
        self.filepage = FileManagepage(self.dr)
        self.log = Log()

    def tearDown(self):
        self.dr.quit()

    def test_files_01(self):
        self.log.info('>>> test_files_01测试用例执行开始：上传超大文件')
        try:
            login(self.dr)
            self.filepage.forward_page_filemanage()
            self.log.info('>>> 上传超大文件')
            self.filepage.upload_file()
            self.log.info('>>> test_files_01测试用例执行开始：上传超大文件,执行成功')
        except Exception as e:
            self.log.info('>>> test_files_01测试用例执行开始：上传超大文件,执行失败:{}'.format(e))
            screen_shot(self.dr, 'test_files_01.png')
            raise e


if __name__ == '__main__':
    unittest.main()