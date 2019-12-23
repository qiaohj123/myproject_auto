# -*- coding:utf-8 -*-
from rbemp_po.Common.PageObject import PageObject
from rbemp_po.Common.CommonLib import *
from selenium.webdriver.common.keys import Keys
import random

class SpConfigGatepage(PageObject):

    # 新建页面元素
    def page_ele(self):
        # SP账号
        sp_account0 = self.Find_element('xpth', '//form[@class="el-form"]/div[1]/div/div/div[1]/input')
        # 路由状态
        rout_status1 = self.Find_element('xpth', '//form[@class="el-form"]/div[2]/div/div/div[1]/input')
        # 路由类型
        rout_style2 = self.Find_element('xpth', '//form[@class="el-form"]/div[3]/div/div/div[1]/input')
        # 通道号码
        gate_num3 = self.Find_element('xpth', '//form[@class="el-form"]/div[4]/div/div/div[1]/input')
        # 子号设定
        sub_num4 = self.Find_element('xpth', '//form[@class="el-form"]/div[15]/div/div/input')
        # 路由描述
        rout_ps5 = self.Find_element('xpth', '//form[@class="el-form"]/div[16]/div/div/input')
        # 指令代码
        order_code6 = self.Find_element('xpth', '//form[@class="el-form"]/div[17]/div/div/input')
        # 确定按钮
        commit7 = self.Find_element('xpth', '//form[@class="el-form"]/div[18]/div/button')
        return sp_account0,rout_status1,rout_style2,gate_num3,sub_num4,rout_ps5,order_code6,commit7


    # 进入到账户通道配置页面
    def forward_page_account(self):
        communicate_m = self.Find_element('xpth', '//span[text()="通信管理"]')
        communicate_m.click()
        wgconf = self.Find_element('xpth', '//span[text()="网关前端配置"]')
        wgconf.click()
        spcreate = self.Find_element('xpth', '//span[text()="账户通道配置"]')
        spcreate.click()
        self.Find_element('css', '.el-table__body')

    # 新建功能装
    def newcreate(self):
        newcreates = self.Find_element('css', '.el-icon-circle-plus-outline')
        newcreates.click()

    # 获取sp账号及匹配
    def sp_get(self):
        dxsp = read_content('spdata.txt',0).strip()+'(短信)'
        cxsp = read_content('spdata.txt',1).strip()+'(彩信)'
        fxsp = read_content('spdata.txt',2).strip()+'(短信)'
        dfsp = read_content('spdata.txt',3).strip()+'(短信)'
        return dxsp,cxsp,fxsp,dfsp

    # 选择sp账号
    def page_sp(self,style):
        self.page_ele()[0].click()
        if style == '短信':
            time.sleep(2)
            a = self.sp_get()[0]
            self.Find_element('xpth', '//span[text()='+'"'+a+'"'+']').click()
        elif style == '彩信':
            a = self.sp_get()[1]
            self.Find_element('xpth', '//span[text()='+'"'+a+'"'+']').click()
    # 路由状态选择
    def page_routstatus(self,status):
        self.page_ele()[1].click()
        if status == '启用':
            self.Find_element('xpth', '//span[text()="启用"]').click()
        elif status == '禁用':
            self.Find_element('xpth', '//span[text()="禁用"]').click()


    # 路由类型选择
    def page_routstyle(self):
        self.page_ele()[2].click()
        self.Find_element('xpth', '//div[@x-placement="bottom-start"]/div/div/ul/li[3]').click()
    # 通道号码选择
    def page_gate(self,type):
        self.page_ele()[3].click()
        yd_gate = read_content('libdatagate.txt',0).strip()+'(移动短信)'
        lt_gate = read_content('libdatagate.txt',1).strip()+'(联通短信)'
        dx_gate = read_content('libdatagate.txt',2).strip()+'(电信短信)'
        if type == '移动':
            self.Find_element('xpth', '//span[text()='+'"'+yd_gate+'"'+']').click()
        elif type == '联通':
            self.Find_element('xpth', '//span[text()='+'"'+lt_gate+'"'+']').click()
        elif type == '电信':
            self.Find_element('xpth', '//span[text()='+'"'+dx_gate+'"'+']').click()

            # 提交创建及创建结果断言


    def commit(self):
        self.page_ele()[7].click()
        create_result = self.Wait_Elepresence('css', '.el-message__content').text
        if create_result == '新增成功!':
            self.log.info('>>> 绑定通道号码成功')
        else:
            self.log.info('>>> 绑定通道号码成功')
