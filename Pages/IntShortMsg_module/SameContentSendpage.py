# -*- coding:utf-8 -*-
from rbemp_po.Common.PageObject import PageObject
from rbemp_po.Common.CommonLib import *
from selenium.webdriver.common.keys import Keys


class SameContentSendpage(PageObject):
    # 发送文件路径
    file_path = 'D:\PycharmProjects\\untitled\\rbemp_po\Datafile\samecontent\\samecontent'  # samecomtent 为文件名
    # 页面输入值
    # 发送主题
    send_theme_content = '测试发送主题12'
    # 发送手机号码
    send_phones_content = create_phone()+','+create_phone()+','+create_phone()+','+create_phone()+','+create_phone()
    # 发送内容
    send_content = '这是发送内容'
    send_content_time = '这是定时发送内容'

    # 进入到相同内容发送页面
    def forward_page_samesend(self):
        # 企业短信
        entsms = self.Find_element('xpth', '//span[text()="企业短信"]')
        entsms.click()
        samesend = self.Find_element('xpth', '//span[text()="相同内容发送"]')
        samesend.click()
    # 相同内容发送主页面元素
    def page_ele(self):
        # 发送主题输入框
        send_theme0 = self.Find_element('xpth', '//section[@class="app-main"]/div/form/div[1]/div/div/input')
        # 发送手机输入框
        send_phones1 = self.Find_element('css', 'input[valuekey="value"]')
        # 手机号码输入确定按钮
        theme_confirm2 = self.Find_element('xpth', '//span[text()="确定"]')
        # 上传文件按钮
        file_load3 = self.Find_element('css', '.el-icon-ali-upload')
        # 通讯录按钮
        address_book4 = self.Find_element('xpth', '//div[@class="contact-picker"]')
        # 批量添加按钮
        batch_add5 = self.Find_element('xpth', '//div[@class="batch-picker"]')
        # 超大文件按钮
        large_file6 = self.Find_element('css', '.el-icon-ali-import')
        # 发送内容输入框
        send_conet_ele7 = self.Find_element('xpth', '//div[@class="content"]/div/textarea')
        # 选择模板按钮
        select_tmp8 = self.Find_element('css', '.el-icon-ali-template')
        # 草稿箱按钮
        draft_box9 = self.Find_element('xpth', '//*[@id="app"]/div/div[3]/section/div/form/div[3]/div/div[2]/a[2]/span')
        # 提交发送
        send_commit10 = self.Find_element('xpth', '//span[text()="提交发送"]')
        # 暂存草稿
        save_draft11 = self.Find_element('xpth', '//span[text()="暂存草稿"]')

        return send_theme0,send_phones1,theme_confirm2,file_load3,address_book4,batch_add5,large_file6,send_conet_ele7,select_tmp8,draft_box9,send_commit10,save_draft11

    # 批量输入功能封装
    def batch_add(self):
        a = 0
        while a < 100:
            batch_area = self.Find_element('xpth', '//div[@class="batch-picker"]/div/div/div[2]/form/div[1]/div/div/textarea')
            batch_area.send_keys(create_phone())
            batch_area.send_keys(Keys.ENTER)
            a += 1
        self.Find_element('xpth', '//div[@class="batch-picker"]/div/div/div[3]/div/button').click()

    # 草稿箱获取功能封装
    def draft_box_get(self):
        self.page_ele()[9].click()
        self.Wait_Elepresence('css', '.el-table__body')
        self.Find_element('xpth', '//table[@class="el-table__body"]/tbody/tr[1]/td[6]/div/button[1]').click()

    # 草稿箱功能封装
    def draft_box(self):
        # 获取保存之前草稿数量
        self.page_ele()[9].click()
        result = self.Wait_Elepresence('css','.el-table__body')
        if result == None:
            draft_num = 0
        else:
            draft_num = getrows(self.dr)
        self.Find_element('xpth', '//div[@id="tab-sms-draft-list"]/div/i').click()
        self.page_ele()[11].click()
        time.sleep(20)
        self.page_ele()[9].click()
        self.Wait_Elepresence('css', '.el-table__body')
        time.sleep(2)
        draft_num2 = getrows(self.dr)
        if draft_num2 == draft_num+1:
            self.log.info('>>> 保存草稿箱成功')
        else:
            self.log.warning('>>> 保存草稿箱失败')
        self.Find_element('xpth', '//div[@id="tab-sms-draft-list"]/div/i').click()
    # 提交发送功能封装
    def send_commit(self):
        self.Find_element('xpth', '//span[text()="提交发送"]').click()
        self.Find_element('xpth', '//span[@class="dialog-footer"]/button[2]').click()
        self.Find_element('xpth', '//*[@id="app"]/div/div[3]/section/div/div[2]/div/div[3]/div/button[1]').click()
        ele = self.Wait_Elepresence('xpth', '//span[text()="查看发送记录"]')
        if ele != None:
            self.log.info('>>> 提交发送成功')
        else:
            self.log.info('>>> 提交发送失败')
            screen_shot(self.dr, '提交发送失败.png')
        self.Find_element('xpth', '//*[@id="app"]/div/div[3]/section/div/div[3]/div/div[3]/div/button').click()
    # 超大文件选择功能封装
    def large_file(self):
        self.Find_element('css', '.el-table__body')
        getelement(self.dr, 0, 6).click()
    # 通讯录选择功能封装
    def address_book(self):
        self.Find_element('css', '.el-tree-node__label').click()
    # 选择模板功能封装
    def send_tmpl(self):
        self.page_ele()[8].click()
        result = self.Wait_Elepresence('css', '.el-table__body')
        if result == None:
            nums = 0
        else:
            nums = getrows(self.dr)
        self.log.info('>>> 新建测试模板')
        self.Find_element('css', '.el-icon-circle-plus-outline').click()
        self.Find_element('xpth', '//div[@class="content-box"]/form/div[1]/div/div/input').send_keys('通用静态测试发送模板：测试发送使用')
        self.Find_element('xpth', '//div[@class="content-box"]/form/div[2]/div/div/input').send_keys('20000000011')
        self.Find_element('xpth', '//div[@class="content-box"]/form/div[3]/div/div/div/input').click()
        self.Find_element('xpth', '//span[text()="通用静态模块"]').click()
        self.Find_element('css', '.el-textarea__inner').send_keys('模板内容：尊敬的先生，现在给你分享一篇励志文章。你的人生你做主，我的地盘我做主')
        self.Find_element('xpth', '//div[@class="content-box"]/form/div[6]/div/button').click()
        self.Find_element('css', '.el-table__body')
        nums_later = getrows(self.dr)
        if nums_later == nums + 1:
            self.log.info('>>> 新建测试模板成功')
            getelement(self.dr, 0, 4).click()
        else:
            self.log.info('>>> 新建测试模板失败')

