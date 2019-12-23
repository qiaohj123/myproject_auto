# -*- coding:utf-8 -*-
from rbemp_po.Common.PageObject import PageObject
from rbemp_po.Common.CommonLib import *
from selenium.webdriver.common.keys import Keys

class FileManagepage(PageObject):
    # 超大文件存放路劲
    file_path = 'D:\PycharmProjects\\untitled\\rbemp_po\Datafile\samecontent\\samecontent'

    # 页面主要元素
    def page_ele(self):
        # 上传文件按钮
        upload_file0 = self.Find_element('css', '.el-icon-ali-upload')

        return upload_file0

     # 进入到文件管理页面

    def forward_page_filemanage(self):
        # 企业短信
        entsms = self.Find_element('xpth', '//span[text()="企业短信"]')
        entsms.click()
        samesend = self.Find_element('xpth', '//span[text()="文件管理"]')
        samesend.click()

    # 上传文件功能封装
    def upload_file(self):
        self.page_ele().click()
        self.Find_element('xpth', '//div[@class="el-dialog__body"]/form/div/div/div/input').send_keys('超大文件名称上传的名称')
        self.Find_element('xpth', '//div[@class="el-dialog__body"]/form/div[2]/div/div/div/input').click()
        self.Find_element('xpth', '//div[@x-placement="bottom-start"]/div/div/ul/li[1]').click()
        upload_file(self.dr, self.file_path)
        self.Find_element('xpth', '//div[@class="el-dialog__footer"]/div/button[1]/span').click()
        self.Wait_Elepresence('css', '.el-message__content')
        self.Find_element('css', '.el-icon-search').click()
        upload_result = self.Wait_Elepresence('css', '.el-message__content').text
        if upload_result == "文件提交成功!":
            self.log.info('>>> 上传文件成功')
        else:
            self.log.info('>>> 上传文件失败')
            screen_shot(self.dr, '上传文件失败.png')
