# -*- coding:utf-8 -*-
from rbemp_po.Common.PageObject import PageObject
from rbemp_po.Common.CommonLib import *
from selenium.webdriver.common.keys import Keys
import random

class GateWaypage(PageObject):
    # 通道名称
    randums = str(random.randint(1000,9999))
    gate_name_yd = '移动运营商使用发送通道'+randums
    gate_name_lt = '联通运营商使用发送通道'+randums
    gate_name_dx = '电信运营商使用发送通道'+randums


    # 最大扩展位数
    expend_num = 6

    # 短信签名
    sign_sms = '[自动化测试签名专属测试使用]'


    # 新建页面元素
    def page_ele(self):
        # 通道类型
        gate_style0 = self.Find_element('xpth', '//section[@class="app-main"]/div/form/div[1]/div/div/div[1]/input')
        # 运营商类型
        operator_style1 = self.Find_element('xpth', '//section[@class="app-main"]/div/form/div[2]/div/div/div[1]/input')
        # 通道名称
        gate_name2 = self.Find_element('xpth', '//section[@class="app-main"]/div/form/div[3]/div/div/input')
        # 通道号码
        gate_num3 = self.Find_element('xpth', '//section[@class="app-main"]/div/form/div[4]/div/div/input')
        # 最大扩展位数
        expend_num4 = self.Find_element('xpth', '//section[@class="app-main"]/div/form/div[5]/div/div/input')
        # 短信签名
        sign_send5 = self.Find_element('xpth' ,'//section[@class="app-main"]/div/form/div[6]/div/div/input')
        # 签名长度
        sign_len6 = self.Find_element('xpth', '//section[@class="app-main"]/div/form/div[7]/div/div/label[2]/span[2]')
        # 签名位置前置
        sign_local7 = self.Find_element('xpth', '//section[@class="app-main"]/div/form/div[8]/div/div/label[1]/span[2]')
        # 由运营商签名为 否
        sign_no8 = self.Find_element('xpth', '//section[@class="app-main"]/div/form/div[9]/div/div/label[2]/span[2]')
        # 支持长短信 否
        long_msg9 = self.Find_element('xpth', '//section[@class="app-main"]/div/form/div[10]/div/div/label[2]/span[2]')
        # 按长短信拆分 否
        split_long10 = self.Find_element('xpth', '//section[@class="app-main"]/div/form/div[11]/div/div/label[2]/span[2]')
        # 支持整条提交 是
        commit_all11 = self.Find_element('xpth', '//section[@class="app-main"]/div/form/div[12]/div/div/label[1]/span[2]')
        # 中文单条短信字数
        single_msg12 = self.Find_element('xpth', '//section[@class="app-main"]/div/form/div[13]/div/div/input')
        # 中文最大字数
        large_msg13 = self.Find_element('xpth', '//section[@class="app-main"]/div/form/div[14]/div/div/input')
        # 费率输入框
        fee_lv14 = self.Find_element('xpth', '//section[@class="app-main"]/div/form/div[15]/div/div/input')
        # 预览按钮
        preview_button15 = self.Find_element('xpth', '//section[@class="app-main"]/div/form/div[17]/div/div/button/span')

        return gate_style0,operator_style1,gate_name2,gate_num3,expend_num4,sign_send5,sign_len6,sign_local7,sign_no8,long_msg9,split_long10,commit_all11,single_msg12,large_msg13,fee_lv14,preview_button15

    # 进入到通道创建页面
    def forward_page_gate(self):
        communicate_m = self.Find_element('xpth', '//span[text()="通信管理"]')
        communicate_m.click()
        wgconf = self.Find_element('xpth', '//span[text()="网关后端配置"]')
        wgconf.click()
        spcreate = self.Find_element('xpth', '//span[text()="通道管理"]')
        spcreate.click()
        # 新建按钮
        newcreate = self.Find_element('css', '.el-icon-circle-plus-outline')
        newcreate.click()


    # 通道类型选择 短信
    def gate_style(self,style):
        self.page_ele()[0].click()
        if style == '短信':
            time.sleep(1)
            self.Find_element('xpth', '//span[text()="短信"]').click()
        elif style == '彩信':
            self.Find_element('xpth', '//span[text()="彩信"]').click()

    # 运营商类型选择
    def operator_style(self, style):
        self.page_ele()[1].click()
        if style == '移动':
            self.Find_element('xpth', '//span[text()="移动"]').click()
        elif style == '联通':
            self.Find_element('xpth', '//span[text()="联通"]').click()
        elif style == '电信':
            self.Find_element('xpth', '//span[text()="电信"]').click()

    # 确认创建
    def commit_create(self):
        self.page_ele()[15].click()
        self.Find_element('xpth', '//div[@class="el-dialog__footer"]/div/button[1]').click()
        create_result = self.Wait_Elepresence('css', '.el-message__content').text
        if create_result == '新增成功!':
            self.log.info('>>> 新建sp账号成功')
        else:
            self.log.info('>>> 新建sp账号失败')

    # 新建按钮
    def new_create(self):
        self.Find_element('css', '.el-icon-circle-plus-outline').click()

    # 生成通道号码文件,每次仅执行一次，不可重复调用
    def gate_nums(self):
        move_content('libdatagate.txt')
        num_yd = str(random.randint(100000000000, 9999999999999))
        num_lt = str(random.randint(100000000000, 9999999999999))
        num_dx = str(random.randint(100000000000, 9999999999999))
        write_get('libdatagate.txt',['%s\n' % (num_yd), '%s\n' % (num_lt), '%s\n' % (num_dx)])

    # 读取通道号码
    def read_nums(self):
        gate_num_yd = read_content('libdatagate.txt', 0)
        gate_num_lt = read_content('libdatagate.txt', 1)
        gate_num_dx = read_content('libdatagate.txt', 2)
        return gate_num_yd,gate_num_lt,gate_num_dx


