# -*- coding:utf-8 -*-
from rbemp_po.Common.PageObject import PageObject
from rbemp_po.Common.CommonLib import *
from selenium.webdriver.common.keys import Keys


class DifferentContentSendpage(PageObject):
    # 发送文件路径
    file_path = 'D:\PycharmProjects\\untitled\\rbemp_po\Datafile\differentcontent\\differentcontent'
    # 页面输入值
    # 发送主题
    var_theme_content = '动态模板发送主题：（测试发送）'
    file_theme_content = '文件内容发送主题：测试发送'

    # 发送内容
    var_send_content = '参数加上文本内容同时发送使用：测试发送使用'
    var_send_content_time = '参数加上文本内容同时发送使用：测试定时发送使用'

    # 进入到不同内容发送页面
    def forward_page_differentsend(self):
        # 企业短信
        entsms = self.Find_element('xpth', '//span[text()="企业短信"]')
        entsms.click()
        samesend = self.Find_element('xpth', '//span[text()="不同内容发送"]')
        samesend.click()

    # 不同内容发送主页面元素
    def page_ele_var(self):
        # 发送主题输入框
        send_theme0 = self.Find_element('xpth', '//*[@id="pane-template"]/div/form/div[1]/div/div/input')
        # 发送内容输入框
        send_phones1 = self.Find_element('xpth', '//div[@class="content"]/div/textarea')
        # 上传文件按钮
        file_load2 = self.Find_element('css', '.el-icon-ali-upload')
        # 选择模板按钮
        select_tmp3 = self.Find_element('css', '.el-icon-ali-template')
        # 草稿箱按钮
        draft_box4 = self.Find_element('css', '.el-icon-ali-draft')
        # 提交发送
        send_commit5 = self.Find_element('xpth', '//span[text()="提交发送"]')
        # 暂存草稿
        save_draft6 = self.Find_element('xpth', '//span[text()="暂存草稿"]')

        return send_theme0,send_phones1,file_load2,select_tmp3,draft_box4,send_commit5,save_draft6

    # 发送内容输入功能封装
    def insert_content(self):
        self.Find_element('xpth', '//span[text()="参数1"]').click()
        self.Find_element('xpth', '//span[text()="参数2"]').click()
        self.Find_element('xpth', '//span[text()="参数3"]').click()
        self.Find_element('xpth', '//span[text()="参数4"]').click()
        self.Find_element('xpth', '//span[text()="参数5"]').click()
        self.Find_element('xpth', '//span[text()="参数6"]').click()
        self.Find_element('xpth', '//span[text()="参数7"]').click()
        self.Find_element('xpth', '//span[text()="参数8"]').click()
        self.Find_element('xpth', '//span[text()="参数9"]').click()
        self.Find_element('xpth', '//span[text()="参数10"]').click()


    # 草稿箱获取功能封装
    def draft_box_get(self):
        self.page_ele_var()[4].click()
        self.Wait_Elepresence('css', '.el-table__body')
        self.Find_element('xpth', '//table[@class="el-table__body"]/tbody/tr[1]/td[6]/div/button[1]').click()

    # 草稿箱功能封装
    def draft_box(self):
        # 获取保存之前草稿数量
        self.page_ele_var()[4].click()
        result = self.Wait_Elepresence('css','.el-table__body')
        if result == None:
            draft_num = 0
        else:
            draft_num = getrows(self.dr)
        self.Find_element('xpth', '//div[@id="tab-sms-draft-list"]/div/i').click()
        self.page_ele_var()[6].click()
        time.sleep(20)
        self.page_ele_var()[4].click()
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
        self.Find_element('xpth', '//*[@id="pane-template"]/div/div[4]/div/div[3]/span/button[2]').click()
        self.Find_element('xpth', '//*[@id="pane-template"]/div/div[2]/div/div[3]/div/button[1]').click()
        ele = self.Wait_Elepresence('xpth', '//span[text()="查看发送记录"]')
        if ele != None:
            self.log.info('>>> 提交发送成功')
        else:
            self.log.info('>>> 提交发送失败')
            screen_shot(self.dr, '提交发送失败.png')
        self.Find_element('xpth', '//*[@id="pane-template"]/div/div[3]/div/div[3]/div/button').click()

    # 选择模板功能封装
    def send_tmpl(self):
        self.page_ele_var()[3].click()
        result = self.Wait_Elepresence('css', '.el-table__body')
        if result == None:
            nums = 0
        else:
            nums = getrows(self.dr)
        self.log.info('>>> 新建测试模板')
        self.Find_element('css', '.el-icon-circle-plus-outline').click()
        self.Find_element('xpth', '//div[@class="content-box"]/form/div[1]/div/div/input').send_keys('通用动态测试发送模板：测试发送使用')
        self.Find_element('xpth', '//div[@class="content-box"]/form/div[2]/div/div/input').send_keys('30000000022')
        # self.Find_element('xpth', '//div[@class="item-select-template"]/form/div[3]/div/div/div/input').click()
        self.Find_element('css', '.el-select__caret').click()
        time.sleep(2)
        self.Find_element('xpth', '//div[@x-placement="bottom-start"]/div[1]/div[1]/ul/li[2]/span').click()
        time.sleep(2)
        self.insert_content()
        self.Find_element('css', '.el-textarea__inner').send_keys('10个参数加上文本内容组成发送内容')
        self.Find_element('xpth', '//div[@class="content-box"]/form/div[6]/div/button').click()
        self.Find_element('css', '.el-table__body')
        nums_later = getrows(self.dr)
        if nums_later == nums + 1:
            self.log.info('>>> 新建测试模板成功')
            self.Find_element('css', '.el-table__body')
            getelement(self.dr, 0, 4).click()
        else:
            self.log.info('>>> 新建测试模板失败')





