# -*- coding:utf-8 -*-
from rbemp_po.Common.PageObject import PageObject
from rbemp_po.Common.CommonLib import *
from selenium.webdriver.common.keys import Keys
import random

class GateAccountpage(PageObject):
    # 新建页面输入值

    # 短信SP通道账户页面测试数据输入值
    nums = str(random.randint(1000,9999))
    # EMP基本账户信息
    gate_account_name = '短信通道账户名称'+nums
    gate_account = 'DX'+nums
    password = '123456'
    wg_ip = '192.169.3.10'
    wg_port = '8082'
    # 运营商接入账号基本信息
    cop_id = 'Test01'
    cop_pwd = '123456'
    cop_ip = '192.169.3.88'
    cop_port = '7893'
    yw_style = '默认业务'

    # 彩信SP通道账户页面测试数据输入值
    nums = str(random.randint(1000, 9999))
    # EMP基本账户信息
    cx_gate_account_name = '彩信通道账户名称' + nums
    cx_gate_account = 'CX' + nums
    cx_password = '123456'
    cx_wg_ip = '192.169.3.10'
    cx_wg_port = '8082'
    # 运营商接入账号基本信息
    cx_cop_id = 'CXCOP'+nums
    cx_cop_pwd = '123456'
    cx_cop_ip = '192.169.3.88'
    cx_cop_port = '7893'
    cx_yw_style = '默认业务'

    # 富信SP通道账户页面测试数据输入值
    nums = str(random.randint(1000, 9999))
    # EMP基本账户信息
    fx_gate_account_name = '富信通道账户名称' + nums
    fx_gate_account = 'FX' + nums
    fx_password = '123456'
    fx_wg_ip = '192.169.3.10'
    fx_wg_port = '8082'
    # 运营商接入账号基本信息
    fx_cop_id = 'CXCOP' + nums
    fx_cop_pwd = '123456'
    fx_cop_ip = '192.169.3.88'
    fx_cop_port = '7893'
    fx_yw_style = '默认业务'


    # 计费类型-后付费
    def charge_style(self):
        self.page_ele()[16].click()
        self.Find_element('xpth', '//div[@x-placement="bottom-start"]/div/div/ul/li[2]').click()



    def page_ele(self):
        # 账户类型选择
        # 短信sp账户
        account_sms0 = self.Find_element('xpth', '//section[@class="app-main"]/div/form/div/div/label[1]/span[2]')
        # 彩信sp账户
        account_mms1 = self.Find_element('xpth', '//section[@class="app-main"]/div/form/div/div/label[2]/span[2]')
        # 富信sp账户
        account_fx2 = self.Find_element('xpth', '//section[@class="app-main"]/div/form/div/div/label[3]/span[2]')
        # 通道账户名称
        gate_account_name3 = self.Find_element('xpth', '//section[@class="app-main"]/div/div/div/div[2]/div/form/div[1]/div/div/input')
        # 通道账号
        gate_account4 = self.Find_element('xpth', '//section[@class="app-main"]/div/div/div/div[2]/div/form/div[2]/div/div/input')
        # 账号密码
        accoun_pwd5 = self.Find_element('xpth', '//section[@class="app-main"]/div/div/div/div[2]/div/form/div[3]/div/div/input')
        # EMP网关地址
        wg_ulr6 = self.Find_element('xpth', '//section[@class="app-main"]/div/div/div/div[2]/div/form/div[5]/div/div[1]/input')
        # EMP网关端口
        wg_port7 = self.Find_element('xpth', '//section[@class="app-main"]/div/div/div[1]/div[2]/div/form/div[5]/div/div[2]/input')
        # 运营商账户ID
        operator_id8 = self.Find_element('xpth', '//section[@class="app-main"]/div/div/div[2]/div[2]/div/form/div[1]/div/div/input')
        # 运营商账户密码
        operator_pwd9 = self.Find_element('xpth', '//section[@class="app-main"]/div/div/div[2]/div[2]/div/form/div[2]/div/div/input')
        # 技术合作商
        cooperate10 = self.Find_element('xpth', '//section[@class="app-main"]/div/div/div[2]/div[2]/div/form/div[3]/div/div/div/input')
        # 运营商IP
        operator_url11 = self.Find_element('xpth', '//section[@class="app-main"]/div/div/div[2]/div[2]/div/form/div[4]/div/div[2]/input')
        # 运营商端口
        operator_port12 = self.Find_element('xpth', '//section[@class="app-main"]/div/div/div[2]/div[2]/div/form/div[4]/div/div[3]/input')
        # 业务类型
        yw_style13 = self.Find_element('xpth', '//section[@class="app-main"]/div/div/div[2]/div[2]/div/form/div[5]/div/div/input')
        # SP企业代码
        sp_code14 = self.Find_element('xpth', '//section[@class="app-main"]/div/div/div[2]/div[2]/div/form/div[6]/div/div/input')
        # 通讯协议
        communicate_cop15 = self.Find_element('xpth', '//section[@class="app-main"]/div/div/div[2]/div[2]/div/form/div[8]/div/div/div[1]/input')
        # 计费类型
        charge_style16 = self.Find_element('xpth', '//section[@class="app-main"]/div/div/div[2]/div[2]/div/form/div[10]/div/div/div[1]/input')
        # 余额查看地址
        charge_url17 = self.Find_element('xpth', '//section[@class="app-main"]/div/div/div[2]/div[2]/div/form/div[11]/div/div/input')
        # 保存按钮
        save_button18 = self.Find_element('xpth', '//section[@class="app-main"]/div/div[2]/button')

        return account_sms0,account_mms1,account_fx2,gate_account_name3,gate_account4,accoun_pwd5,wg_ulr6,wg_port7,operator_id8,operator_pwd9,cooperate10,operator_url11,operator_port12,yw_style13,sp_code14,communicate_cop15,charge_style16,charge_url17,save_button18

    # 进入到通道账户管理页面
    def forward_page_account(self):
        communicate_m = self.Find_element('xpth', '//span[text()="通信管理"]')
        communicate_m.click()
        wgconf = self.Find_element('xpth', '//span[text()="网关后端配置"]')
        wgconf.click()
        spcreate = self.Find_element('xpth', '//span[text()="通道账户管理"]')
        spcreate.click()
        self.Find_element('css', '.el-table__body')

    # 新建功能装
    def newcreate(self):
        newcreate = self.Find_element('css', '.el-icon-circle-plus-outline')
        newcreate.click()

    # 选择后付费类型
    def charge_forward(self):
        self.page_ele()[16].click()
        self.Find_element('xpth', '//div[@x-placement="top-start"]/div/div/ul/li[2]').click()

    # 提交创建及创建结果断言
    def commit(self):
        self.page_ele()[18].click()
        create_result = self.Wait_Elepresence('css', '.el-message__content').text
        if create_result == '新增成功!':
            self.log.info('>>> 新建后端通道账户成功')
        else:
            self.log.info('>>> 新建后端通道账户失败')

    # 通道账户绑定通道号码
    def bind_gate(self):
        self.Find_element('css', '.el-table__body')
        self.Find_element('xpth', '//table[@class="el-table__body"]/tbody/tr[1]/td[10]/div/button/span').click()
        self.Find_element('xpth', '//div[@class="account-search"]/span/div[2]/input').send_keys('123433454')
        table = self.Find_element('xpth', '//div[@class="first-content"]/div[3]/div/div[3]')
        # 获取列表表格的行数
        table_rows = table.find_elements_by_tag_name('tr')
        try:
            for i in range(len(table_rows)):
                if i <= len(table_rows)-1:
                    txt = table_rows[i].find_elements_by_tag_name('td')[1].text
                    if txt == read_content('libdatagate.txt',0).strip():           # 0 移动短信通道
                        self.log.info('>>> 添加移动通道')
                        self.Find_element('xpth',
                                          '//div[@class="first-content"]/div[3]/div/div[3]/table/tbody/tr['+str(
                                              i+1)+']/td[1]/div/label/span/span').click()
                    elif txt == read_content('libdatagate.txt',1).strip():         # 1 联通短信通道
                        self.log.info('>>> 添加联通通道')
                        self.Find_element('xpth',
                                          '//div[@class="first-content"]/div[3]/div/div[3]/table/tbody/tr[' + str(
                                              i + 1) + ']/td[1]/div/label/span/span').click()
                    elif txt == read_content('libdatagate.txt',2).strip():         # 2 电信短信通道
                        self.log.info('>>> 添加电信通道')
                        self.Find_element('xpth',
                                          '//div[@class="first-content"]/div[3]/div/div[3]/table/tbody/tr[' + str(
                                              i + 1) + ']/td[1]/div/label/span/span').click()
                    else:
                       pass
                else:
                    pass
            self.Find_element('xpth', '//div[@class="second-content"]/button[1]').click()
            self.Find_element('xpth','//div[@class="foot-account"]/button[1]').click()
            create_result = self.Wait_Elepresence('css', '.el-message__content').text
            if create_result == '操作成功!':
                self.log.info('>>> 绑定通道账户成功')
            else:
                self.log.info('>>> 绑定通道账户失败')
        except Exception as e:
            Log().warning("添加通道号码失败%s" % (e))
            raise e
