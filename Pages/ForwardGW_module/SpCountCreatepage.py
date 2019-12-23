# -*- coding:utf-8 -*-
from rbemp_po.Common.PageObject import PageObject
from rbemp_po.Common.CommonLib import *
from selenium.webdriver.common.keys import Keys
import random

class SpCountCreatepage(PageObject):
    # 新建页面输入框

    # # sp账号列表
    # def splist(self,style):
    #     if style == 'dx':
    #         sp = 'DX'+str(random.randint(1000,9999))
    #         return sp
    #     elif style == 'cx':
    #         sp = 'CX' + str(random.randint(1000, 9999))
    #         return sp
    #     elif style == 'fx':
    #         sp = 'FX' + str(random.randint(1000, 9999))
    #         return sp
    #     elif style == 'df':
    #         sp = 'DF' + str(random.randint(1000, 9999))
    #         return sp

    # 自动生成sp账号
    def sp_create(self):
        move_content('spdata.txt')
        dxsp = 'DX'+str(random.randint(1000,9999))
        cxsp = 'CX' + str(random.randint(1000, 9999))
        fxsp = 'FX' + str(random.randint(1000, 9999))
        dfsp = 'DF' + str(random.randint(1000, 9999))
        write_get('spdata.txt',['%s\n'%(dxsp),'%s\n'%(cxsp),'%s\n'%(fxsp),'%s\n'%(dfsp)])

    # 读取sp账号
    def sp_get(self):
        dxsp = read_content('spdata.txt',0).strip()
        cxsp = read_content('spdata.txt',1).strip()
        fxsp = read_content('spdata.txt',2).strip()
        dfsp = read_content('spdata.txt',3).strip()
        return dxsp,cxsp,fxsp,dfsp


    # 上行URL
    mo_url = 'http://192.169.7.138:8109/moreceive.hts'
    # 状态报告url
    report_url = 'http://192.169.7.138:8109/rptreceive.hts'



    # 新建短富信sp账号页面元素
    def page_ele(self):
        # 短信sp账户
        style_sms0 = self.Find_element('xpth', '//form[@class="el-form"]/div[1]/div/label[1]/span[1]')
        # 彩信sp账户
        style_mms1 = self.Find_element('xpth', '//form[@class="el-form"]/div[1]/div/label[2]/span[1]')
        # 富信sp账户
        style_fx2 = self.Find_element('xpth', '//form[@class="el-form"]/div[1]/div/label[3]/span[1]')
        # sp账号
        sp_account3 = self.Find_element('xpth', '//form[@class="el-form"]/div[2]/div/div/input')
        # 账号名称
        account_name4 = self.Find_element('xpth', '//form[@class="el-form"]/div[3]/div/div[1]/input')
        # 账号密码
        account_pwd5 = self.Find_element('xpth', '//form[@class="el-form"]/div[4]/div/div/input')
        # 应用类型
        app_style6 = self.Find_element('xpth', '//form[@class="el-form"]/div[5]/div/div/div[1]/input')
        # 账户状态
        account_statu7 = self.Find_element('xpth', '//form[@class="el-form"]/div[6]/div/div/div/input')
        # 发送级别
        send_level8 = self.Find_element('xpth', '//form[@class="el-form"]/div[7]/div/div/div/input')
        # 计费类型
        charge_style9 = self.Find_element('xpth', '//form[@class="el-form"]/div[8]/div/div/div[1]/input')
        # 连接方式
        connet_style10 = self.Find_element('xpth', '//form[@class="el-form"]/div[9]/div[1]/div/div/div/input')
        # 需要上行
        mo_need11 = self.Find_element('xpth', '//form[@class="el-form"]/div[9]/div[2]/div/label[1]/span[1]')
        # 需要状态报告
        report_need12 = self.Find_element('xpth', '//form[@class="el-form"]/div[9]/div[2]/div/label[2]/span[1]/span')
        # 上行、状态报告获取方式
        mo_style13 = self.Find_element('xpth', '//form[@class="el-form"]/div[9]/div[3]/div/div/div/input')
        # 上行URL
        mo_url14 = self.Find_element('xpth', '//form[@class="el-form"]/div[9]/div[6]/div/div[1]/input')
        # 状态报告URL
        report_url15 = self.Find_element('xpth', '//form[@class="el-form"]/div[9]/div[7]/div/div[1]/input')
        # 确定按钮
        commit16 = self.Find_element('xpth', '//section[@class="app-main"]/div/form/div[10]/div/button')

        return style_sms0,style_mms1,style_fx2,sp_account3,account_name4,account_pwd5,app_style6,account_statu7,send_level8,charge_style9,connet_style10,mo_need11,report_need12,mo_style13,mo_url14,report_url15,commit16
    # 新建彩信sp账号页面元素
    def page_ele_cx(self):
        # 短信sp账户
        style_sms0 = self.Find_element('xpth', '//form[@class="el-form"]/div[1]/div/label[1]/span[1]')
        # 彩信sp账户
        style_mms1 = self.Find_element('xpth', '//form[@class="el-form"]/div[1]/div/label[2]/span[1]')
        # 富信sp账户
        style_fx2 = self.Find_element('xpth', '//form[@class="el-form"]/div[1]/div/label[3]/span[1]')
        # sp账号
        sp_account3 = self.Find_element('xpth', '//form[@class="el-form"]/div[2]/div/div/input')
        # 账号名称
        account_name4 = self.Find_element('xpth', '//form[@class="el-form"]/div[3]/div/div[1]/input')
        # 账号密码
        account_pwd5 = self.Find_element('xpth', '//form[@class="el-form"]/div[4]/div/div/input')
        # 应用类型
        app_style6 = self.Find_element('xpth', '//form[@class="el-form"]/div[5]/div/div/div[1]/input')
        # 账户状态
        account_statu7 = self.Find_element('xpth', '//form[@class="el-form"]/div[6]/div/div/div/input')
        # 发送级别
        send_level8 = self.Find_element('xpth', '//form[@class="el-form"]/div[7]/div/div/div/input')
        # 计费类型
        charge_style9 = self.Find_element('xpth', '//form[@class="el-form"]/div[8]/div/div/div[1]/input')

        return style_sms0,style_mms1,style_fx2,sp_account3,account_name4,account_pwd5,app_style6,account_statu7,send_level8,charge_style9

    # 进入到sp账号新建页面
    def forward_page_spcreate(self):
        # 通信管理
        communicate_m = self.Find_element('xpth', '//span[text()="通信管理"]')
        communicate_m.click()
        wgconf = self.Find_element('xpth', '//span[text()="网关前端配置"]')
        wgconf.click()
        spcreate = self.Find_element('xpth', '//span[text()="短彩SP账户"]')
        spcreate.click()
        # 新建按钮
        newcreate = self.Find_element('css', '.el-icon-circle-plus-outline')
        newcreate.click()

    # 新建元素按钮
    def newcreat(self):
        return self.Find_element('css', '.el-icon-circle-plus-outline')

    # 彩信页面确定按钮
    def cxcommit(self):
        return self.Find_element('xpth', '//*[@id="app"]/div/div[3]/section/div/form/div[9]/div/button')


